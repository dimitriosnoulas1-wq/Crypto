"""OKX public REST client for USDT-margined perpetual swaps (no API key, read-only).

Used because Binance and Bybit refuse requests from the cloud environment's
location (Binance HTTP 451 "restricted location", Bybit CloudFront country block).

Output of `fetch_panel` matches what live_cycle expects: index (date, symbol) with
open, high, low, close, volume, quote_volume, funding, taker_buy_quote, oi_value
(OKX publishes no trade counts).
Rate limits (public): candles 40/2s, history-candles 20/2s, funding 10/2s, rubik 5/2s.
"""
from __future__ import annotations

import time
from pathlib import Path

import numpy as np
import pandas as pd
import requests

BASE = "https://www.okx.com"
SESSION = requests.Session()
SESSION.headers["User-Agent"] = "cil-research/0.1"
HOUR_MS = 3_600_000
_last_call: dict[str, float] = {}
_MIN_GAP = {"history-candles": 0.11, "candles": 0.06, "funding-rate-history": 0.21, "rubik": 0.45}


class OkxError(RuntimeError):
    pass


def get(path, params=None, retries=5):
    group = next((k for k in _MIN_GAP if k in path), "")
    wait = _MIN_GAP.get(group, 0.05) - (time.time() - _last_call.get(group, 0))
    if wait > 0:
        time.sleep(wait)
    for attempt in range(retries):
        _last_call[group] = time.time()
        try:
            r = SESSION.get(BASE + path, params=params, timeout=20)
        except requests.RequestException as e:
            if attempt == retries - 1:
                raise OkxError(f"{path}: {e}") from e
            time.sleep(2 ** attempt)
            continue
        if r.status_code == 429:
            time.sleep(2 + 2 ** attempt)
            continue
        if r.status_code != 200:
            raise OkxError(f"{path} {params}: HTTP {r.status_code} {r.text[:200]}")
        j = r.json()
        if j.get("code") == "50011":  # rate limited
            time.sleep(2 + 2 ** attempt)
            continue
        if j.get("code") != "0":
            raise OkxError(f"{path} {params}: {j.get('code')} {j.get('msg')}")
        return j["data"]
    raise OkxError(f"{path}: retries exhausted")


def server_time_ms() -> int:
    return int(get("/api/v5/public/time")[0]["ts"])


def universe(top_n=60) -> tuple[list[str], dict[str, float]]:
    """Most liquid live USDT perpetuals by 24h USD volume; BTC always included. Also returns last prices."""
    # instCategory "1" = crypto; "3" = tokenised stocks, "4" = commodities (excluded).
    live = {d["instId"] for d in get("/api/v5/public/instruments", {"instType": "SWAP"})
            if d["instId"].endswith("-USDT-SWAP") and d["state"] == "live" and d.get("instCategory") == "1"}
    t = pd.DataFrame(get("/api/v5/market/tickers", {"instType": "SWAP"}))
    t = t[t.instId.isin(live)].copy()
    t["last"] = t["last"].astype(float)
    t["usd_vol"] = t["volCcy24h"].astype(float) * t["last"]
    t = t.sort_values("usd_vol", ascending=False)
    ids = list(t.instId.head(top_n))
    if "BTC-USDT-SWAP" not in ids:
        ids.insert(0, "BTC-USDT-SWAP")
    return ids, dict(zip(t.instId, t["last"]))


def candles(inst, bars=1500, since_ms=None) -> pd.DataFrame:
    """Hourly candles, oldest first. Pages backwards with `after` (100 per call)."""
    rows, after = [], None
    while len(rows) < bars:
        params = {"instId": inst, "bar": "1H", "limit": 100}
        if after:
            params["after"] = after
        page = get("/api/v5/market/history-candles", params)
        if not page:
            break
        rows += page
        after = page[-1][0]
        if since_ms is not None and int(after) <= since_ms:
            break
    k = pd.DataFrame(rows, columns=["ts", "open", "high", "low", "close", "volume_ct", "volume",
                                    "quote_volume", "confirm"]).drop_duplicates("ts")
    k["ts"] = k["ts"].astype("int64")
    for c in ("open", "high", "low", "close", "volume", "quote_volume"):
        k[c] = k[c].astype(float)
    k["confirm"] = k["confirm"].astype(int)
    return k.sort_values("ts").reset_index(drop=True)


