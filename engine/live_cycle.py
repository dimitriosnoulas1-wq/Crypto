"""Hourly live paper-prediction cycle with health monitoring.

Run once per hour, a few minutes after the hour (cron or a scheduled task):
    python live_cycle.py

Each run:
 1. fetches the latest closed 1h bars (+ funding, open interest, taker volume) for
    the most liquid Binance USDT-M perpetuals (public endpoints, no keys);
 2. retrains every model on labels whose outcome is already known;
 3. appends predictions for the latest closed bar to the tamper-evident ledger
    (horizons 1h and 4h), together with the live price at prediction time;
 4. resolves predictions whose horizon has passed;
 5. writes a monitoring report (results/live/monitor.json + monitor.md) with health
    checks for everything that tends to break in live use.
No orders are ever placed.

`--offline` runs the same cycle on the archived daily data, for testing the
pipeline when the exchanges are unreachable.
"""
from __future__ import annotations

import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from cil.features import build_features
from cil.labels import build_labels
from cil.ledger import Ledger
from cil.metrics import brier, ece, wilson
from cil.models import GBM, BaseRate, ConditionalFrequency, Logistic
from cil.orthosys import DEFAULT as ORTHO_PARAMS, orthosys_panel

ROOT = Path(__file__).resolve().parent.parent
LIVE = ROOT / "results" / "live"
CACHE = ROOT / "data_cache"
HORIZONS = (1, 4)            # in bars
BAR = pd.Timedelta(hours=1)
FEE_BPS = 5                  # per side, taker on Binance USD-M is ~4.5 bps for regular users
CONF = 0.55                  # paper position threshold


# ---------------------------------------------------------------- data
def fetch_live(top_n: int, log: list) -> tuple[pd.DataFrame, dict, int]:
    from cil import binance as bn
    t0 = time.time()
    now_ms = bn.server_time_ms()
    syms = bn.universe(top_n)
    CACHE.mkdir(exist_ok=True)
    frames = []
    for s in syms:
        path = CACHE / f"{s}_1h.parquet"
        try:
            old = pd.read_parquet(path) if path.exists() else None
            start = None if old is None else int(old.open_time.max()) - 3 * 3_600_000
            new = bn.klines(s, "1h", 1500, start)
            k = new if old is None else pd.concat([old, new]).drop_duplicates("open_time", keep="last")
            k = k.sort_values("open_time").tail(2500)
            k.to_parquet(path)
            k = k[k.close_time < now_ms]                      # closed bars only
            f = bn.funding_history(s, int(k.open_time.min()))
            oi = bn.open_interest_hist(s, "1h", 500)
        except Exception as e:  # one bad symbol must not stop the cycle
            log.append(f"fetch_failed {s}: {e}")
            continue
        k = k.copy()
        k["date"] = pd.to_datetime(k.open_time, unit="ms", utc=True)
        k["symbol"] = s.removesuffix("USDT")
        if len(f):
            f["date"] = pd.to_datetime(f.fundingTime, unit="ms", utc=True).dt.floor("h")
            k = k.merge(f.groupby("date").fundingRate.sum().rename("funding"), on="date", how="left")
        else:
            k["funding"] = np.nan
        if len(oi):
            oi["date"] = pd.to_datetime(oi.timestamp, unit="ms", utc=True) - BAR  # OI stamped at bar end
            k = k.merge(oi.groupby("date").sumOpenInterestValue.last().rename("oi_value"), on="date", how="left")
        k["funding"] = k["funding"].fillna(0.0)               # no settlement in that hour
        frames.append(k[["date", "symbol", "open", "high", "low", "close", "volume", "quote_volume",
                         "trades", "taker_buy_quote", "funding"] + (["oi_value"] if "oi_value" in k else [])])
    df = pd.concat(frames).set_index(["date", "symbol"]).sort_index()
    prices = {s.removesuffix("USDT"): p for s, p in bn.last_prices().items()}
    log.append(f"fetch_seconds {time.time() - t0:.1f}")
    return df, prices, now_ms


