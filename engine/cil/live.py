"""Live market data through CCXT (public endpoints only, no API keys).

UNTESTED IN THIS ENVIRONMENT: the cloud session's network policy blocks every
exchange host. Allow api.binance.com / fapi.binance.com (or another venue) and
run `python -m cil.live` to check.

Output has the same columns as `data.load_trendscan_history`, so the feature,
model and ledger code is shared between research and live use.
"""
from __future__ import annotations

import time

import pandas as pd

DEFAULT_SYMBOLS = ["BTC", "ETH", "SOL", "AVAX", "LINK", "DOGE", "ARB", "OP", "INJ", "SUI", "NEAR", "APT", "TIA"]


def make_exchange(name: str = "binanceusdm"):
    import ccxt
    ex = getattr(ccxt, name)({"enableRateLimit": True})
    return ex


def fetch_daily(symbols=DEFAULT_SYMBOLS, days=400, exchange=None) -> pd.DataFrame:
    ex = exchange or make_exchange()
    since = ex.milliseconds() - days * 86_400_000
    frames = []
    for s in symbols:
        market = f"{s}/USDT:USDT"
        rows, cursor = [], since
        while True:
            batch = ex.fetch_ohlcv(market, "1d", since=cursor, limit=1000)
            if not batch:
                break
            rows += batch
            cursor = batch[-1][0] + 86_400_000
            if len(batch) < 1000:
                break
        k = pd.DataFrame(rows, columns=["t", "open", "high", "low", "close", "volume"]).drop_duplicates("t")
        k["date"] = pd.to_datetime(k["t"], unit="ms", utc=True).dt.normalize()
        # Drop the still-open daily candle: it is not a finished bar.
        k = k[k["t"] + 86_400_000 <= ex.milliseconds()]
        k["quote_volume"] = k["volume"] * k["close"]  # approximation; CCXT OHLCV has no quote volume
        k["trades"] = float("nan")
        try:
            fr = ex.fetch_funding_rate_history(market, since=since, limit=1000)
            f = pd.DataFrame(fr)
            f["date"] = pd.to_datetime(f["timestamp"], unit="ms", utc=True).dt.normalize()
            k = k.merge(f.groupby("date")["fundingRate"].sum().rename("funding"), on="date", how="left")
        except Exception:  # venue without funding history
            k["funding"] = float("nan")
        k["symbol"] = s
        frames.append(k.drop(columns="t"))
        time.sleep(ex.rateLimit / 1000)
    return pd.concat(frames).set_index(["date", "symbol"]).sort_index()


if __name__ == "__main__":
    df = fetch_daily(days=30)
    print(df.groupby(level="symbol").tail(1))
