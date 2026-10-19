"""Targets. A label at date d uses closes strictly after d only.

`fwd_ret`    : log return from close(d) to close(d+h bars).
`up`         : 1 if fwd_ret_h > 0 else 0 (NaN when the future is not known yet).
`label_end`  : last date the label depends on; used to purge overlapping rows.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def build_labels(df: pd.DataFrame, horizon: int, bar: pd.Timedelta = pd.Timedelta(days=1)) -> pd.DataFrame:
    out = []
    for sym, g in df.groupby(level="symbol"):
        logc = np.log(g["close"])
        dates = g.index.get_level_values("date")
        fwd = logc.shift(-horizon) - logc
        lab = pd.DataFrame(index=g.index)
        lab["fwd_ret"] = fwd
        lab["up"] = (fwd > 0).astype(float).where(fwd.notna())
        lab["label_end"] = pd.Series(dates, index=g.index).shift(-horizon)
        # Require consecutive bars: a gap inside the window makes the label unreliable.
        span = lab["label_end"] - pd.Series(dates, index=g.index)
        bad = span != horizon * bar
        lab.loc[bad, ["fwd_ret", "up"]] = np.nan
        out.append(lab)
    return pd.concat(out).sort_index()
