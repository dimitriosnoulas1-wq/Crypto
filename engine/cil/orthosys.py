"""Python port of TrendScan's `src/lib/signal/orthogonal.js` (OrthoSys v6.1).

The JS file states it is itself a port of a Pine Script under the Mozilla Public
License 2.0, so this file is MPL-2.0-derived. Kept for personal research only.

Pipeline: 9 raw signals -> rolling z-score (zsc_len) -> SMA(lb) -> weighted mean
-> composite; position +1 if composite > thresh and pivot filter agrees, -1 if
composite < -thresh and pivot filter agrees, else 0.
taker_ratio is the JS proxy (up-candle volume vs down-candle volume), not real
taker flow.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

DEFAULT = dict(lb=5, zsc_len=80, thresh=0.5, use_pivot=True, pivot_tau=0.0,
               weights=dict(vol_ratio=1, bb_width=1, rsi_signal=1, zscore_20=1, mom_6=1,
                            mom_18=1, ema_cross=1, hl_mom=1, taker_ratio=1))
# TrendScan's own recommendation for daily bars (docs/ORTHOSYS_BACKTEST_REPORT.md section 6.3).
TRENDSCAN_DAILY = dict(DEFAULT, lb=3, zsc_len=120, thresh=0.4,
                       weights=dict(DEFAULT["weights"], mom_6=0))


def _rsi_pine(c: np.ndarray, n=14):
    out = np.full(len(c), np.nan)
    if len(c) < n + 1:
        return out
    d = np.diff(c)
    g, l = np.clip(d, 0, None), np.clip(-d, 0, None)
    ag, al = g[:n].mean(), l[:n].mean()
    out[n] = 100 if al == 0 else 100 - 100 / (1 + ag / al)
    for i in range(n + 1, len(c)):
        ag = (ag * (n - 1) + g[i - 1]) / n
        al = (al * (n - 1) + l[i - 1]) / n
        out[i] = 100 if al == 0 else 100 - 100 / (1 + ag / al)
    return out


def raw_signals(g: pd.DataFrame) -> pd.DataFrame:
    o, h, l, c, v = (g[k].to_numpy(float) for k in ("open", "high", "low", "close", "volume"))
    cs, vs = pd.Series(c), pd.Series(v)
    out = {}
    vsma = vs.rolling(20).mean().to_numpy()
    direction = np.where(c > o, 1.0, -1.0)
    out["vol_ratio"] = np.nan_to_num(direction * v / vsma * -1)
    basis = cs.rolling(20).mean().to_numpy()
    dev = cs.rolling(20).std(ddof=0).to_numpy()
    out["bb_width"] = np.nan_to_num(dev * 2 / basis)
    out["rsi_signal"] = np.nan_to_num((_rsi_pine(c) - 50) / 50)
    out["zscore_20"] = np.nan_to_num(np.where(dev > 0, (c - basis) / np.where(dev > 0, dev, 1), 0) * -1)
    out["mom_6"] = np.nan_to_num((cs / cs.shift(6) - 1).to_numpy() * -1)
    out["mom_18"] = np.nan_to_num((cs / cs.shift(18) - 1).to_numpy() * -1)
    # JS ema seeds with the first value (no warm-up), as here with adjust=False.
    out["ema_cross"] = (cs.ewm(span=12, adjust=False).mean() - cs.ewm(span=26, adjust=False).mean()).to_numpy() / c
    rng = h - l
    out["hl_mom"] = np.where(rng > 0, ((c - l) / np.where(rng > 0, rng, 1) - 0.5) * -1, 0)
    up = pd.Series(np.where(c > o, v, 0.0)).rolling(20).sum()
    dn = pd.Series(np.where(c < o, v, 0.0)).rolling(20).sum()
    out["taker_ratio"] = np.nan_to_num(((up - dn) / (up + dn).replace(0, np.nan)).to_numpy() * -1)
    return pd.DataFrame(out, index=g.index)


def _pivot_signal(h, l, c, left=7, right=1):
    n = len(c)
    out = np.zeros(n)
    last_ph = last_pl = None
    for i in range(n):
        p = i - right  # pivot candidate confirmed at bar i
        if p - left >= 0:
            if all(h[j] < h[p] for j in range(p - left, p)) and all(h[j] < h[p] for j in range(p + 1, i + 1)):
                last_ph = h[p]
            if all(l[j] > l[p] for j in range(p - left, p)) and all(l[j] > l[p] for j in range(p + 1, i + 1)):
                last_pl = l[p]
        if last_ph is not None and last_pl is not None and last_ph > last_pl:
            out[i] = -((c[i] - last_pl) / (last_ph - last_pl) - 0.5)
    return out


def orthosys(g: pd.DataFrame, params=DEFAULT) -> pd.DataFrame:
    raw = raw_signals(g)
    n = params["zsc_len"]
    z = (raw - raw.rolling(n).mean()) / raw.rolling(n).std(ddof=0)
    z = z.where(raw.rolling(n).std(ddof=0) != 0, 0).fillna(0)
    sm = z.rolling(params["lb"]).mean()
    w = pd.Series(params["weights"], dtype=float)
    comp = (sm[w.index] * w).sum(axis=1) / w.sum()
    comp.iloc[: n + params["lb"] - 2] = np.nan
    piv = _pivot_signal(g["high"].to_numpy(float), g["low"].to_numpy(float), g["close"].to_numpy(float))
    t = params["thresh"]
    no_pivot = not params["use_pivot"]
    long_ = (comp > t) & (no_pivot | (piv > params["pivot_tau"]))
    short = (comp < -t) & (no_pivot | (piv < -params["pivot_tau"]))
    pos = long_.astype(int) - short.astype(int)
    return pd.DataFrame({"composite": comp, "pivot": piv, "position": pos}, index=g.index)


def orthosys_panel(df: pd.DataFrame, params=DEFAULT) -> pd.DataFrame:
    return pd.concat([orthosys(g, params) for _, g in df.groupby(level="symbol")]).sort_index()
