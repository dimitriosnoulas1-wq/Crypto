"""What professional systematic traders do, tested honestly on our OKX daily data (4 years, up to 71 perps).

A. Time-series momentum / trend following (CTA style): per coin, long if the L-day return > 0 else short,
   sized by target_vol / realised_vol, equal-weight across coins, daily rebalance, 5 bps per side on turnover.
B. Cross-sectional momentum restricted to large caps (the literature says the effect lives in large caps).
C. Risk management on the low-vol long-short: volatility targeting and a BTC trend filter.
All numbers are net of costs; survivorship bias (today's top perps only) is NOT corrected.
"""
from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_xs import day_boot, rank_cs  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FEE = 5 / 1e4
ANN = 365


def panel():
    C, Q = [], []
    for f in glob.glob(str(ROOT / "data_cache/daily/*_1d.parquet")):
        k = pd.read_parquet(f); k = k[k.confirm == 1].set_index("ts"); s = Path(f).name.split("-")[0]
        C.append(k["close"].rename(s)); Q.append(k["quote_volume"].rename(s))
    c, q = pd.concat(C, axis=1).sort_index(), pd.concat(Q, axis=1).sort_index()
    for d in (c, q):
        d.index = pd.to_datetime(d.index, unit="ms", utc=True)
    keep = c.notna().sum() > 120
    return c.loc[:, keep].astype(float), q.loc[:, keep].astype(float)


def stats(r: pd.Series) -> dict:
    r = r.dropna()
    eq = (1 + r).cumprod()
    dd = (eq / eq.cummax() - 1).min()
    sh = r.mean() / r.std() * np.sqrt(ANN) if r.std() > 0 else 0
    yr = ((1 + r).groupby(r.index.year).prod() - 1) * 100
    return {"sharpe": round(float(sh), 2), "ann_ret_pct": round(float(r.mean() * ANN * 100), 1),
            "ann_vol_pct": round(float(r.std() * np.sqrt(ANN) * 100), 1), "max_dd_pct": round(float(dd * 100), 1),
            "by_year_pct": {int(k): round(float(v), 1) for k, v in yr.items()}}


def tsmom(c, ret, lookback, target_vol=0.5, cap=3.0, long_only=False, universe=None):
    vol = ret.rolling(20).std() * np.sqrt(ANN)
    sig = np.sign(np.log(c).diff(lookback))
    if long_only:
        sig = sig.clip(lower=0)
    lev = (target_vol / vol).clip(upper=cap)
    live = ret.notna() & vol.notna() & sig.notna()
    if universe is not None:
        live &= universe
    n = live.sum(axis=1).replace(0, np.nan)
    w = (sig * lev).where(live, 0).div(n, axis=0).fillna(0)
    gross = (w.shift(1) * ret).sum(axis=1)                       # weights set at close t-1 earn day t
    cost = FEE * (w - w.shift(1)).abs().sum(axis=1)
    return (gross - cost).iloc[lookback + 25:]


