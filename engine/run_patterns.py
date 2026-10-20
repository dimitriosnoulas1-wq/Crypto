"""Event study of classic technical signals (RSI, candlestick patterns, chart patterns) on OKX data.

Design rules (the reason the GitHub libraries are NOT used as-is):
* Every signal at bar t uses only bars <= t. Pivots (needed for double tops, head & shoulders,
  triangles) are confirmed K bars after they form, and a pattern fires only when the CLOSE breaks the
  neckline / trendline. (scipy argrelextrema-style detectors look at future bars and leak.)
* Outcome = forward return over h bars minus the cross-sectional mean of all coins at t (market removed),
  signed by the signal direction (+1 bullish / -1 bearish).
* Events of the same coin closer than h bars are dropped (no overlap). 10 bps round-trip cost.
* Confidence intervals resample whole days. ~100 signal x horizon tests are run, so a signal is called
  "survives" only if |t| > 3.5 (Bonferroni-like), not just if its 95% CI misses zero.
"""
from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
ROOT = Path(__file__).resolve().parent.parent
COST = 10 / 1e4


def load(kind: str):
    pat = "data_cache/daily/*_1d.parquet" if kind == "daily" else "data_cache/okx_*-USDT-SWAP_1h.parquet"
    o, h, l, c = {}, {}, {}, {}
    for f in glob.glob(str(ROOT / pat)):
        name = Path(f).name
        sym = name.split("-")[0] if kind == "daily" else name.split("_")[1].split("-")[0]
        k = pd.read_parquet(f)
        k = k[k.confirm == 1].drop_duplicates("ts").set_index("ts").sort_index()
        o[sym], h[sym], l[sym], c[sym] = k["open"], k["high"], k["low"], k["close"]
    out = []
    for d in (o, h, l, c):
        df = pd.DataFrame(d).sort_index()
        df.index = pd.to_datetime(df.index, unit="ms", utc=True)
        out.append(df.astype(float))
    keep = out[3].notna().sum() > (120 if kind == "daily" else 24 * 20)
    return [x.loc[:, keep] for x in out]


def rsi(c: pd.DataFrame, n=14) -> pd.DataFrame:
    d = c.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / dn.replace(0, np.nan))


def candle_signals(o, h, l, c, trend_n) -> dict[str, pd.DataFrame]:
    body, rng = (c - o).abs(), (h - l).replace(0, np.nan)
    upper, lower = h - np.maximum(o, c), np.minimum(o, c) - l
    down, up = c < c.shift(trend_n), c > c.shift(trend_n)
    o1, c1, o2, c2 = o.shift(1), c.shift(1), o.shift(2), c.shift(2)
    hammer = (lower >= 2 * body) & (upper <= 0.3 * body + 1e-12) & (body / rng < 0.4) & down
    star = (upper >= 2 * body) & (lower <= 0.3 * body + 1e-12) & (body / rng < 0.4) & up
    bull_eng = (c1 < o1) & (c > o) & (o <= c1) & (c >= o1) & down
    bear_eng = (c1 > o1) & (c < o) & (o >= c1) & (c <= o1) & up
    long_bear2 = (c2 < o2) & ((o2 - c2) / (h.shift(2) - l.shift(2)).replace(0, np.nan) > 0.6)
    long_bull2 = (c2 > o2) & ((c2 - o2) / (h.shift(2) - l.shift(2)).replace(0, np.nan) > 0.6)
    small1 = (c1 - o1).abs() < 0.3 * (o2 - c2).abs()
    morning = long_bear2 & small1 & (c > o) & (c > (o2 + c2) / 2)
    small1b = (c1 - o1).abs() < 0.3 * (c2 - o2).abs()
    evening = long_bull2 & small1b & (c < o) & (c < (o2 + c2) / 2)
    sig = lambda bull, bear: bull.astype(float).fillna(0) - bear.astype(float).fillna(0)
    return {"hammer(bull)": sig(hammer, hammer & False), "shooting_star(bear)": sig(star & False, star),
            "engulfing(bull)": sig(bull_eng, bull_eng & False), "engulfing(bear)": sig(bear_eng & False, bear_eng),
            "morning_star(bull)": sig(morning, morning & False), "evening_star(bear)": sig(evening & False, evening)}


