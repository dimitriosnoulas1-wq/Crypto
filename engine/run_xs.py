"""Cross-sectional ("which coins beat the others") research on the accumulated OKX hourly history.

Why: the live models predict absolute up/down per coin, which is dominated by the common market
move (all coins fall together). Ranking coins against each other removes that factor and is the
standard formulation in the literature. This is an offline, walk-forward test; nothing here writes
to the live ledger.

Setup: closed 1h bars, features known at bar close t, target = forward return over h bars minus the
cross-sectional mean at t. Entry at the bar close (the live system enters ~7 min later, which costs
slippage not modelled here: the h=1 numbers are therefore optimistic). Portfolio: long top quintile,
short bottom quintile, rebalanced every h bars (non-overlapping), 5 bps/side/leg => 20 bps per
rebalance on the long-short spread. Confidence intervals resample whole days.
"""
from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from lightgbm import LGBMRegressor

ROOT = Path(__file__).resolve().parent.parent
FEE_RT_LS = 4 * 5 / 1e4          # 2 legs x (entry+exit) x 5 bps
HORIZONS = (1, 4, 24)
MIN_COINS = 30


def load_panel() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    close, vol, high = {}, {}, {}
    for f in glob.glob(str(ROOT / "data_cache" / "okx_*-USDT-SWAP_1h.parquet")):
        sym = Path(f).name.split("_")[1].split("-")[0]
        k = pd.read_parquet(f)
        k = k[k.confirm == 1].drop_duplicates("ts").set_index("ts").sort_index()
        close[sym], vol[sym] = k["close"].astype(float), k["quote_volume"].astype(float)
        high[sym] = k["high"].astype(float)
    c = pd.DataFrame(close).sort_index()
    idx = pd.to_datetime(c.index, unit="ms", utc=True)
    c.index = idx
    v = pd.DataFrame(vol).sort_index(); v.index = idx
    h = pd.DataFrame(high).sort_index(); h.index = idx
    keep = c.notna().sum() > 24 * 20
    return c.loc[:, keep], v.loc[:, keep], h.loc[:, keep]


def rank_cs(df: pd.DataFrame) -> pd.DataFrame:
    return df.rank(axis=1, pct=True) - 0.5


def features(c, v, h) -> dict[str, pd.DataFrame]:
    lr = np.log(c).diff()
    f = {
        "r1": lr,
        "r4": np.log(c).diff(4),
        "r24": np.log(c).diff(24),
        "r72": np.log(c).diff(72),
        "vol24": lr.rolling(24).std(),
        "volu_z": np.log1p(v) - np.log1p(v).rolling(72).mean(),
        "dist_hi24": np.log(c / h.rolling(24).max()),
        "r1_vs_vol": lr / lr.rolling(24).std(),
    }
    return {k: rank_cs(x) for k, x in f.items()}


def day_boot(x: pd.Series, n=2000, seed=0):
    """Mean and 95% CI resampling whole days."""
    g = x.groupby(x.index.date).agg(["sum", "count"])
    s, k = g["sum"].to_numpy(), g["count"].to_numpy()
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(s), (n, len(s)))
    m = s[idx].sum(1) / k[idx].sum(1)
    return float(x.mean()), float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))


