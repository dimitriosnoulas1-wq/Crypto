"""Binance USD-M futures public REST client (no API key, read-only).

Uses raw endpoints instead of CCXT where CCXT drops fields we need
(taker-buy volume in klines, open-interest history).
Respects the X-MBX-USED-WEIGHT-1M header and backs off on 429/418.
"""
from __future__ import annotations

import time

import pandas as pd
import requests

BASE = "https://fapi.binance.com"
SESSION = requests.Session()
SESSION.headers["User-Agent"] = "cil-research/0.1"
KLINE_COLS = ["open_time", "open", "high", "low", "close", "volume", "close_time", "quote_volume",
              "trades", "taker_buy_base", "taker_buy_quote", "_"]
INTERVAL_MS = {"5m": 300_000, "15m": 900_000, "1h": 3_600_000, "4h": 14_400_000, "1d": 86_400_000}


class BinanceError(RuntimeError):
    pass


def get(path, params=None, retries=4):
    for attempt in range(retries):
        try:
            r = SESSION.get(BASE + path, params=params, timeout=20)
        except requests.RequestException as e:
            if attempt == retries - 1:
                raise BinanceError(f"{path}: {e}") from e
            time.sleep(2 ** attempt)
            continue
        used = int(r.headers.get("X-MBX-USED-WEIGHT-1M", 0) or 0)
        if r.status_code in (418, 429):
            time.sleep(int(r.headers.get("Retry-After", 30)))
            continue
        if r.status_code != 200:
            raise BinanceError(f"{path} {params}: HTTP {r.status_code} {r.text[:200]}")
        if used > 1800:  # limit is 2400/min; slow down well before it
            time.sleep(10)
        return r.json()
    raise BinanceError(f"{path}: retries exhausted")


def server_time_ms() -> int:
    return get("/fapi/v1/time")["serverTime"]


def universe(top_n=60, min_quote_volume=20e6) -> list[str]:
    """Most liquid USDT-margined perpetuals that are trading now. BTC is always included."""
    info = get("/fapi/v1/exchangeInfo")
    ok = {s["symbol"] for s in info["symbols"]
          if s["contractType"] == "PERPETUAL" and s["quoteAsset"] == "USDT" and s["status"] == "TRADING"}
    tick = pd.DataFrame(get("/fapi/v1/ticker/24hr"))
    tick = tick[tick.symbol.isin(ok)].copy()
    tick["quoteVolume"] = tick["quoteVolume"].astype(float)
    tick = tick[tick.quoteVolume >= min_quote_volume].sort_values("quoteVolume", ascending=False)
    syms = list(tick.symbol.head(top_n))
    if "BTCUSDT" not in syms:
        syms.insert(0, "BTCUSDT")
    return syms


def klines(symbol, interval="1h", limit=1500, start_ms=None) -> pd.DataFrame:
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    if start_ms is not None:
        params["startTime"] = int(start_ms)
    k = pd.DataFrame(get("/fapi/v1/klines", params), columns=KLINE_COLS).drop(columns="_")
    for c in KLINE_COLS[1:-1]:
        if c not in ("open_time", "close_time"):
            k[c] = k[c].astype(float)
    return k


def funding_history(symbol, start_ms) -> pd.DataFrame:
    f = pd.DataFrame(get("/fapi/v1/fundingRate", {"symbol": symbol, "startTime": int(start_ms), "limit": 1000}))
    if f.empty:
        return pd.DataFrame(columns=["fundingTime", "fundingRate"])
    f["fundingRate"] = f["fundingRate"].astype(float)
    return f[["fundingTime", "fundingRate"]]


def open_interest_hist(symbol, period="1h", limit=500) -> pd.DataFrame:
    o = pd.DataFrame(get("/futures/data/openInterestHist", {"symbol": symbol, "period": period, "limit": limit}))
    if o.empty:
        return pd.DataFrame(columns=["timestamp", "sumOpenInterestValue"])
    o["sumOpenInterestValue"] = o["sumOpenInterestValue"].astype(float)
    return o[["timestamp", "sumOpenInterestValue"]]


def last_prices() -> dict[str, float]:
    return {d["symbol"]: float(d["price"]) for d in get("/fapi/v1/ticker/price")}