def offline(asof: str, log: list):
    from cil.data import load_trendscan_history
    global BAR
    BAR = pd.Timedelta(days=1)
    df = load_trendscan_history()
    df = df[df.index.get_level_values("date") <= pd.Timestamp(asof, tz="UTC")]
    last = df.groupby(level="symbol").tail(1)["close"]
    prices = {s: float(v) for (_, s), v in last.items()}
    now_ms = int((df.index.get_level_values("date").max() + BAR).timestamp() * 1000) + 300_000
    log.append("offline mode: daily archive")
    return df, prices, now_ms


# ---------------------------------------------------------------- models
def models_for(cols):
    return [BaseRate(), ConditionalFrequency("momentum_24", "ret_14", [0.0]), Logistic(cols),
            GBM(cols, calibrate=True)]


def predict(df: pd.DataFrame, feats: pd.DataFrame, last_bar, h: int):
    labels = build_labels(df, h, BAR)
    train = feats.join(labels).dropna(subset=["up"])
    train = train[train["label_end"] <= last_bar]
    cols = list(feats.columns)
    today = feats[feats.index.get_level_values("date") == last_bar]
    out = {}
    for m in models_for(cols):
        if isinstance(m, GBM):
            m.fit(train[cols], train["up"].to_numpy(), dates=train.index.get_level_values("date"), horizon=h, bar=BAR)
        else:
            m.fit(train[cols], train["up"].to_numpy())
        out[m.name] = pd.Series(m.predict_proba(today[cols]), index=today.index)
    # OrthoSys is a rule: map its position to P(up) using its own historical hit rate.
    o = orthosys_panel(df, ORTHO_PARAMS)
    hist = o.join(labels).dropna(subset=["up"])
    hist = hist[(hist.position != 0) & (hist["label_end"] <= last_bar)]
    hit = float((np.sign(hist.fwd_ret) == hist.position).mean()) if len(hist) else 0.5
    pos = o.loc[o.index.get_level_values("date") == last_bar, "position"]
    out["orthosys"] = (0.5 + pos * (hit - 0.5)).astype(float)
    return out, len(train), hit


# ---------------------------------------------------------------- monitor
def monitor(tr: pd.DataFrame, health: dict) -> dict:
    """tr: resolved predictions with p_up, up, ref_price_entry, live_price, exit_px."""
    rep = {"generated_at": datetime.now(timezone.utc).isoformat(), "health": health, "models": {}}
    if tr.empty:
        return rep
    for (model, h), g in tr.groupby(["model_name", "horizon_days"]):
        y, p = g.up.to_numpy(), g.p_up.to_numpy()
        base = np.full(len(y), 0.5)
        calls = p != 0.5
        k = int(((p[calls] >= 0.5) == y[calls]).sum())
        n = int(calls.sum())
        side = np.where(p >= CONF, 1, np.where(p <= 1 - CONF, -1, 0))
        # Executable return: from the live price when we predicted, not the bar close.
        exe = np.log(g.exit_px.to_numpy() / g.live_price.to_numpy())
        pnl = side * np.expm1(exe) - (side != 0) * 2 * FEE_BPS / 1e4
        lo, hi = wilson(k, n)
        rep["models"][f"{model}|h{h}"] = {
            "resolved": len(g), "directional_calls": n, "hit_rate": k / n if n else None, "hit_ci95": (lo, hi),
            "mean_p": float(p.mean()), "up_rate": float(y.mean()),
            "brier": brier(p, y), "brier_skill_vs_0.5": 1 - brier(p, y) / brier(base, y), "ece": ece(p, y),
            "paper_trades": int((side != 0).sum()), "paper_pnl_sum": float(pnl.sum()),
            "paper_pnl_mean_bps": float(pnl[side != 0].mean() * 1e4) if (side != 0).any() else None,
            "latency_cost_bps": float(np.mean(np.log(g.live_price / g.ref_price_entry)) * 1e4),
        }
    return rep


