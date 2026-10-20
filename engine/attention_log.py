"""Append-only log of free "attention" data (CoinGecko trending) for a later honest test.

Why: crypto "social" signals (X/Twitter, Reddit, Google Trends, Wikipedia) are the favourite alpha source of
AI agents, but from this environment those hosts are blocked or paid. CoinGecko's trending list is free,
needs no key and is reachable. Alone it proves nothing: this script only starts the history.

Pre-registered test (do NOT run before >= 14 days of hourly snapshots exist; write the result either way):
  event  = a coin enters the CoinGecko trending list (was absent in the previous snapshot), joined to the OKX perps;
  outcome = forward return over 1h / 4h / 24h / 5d minus the cross-sectional mean (market removed);
  sign   = BOTH directions are reported (the literature is split: attention pumps vs. later reversal);
  stats  = events spaced >= horizon per coin, day-clustered bootstrap CI, |t| > 3.5 needed (many tests).
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

OUT = Path(__file__).resolve().parent.parent / "results" / "live" / "attention.jsonl"
URL = "https://api.coingecko.com/api/v3/search/trending"


def parse(payload: dict) -> dict:
    coins = []
    for c in payload.get("coins", []):
        it = c.get("item", {})
        d = it.get("data") or {}
        chg = (d.get("price_change_percentage_24h") or {}).get("usd")
        coins.append({"symbol": it.get("symbol"), "id": it.get("id"), "score": it.get("score"),
                      "mcap_rank": it.get("market_cap_rank"), "price": d.get("price"), "chg24h_pct": chg})
    cats = [c.get("name") for c in payload.get("categories", [])]
    return {"coins": coins, "categories": cats}


def snapshot(now: datetime | None = None, path: Path = OUT, get=requests.get) -> dict | None:
    now = now or datetime.now(timezone.utc)
    r = get(URL, timeout=20)
    if r.status_code != 200:
        print(f"attention_log: HTTP {r.status_code}, skipped", file=sys.stderr)
        return None
    rec = {"ts": now.isoformat(), **parse(r.json())}
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(json.dumps(rec, sort_keys=True) + "\n")
    return rec


if __name__ == "__main__":
    rec = snapshot()
    print(f"logged {len(rec['coins'])} trending coins" if rec else "no snapshot")
