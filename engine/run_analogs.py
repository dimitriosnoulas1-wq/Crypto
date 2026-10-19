"""Historical-analog ("similar past cycles") agent: honest walk-forward test.

For each test day, find the K most similar past (coin, day) states and use what happened
next to them as the forecast. Only analogs whose outcome was fully known before the test
month (label_end < month start) are eligible. Features are standardised with training
statistics only. Compared with the base rate, a recent (7d) base rate, and logistic regression.

Two variants:
  panel : all coins, coin state + BTC/market context
  btc   : BTC only, market-cycle state (longer-horizon trend/drawdown/funding)
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors

from cil.data import load_trendscan_history
from cil.features import build_features
from cil.labels import build_labels
from cil.metrics import block_bootstrap_bss, brier, ece, score, selective, wilson
from cil.models import Logistic

OUT = Path(__file__).resolve().parent.parent / "results"
STATE = ["ret_7", "ret_30", "ret_90", "vol_30", "dist_sma_50", "dist_sma_200", "drawdown_90",
         "funding_7d", "rsi_14", "btc_ret_30", "btc_dist_sma_200"]


def analog_predict(train: pd.DataFrame, test: pd.DataFrame, k: int) -> np.ndarray:
    Xtr = train[STATE]
    mu, sd = Xtr.mean(), Xtr.std().replace(0, 1)
    A = ((Xtr - mu) / sd).fillna(0).to_numpy()
    B = ((test[STATE] - mu) / sd).fillna(0).to_numpy()
    nn = NearestNeighbors(n_neighbors=min(k, len(A))).fit(A)
    dist, idx = nn.kneighbors(B)
    w = 1 / (dist + 1e-6)
    y = train["up"].to_numpy()[idx]
    base = train["up"].mean()
    # Shrink toward the training base rate (avoids overconfident tiny-k estimates).
    return ((w * y).sum(1) + 5 * base) / (w.sum(1) + 5 * 1 / max(dist.mean(), 1e-6))


def run(df, feats, horizon, variant, k, start="2023-01-01", end="2025-07-01"):
    lab = build_labels(df, horizon)
    data = feats.join(lab).dropna(subset=["up"])
    if variant == "btc":
        data = data[data.index.get_level_values("symbol") == "BTC"]
    data = data.dropna(subset=["ret_90", "dist_sma_200"])
    dates = data.index.get_level_values("date")
    out = []
    for m0 in pd.date_range(pd.Timestamp(start, tz="UTC"), pd.Timestamp(end, tz="UTC"), freq="MS"):
        m1 = m0 + pd.offsets.MonthBegin(1)
        tr = data[(data["label_end"] < m0) & (dates < m0 - pd.Timedelta(days=horizon))]
        te = data[(dates >= m0) & (dates < m1)]
        if len(tr) < 200 or te.empty:
            continue
        p_an = analog_predict(tr, te, k)
        trd = tr.index.get_level_values("date")
        p_recent = float(tr[trd >= trd.max() - pd.Timedelta(days=30)]["up"].mean())
        lg = Logistic(STATE).fit(tr[STATE], tr["up"].to_numpy())
        out.append(pd.DataFrame({"date": te.index.get_level_values("date"), "symbol": te.index.get_level_values("symbol"),
                                 "y": te["up"].to_numpy(), "analog": p_an, "base": tr["up"].mean(),
                                 "recent_30d": p_recent, "logistic": lg.predict_proba(te[STATE])}))
    x = pd.concat(out, ignore_index=True)
    res = {"n": len(x), "days": int(x.date.nunique()), "up_rate": float(x.y.mean())}
    for col in ("analog", "base", "recent_30d", "logistic"):
        s = score(x[col].to_numpy(), x.y.to_numpy(), x.base.to_numpy())
        s["bss_ci95_by_month"] = block_bootstrap_bss(x[col].to_numpy(), x.y.to_numpy(), x.base.to_numpy(),
                                                     x.date.dt.strftime("%Y-%m"), 500)
        s["selective"] = selective(x[col].to_numpy(), x.y.to_numpy()).to_dict("records")
        if variant == "panel":
            from sklearn.metrics import roc_auc_score
            aucs = [roc_auc_score(g.y, g[col]) for _, g in x.groupby("date") if g.y.nunique() == 2 and g[col].std() > 0]
            s["within_day_auc"] = float(np.mean(aucs)) if aucs else None
        res[col] = s
    return res


def main():
    df = load_trendscan_history()
    feats = build_features(df)
    rep = {"generated_at": datetime.now(timezone.utc).isoformat(), "state_features": STATE, "runs": {}}
    for variant, k in (("panel", 100), ("btc", 20)):
        for h in (3, 7, 30):
            rep["runs"][f"{variant}|h{h}d|k{k}"] = run(df, feats, h, variant, k)
            print(variant, h, "done")
    (OUT / "analogs_latest.json").write_text(json.dumps(rep, indent=1, default=str))


if __name__ == "__main__":
    main()