def alerts(rep: dict) -> list[str]:
    """Things that break in live use and that a backtest cannot show."""
    h, out = rep["health"], []
    if h.get("minutes_since_bar_close", 0) > 20:
        out.append(f"LATE: predicted {h['minutes_since_bar_close']} min after bar close (prices moved meanwhile)")
    if h.get("stale_symbols"):
        out.append(f"STALE DATA: {len(h['stale_symbols'])} symbols missing the latest bar: {h['stale_symbols'][:10]}")
    if any(x.startswith("fetch_failed") for x in h.get("fetch_log", [])):
        out.append("FETCH FAILURES: " + "; ".join(x for x in h["fetch_log"] if x.startswith("fetch_failed"))[:400])
    if h.get("feature_nan_share_latest_bar", 0) > 0.15:
        out.append(f"MISSING INPUTS: {h['feature_nan_share_latest_bar']:.0%} of features are NaN on the latest bar")
    for k, v in h.items():
        if k.startswith("p_spread_") and ("lgbm" in k or "logistic" in k) and v < 0.002:
            out.append(f"MODEL COLLAPSED: {k} = {v} (same probability for every coin)")
    if not h.get("ledger_chain_valid", True):
        out.append("LEDGER TAMPERED OR CORRUPTED")
    for name, m in rep["models"].items():
        if m["resolved"] >= 300 and m["ece"] > 0.08:
            out.append(f"MISCALIBRATED: {name} says {m['mean_p']:.2f} on average, reality {m['up_rate']:.2f} (ECE {m['ece']:.3f})")
        if m["resolved"] >= 300 and m["hit_ci95"][1] < 0.5:
            out.append(f"WORSE THAN COIN FLIP: {name} hit-rate CI upper bound {m['hit_ci95'][1]:.3f}")
        if m["resolved"] >= 100 and abs(m["latency_cost_bps"]) > 15:
            out.append(f"LATENCY SLIPPAGE: {name} live price differs from bar close by {m['latency_cost_bps']:+.1f} bps on average")
    return out


