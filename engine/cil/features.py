"""Feature engineering.

Rule: a feature at row (date d, symbol s) may only use bars with date <= d.
`tests/test_leakage.py` enforces this by recomputing features on truncated
history and checking that past rows do not change.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def rsi_wilder(close: pd.Series, period: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0).ewm(alpha=1 / period, adjust=False, min_periods=period).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1 / period, adjust=False, min_periods=period).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def robust_z(x: pd.Series, window: int) -> pd.Series:
    med = x.rolling(window, min_periods=window // 2).median()
    mad = (x - med).abs().rolling(window, min_periods=window // 2).median()
    return (x - med) / (1.4826 * mad.replace(0, np.nan))


def _symbol_features(g: pd.DataFrame) -> pd.DataFrame:
    c = g["close"]
    logc = np.log(c)
    r1 = logc.diff()
    f = pd.DataFrame(index=g.index)
    for n in (1, 3, 7, 14, 30, 90):
        f[f"ret_{n}"] = logc.diff(n)
    f["vol_7"] = r1.rolling(7, min_periods=5).std()
    f["vol_30"] = r1.rolling(30, min_periods=20).std()
    f["vol_ratio"] = f["vol_7"] / f["vol_30"]
    # Momentum scaled by volatility (comparable across coins).
    f["mom_7_z"] = f["ret_7"] / (f["vol_30"] * np.sqrt(7))
    f["mom_30_z"] = f["ret_30"] / (f["vol_30"] * np.sqrt(30))
    f["rsi_14"] = rsi_wilder(c, 14)
    ema12 = c.ewm(span=12, adjust=False, min_periods=12).mean()
    ema26 = c.ewm(span=26, adjust=False, min_periods=26).mean()
    macd = ema12 - ema26
    f["macd_hist_n"] = (macd - macd.ewm(span=9, adjust=False, min_periods=9).mean()) / c
    for n in (20, 50, 200):
        f[f"dist_sma_{n}"] = c / c.rolling(n, min_periods=n).mean() - 1
    f["range_n"] = (g["high"] - g["low"]) / c
    f["close_pos"] = (c - g["low"]) / (g["high"] - g["low"]).replace(0, np.nan)
    f["qvol_z"] = robust_z(np.log(g["quote_volume"].replace(0, np.nan)), 30)
    f["trades_z"] = robust_z(np.log(g["trades"].replace(0, np.nan)), 30)
    fund = g["funding"]
    f["funding_1d"] = fund
    f["funding_7d"] = fund.rolling(7, min_periods=5).sum()
    f["funding_z"] = robust_z(fund, 60)
    f["drawdown_90"] = c / c.rolling(90, min_periods=30).max() - 1
    # Optional live-only inputs (Binance klines / OI history); absent in the daily archive.
    if "taker_buy_quote" in g:
        tr = g["taker_buy_quote"] / g["quote_volume"].replace(0, np.nan)
        f["taker_ratio"] = tr
        f["taker_ratio_24"] = tr.rolling(24, min_periods=12).mean()
    if "oi_value" in g:
        oi = np.log(g["oi_value"].replace(0, np.nan))
        f["oi_chg_1"] = oi.diff()
        f["oi_chg_24"] = oi.diff(24)
        f["oi_chg_z"] = robust_z(oi.diff(), 72)
    return f


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    parts = [_symbol_features(g) for _, g in df.groupby(level="symbol", group_keys=False)]
    feats = pd.concat(parts).sort_index()

    # Market (BTC) context, joined by date. BTC's own row gets the same values.
    btc = feats.xs("BTC", level="symbol")[["ret_1", "ret_7", "ret_30", "vol_30", "dist_sma_200"]]
    btc = btc.add_prefix("btc_")
    feats = feats.join(btc, on="date")

    # Rolling 60d beta to BTC and the idiosyncratic part of the last 7 days (Argus idea).
    r1 = feats["ret_1"]
    br1 = feats["btc_ret_1"]
    cov = (r1 * br1).groupby(level="symbol").transform(lambda s: s.rolling(60, min_periods=30).mean()) - \
        r1.groupby(level="symbol").transform(lambda s: s.rolling(60, min_periods=30).mean()) * \
        br1.groupby(level="symbol").transform(lambda s: s.rolling(60, min_periods=30).mean())
    var = br1.groupby(level="symbol").transform(lambda s: s.rolling(60, min_periods=30).var(ddof=0))
    feats["beta_60"] = cov / var.replace(0, np.nan)
    feats["idio_7"] = feats["ret_7"] - feats["beta_60"] * feats["btc_ret_7"]

    # Cross-sectional ranks per date (only coins listed on that date).
    for col in ("ret_7", "ret_30", "funding_7d", "qvol_z"):
        feats[f"xs_rank_{col}"] = feats.groupby(level="date")[col].rank(pct=True)
    return feats