def main():
    c, q = panel()
    ret = c.pct_change()
    top20 = q.rolling(30).mean().rank(axis=1, ascending=False) <= 20
    out = {"panel": {"coins": int(c.shape[1]), "days": int(len(c)), "from": str(c.index.min().date())}, "A": {}, "B": {}, "C": {}}

    ew = ret.mean(axis=1).iloc[120:]
    out["A"]["buy&hold equal-weight (reference)"] = stats(ew)
    print("A. Trend following (time-series momentum), vol-targeted, net of 5 bps/side")
    print(f"{'ref buy&hold EW':34s}", out["A"]["buy&hold equal-weight (reference)"])
    for uni_name, uni in (("all coins", None), ("top-20 liquid", top20)):
        for L in (20, 60, 120):
            for lo in (False, True):
                nm = f"{uni_name} L={L} {'long-only' if lo else 'long/short'}"
                s = stats(tsmom(c, ret, L, long_only=lo, universe=uni)); out["A"][nm] = s
                print(f"{nm:34s} Sharpe {s['sharpe']:+.2f}  ret {s['ann_ret_pct']:+6.1f}%  vol {s['ann_vol_pct']:5.1f}%  maxDD {s['max_dd_pct']:6.1f}%  {s['by_year_pct']}")

    print("\nB. Cross-sectional momentum, large caps only (top-20 liquid), 5d hold, net 20 bps/rebalance")
    for L in (20, 60):
        fwd = np.log(c).shift(-5) - np.log(c); fwd = fwd.sub(fwd.mean(axis=1), axis=0)
        sc = rank_cs(np.log(c).diff(L)).where(top20)
        rows = []
        for t in sc.index[::5]:
            a, b = sc.loc[t].dropna(), fwd.loc[t]
            b = b[a.index].dropna(); a = a[b.index]
            if len(a) < 15:
                continue
            n = max(int(len(a) * 0.25), 2); o = a.sort_values()
            rows.append((t, b[o.index[-n:]].mean() - b[o.index[:n]].mean()))
        s = pd.Series(dict(rows)) * 1e4 - 20
        m, lo, hi = day_boot(s)
        out["B"][f"top20 momentum L={L}"] = {"net_bps": round(m, 1), "ci95": [round(lo, 1), round(hi, 1)], "n": len(s)}
        print(f"top-20 momentum L={L}: net {m:+.0f} bps [{lo:+.0f},{hi:+.0f}] n={len(s)}")

    print("\nC. Risk management on the low-vol long/short (5d rebalance, net 20 bps)")
    lr = np.log(c).diff(); vol20 = lr.rolling(20).std(); fwd = np.log(c).shift(-5) - np.log(c)
    sc = -rank_cs(vol20); rows = []
    for t in sc.index[::5]:
        a, b = sc.loc[t], fwd.loc[t]; m = a.notna() & b.notna()
        if m.sum() < 30:
            continue
        a, b = a[m], b[m]; n = max(int(len(a) * .2), 2); o = a.sort_values()
        rows.append((t, b[o.index[-n:]].mean() - b[o.index[:n]].mean() - 0.002))
    base = pd.Series(dict(rows))
    btc = c["BTC"]
    trend_ok = (btc > btc.rolling(100).mean()).reindex(base.index)
    tgt = base.rolling(12).std().shift(1)
    scale = (tgt.expanding(min_periods=12).mean() / tgt).clip(upper=2.0).fillna(1.0)   # keep average risk equal
    variants = {"plain low-vol L/S": base, "vol-targeted (inverse trailing vol)": base * scale,
                "only when BTC > 100d SMA": base.where(trend_ok, 0.0), "only when BTC < 100d SMA": base.where(~trend_ok, 0.0)}
    for nm, r in variants.items():
        sh = r.mean() / r.std() * np.sqrt(ANN / 5)
        eq = (1 + r * 0.5).cumprod()
        dd = (eq / eq.cummax() - 1).min() * 100
        worst = r.min() * 1e4
        out["C"][nm] = {"sharpe": round(float(sh), 2), "mean_bps": round(float(r.mean() * 1e4), 1), "worst_rebalance_bps": round(float(worst), 0),
                        "max_dd_pct_at_half_notional": round(float(dd), 1), "n_active": int((r != 0).sum())}
        print(f"{nm:38s} Sharpe {sh:+.2f}  mean {r.mean() * 1e4:+6.1f} bps  worst {worst:+7.0f} bps  maxDD {dd:6.1f}%  active {int((r != 0).sum())}/{len(r)}")

    print("\nD. Combining the two streams (what funds do: diversify across low-correlation strategies)")
    tr = tsmom(c, ret, 60)                                         # trend following, all coins, L=60, long/short, vol-targeted
    wins = pd.Series({t: (1 + tr[(tr.index > t) & (tr.index <= t + pd.Timedelta(days=5))]).prod() - 1 for t in base.index})
    lowvol = base * 0.5                                            # half notional per leg => gross exposure 1
    both = pd.concat({"lowvol": lowvol, "trend": wins}, axis=1).dropna()
    both = both[both.trend != 0]
    corr = float(both.corr().iloc[0, 1])
    z = both / both.std()                                          # equal risk contribution
    combo = z.mean(axis=1) * both.std().mean()
    out["D"] = {"corr_5d": round(corr, 2), "n": int(len(both))}
    print(f"correlation of 5d returns: {corr:+.2f} (n={len(both)})")
    for nm, r in {"low-vol only": both.lowvol, "trend-following only": both.trend, "50/50 equal-risk combo": combo}.items():
        sh = r.mean() / r.std() * np.sqrt(ANN / 5)
        eq = (1 + r).cumprod(); dd = (eq / eq.cummax() - 1).min() * 100
        yr = ((1 + r).groupby(r.index.year).prod() - 1) * 100
        out["D"][nm] = {"sharpe": round(float(sh), 2), "max_dd_pct": round(float(dd), 1), "by_year_pct": {int(k): round(float(v), 1) for k, v in yr.items()}}
        print(f"{nm:26s} Sharpe {sh:+.2f}  maxDD {dd:6.1f}%  by year {out['D'][nm]['by_year_pct']}")
    print("Note: Sharpe standard error over ~4 years is about +/-0.5, so differences below ~1 are not significant.")
    (ROOT / "results" / "pro_methods_latest.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