def pivot_patterns(h: pd.Series, l: pd.Series, c: pd.Series, k: int, tol=0.03, min_gap=4, max_span=80):
    """Causal pattern detection on one coin. Returns dict name -> +1/-1 series (fires on the breakout close)."""
    n = len(c)
    H, L, C = h.to_numpy(), l.to_numpy(), c.to_numpy()
    ph = (h.shift(k) == h.rolling(2 * k + 1).max()).to_numpy()      # pivot at t-k, known at t
    pl = (l.shift(k) == l.rolling(2 * k + 1).min()).to_numpy()
    out = {nm: np.zeros(n) for nm in ("double_top(bear)", "double_bottom(bull)", "head_shoulders(bear)",
                                       "inv_head_shoulders(bull)", "triangle_break_up(bull)", "triangle_break_down(bear)")}
    highs, lows = [], []                                           # (index of pivot, value)
    fired = {nm: -10**9 for nm in out}
    for t in range(n):
        if ph[t] and t - k >= 0:
            highs.append((t - k, H[t - k]))
        if pl[t] and t - k >= 0:
            lows.append((t - k, L[t - k]))
        highs, lows = highs[-4:], lows[-4:]
        if t == 0 or np.isnan(C[t]) or np.isnan(C[t - 1]):
            continue
        # double top: two similar highs, a valley between; fires when close breaks the valley
        if len(highs) >= 2:
            (i1, v1), (i2, v2) = highs[-2:]
            val = [v for (j, v) in lows if i1 < j < i2]
            if val and abs(v1 - v2) / max(v1, v2) < tol and min_gap <= i2 - i1 <= max_span and (min(v1, v2) - min(val)) / min(v1, v2) > tol:
                neck = min(val)
                if C[t] < neck <= C[t - 1] and t - fired["double_top(bear)"] > max_span:
                    out["double_top(bear)"][t] = -1; fired["double_top(bear)"] = t
        if len(lows) >= 2:
            (i1, v1), (i2, v2) = lows[-2:]
            val = [v for (j, v) in highs if i1 < j < i2]
            if val and abs(v1 - v2) / max(v1, v2) < tol and min_gap <= i2 - i1 <= max_span and (max(val) - max(v1, v2)) / max(v1, v2) > tol:
                neck = max(val)
                if C[t] > neck >= C[t - 1] and t - fired["double_bottom(bull)"] > max_span:
                    out["double_bottom(bull)"][t] = 1; fired["double_bottom(bull)"] = t
        # head & shoulders: three highs, middle highest, shoulders similar; neckline = lower of the two valleys
        if len(highs) >= 3:
            (i1, a), (i2, b), (i3, d) = highs[-3:]
            vs = [v for (j, v) in lows if i1 < j < i3]
            if vs and b > a and b > d and abs(a - d) / max(a, d) < tol and (b - max(a, d)) / b > 0.02 and i3 - i1 <= max_span:
                neck = min(vs)
                if C[t] < neck <= C[t - 1] and t - fired["head_shoulders(bear)"] > max_span:
                    out["head_shoulders(bear)"][t] = -1; fired["head_shoulders(bear)"] = t
        if len(lows) >= 3:
            (i1, a), (i2, b), (i3, d) = lows[-3:]
            vs = [v for (j, v) in highs if i1 < j < i3]
            if vs and b < a and b < d and abs(a - d) / max(a, d) < tol and (min(a, d) - b) / min(a, d) > 0.02 and i3 - i1 <= max_span:
                neck = max(vs)
                if C[t] > neck >= C[t - 1] and t - fired["inv_head_shoulders(bull)"] > max_span:
                    out["inv_head_shoulders(bull)"][t] = 1; fired["inv_head_shoulders(bull)"] = t
        # symmetrical triangle: falling highs + rising lows; fires on a close beyond the last pivot
        if len(highs) >= 2 and len(lows) >= 2 and highs[-1][1] < highs[-2][1] and lows[-1][1] > lows[-2][1]:
            if C[t] > highs[-1][1] >= C[t - 1] and t - fired["triangle_break_up(bull)"] > max_span:
                out["triangle_break_up(bull)"][t] = 1; fired["triangle_break_up(bull)"] = t
            if C[t] < lows[-1][1] <= C[t - 1] and t - fired["triangle_break_down(bear)"] > max_span:
                out["triangle_break_down(bear)"][t] = -1; fired["triangle_break_down(bear)"] = t
    return {k_: pd.Series(v, index=c.index) for k_, v in out.items()}


def rsi_divergence(l, h, c, r, k):
    """Causal RSI divergence on pivots: price lower low but RSI higher low (bull), mirror for bear."""
    bull = pd.DataFrame(0.0, index=c.index, columns=c.columns)
    bear = bull.copy()
    for s in c.columns:
        pl = (l[s].shift(k) == l[s].rolling(2 * k + 1).min()).to_numpy()
        ph = (h[s].shift(k) == h[s].rolling(2 * k + 1).max()).to_numpy()
        Lv, Hv, R = l[s].to_numpy(), h[s].to_numpy(), r[s].to_numpy()
        lows, highs = [], []
        b, br = np.zeros(len(c)), np.zeros(len(c))
        for t in range(len(c)):
            if pl[t] and t - k >= 0:
                lows.append((t - k, Lv[t - k], R[t - k])); lows = lows[-2:]
                if len(lows) == 2 and lows[1][1] < lows[0][1] and lows[1][2] > lows[0][2] + 2 and lows[0][2] < 40 and t - lows[0][0] < 60:
                    b[t] = 1                                    # known at t (pivot confirmed now)
            if ph[t] and t - k >= 0:
                highs.append((t - k, Hv[t - k], R[t - k])); highs = highs[-2:]
                if len(highs) == 2 and highs[1][1] > highs[0][1] and highs[1][2] < highs[0][2] - 2 and highs[0][2] > 60 and t - highs[0][0] < 60:
                    br[t] = -1
        bull[s], bear[s] = b, br
    return {"rsi_bull_divergence": bull, "rsi_bear_divergence": bear}