def funding(inst, since_ms) -> pd.DataFrame:
    rows, after = [], None
    while True:
        params = {"instId": inst, "limit": 100}
        if after:
            params["after"] = after
        page = get("/api/v5/public/funding-rate-history", params)
        if not page:
            break
        rows += page
        after = page[-1]["fundingTime"]
        if int(after) <= since_ms or len(page) < 100:
            break
    f = pd.DataFrame(rows)
    if f.empty:
        return pd.DataFrame(columns=["ts", "rate"])
    return pd.DataFrame({"ts": f.fundingTime.astype("int64"), "rate": f.realizedRate.replace("", np.nan)
                         .fillna(f.fundingRate).astype(float)})


def rubik(path, inst) -> list:
    return get(f"/api/v5/rubik/stat/{path}", {"instId": inst, "period": "1H", "limit": 100})


def _accumulate(path: Path, new: pd.DataFrame) -> pd.DataFrame:
    """OKX only serves the last 100 hours of OI/taker stats; keep everything we have seen."""
    if path.exists():
        new = pd.concat([pd.read_parquet(path), new]).drop_duplicates("ts", keep="last")
    new = new.sort_values("ts").tail(5000)
    new.to_parquet(path)
    return new


def fetch_panel(top_n: int, cache: Path, log: list) -> tuple[pd.DataFrame, dict, int]:
    t0 = time.time()
    now_ms = server_time_ms()
    ids, last = universe(top_n)
    cache.mkdir(exist_ok=True)
    frames = []
    for inst in ids:
        sym = inst.split("-")[0]
        path = cache / f"okx_{inst}_1h.parquet"
        try:
            old = pd.read_parquet(path) if path.exists() else None
            if old is None:
                k = candles(inst, 1500)
            else:
                new = candles(inst, 300, since_ms=int(old.ts.max()) - 3 * HOUR_MS)
                k = pd.concat([old, new]).drop_duplicates("ts", keep="last").sort_values("ts")
            k = k.tail(2500)
            k.to_parquet(path)
            k = k[(k.confirm == 1) & (k.ts + HOUR_MS <= now_ms)].copy()   # closed bars only
            f = funding(inst, int(k.ts.min()))
            oi = pd.DataFrame(rubik("contracts/open-interest-history", inst), columns=["ts", "oi", "oi_ccy", "oi_usd"])
            oi = _accumulate(cache / f"okx_{inst}_oi.parquet", oi.astype({"ts": "int64"}))
            tk = pd.DataFrame(rubik("taker-volume-contract", inst), columns=["ts", "sell", "buy"])
            tk = _accumulate(cache / f"okx_{inst}_taker.parquet", tk.astype({"ts": "int64"}))
        except Exception as e:  # one bad instrument must not stop the cycle
            log.append(f"fetch_failed {inst}: {e}")
            continue
        k["date"] = pd.to_datetime(k.ts, unit="ms", utc=True)
        k["symbol"] = sym
        if len(f):
            f["date"] = pd.to_datetime(f.ts, unit="ms", utc=True).dt.floor("h")
            k = k.merge(f.groupby("date").rate.sum().rename("funding"), on="date", how="left")
        else:
            k["funding"] = np.nan
        k["funding"] = k["funding"].fillna(0.0)                   # no settlement in that hour
        if len(oi):
            oi["date"] = pd.to_datetime(oi.ts.astype("int64"), unit="ms", utc=True)
            k = k.merge(oi.assign(oi_value=oi.oi_usd.astype(float))[["date", "oi_value"]], on="date", how="left")
        if len(tk):
            tk["date"] = pd.to_datetime(tk.ts.astype("int64"), unit="ms", utc=True)
            b, s = tk.buy.astype(float), tk.sell.astype(float)
            tk["buy_share"] = b / (b + s).replace(0, np.nan)
            k = k.merge(tk[["date", "buy_share"]], on="date", how="left")
            k["taker_buy_quote"] = k["buy_share"] * k["quote_volume"]
        cols = ["date", "symbol", "open", "high", "low", "close", "volume", "quote_volume", "funding"]
        cols += [c for c in ("taker_buy_quote", "oi_value") if c in k]
        frames.append(k[cols])
    if not frames:
        raise OkxError("no instrument could be fetched")
    df = pd.concat(frames).set_index(["date", "symbol"]).sort_index()
    prices = {i.split("-")[0]: p for i, p in last.items() if i in ids}
    log.append(f"fetch_seconds {time.time() - t0:.1f} instruments {len(frames)}/{len(ids)}")
    return df, prices, now_ms
