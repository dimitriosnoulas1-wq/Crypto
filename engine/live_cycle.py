"""Hourly live paper-prediction cycle with health monitoring.

Run once per hour, a few minutes after the hour (cron or a scheduled task):
    python live_cycle.py

Each run:
 1. fetches the latest closed 1h bars (+ funding, open interest, taker volume) for
    the most liquid OKX USDT perpetuals (public endpoints, no keys; Binance/Bybit are
    geo-blocked from the cloud environment, `--venue binance` remains for other hosts);
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
from cil.models import GBM, BaseRate, ConditionalFrequency, Logistic, RecentBaseRate
from cil.orthosys import DEFAULT as ORTHO_PARAMS, orthosys_panel

ROOT = Path(__file__).resolve().parent.parent
LIVE = ROOT / "results" / "live"
CACHE = ROOT / "data_cache"
HORIZONS = (1, 4)            # in bars
BAR = pd.Timedelta(hours=1)
FEE_BPS = 5                  # per side, taker on Binance USD-M is ~4.5 bps for regular users
CONF = 0.55                  # paper position threshold


# ---------------------------------------------------------------- data
def fetch_live(top_n: int, log: list, venue: str = "okx") -> tuple[pd.DataFrame, dict, int]:
    if venue == "okx":  # Binance/Bybit geo-block the cloud environment
        from cil import okx
        return okx.fetch_panel(top_n, CACHE, log)
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


def fresh_prices(venue: str, fallback: dict) -> tuple[dict, int]:
    if venue == "okx":
        from cil import okx
        t = okx.get("/api/v5/market/tickers", {"instType": "SWAP"})
        px = {d["instId"].split("-")[0]: float(d["last"]) for d in t if d["instId"].endswith("-USDT-SWAP")}
        return px, max(int(d["ts"]) for d in t)
    from cil import binance as bn
    return bn.last_prices(), bn.server_time_ms()


# ---------------------------------------------------------------- models
def models_for(cols):
    return [BaseRate(), RecentBaseRate(7), ConditionalFrequency("momentum_24", "ret_14", [0.0]), Logistic(cols),
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


def resolve_pending(ledger: Ledger, closes: pd.Series, bar: pd.Timedelta) -> int:
    """Score each unresolved prediction once its horizon bar has CLOSED.

    A prediction made from bar `asof` (open time) uses close(asof) as reference; its outcome for
    horizon h is close(asof + h*bar), the close of the h-th following bar. `closes` must contain
    closed bars only. Already scored predictions are never rescored.
    """
    n = 0
    for pid, asof, sym, h, ref in ledger.unresolved():
        end = pd.Timestamp(asof) + h * bar
        if (end, sym) in closes.index:
            exit_px = float(closes.loc[(end, sym)])
            n += ledger.resolve(pid, datetime.now(timezone.utc).isoformat(), exit_px, float(np.log(exit_px / ref)))
    return n


# ---------------------------------------------------------------- monitor
def monitor(tr: pd.DataFrame, pending: pd.DataFrame, health: dict) -> dict:
    """Realized results only. `tr`: resolved predictions; `pending`: not yet matured (never scored).

    Per (model, horizon): sample counts, directional hit rate with Wilson CI, Brier score and Brier
    skill versus (a) the naive base-rate model on exactly the same (bar, coin, horizon) rows and
    (b) a constant 0.5, ECE plus reliability bins, coverage of paper positions, and
    paper P&L measured from the live price at prediction time (executable) after fees.
    On-time and late predictions are reported separately.
    """
    rep = {"generated_at": datetime.now(timezone.utc).isoformat(), "health": health, "models": {},
           "pending": {f"{m}|h{h}": int(n) for (m, h), n in
                       pending.groupby(["model_name", "horizon_days"]).size().items()} if len(pending) else {}}
    if tr.empty:
        return rep
    key = ["asof", "symbol", "horizon_days"]
    base = tr[tr.model_name == "base_rate"].set_index(key)["p_up"].rename("p_base")
    tr = tr.join(base, on=key)
    for (model, h), g in tr.groupby(["model_name", "horizon_days"]):
        for subset, gg in (("all", g), ("on_time", g[~g.late]), ("late", g[g.late])):
            if gg.empty:
                continue
            y, p = gg.up.to_numpy(), gg.p_up.to_numpy()
            pb = gg.p_base.fillna(0.5).to_numpy()
            calls = np.abs(p - 0.5) > 1e-9
            k, n = int(((p[calls] >= 0.5) == y[calls]).sum()), int(calls.sum())
            side = np.where(p >= CONF, 1, np.where(p <= 1 - CONF, -1, 0))
            exe = np.log(gg.exit_px.to_numpy() / gg.live_price.to_numpy())
            pnl = side * np.expm1(exe) - (side != 0) * 2 * FEE_BPS / 1e4
            bins = pd.cut(pd.Series(p), [0, 0.4, 0.45, 0.5, 0.55, 0.6, 1.0], include_lowest=True)
            rel = pd.DataFrame({"bin": bins.astype(str), "p": p, "y": y}).groupby("bin").agg(
                n=("y", "size"), mean_p=("p", "mean"), up_rate=("y", "mean")).round(4)
            rep["models"][f"{model}|h{h}|{subset}"] = {
                "resolved": len(gg), "bars": int(gg.asof.nunique()), "coins": int(gg.symbol.nunique()),
                "directional_calls": n, "hit_rate": k / n if n else None, "hit_ci95": wilson(k, n),
                "mean_p": float(p.mean()), "up_rate": float(y.mean()),
                "brier": brier(p, y), "brier_base_rate_model": brier(pb, y),
                "brier_skill_vs_base_rate": 1 - brier(p, y) / brier(pb, y) if brier(pb, y) > 0 else None,
                "brier_skill_vs_0.5": 1 - brier(p, y) / 0.25,
                "ece": ece(p, y), "reliability": rel.reset_index().to_dict("records"),
                "coverage_paper_positions": float((side != 0).mean()),
                "paper_trades": int((side != 0).sum()),
                "paper_pnl_mean_bps": float(pnl[side != 0].mean() * 1e4) if (side != 0).any() else None,
                "close_vs_live_entry_bps": float(np.mean(np.log(gg.live_price / gg.ref_price_entry)) * 1e4),
            }
    return rep


def alerts(rep: dict) -> list[str]:
    """Things that break in live use and that a backtest cannot show."""
    h, out = rep["health"], []
    if h.get("prediction_latency_min", 0) > 15:
        out.append(f"LATE: predictions written {h['prediction_latency_min']} min after bar close "
                   f"(h1 predictions flagged late above 15 min, h4 above 60 min)")
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
        if not name.endswith("|all"):
            continue
        if m["resolved"] >= 300 and m["ece"] > 0.08:
            out.append(f"MISCALIBRATED: {name} says {m['mean_p']:.2f} on average, reality {m['up_rate']:.2f} (ECE {m['ece']:.3f})")
        if m["resolved"] >= 300 and m["hit_ci95"][1] < 0.5:
            out.append(f"WORSE THAN COIN FLIP: {name} hit-rate CI upper bound {m['hit_ci95'][1]:.3f}")
        if m["resolved"] >= 100 and abs(m["close_vs_live_entry_bps"]) > 15:
            out.append(f"LATENCY SLIPPAGE: {name} live price differs from bar close by "
                       f"{m['close_vs_live_entry_bps']:+.1f} bps on average")
    return out


def write_markdown(rep: dict):
    lines = [f"# Live monitor ({rep['generated_at']})", "", "## Alerts", ""]
    lines += [f"- {a}" for a in rep.get("alerts", [])] or ["- none"]
    lines += ["", "## Health", ""]
    for k, v in rep["health"].items():
        lines.append(f"- **{k}**: {v}")
    lines += ["", "## Realized results (resolved predictions only)", "",
              "Brier skill vs base rate = improvement over the naive base-rate model on the same rows "
              "(0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.", "",
              "| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | "
              "Brier skill vs base | ECE | coverage | mean paper pnl bps |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for name, m in rep["models"].items():
        hr = "-" if m["hit_rate"] is None else f"{m['hit_rate']:.3f}"
        pnl = "-" if m["paper_pnl_mean_bps"] is None else f"{m['paper_pnl_mean_bps']:+.1f}"
        bss = "-" if m["brier_skill_vs_base_rate"] is None else f"{m['brier_skill_vs_base_rate']:+.4f}"
        lines.append(f"| {name} | {m['resolved']} | {m['bars']} | {m['directional_calls']} | {hr} | "
                     f"{m['hit_ci95'][0]:.2f}-{m['hit_ci95'][1]:.2f} | {m['up_rate']:.3f} | {m['mean_p']:.3f} | "
                     f"{bss} | {m['ece']:.3f} | {m['coverage_paper_positions']:.2f} | {pnl} |")
    lines += ["", "## Unverified (pending, not scored)", ""]
    lines += [f"- {k}: {v}" for k, v in rep.get("pending", {}).items()] or ["- none"]
    (LIVE / "monitor.md").write_text("\n".join(lines) + "\n")


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=60)
    ap.add_argument("--offline", metavar="ASOF", help="test on archived daily data up to this date")
    ap.add_argument("--venue", choices=["okx", "binance"], default="okx")
    ap.add_argument("--ledger", default=None)
    a = ap.parse_args()
    LIVE.mkdir(parents=True, exist_ok=True)
    log: list[str] = []
    df, prices, now_ms = offline(a.offline, log) if a.offline else fetch_live(a.top, log, a.venue)
    ledger = Ledger(Path(a.ledger) if a.ledger else
                    LIVE / ("ledger_offline.sqlite" if a.offline else f"ledger_{a.venue}.sqlite"))
    health_venue = "offline" if a.offline else a.venue

    last_bar = df.index.get_level_values("date").max()
    bar_close = last_bar + BAR
    per_sym_last = df.reset_index().groupby("symbol").date.max()
    stale = sorted(per_sym_last[per_sym_last < last_bar].index)
    fresh = df[df.index.get_level_values("date") == last_bar]
    health = {
        "venue": health_venue,
        "symbols": int(df.index.get_level_values("symbol").nunique()),
        "last_closed_bar": str(last_bar),
        "minutes_since_bar_close_at_fetch": round((now_ms / 1000 - bar_close.timestamp()) / 60, 1),
        "stale_symbols": stale,
        "fetch_log": log,
    }

    # Skip if this bar was already predicted (cycle ran twice).
    done = ledger.db.execute("SELECT COUNT(*) FROM predictions WHERE asof = ?", (str(last_bar),)).fetchone()[0]
    feats = build_features(df)
    health["feature_nan_share_latest_bar"] = round(float(feats.loc[fresh.index].isna().mean().mean()), 3)
    written = 0
    if done:
        health["note"] = "bar already predicted; only resolving"
    else:
        all_preds = {}
        for h in HORIZONS:
            all_preds[h] = predict(df, feats, last_bar, h)
        # Live price fetched immediately before writing, with its exchange timestamp, so the
        # executable entry price and the latency are measured at the moment of prediction.
        live, price_ts_ms = fresh_prices(a.venue, prices) if not a.offline else (prices, now_ms)
        written_at = datetime.now(timezone.utc)
        latency_min = (written_at.timestamp() - bar_close.timestamp()) / 60
        health["prediction_latency_min"] = round(latency_min, 1)
        health["price_snapshot_age_s"] = round(written_at.timestamp() - price_ts_ms / 1000, 1)
        for h in HORIZONS:
            preds, n_train, ortho_hit = all_preds[h]
            health[f"train_rows_h{h}"] = n_train
            health[f"orthosys_hist_hit_h{h}"] = round(ortho_hit, 4)
            for model, ser in preds.items():
                health[f"p_spread_{model}_h{h}"] = round(float(ser.std()), 4) if len(ser) > 1 else 0.0
                for (d, sym), p in ser.items():
                    row = feats.loc[(d, sym)]
                    ledger.append(created_at=written_at.isoformat(), asof=str(d), symbol=sym, horizon_days=h,
                                  model=model, p_up=float(p), ref_price=float(df.loc[(d, sym), "close"]),
                                  meta={"live_price": live.get(sym), "live_price_ts_ms": price_ts_ms,
                                        "latency_min": round(latency_min, 2),
                                        # Too late if more than a quarter of the horizon has already elapsed.
                                        "late": bool(latency_min > 0.25 * h * BAR.total_seconds() / 60),
                                        "bar": str(BAR),
                                        "inputs": {k: round(float(row[k]), 5) for k in
                                                   ("ret_1", "ret_14", "rsi_14", "qvol_z", "funding_z")
                                                   if k in row and pd.notna(row[k])}})
                    written += 1
    health["predictions_written"] = written

    resolved = resolve_pending(ledger, df["close"], BAR)
    health["resolved_this_cycle"] = resolved
    ok, n = ledger.verify()
    health["ledger_chain_valid"] = ok
    health["ledger_rows"] = n

    # Realized track record (resolved only) and pending predictions, kept apart.
    q = ("SELECT p.asof, p.created_at, p.symbol, p.model AS model_name, p.horizon_days, p.p_up, p.ref_price AS ref_price_entry, "
         "p.meta, o.exit_price AS exit_px, o.up FROM predictions p {} JOIN outcomes o ON o.prediction_id = p.id {}")
    tr = pd.read_sql_query(q.format("", ""), ledger.db)
    pending = pd.read_sql_query(q.format("LEFT", "WHERE o.prediction_id IS NULL"), ledger.db)
    if not tr.empty:
        meta = [json.loads(m) for m in tr.meta]
        tr["live_price"] = [m.get("live_price") or r for m, r in zip(meta, tr.ref_price_entry)]
        # Rows written before latency was logged: derive it from created_at - bar close. For the first
        # cycle created_at was the run start, so this is a lower bound (true latency ~5 min larger).
        derived = ((pd.to_datetime(tr.created_at) - (pd.to_datetime(tr.asof) + BAR)).dt.total_seconds() / 60)
        lat = [m.get("latency_min", d) for m, d in zip(meta, derived)]
        tr["late"] = [la > 0.25 * h * BAR.total_seconds() / 60 for la, h in zip(lat, tr.horizon_days)]
    rep = monitor(tr, pending, health)
    rep["alerts"] = alerts(rep)
    # One history line per cycle that changed the ledger; reruns that add nothing are not recorded twice.
    if written or resolved:
        line = {"t": rep["generated_at"], "health": {k: v for k, v in health.items() if k != "fetch_log"},
                "alerts": rep["alerts"], "models": rep["models"]}
        with open(LIVE / "history.jsonl", "a") as fh:
            fh.write(json.dumps(line, default=str) + "\n")
    (LIVE / "monitor.json").write_text(json.dumps(rep, indent=1, default=str))
    write_markdown(rep)
    print(json.dumps(health, default=str)[:2000])


if __name__ == "__main__":
    main()
