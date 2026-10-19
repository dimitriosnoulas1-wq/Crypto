"""Market data loading.

Two sources:
- `load_trendscan_history`: real Binance USD-M futures daily klines + funding
  events committed in the TrendScan repository (2022-01 .. 2025-07, 13 coins).
- `live.py`: CCXT-based live fetchers (need network access to the exchanges).

Every frame is indexed by (date, symbol) and only ever uses data that existed
at the close of that date.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

DEFAULT_HISTORY = Path(
    "/home/user/crypto-intelligence-lab/sources/repositories/screeners/"
    "trend-scan.github.io/data/historical"
)


def _load_symbol(folder: Path) -> pd.DataFrame:
    klines = pd.DataFrame(json.loads((folder / "klines_1d.json").read_text()))
    klines = klines.rename(
        columns={"o": "open", "h": "high", "l": "low", "c": "close",
                 "v": "volume", "q": "quote_volume", "n": "trades"}
    )
    klines["date"] = pd.to_datetime(klines["t"], unit="ms", utc=True).dt.normalize()
    klines = klines[["date", "open", "high", "low", "close", "volume", "quote_volume", "trades"]]

    funding = pd.DataFrame(json.loads((folder / "funding.json").read_text()))
    if funding.empty:
        klines["funding"] = np.nan
    else:
        funding["date"] = pd.to_datetime(funding["t"], unit="ms", utc=True).dt.normalize()
        # Sum of funding payments settled during that UTC day (8h or 4h intervals).
        daily = funding.groupby("date")["rate"].sum().rename("funding")
        klines = klines.merge(daily, on="date", how="left")

    klines["symbol"] = folder.name
    return klines


def load_trendscan_history(path: Path = DEFAULT_HISTORY) -> pd.DataFrame:
    frames = [_load_symbol(p) for p in sorted(path.iterdir()) if p.is_dir()]
    df = pd.concat(frames, ignore_index=True)
    df = df.drop_duplicates(["date", "symbol"]).sort_values(["symbol", "date"])
    return df.set_index(["date", "symbol"]).sort_index()


def quality_report(df: pd.DataFrame) -> pd.DataFrame:
    """Per-symbol coverage, gaps and suspicious bars."""
    rows = []
    for sym, g in df.groupby(level="symbol"):
        dates = g.index.get_level_values("date")
        expected = pd.date_range(dates.min(), dates.max(), freq="D")
        bad_bars = ((g["high"] < g[["open", "close"]].max(axis=1)) |
                    (g["low"] > g[["open", "close"]].min(axis=1)) |
                    (g["close"] <= 0)).sum()
        rows.append({
            "symbol": sym, "first": dates.min().date(), "last": dates.max().date(),
            "bars": len(g), "missing_days": len(expected) - len(g),
            "bad_bars": int(bad_bars),
            "funding_missing_days": int(g["funding"].isna().sum()),
        })
    return pd.DataFrame(rows).set_index("symbol")
