"""Skeptic agent (meta-labeling), honest walk-forward test on the out-of-sample predictions.

A primary model makes directional calls (|p - 0.5| >= 0.05). The skeptic never predicts the
price. It learns, from calls whose outcome was known BEFORE the test month, in which situations
the primary model's calls were wrong (low volume, extreme funding, high volatility, weak signal...)
and vetoes those calls. Compared with taking every call, with a random veto of the same size
(permutation null), and judged on hit rate and net return (10 bps round trip) with CIs that
resample whole days (calls on one day are correlated).

Features available at decision time only (built by build_features); purge = label horizon.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from lightgbm import LGBMClassifier

from cil.data import load_trendscan_history
from cil.features import build_features

OUT = Path(__file__).resolve().parent.parent / "results"
FEAT = ["vol_30", "vol_ratio", "qvol_z", "funding_z", "funding_7d", "rsi_14", "ret_7", "ret_30",
        "dist_sma_50", "dist_sma_200", "drawdown_90", "range_n", "close_pos", "beta_60",
        "btc_ret_30", "btc_dist_sma_200", "btc_vol_30", "xs_rank_ret_7", "xs_rank_qvol_z"]
EDGE = 0.05
FEE = 0.001


def day_ci(x: pd.Series, dates: pd.Series, n=2000, seed=0):
    rng = np.random.default_rng(seed)
    g = pd.DataFrame({"x": x.to_numpy(), "d": dates.to_numpy()}).groupby("d").x.agg(["sum", "count"])
    s, c = g["sum"].to_numpy(), g["count"].to_numpy()
    idx = rng.integers(0, len(s), (n, len(s)))
    m = s[idx].sum(1) / c[idx].sum(1)
    return float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))


def run(preds, feats, model, horizon, keep_quantile=0.5):
    d = preds[(preds.model == model) & (preds.horizon == horizon)].copy()
    d = d[(d.p - 0.5).abs() >= EDGE]
    d["side"] = np.where(d.p >= 0.5, 1, -1)
    d["correct"] = ((d.side == 1) == (d.y == 1)).astype(int)
    d["net"] = d.side * np.expm1(d.fwd_ret) - FEE
    d["edge"] = (d.p - 0.5).abs()
    d = d.join(feats[FEAT], on=["date", "symbol"])
    cols = FEAT + ["edge"]
    d["fold"] = pd.to_datetime(d.fold + "-01", utc=True)
    keep = pd.Series(np.nan, index=d.index)
    for m0 in sorted(d.fold.unique()):
        tr = d[(d.date < m0 - pd.Timedelta(days=horizon)) & (d.fold < m0)]
        te = d[d.fold == m0]
        if len(tr) < 400 or te.empty:
            continue
        sk = LGBMClassifier(n_estimators=150, learning_rate=0.03, num_leaves=5, min_child_samples=80,
                            subsample=0.7, subsample_freq=1, colsample_bytree=0.7, reg_lambda=10,
                            random_state=3, verbose=-1).fit(tr[cols], tr.correct)
        # Veto threshold: keep the calls the skeptic trusts above the TRAINING median trust.
        thr = np.quantile(sk.predict_proba(tr[cols])[:, 1], 1 - keep_quantile)
        keep.loc[te.index] = (sk.predict_proba(te[cols])[:, 1] >= thr).astype(float)
    d["keep"] = keep
    d = d.dropna(subset=["keep"])
    allowed, vetoed = d[d.keep == 1], d[d.keep == 0]

    def stats(x):
        if x.empty:
            return None
        return {"calls": len(x), "days": int(x.date.nunique()), "hit": float(x.correct.mean()),
                "hit_ci95_by_day": day_ci(x.correct, x.date), "mean_net_bps": float(x.net.mean() * 1e4),
                "net_ci95_bps": [v * 1e4 for v in day_ci(x.net, x.date)]}

    rng = np.random.default_rng(5)
    null_hits = []
    for _ in range(300):  # random veto keeping the same share of calls
        k = rng.random(len(d)) < d.keep.mean()
        null_hits.append(d.correct[k].mean())
    res = {"all_calls": stats(d), "skeptic_allowed": stats(allowed), "skeptic_vetoed": stats(vetoed),
           "random_veto_hit_95pct_range": [float(np.percentile(null_hits, 2.5)), float(np.percentile(null_hits, 97.5))]}
    res["skeptic_hit_vs_random_veto_p"] = float((np.array(null_hits) >= allowed.correct.mean()).mean())
    return res


def main():
    df = load_trendscan_history()
    feats = build_features(df)
    pf = sorted(OUT.glob("oos_predictions_*.parquet"))[-1]
    preds = pd.read_parquet(pf)
    rep = {"preds_file": pf.name, "edge": EDGE, "fee_round_trip": FEE, "runs": {}}
    for model in ("lgbm_calibrated", "logistic"):
        for h in (1, 3, 7):
            rep["runs"][f"{model}|h{h}d"] = run(preds, feats, model, h)
            print(model, h, "done")
    (OUT / "skeptic_latest.json").write_text(json.dumps(rep, indent=1, default=str))


if __name__ == "__main__":
    main()
