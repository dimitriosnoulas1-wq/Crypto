"""Daily cross-sectional test on years of OKX daily candles (public endpoint, no keys).

Same questions as run_xs.py but with a far larger sample. Caveat printed with the results: the coin
list is today's most-traded perpetuals, so coins that died earlier are missing (survivorship bias),
and coins listed late only enter the cross-section when they have 60 days of history.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cil import okx  # noqa: E402
from run_xs import FEE_RT_LS, ROOT, evaluate, rank_cs, walk_forward_lgbm  # noqa: E402

CACHE = ROOT / "data_cache" / "daily"
HORIZONS = (1, 5, 10)


def daily(inst: str, bars=1500) -> pd.DataFrame:
    path = CACHE / f"{inst}_1d.parquet"
    if path.exists():
        return pd.read_parquet(path)
    rows, after = [], None
    while len(rows) < bars:
        params = {"instId": inst, "bar": "1D", "limit": 100}
        if after:
            params["after"] = after
        page = okx.get("/api/v5/market/history-candles", params)
        if not page:
            break
        rows += page
        after = page[-1][0]
    k = pd.DataFrame(rows, columns=["ts", "open", "high", "low", "close", "volume_ct", "volume", "quote_volume", "confirm"])
    k = k.drop_duplicates("ts")
    k["ts"] = k["ts"].astype("int64")
    for c in ("open", "high", "low", "close", "volume", "quote_volume"):
        k[c] = k[c].astype(float)
    k["confirm"] = k["confirm"].astype(int)
    k = k.sort_values("ts").reset_index(drop=True)
    CACHE.mkdir(parents=True, exist_ok=True)
    k.to_parquet(path)
    return k


def main():
    ids, _ = okx.universe(80)
    c, v, h = {}, {}, {}
    t0 = time.time()
    for i, inst in enumerate(ids):
        try:
            k = daily(inst)
        except Exception as e:
            print("skip", inst, e, flush=True)
            continue
        k = k[k.confirm == 1].set_index("ts")
        sym = inst.split("-")[0]
        c[sym], v[sym], h[sym] = k["close"], k["quote_volume"], k["high"]
        if i % 10 == 0:
            print(f"fetched {i + 1}/{len(ids)} ({time.time() - t0:.0f}s)", flush=True)
    idx = lambda d: pd.DataFrame(d).sort_index().set_axis(pd.to_datetime(pd.DataFrame(d).sort_index().index, unit="ms", utc=True))
    c, v, h = idx(c), idx(v), idx(h)
    keep = c.notna().sum() > 120
    c, v, h = c.loc[:, keep], v.loc[:, keep], h.loc[:, keep]
    print(f"panel {c.shape[1]} coins x {len(c)} days, {c.index.min().date()} -> {c.index.max().date()}", flush=True)
    lr = np.log(c).diff()
    F = {"r1": lr, "r5": np.log(c).diff(5), "r20": np.log(c).diff(20), "r60": np.log(c).diff(60),
         "vol20": lr.rolling(20).std(), "volu_z": np.log1p(v) - np.log1p(v).rolling(30).mean(),
         "dist_hi30": np.log(c / h.rolling(30).max())}
    F = {k: rank_cs(x) for k, x in F.items()}
    out = {"panel": {"coins": int(c.shape[1]), "days": int(len(c)), "from": str(c.index.min().date()), "to": str(c.index.max().date())},
           "caveat": "survivorship bias: today's top-traded perps only", "fee_round_trip_ls_bps": FEE_RT_LS * 1e4, "runs": []}
    for hz in HORIZONS:
        fwd = np.log(c).shift(-hz) - np.log(c)
        fwd = fwd.sub(fwd.mean(axis=1), axis=0)
        y = rank_cs(fwd)
        base = {"reversal(-r1)": -F["r1"], "reversal(-r5)": -F["r5"], "momentum(r20)": F["r20"], "momentum(r60)": F["r60"],
                "reversal(-r20)": -F["r20"], "low_vol(-vol20)": -F["vol20"], "volume_surge": F["volu_z"],
                "near_high(dist_hi30)": F["dist_hi30"]}
        for k, sc in base.items():
            r = evaluate(sc, fwd, hz, k); out["runs"].append(r); print(r, flush=True)
        p = walk_forward_lgbm(F, y, hz, train_days=365, step_days=60, bar=pd.Timedelta(days=1))
        r = evaluate(p, fwd, hz, "LGBM walk-forward (cross-sectional)"); out["runs"].append(r); print(r, flush=True)
    (ROOT / "results" / "xs_daily_latest.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