def evaluate(score: pd.DataFrame, fwd: pd.DataFrame, h: int, label: str) -> dict:
    """score/fwd: bars x coins (fwd already demeaned across coins). Non-overlapping every h bars."""
    s = score.iloc[::h]
    f = fwd.reindex(s.index)
    ic, ls = [], []
    for t in s.index:
        a, b = s.loc[t], f.loc[t]
        m = a.notna() & b.notna()
        if m.sum() < MIN_COINS:
            continue
        a, b = a[m], b[m]
        ic.append((t, a.rank().corr(b.rank())))
        n = max(int(len(a) * 0.2), 2)
        order = a.sort_values()
        ls.append((t, b[order.index[-n:]].mean() - b[order.index[:n]].mean()))
    ic = pd.Series(dict(ic)); ls = pd.Series(dict(ls))
    if len(ls) < 30:
        return {"label": label, "bars": len(ls)}
    ic_m, ic_lo, ic_hi = day_boot(ic)
    g_m, g_lo, g_hi = day_boot(ls * 1e4)
    n_m, n_lo, n_hi = day_boot(ls * 1e4 - FEE_RT_LS * 1e4)
    return {"label": label, "h": h, "rebalances": len(ls), "days": int(ls.index.normalize().nunique()),
            "ic_mean": round(ic_m, 4), "ic_ci95": [round(ic_lo, 4), round(ic_hi, 4)],
            "ls_gross_bps": round(g_m, 1), "ls_gross_ci95": [round(g_lo, 1), round(g_hi, 1)],
            "ls_net_bps": round(n_m, 1), "ls_net_ci95": [round(n_lo, 1), round(n_hi, 1)],
            "hit_net": round(float(((ls * 1e4 - FEE_RT_LS * 1e4) > 0).mean()), 3)}


def walk_forward_lgbm(F: dict, y: pd.DataFrame, h: int, train_days=35, step_days=7, bar=pd.Timedelta(hours=1)) -> pd.DataFrame:
    names = list(F)
    idx = y.index
    stack = pd.concat({k: F[k].stack(future_stack=True) for k in names}, axis=1)
    stack["y"] = y.stack(future_stack=True)
    stack = stack.dropna(subset=names)
    pred = pd.Series(np.nan, index=stack.index)
    t0 = idx[0] + pd.Timedelta(days=train_days)
    starts = pd.date_range(t0, idx[-1], freq=f"{step_days}D")
    for a in starts:
        b = a + pd.Timedelta(days=step_days)
        tr = stack[(stack.index.get_level_values(0) < a - h * bar) & stack.y.notna()]
        te = stack[(stack.index.get_level_values(0) >= a) & (stack.index.get_level_values(0) < b)]
        if len(tr) < 5000 or te.empty:
            continue
        m = LGBMRegressor(n_estimators=150, learning_rate=0.03, num_leaves=7, min_child_samples=300,
                          subsample=0.7, subsample_freq=1, colsample_bytree=0.8, reg_lambda=10,
                          random_state=3, verbose=-1).fit(tr[names], tr["y"])
        pred.loc[te.index] = m.predict(te[names])
    return pred.unstack().reindex(idx)


def main():
    c, v, hi = load_panel()
    print(f"panel: {c.shape[1]} coins, {len(c)} hourly bars, {c.index.min()} -> {c.index.max()}", flush=True)
    F = features(c, v, hi)
    out = {"panel": {"coins": int(c.shape[1]), "bars": int(len(c)), "from": str(c.index.min()), "to": str(c.index.max())},
           "fee_round_trip_ls_bps": FEE_RT_LS * 1e4, "runs": []}
    for h in HORIZONS:
        fwd = np.log(c).shift(-h) - np.log(c)
        fwd = fwd.sub(fwd.mean(axis=1), axis=0)                 # cross-sectional demeaning
        y = rank_cs(fwd)
        base = {"reversal(-r1)": -F["r1"], "reversal(-r4)": -F["r4"], "momentum(r24)": F["r24"],
                "reversal(-r24)": -F["r24"], "momentum(r72)": F["r72"], "low_vol(-vol24)": -F["vol24"],
                "volume_surge(volu_z)": F["volu_z"], "near_high(dist_hi24)": F["dist_hi24"]}
        for k, sc in base.items():
            r = evaluate(sc, fwd, h, k); out["runs"].append(r); print(r, flush=True)
        p = walk_forward_lgbm(F, y, h)
        r = evaluate(p, fwd, h, "LGBM walk-forward (cross-sectional)"); out["runs"].append(r); print(r, flush=True)
    (ROOT / "results" / "xs_latest.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