def all_signals(o, h, l, c, kind) -> dict[str, pd.DataFrame]:
    k = 3 if kind == "daily" else 4
    r = rsi(c)
    S = {"rsi<30(bull)": (r < 30).astype(float), "rsi>70(bear)": -(r > 70).astype(float),
         "rsi<20(bull)": (r < 20).astype(float), "rsi>80(bear)": -(r > 80).astype(float),
         "rsi_cross_up_30(bull)": ((r > 30) & (r.shift(1) <= 30)).astype(float),
         "rsi_cross_down_70(bear)": -((r < 70) & (r.shift(1) >= 70)).astype(float),
         "donchian20_break_up(bull)": (c > h.shift(1).rolling(20).max()).astype(float),
         "donchian20_break_down(bear)": -(c < l.shift(1).rolling(20).min()).astype(float)}
    S.update(candle_signals(o, h, l, c, 5))
    pp = [pivot_patterns(h[s], l[s], c[s], k) for s in c.columns]
    for nm in pp[0]:
        S[nm] = pd.DataFrame({s: p[nm] for s, p in zip(c.columns, pp)})
    S.update(rsi_divergence(l, h, c, r, k))
    return {n_: s.reindex_like(c).fillna(0) for n_, s in S.items()}


def events(sig: pd.DataFrame, fwd: pd.DataFrame, h: int) -> pd.Series:
    rows = {}
    for s in sig.columns:
        x = sig[s].to_numpy(); last = -10**9; f = fwd[s].to_numpy()
        for t in np.flatnonzero(x != 0):
            if t - last < h or np.isnan(f[t]):
                continue
            rows[(sig.index[t], s)] = x[t] * f[t]; last = t
    return pd.Series(rows, dtype=float)


def day_stats(ev: pd.Series, n=1500, seed=0):
    idx = ev.index.get_level_values(0)
    days = pd.Series(ev.to_numpy(), index=idx).groupby(idx.date).agg(["sum", "count"])
    s, k = days["sum"].to_numpy(), days["count"].to_numpy()
    rng = np.random.default_rng(seed)
    pick = rng.integers(0, len(s), (n, len(s)))
    m = s[pick].sum(1) / k[pick].sum(1)
    mean = ev.mean()
    return mean, np.percentile(m, 2.5), np.percentile(m, 97.5), mean / m.std() if m.std() > 0 else 0.0


def run(kind: str, horizons) -> list[dict]:
    o, h, l, c = load(kind)
    print(f"[{kind}] {c.shape[1]} coins x {len(c)} bars {c.index.min()} -> {c.index.max()}", flush=True)
    S = all_signals(o, h, l, c, kind)
    res = []
    for hz in horizons:
        fwd = np.log(c).shift(-hz) - np.log(c)
        fwd = fwd.sub(fwd.mean(axis=1), axis=0)
        for name, sig in S.items():
            ev = events(sig, fwd, hz)
            if len(ev) < 30:
                res.append({"tf": kind, "h": hz, "signal": name, "n": int(len(ev))}); continue
            m, lo, hi, t = day_stats(ev)
            res.append({"tf": kind, "h": hz, "signal": name, "n": int(len(ev)), "mean_bps": round(m * 1e4, 1),
                        "ci95_bps": [round(lo * 1e4, 1), round(hi * 1e4, 1)], "t": round(float(t), 2),
                        "hit": round(float((ev > 0).mean()), 3), "net_bps": round(m * 1e4 - COST * 1e4, 1),
                        "survives": bool(abs(t) > 3.5 and m * 1e4 > COST * 1e4)})
    return res


def main():
    out = run("daily", (1, 5, 10)) + run("hourly", (1, 4, 24))
    (ROOT / "results" / "patterns_latest.json").write_text(json.dumps(out, indent=1))
    tested = [r for r in out if "t" in r]
    print(f"\n{len(tested)} signal x horizon tests; expected false |t|>3.5 by chance: ~{len(tested) * 0.0005:.2f}")
    print("\nTop by |t| (net = mean - 10 bps cost):")
    for r in sorted(tested, key=lambda r: -abs(r["t"]))[:14]:
        print(f"{r['tf']:6s} h={r['h']:>2d} {r['signal']:28s} n={r['n']:5d} mean {r['mean_bps']:+7.1f} {r['ci95_bps']} t={r['t']:+.2f} hit={r['hit']:.3f} net {r['net_bps']:+7.1f}")
    print("\nSurvive (|t|>3.5 and net positive):", [f"{r['tf']}/h{r['h']}/{r['signal']}" for r in tested if r["survives"]] or "NONE")


if __name__ == "__main__":
    main()
