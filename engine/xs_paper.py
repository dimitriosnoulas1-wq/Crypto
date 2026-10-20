"""Live paper track for the daily cross-sectional LOW-VOLATILITY strategy (run_xs_daily.py finding).

Rule (decided in research, not tuned here): each day, rank the liquid OKX USDT perpetuals by 20-day
volatility of daily returns (closed days only). Long the lowest-volatility quintile, short the
highest-volatility quintile, equal weight inside each leg, hold H=5 days. One book is opened per day,
so a book uses 1/H of the paper capital. Paper only: no orders, no keys. Entry/exit at the public
OKX last price when this script runs; 5 bps/side on every leg (20 bps on the long-short spread).

State is an append-only, hash-chained JSONL (results/live/xs_book.jsonl): `open` and `close` records.
Nothing is edited. Run it as often as you like; it opens at most one book per UTC day and closes books
whose maturity has passed.
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cil import okx  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "results" / "live" / "xs_book.jsonl"
H_DAYS = 5
UNIVERSE_N = 40          # most liquid perps only: research showed the edge holds (and is cleaner) there
QUINTILE = 0.2
FEE_SIDE = 5 / 1e4
CAPITAL = 1000.0
MIN_COINS = 30
VOL_WIN = 20


def _hash(prev: str, rec: dict) -> str:
    return hashlib.sha256((prev + json.dumps(rec, sort_keys=True)).encode()).hexdigest()


def read_book(path: Path = BOOK) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text().splitlines() if l.strip()]


def verify(recs: list[dict]) -> bool:
    prev = "GENESIS"
    for r in recs:
        body = {k: v for k, v in r.items() if k not in ("prev_hash", "hash")}
        if r["prev_hash"] != prev or r["hash"] != _hash(prev, body):
            return False
        prev = r["hash"]
    return True


def append(rec: dict, path: Path = BOOK) -> dict:
    recs = read_book(path)
    prev = recs[-1]["hash"] if recs else "GENESIS"
    rec = {**rec, "prev_hash": prev, "hash": _hash(prev, rec)}
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(json.dumps(rec, sort_keys=True) + "\n")
    return rec


def pick_legs(vol: pd.Series) -> tuple[list[str], list[str]]:
    vol = vol.dropna().sort_values()
    n = max(int(len(vol) * QUINTILE), 2)
    return list(vol.index[:n]), list(vol.index[-n:])          # (long low-vol, short high-vol)


def book_return(rec: dict, exit_px: dict) -> dict | None:
    """Spread return of an open book at `exit_px`; None if a leg has no price."""
    try:
        lr = [exit_px[s] / rec["entry_px"][s] - 1 for s in rec["long"]]
        sr = [exit_px[s] / rec["entry_px"][s] - 1 for s in rec["short"]]
    except KeyError:
        return None
    gross = float(np.mean(lr) - np.mean(sr))
    net = gross - 4 * FEE_SIDE
    return {"gross_bps": round(gross * 1e4, 1), "net_bps": round(net * 1e4, 1),
            "long_bps": round(float(np.mean(lr)) * 1e4, 1), "short_bps": round(float(np.mean(sr)) * 1e4, 1)}


def summary(recs: list[dict]) -> dict:
    opens = [r for r in recs if r["type"] == "open"]
    closes = [r for r in recs if r["type"] == "close"]
    eq = CAPITAL
    for c in closes:                                          # each book carries 1/H of capital, 0.5 per leg
        eq *= 1 + c["net_bps"] / 1e4 * 0.5 / H_DAYS
    return {"books_opened": len(opens), "books_closed": len(closes), "books_open": len(opens) - len(closes),
            "equity": round(eq, 2), "return_pct": round((eq / CAPITAL - 1) * 100, 3),
            "mean_net_bps": round(float(np.mean([c["net_bps"] for c in closes])), 1) if closes else None,
            "mean_mkt_bps": round(float(np.mean([c["mkt_bps"] for c in closes])), 1) if closes else None,
            "chain_valid": verify(recs)}


def run(now: datetime | None = None, path: Path = BOOK) -> dict:
    now = now or datetime.now(timezone.utc)
    ids, last = okx.universe(UNIVERSE_N)
    px = {i.split("-")[0]: float(p) for i, p in last.items() if i in ids}
    recs = read_book(path)
    done = {r["id"] for r in recs if r["type"] == "close"}

    # 1) close matured books
    for r in recs:
        if r["type"] == "open" and r["id"] not in done and now >= datetime.fromisoformat(r["matures_at"]):
            res = book_return(r, px)
            if res is None:
                continue
            mk = float(np.mean([px[s] / r["entry_px"][s] - 1 for s in r["entry_px"] if s in px])) * 1e4
            append({"type": "close", "id": r["id"], "closed_at": now.isoformat(), "mkt_bps": round(mk, 1), **res}, path)

    # 2) open today's book (once per UTC day)
    today = now.date().isoformat()
    if not any(r["type"] == "open" and r["id"] == today for r in read_book(path)):
        closes = {}
        for inst in ids:
            sym = inst.split("-")[0]
            try:
                k = daily_closed(inst)
            except Exception:
                continue
            if len(k) >= VOL_WIN + 5:
                closes[sym] = k
        panel = pd.DataFrame(closes).sort_index()
        panel = panel[panel.index < pd.Timestamp(now.date(), tz="UTC")]       # closed days only
        vol = np.log(panel).diff().tail(VOL_WIN).std()
        vol = vol[vol.index.isin(px)]
        if vol.notna().sum() >= MIN_COINS:
            lo, hi = pick_legs(vol)
            append({"type": "open", "id": today, "opened_at": now.isoformat(),
                    "matures_at": (now + timedelta(days=H_DAYS)).isoformat(), "h_days": H_DAYS,
                    "long": lo, "short": hi, "entry_px": {s: px[s] for s in lo + hi},
                    "universe": int(vol.notna().sum()), "vol_long_mean": round(float(vol[lo].mean()), 4),
                    "vol_short_mean": round(float(vol[hi].mean()), 4)}, path)
    return summary(read_book(path))


def daily_closed(inst: str) -> pd.Series:
    """Recent daily closes for one instrument (closed days)."""
    page = okx.get("/api/v5/market/history-candles", {"instId": inst, "bar": "1D", "limit": 100})
    k = pd.DataFrame(page, columns=["ts", "o", "h", "l", "c", "v1", "v2", "qv", "confirm"])
    k = k[k.confirm == "1"]
    s = pd.Series(k["c"].astype(float).to_numpy(), index=pd.to_datetime(k["ts"].astype("int64"), unit="ms", utc=True))
    return s.sort_index()


# ---------------------------------------------------------------------------------------------
# Sleeve 2: trend following (time-series momentum), the classic CTA sleeve. Research: run_pro_methods.py.
# Per liquid coin: sign of the TREND_L-day return, sized by target_vol / 20d realised vol (cap 3x),
# equal weight across coins, rebalanced daily, 5 bps per side on turnover. Low correlation (+0.08) with
# the low-vol sleeve; the 50/50 combination had a higher Sharpe and half the drawdown in research.
TREND_BOOK = ROOT / "results" / "live" / "trend_book.jsonl"
TREND_L = 60
TARGET_VOL = 0.5
LEV_CAP = 3.0


def trend_weights(closes: pd.DataFrame) -> pd.Series:
    """closes: closed daily closes (rows = days, cols = coins). Weights for the next day, summing |w|/N-scaled."""
    ok = closes.notna().sum() >= TREND_L + 25
    closes = closes.loc[:, ok]
    sig = np.sign(np.log(closes.iloc[-1] / closes.iloc[-1 - TREND_L]))
    vol = np.log(closes).diff().tail(20).std() * np.sqrt(365)
    lev = (TARGET_VOL / vol).clip(upper=LEV_CAP)
    w = (sig * lev).dropna()
    return w / max(len(w), 1)


def trend_summary(recs: list[dict]) -> dict:
    closes = [r for r in recs if r["type"] == "close"]
    eq = CAPITAL
    for c in closes:
        eq *= 1 + c["net_bps"] / 1e4
    return {"days_closed": len(closes), "equity": round(eq, 2), "return_pct": round((eq / CAPITAL - 1) * 100, 3),
            "mean_net_bps_per_day": round(float(np.mean([c["net_bps"] for c in closes])), 1) if closes else None,
            "chain_valid": verify(recs)}


def run_trend(now: datetime | None = None, path: Path = TREND_BOOK) -> dict:
    now = now or datetime.now(timezone.utc)
    ids, last = okx.universe(UNIVERSE_N)
    px = {i.split("-")[0]: float(p) for i, p in last.items() if i in ids}
    recs = read_book(path)
    today = now.date().isoformat()
    if any(r["type"] == "open" and r["id"] == today for r in recs):
        return trend_summary(recs)
    opens = [r for r in recs if r["type"] == "open"]
    closed_ids = {r["id"] for r in recs if r["type"] == "close"}

    series = {}
    for inst in ids:
        try:
            series[inst.split("-")[0]] = daily_closed(inst)
        except Exception:
            continue
    closes = pd.DataFrame(series).sort_index()
    closes = closes[closes.index < pd.Timestamp(now.date(), tz="UTC")]
    if closes.shape[1] < MIN_COINS:
        return trend_summary(recs)
    w_new = trend_weights(closes).to_dict()

    prev = opens[-1] if opens and opens[-1]["id"] not in closed_ids else None
    if prev is not None:                                           # close yesterday's weights at today's price
        gross = sum(w * (px[s] / prev["entry_px"][s] - 1) for s, w in prev["weights"].items() if s in px and s in prev["entry_px"])
        turnover = sum(abs(w_new.get(s, 0.0) - prev["weights"].get(s, 0.0)) for s in set(w_new) | set(prev["weights"]))
        net = gross - FEE_SIDE * turnover
        append({"type": "close", "id": prev["id"], "closed_at": now.isoformat(), "gross_bps": round(gross * 1e4, 1),
                "turnover": round(turnover, 3), "net_bps": round(net * 1e4, 1)}, path)
    append({"type": "open", "id": today, "opened_at": now.isoformat(), "lookback": TREND_L,
            "weights": {s: round(float(w), 5) for s, w in w_new.items()},
            "entry_px": {s: px[s] for s in w_new if s in px}, "gross_exposure": round(float(sum(abs(v) for v in w_new.values())), 3)}, path)
    return trend_summary(read_book(path))


if __name__ == "__main__":
    print(json.dumps({"lowvol_5d": run(), "trend_60d": run_trend()}, indent=1))