def write_markdown(rep: dict):
    lines = [f"# Live monitor ({rep['generated_at']})", "", "## Alerts", ""]
    lines += [f"- {a}" for a in rep.get("alerts", [])] or ["- none"]
    lines += ["", "## Health", ""]
    for k, v in rep["health"].items():
        lines.append(f"- **{k}**: {v}")
    lines += ["", "## Models (resolved predictions only)", "",
              "| model | resolved | calls | hit rate | 95% CI | Brier skill | ECE | paper trades | mean pnl bps |",
              "|---|---|---|---|---|---|---|---|---|"]
    for name, m in rep["models"].items():
        hr = "-" if m["hit_rate"] is None else f"{m['hit_rate']:.3f}"
        pnl = "-" if m["paper_pnl_mean_bps"] is None else f"{m['paper_pnl_mean_bps']:+.1f}"
        lines.append(f"| {name} | {m['resolved']} | {m['directional_calls']} | {hr} | "
                     f"{m['hit_ci95'][0]:.2f}-{m['hit_ci95'][1]:.2f} | {m['brier_skill_vs_0.5']:+.4f} | "
                     f"{m['ece']:.3f} | {m['paper_trades']} | {pnl} |")
    (LIVE / "monitor.md").write_text("\n".join(lines) + "\n")


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=60)
    ap.add_argument("--offline", metavar="ASOF", help="test on archived daily data up to this date")
    ap.add_argument("--ledger", default=None)
    a = ap.parse_args()
    LIVE.mkdir(parents=True, exist_ok=True)
    wall = datetime.now(timezone.utc)
    log: list[str] = []
    df, prices, now_ms = offline(a.offline, log) if a.offline else fetch_live(a.top, log)
    ledger = Ledger(Path(a.ledger) if a.ledger else LIVE / ("ledger_offline.sqlite" if a.offline else "ledger.sqlite"))

    last_bar = df.index.get_level_values("date").max()
    bar_close = last_bar + BAR
    per_sym_last = df.reset_index().groupby("symbol").date.max()
    stale = sorted(per_sym_last[per_sym_last < last_bar].index)
    fresh = df[df.index.get_level_values("date") == last_bar]
    health = {
        "symbols": int(df.index.get_level_values("symbol").nunique()),
        "last_closed_bar": str(last_bar),
        "minutes_since_bar_close": round((now_ms / 1000 - bar_close.timestamp()) / 60, 1),
        "stale_symbols": stale,
        "fetch_log": log,
    }

    # Skip if this bar was already predicted (cycle ran twice).
    done = ledger.db.execute("SELECT COUNT(*) FROM predictions WHERE asof = ?", (str(last_bar),)).fetchone()[0]
    feats = build_features(df)
    health["feature_nan_share_latest_bar"] = round(float(feats.loc[fresh.index].isna().mean().mean()), 3)
    if done:
        health["note"] = "bar already predicted; only resolving"
    else:
        for h in HORIZONS:
            preds, n_train, ortho_hit = predict(df, feats, last_bar, h)
            health[f"train_rows_h{h}"] = n_train
            health[f"orthosys_hist_hit_h{h}"] = round(ortho_hit, 4)
            for model, ser in preds.items():
                health[f"p_spread_{model}_h{h}"] = round(float(ser.std()), 4) if len(ser) > 1 else 0.0
                for (d, sym), p in ser.items():
                    row = feats.loc[(d, sym)]
                    ledger.append(created_at=wall.isoformat(), asof=str(d), symbol=sym, horizon_days=h,
                                  model=model, p_up=float(p), ref_price=float(df.loc[(d, sym), "close"]),
                                  meta={"live_price": prices.get(sym), "bar": str(BAR),
                                        "inputs": {k: round(float(row[k]), 5) for k in
                                                   ("ret_1", "ret_14", "rsi_14", "qvol_z", "funding_z")
                                                   if k in row and pd.notna(row[k])}})

    # Resolve: outcome = close of bar asof + h, versus the bar close we predicted from.
    closes = df["close"]
    resolved = 0
    for pid, asof, sym, h, ref in ledger.unresolved():
        end = pd.Timestamp(asof) + h * BAR
        if (end, sym) in closes.index:
            ledger.resolve(pid, wall.isoformat(), float(closes.loc[(end, sym)]),
                           float(np.log(closes.loc[(end, sym)] / ref)))
            resolved += 1
    health["resolved_this_cycle"] = resolved
    ok, n = ledger.verify()
    health["ledger_chain_valid"] = ok
    health["ledger_rows"] = n

    # Track record with entry/exit prices for the monitor.
    tr = pd.read_sql_query(
        "SELECT p.model AS model_name, p.horizon_days, p.p_up, p.ref_price AS ref_price_entry, p.meta, "
        "o.exit_price AS exit_px, o.up FROM predictions p JOIN outcomes o ON o.prediction_id = p.id", ledger.db)
    if not tr.empty:
        tr["live_price"] = [json.loads(m).get("live_price") or r for m, r in zip(tr.meta, tr.ref_price_entry)]
    rep = monitor(tr, health)
    rep["alerts"] = alerts(rep)
    with open(LIVE / "history.jsonl", "a") as fh:  # one line per cycle, for trend analysis
        fh.write(json.dumps({"t": rep["generated_at"], "health": {k: v for k, v in health.items() if k != "fetch_log"},
                             "alerts": rep["alerts"], "models": rep["models"]}, default=str) + "\n")
    (LIVE / "monitor.json").write_text(json.dumps(rep, indent=1, default=str))
    write_markdown(rep)
    print(json.dumps(health, default=str)[:2000])


if __name__ == "__main__":
    main()
