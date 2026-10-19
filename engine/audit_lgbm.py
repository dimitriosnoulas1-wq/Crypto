"""Audit of the live LightGBM probabilities (diagnostic only, writes no ledger rows).

Checks: class balance per training slice, feature availability per slice and on the
latest bar, raw vs isotonic-calibrated outputs, a variant without the features that only
exist for the last ~100 hours (OI, taker), and a short walk-forward on the same hourly
data with Brier skill versus the base-rate model and calibration error.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import pandas as pd

from cil import okx
from cil.features import build_features
from cil.labels import build_labels
from cil.metrics import brier, ece
from cil.models import GBM, BaseRate, Logistic, RecentBaseRate

ROOT = Path(__file__).resolve().parent.parent
BAR = pd.Timedelta(hours=1)
SPARSE = ("oi_", "taker_")


def within_bar_auc(x: pd.DataFrame) -> float:
    """Mean AUC across bars: can the model rank coins against each other in the same hour?"""
    from sklearn.metrics import roc_auc_score
    vals = [roc_auc_score(g.y, g.p) for _, g in x.groupby("date") if g.y.nunique() == 2 and g.p.std() > 0]
    return float(np.mean(vals)) if vals else float("nan")


def fit(model, train, cols, h):
    if isinstance(model, GBM):
        return model.fit(train[cols], train["up"].to_numpy(), dates=train.index.get_level_values("date"),
                         horizon=h, bar=BAR)
    return model.fit(train[cols], train["up"].to_numpy())


def main():
    log = []
    t0 = time.time()
    df, _, now_ms = okx.fetch_panel(60, ROOT / "data_cache", log)
    out = {"fetch": log, "fetch_seconds_total": round(time.time() - t0, 1)}
    feats = build_features(df)
    cols = list(feats.columns)
    dense = [c for c in cols if not c.startswith(SPARSE)]
    last_bar = feats.index.get_level_values("date").max()
    latest = feats[feats.index.get_level_values("date") == last_bar]
    out["last_bar"] = str(last_bar)
    for h in (1, 4):
        lab = build_labels(df, h, BAR)
        train = feats.join(lab).dropna(subset=["up"])
        train = train[train["label_end"] <= last_bar]
        d = pd.DatetimeIndex(train.index.get_level_values("date"))
        cut = d.sort_values()[int(0.8 * len(d))]
        fit_slice, cal_slice = train[d < cut - h * BAR], train[d >= cut]
        r = {"train_rows": len(train), "calibration_slice_start": str(cut),
             "up_rate": {"all": float(train.up.mean()), "fit_slice": float(fit_slice.up.mean()),
                         "calibration_slice": float(cal_slice.up.mean()),
                         "last_100h": float(train[d >= last_bar - 100 * BAR].up.mean())},
             "feature_availability": {
                 c: {"fit_slice": float(fit_slice[c].notna().mean()), "calibration_slice": float(cal_slice[c].notna().mean()),
                     "latest_bar": float(latest[c].notna().mean())} for c in cols if c.startswith(SPARSE)}}
        variants = {"base_rate": BaseRate(), "logistic": Logistic(cols),
                    "lgbm_calibrated_live": GBM(cols, calibrate=True), "lgbm_raw": GBM(cols, calibrate=False),
                    "lgbm_calibrated_no_sparse": GBM(dense, calibrate=True), "recent_base_rate_7d": RecentBaseRate(7)}
        r["latest_bar_predictions"] = {}
        for name, m in variants.items():
            fit(m, train, cols, h)
            p = m.predict_proba(latest[cols])
            r["latest_bar_predictions"][name] = {"mean": float(p.mean()), "min": float(p.min()),
                                                 "max": float(p.max()), "std": float(p.std())}
        # Short walk-forward: 7 consecutive 2-day test windows ending at the last labelled bar.
        end = train.index.get_level_values("date").max() + BAR
        wf = {k: [] for k in variants}
        for i in range(7, 0, -1):
            a, b = end - i * 2 * pd.Timedelta(days=1), end - (i - 1) * 2 * pd.Timedelta(days=1)
            tdates = train.index.get_level_values("date")
            tr = train[(train["label_end"] < a) & (tdates < a - h * BAR)].sort_index(level="date")
            te = train[(tdates >= a) & (tdates < b)]
            for name in variants:
                m = {"base_rate": BaseRate(), "logistic": Logistic(cols), "lgbm_calibrated_live": GBM(cols, True),
                     "lgbm_raw": GBM(cols, False), "lgbm_calibrated_no_sparse": GBM(dense, True),
                     "recent_base_rate_7d": RecentBaseRate(7)}[name]
                fit(m, tr, cols, h)
                wf[name].append(pd.DataFrame({"p": m.predict_proba(te[cols]), "y": te.up.to_numpy(),
                                              "date": te.index.get_level_values("date")}))
        base = pd.concat(wf["base_rate"])
        r["walk_forward_14d"] = {}
        for name, parts in wf.items():
            x = pd.concat(parts)
            r["walk_forward_14d"][name] = {
                "n": len(x), "up_rate": float(x.y.mean()), "mean_p": float(x.p.mean()),
                "accuracy": float(((x.p >= 0.5) == x.y).mean()),
                "brier_skill_vs_base_rate": 1 - brier(x.p, x.y) / brier(base.p, base.y), "ece": ece(x.p, x.y),
                "mean_within_bar_auc": within_bar_auc(x)}
        out[f"h{h}"] = r
    (ROOT / "results" / "live" / "audit_lgbm.json").write_text(json.dumps(out, indent=1, default=str))
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
