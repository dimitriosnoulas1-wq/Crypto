"""Walk-forward evaluation with purging and embargo.

For each test month M:
  train rows = rows whose label_end < first day of M  (purge: no label overlaps the test month)
               and whose date < first day of M - embargo days
  test rows  = rows dated inside M
Training window is expanding. Every preprocessing step lives inside the model, so
it is refitted per fold.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .models import GBM


def regimes(feats: pd.DataFrame) -> pd.Series:
    """Market regime per date from BTC, using only past data."""
    b = feats.xs("BTC", level="symbol")
    bull = (b["dist_sma_200"] > 0) & (b["ret_90"] > 0.10)
    bear = (b["dist_sma_200"] < 0) & (b["ret_90"] < -0.10)
    reg = pd.Series("sideways", index=b.index)
    reg[bull] = "bull"
    reg[bear] = "bear"
    return reg.rename("regime")


def walk_forward(feats, labels, models, horizon, test_start, test_end, min_train_rows=2000,
                 embargo_days=None):
    embargo = pd.Timedelta(days=embargo_days if embargo_days is not None else horizon)
    data = feats.join(labels).dropna(subset=["up"])
    dates = data.index.get_level_values("date")
    months = pd.date_range(pd.Timestamp(test_start, tz="UTC"), pd.Timestamp(test_end, tz="UTC"), freq="MS")
    cols = [c for c in feats.columns]
    out = []
    for m0 in months:
        m1 = m0 + pd.offsets.MonthBegin(1)
        train = data[(dates < m0 - embargo) & (data["label_end"] < m0)]
        test = data[(dates >= m0) & (dates < m1)]
        if len(train) < min_train_rows or test.empty:
            continue
        for model in models:
            if isinstance(model, GBM):
                model.fit(train[cols], train["up"].to_numpy(),
                          dates=train.index.get_level_values("date"), horizon=horizon)
            else:
                model.fit(train[cols], train["up"].to_numpy())
            p = model.predict_proba(test[cols])
            out.append(pd.DataFrame({
                "date": test.index.get_level_values("date"),
                "symbol": test.index.get_level_values("symbol"),
                "model": model.name, "p": p, "y": test["up"].to_numpy(),
                "fwd_ret": test["fwd_ret"].to_numpy(), "fold": m0.strftime("%Y-%m"),
                "train_rows": len(train),
            }))
    return pd.concat(out, ignore_index=True)
