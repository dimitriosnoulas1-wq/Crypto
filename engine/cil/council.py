"""The council: specialist agents, a president that weights them by their live record,
abstention when trusted members disagree, and a risk veto.

Members write their own predictions to the ledger first (as ordinary models). The council
is one more ledger "model" whose probability is a weighted logit pool of the members.
Weights come only from realised, already-scored predictions in the ledger (Hedge /
exponential weights on log loss), so a member earns influence by being right live.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors

from .models import BaseRate, Logistic

ANALOG_STATE = ["ret_7", "ret_30", "ret_90", "vol_30", "dist_sma_50", "dist_sma_200", "drawdown_90",
                "funding_7d", "rsi_14", "btc_ret_30", "btc_dist_sma_200"]
DERIV_COLS = ["funding_1d", "funding_7d", "funding_z", "oi_chg_1", "oi_chg_24", "oi_chg_z",
              "taker_ratio", "taker_ratio_24"]
ETA = 3.0            # Hedge learning rate on per-bar mean log loss
LOOKBACK_BARS = 72   # scored bars used for weights
MIN_AGREEMENT = 0.6  # weighted share of members on the council's side, else abstain
MIN_EDGE = 0.02      # |p - 0.5| below this -> abstain


class AnalogAgent:
    """'Have we seen this before?' K nearest past states (outcome already known), distance-weighted."""

    def __init__(self, k=100):
        self.k, self.name = k, f"analog_k{k}"

    def fit(self, X, y):
        cols = [c for c in ANALOG_STATE if c in X]
        A = X[cols]
        self.cols, self.mu, self.sd = cols, A.mean(), A.std().replace(0, 1)
        self.y, self.base = np.asarray(y, float), float(np.mean(y))
        self.nn = NearestNeighbors(n_neighbors=min(self.k, len(A))).fit(((A - self.mu) / self.sd).fillna(0).to_numpy())
        return self

    def predict_proba(self, X):
        B = ((X[self.cols] - self.mu) / self.sd).fillna(0).to_numpy()
        dist, idx = self.nn.kneighbors(B)
        w = 1 / (dist + 1e-6)
        prior = 5 / max(float(dist.mean()), 1e-6)   # shrink toward the base rate
        return ((w * self.y[idx]).sum(1) + prior * self.base) / (w.sum(1) + prior)


class DerivativesAgent:
    """Funding, open interest and taker flow only. Falls back to the base rate while those
    histories are too short (features mostly missing)."""
    name = "derivatives"

    def fit(self, X, y):
        cols = [c for c in DERIV_COLS if c in X and X[c].isna().mean() < 0.5]
        self.model = Logistic(cols, C=0.05).fit(X, y) if cols else BaseRate().fit(X, y)
        self.cols = cols
        return self

    def predict_proba(self, X):
        return self.model.predict_proba(X)


def _logit(p):
    p = np.clip(np.asarray(p, float), 1e-4, 1 - 1e-4)
    return np.log(p / (1 - p))


def hedge_weights(scored: pd.DataFrame, members: list[str]) -> tuple[dict, dict]:
    """scored: resolved rows with columns asof, model, p_up, up. Returns (weights, mean log loss)."""
    w = {m: 1.0 for m in members}
    ll = {}
    if scored.empty:
        return {m: 1 / len(members) for m in members}, ll
    s = scored[scored.model.isin(members)].copy()
    p = np.clip(s.p_up.to_numpy(), 1e-4, 1 - 1e-4)
    s["loss"] = -(s.up * np.log(p) + (1 - s.up) * np.log(1 - p))
    bars = sorted(s["asof"].unique())[-LOOKBACK_BARS:]
    s = s[s["asof"].isin(bars)]
    per_bar = s.groupby(["asof", "model"]).loss.mean().unstack()
    per_bar = per_bar.reindex(columns=members)
    # Bars before a member existed are neutral (the bar's median loss): no penalty for being new,
    # no free pass either. Its weight then moves only with the bars it actually predicted.
    per_bar = per_bar.apply(lambda r: r.fillna(r.median()), axis=1)
    regret = (per_bar.sub(per_bar.min(axis=1), axis=0)).sum()
    for m in members:
        w[m] = float(np.exp(-ETA * regret.get(m, 0.0)))
        if m in s.model.values:
            ll[m] = float(s[s.model == m].groupby("asof").loss.mean().mean())  # its own bars only
    tot = sum(w.values())
    return {m: v / tot for m, v in w.items()}, ll


def risk_veto(today_feats: pd.DataFrame) -> pd.Series:
    """Per coin: reason string if the council must stay silent, else ''."""
    reasons = pd.Series("", index=today_feats.index)
    vol = today_feats.get("vol_30")
    if vol is not None:
        med = vol.median()
        wild = (vol > 2.5 * med) & (vol.rank(pct=True) >= 0.9)
        reasons[wild] = "extreme_volatility"
    core = [c for c in ("ret_1", "vol_30", "rsi_14") if c in today_feats]
    missing = today_feats[core].isna().any(axis=1)
    reasons[missing & (reasons == "")] = "missing_inputs"
    return reasons


def convene(member_preds: dict[str, pd.Series], weights: dict[str, float], veto: pd.Series):
    """Weighted logit pool -> (probability series, per-coin meta). Abstains -> 0.5."""
    members = [m for m in weights if m in member_preds]
    P = pd.DataFrame({m: member_preds[m] for m in members})
    W = np.array([weights[m] for m in members])
    W = W / W.sum()
    z = (_logit(P.to_numpy()) * W).sum(axis=1)
    p = 1 / (1 + np.exp(-z))
    side = np.sign(p - 0.5)
    agree = ((np.sign(P.to_numpy() - 0.5) == side[:, None]) * W).sum(axis=1)
    out, meta = [], []
    for i, idx in enumerate(P.index):
        reason = veto.get(idx, "")
        if not reason and abs(p[i] - 0.5) < MIN_EDGE:
            reason = "no_edge"
        if not reason and agree[i] < MIN_AGREEMENT:
            reason = "members_disagree"
        out.append(0.5 if reason else float(p[i]))
        meta.append({"raw_p": round(float(p[i]), 4), "agreement": round(float(agree[i]), 3), "abstain": reason})
    return pd.Series(out, index=P.index), meta
