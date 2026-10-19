"""Run the full offline validation on real historical data and write a report.

Protocol (see crypto-intelligence-lab/EXPERIMENTS.md):
- Development period (model comparison): walk-forward monthly, 2023-01 .. 2024-12.
- Final holdout (touched once, after choices are fixed): 2025-01 .. 2025-07.
- Purge + embargo = horizon. Expanding training window. Baselines included.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from cil.backtest import simulate, summary
from cil.data import load_trendscan_history, quality_report
from cil.features import build_features
from cil.labels import build_labels
from cil.metrics import block_bootstrap_bss, score, selective
from cil.models import GBM, default_models
from cil.validate import regimes, walk_forward

OUT = Path(__file__).resolve().parent.parent / "results"
DEV = ("2023-01-01", "2024-12-01")
HOLDOUT = ("2025-01-01", "2025-07-01")
HORIZONS = (1, 3, 7)


def evaluate(preds: pd.DataFrame, reg: pd.Series) -> dict:
    ref = preds[preds.model == "base_rate"].set_index(["date", "symbol"])["p"]
    res = {}
    for name, g in preds.groupby("model"):
        g = g.set_index(["date", "symbol"])
        pr = ref.reindex(g.index).to_numpy()
        s = score(g.p, g.y, pr)
        s["bss_ci95"] = block_bootstrap_bss(g.p.to_numpy(), g.y.to_numpy(), pr,
                                            g.index.get_level_values("date").strftime("%Y-%m"), n_boot=500)
        s["selective"] = selective(g.p, g.y).to_dict("records")
        by_reg = {}
        rg = reg.reindex(g.index.get_level_values("date")).to_numpy()
        for r in ("bull", "bear", "sideways"):
            m = rg == r
            if m.sum() > 50:
                by_reg[r] = score(g.p[m], g.y[m], pr[m])
        s["by_regime"] = by_reg
        res[name] = s
    return res


def permutation_check(feats, labels, horizon) -> dict:
    """Shuffle labels inside each training fold; skill must vanish."""
    rng = np.random.default_rng(1)
    lab = labels.copy()
    lab["up"] = lab.groupby(level="date")["up"].transform(lambda s: s)  # keep shape
    shuffled = lab.copy()
    mask = shuffled["up"].notna()
    shuffled.loc[mask, "up"] = rng.permutation(shuffled.loc[mask, "up"].to_numpy())
    cols = list(feats.columns)
    models = [m for m in default_models(cols) if m.name in ("base_rate", "lgbm_calibrated")]
    pr = walk_forward(feats, shuffled, models, horizon, *DEV)
    # Score the shuffled-label model against the TRUE labels.
    true = labels["up"]
    out = {}
    for name, g in pr.groupby("model"):
        y = true.reindex(pd.MultiIndex.from_arrays([g.date, g.symbol])).to_numpy()
        ok = ~np.isnan(y)
        out[name] = score(g.p.to_numpy()[ok], y[ok])
    return out


def main():
    OUT.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    df = load_trendscan_history()
    feats = build_features(df)
    reg = regimes(feats)
    cols = list(feats.columns)
    report = {"generated_at": stamp, "data": {
        "source": "TrendScan repo: Binance USD-M daily klines + funding (real data)",
        "rows": len(df), "symbols": sorted(df.index.get_level_values("symbol").unique()),
        "first": str(df.index.get_level_values("date").min().date()),
        "last": str(df.index.get_level_values("date").max().date()),
        "quality": quality_report(df).reset_index().astype(str).to_dict("records"),
        "regime_days": reg.value_counts().to_dict()},
        "features": cols, "horizons": {}, "trials": 0}

    all_preds = []
    for h in HORIZONS:
        labels = build_labels(df, h)
        dev = walk_forward(feats, labels, default_models(cols), h, *DEV)
        hold = walk_forward(feats, labels, default_models(cols), h, *HOLDOUT)
        report["trials"] += dev.model.nunique()
        dev["horizon"], hold["horizon"] = h, h
        dev["period"], hold["period"] = "dev", "holdout"
        all_preds += [dev, hold]
        report["horizons"][h] = {"dev": evaluate(dev, reg), "holdout": evaluate(hold, reg)}
        print(f"h={h}d done", file=sys.stderr)

    # Permutation sanity check on the 1-day horizon.
    report["permutation_h1"] = permutation_check(feats, build_labels(df, 1), 1)

    # Cost-aware backtests (1-day horizon), dev and holdout separately.
    preds = pd.concat(all_preds, ignore_index=True)
    funding = df["funding"]
    bt = {}
    for period in ("dev", "holdout"):
        p1 = preds[(preds.horizon == 1) & (preds.period == period)]
        bh = p1[p1.model == "base_rate"].copy()
        bh["p"] = 1.0  # always long, equal weight = buy and hold benchmark (rebalanced daily)
        bt[period] = {"buy_and_hold_eqw": summary(simulate(bh, funding, 0.5, fee_bps=0, allow_short=False)["net"])}
        for model in ("logistic", "lgbm_calibrated", "momentum_7d", "trend_sma200"):
            for t in (0.52, 0.55, 0.6):
                for fee in (5, 10, 20):
                    sim = simulate(p1[p1.model == model], funding, t, fee_bps=fee)
                    bt[period][f"{model}|t={t}|fee={fee}bps"] = summary(sim["net"]) | {
                        "avg_exposure": float(sim["exposure"].mean())}
    report["backtest_h1"] = bt

    preds.to_parquet(OUT / f"oos_predictions_{stamp}.parquet")
    (OUT / f"research_{stamp}.json").write_text(json.dumps(report, indent=1, default=str))
    (OUT / "latest.json").write_text(json.dumps(report, indent=1, default=str))
    print(OUT / f"research_{stamp}.json")


if __name__ == "__main__":
    main()
