"""Independent check of scored predictions against OKX candles (read-only).

Re-downloads candles straight from OKX (no cache, separate code path from the pipeline)
and verifies, for every resolved prediction (or those of one `--asof` bar):
  - instrument exists as a live crypto USDT perpetual (instCategory 1);
  - ref_price == close of the prediction bar, and that bar was confirmed;
  - exit_price == close of bar asof + h hours, confirmed;
  - written after the input bar closed, and before the outcome bar closed (no future data);
  - fwd_ret and up are consistent with the prices;
  - each prediction has at most one outcome.
Prints a summary and every mismatch.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd

from cil import okx

ROOT = Path(__file__).resolve().parent.parent
H = pd.Timedelta(hours=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", default=str(ROOT / "results" / "live" / "ledger_okx.sqlite"))
    ap.add_argument("--asof", default=None, help="only predictions of this bar (open time, UTC)")
    a = ap.parse_args()
    db = sqlite3.connect(f"file:{a.ledger}?mode=ro", uri=True)
    q = ("SELECT p.id, p.created_at, p.asof, p.symbol, p.horizon_days, p.model, p.ref_price, "
         "o.exit_price, o.fwd_ret, o.up, o.resolved_at FROM predictions p JOIN outcomes o ON o.prediction_id = p.id")
    r = pd.read_sql_query(q, db)
    if a.asof:
        r = r[pd.to_datetime(r["asof"]) == pd.Timestamp(a.asof, tz="UTC")]
    dup = db.execute("SELECT prediction_id, COUNT(*) FROM outcomes GROUP BY prediction_id HAVING COUNT(*) > 1").fetchall()
    crypto = {d["instId"] for d in okx.get("/api/v5/public/instruments", {"instType": "SWAP"})
              if d.get("instCategory") == "1" and d["instId"].endswith("-USDT-SWAP")}

    problems, checked = [], 0
    for sym, g in r.groupby("symbol"):
        inst = f"{sym}-USDT-SWAP"
        if inst not in crypto:
            problems.append(f"{sym}: {inst} is not a live crypto USDT swap")
            continue
        k = okx.candles(inst, 200)                       # fresh download, no cache
        k["date"] = pd.to_datetime(k.ts, unit="ms", utc=True)
        k = k.set_index("date")
        for row in g.itertuples():
            asof = pd.Timestamp(row.asof)
            end = asof + row.horizon_days * H
            created = pd.Timestamp(row.created_at)
            for t, want, label in ((asof, row.ref_price, "ref"), (end, row.exit_price, "exit")):
                if t not in k.index:
                    problems.append(f"{sym} id={row.id} h={row.horizon_days}: {label} bar {t} not found on OKX")
                elif int(k.loc[t, "confirm"]) != 1:
                    problems.append(f"{sym} id={row.id}: {label} bar {t} not confirmed on OKX")
                elif not np.isclose(k.loc[t, "close"], want, rtol=0, atol=1e-12 + 1e-9 * abs(want)):
                    problems.append(f"{sym} id={row.id} h={row.horizon_days}: {label} {want} != OKX close {k.loc[t, 'close']} at {t}")
            if not created >= asof + H:
                problems.append(f"{sym} id={row.id}: written {created} before input bar closed {asof + H}")
            if not created < end + H:
                problems.append(f"{sym} id={row.id}: written {created} after outcome bar closed {end + H} (future known)")
            if not np.isclose(row.fwd_ret, np.log(row.exit_price / row.ref_price)) or row.up != int(row.fwd_ret > 0):
                problems.append(f"{sym} id={row.id}: fwd_ret/up inconsistent")
            checked += 1
    out = {"resolved_checked": checked, "symbols": int(r.symbol.nunique()), "duplicate_outcomes": dup,
           "problems": len(problems), "by_horizon": r.groupby("horizon_days").size().to_dict(),
           "asof_bars": sorted(r["asof"].unique().tolist())}
    print(json.dumps(out, indent=1, default=str))
    for p in problems[:50]:
        print("PROBLEM", p)


if __name__ == "__main__":
    main()
