"""Paper-trading loop with the immutable ledger.

Modes
  replay : walks historical days one at a time as if live (default). At each day D
           the model is retrained only on labels known at D, predictions for D are
           appended to the ledger, and outcomes are resolved only once D+h has closed.
  live   : same loop on CCXT data (needs network access to the exchange). Run once
           per day after the UTC close, e.g. from cron.

No orders are ever sent. There are no API keys in this program.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from cil.data import load_trendscan_history
from cil.features import build_features
from cil.labels import build_labels
from cil.ledger import Ledger
from cil.metrics import score, selective
from cil.models import GBM, Logistic

ROOT = Path(__file__).resolve().parent.parent


def step(ledger: Ledger, df: pd.DataFrame, day: pd.Timestamp, horizon: int, model_name: str,
         retrain_every: int, state: dict, wall_clock: str):
    known = df[df.index.get_level_values("date") <= day]
    feats = build_features(known)
    labels = build_labels(known, horizon)          # labels whose future is already known at `day`
    cols = list(feats.columns)

    if state.get("model") is None or state["since"] >= retrain_every:
        train = feats.join(labels).dropna(subset=["up"])
        train = train[train["label_end"] <= day]
        model = Logistic(cols) if model_name == "logistic" else GBM(cols, calibrate=True)
        if isinstance(model, GBM):
            model.fit(train[cols], train["up"].to_numpy(), dates=train.index.get_level_values("date"),
                      horizon=horizon)
        else:
            model.fit(train[cols], train["up"].to_numpy())
        state.update(model=model, since=0, train_rows=len(train))
    state["since"] += 1

    today = feats[feats.index.get_level_values("date") == day]
    p = state["model"].predict_proba(today[cols])
    closes = known["close"]
    for (d, sym), prob in zip(today.index, p):
        row = today.loc[(d, sym)]
        stale = bool(row[["ret_1", "vol_30"]].isna().any())
        reasons = {k: round(float(row[k]), 4) for k in ("ret_7", "rsi_14", "funding_z", "qvol_z", "dist_sma_200")
                   if pd.notna(row[k])}
        ledger.append(created_at=wall_clock, asof=str(d.date()), symbol=sym, horizon_days=horizon,
                      model=f"{model_name}/train_rows={state['train_rows']}", p_up=prob,
                      ref_price=float(closes.loc[(d, sym)]),
                      meta={"features": reasons, "stale_inputs": stale})

    # Resolve everything whose horizon has now closed.
    for pid, asof, sym, h, ref in ledger.unresolved():
        end = pd.Timestamp(asof, tz="UTC") + pd.Timedelta(days=h)
        if end <= day and (end, sym) in closes.index:
            exit_price = float(closes.loc[(end, sym)])
            ledger.resolve(pid, str(day.date()), exit_price, float(np.log(exit_price / ref)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["replay", "live"], default="replay")
    ap.add_argument("--start", default="2025-01-01")
    ap.add_argument("--end", default="2025-07-31")
    ap.add_argument("--horizon", type=int, default=1)
    ap.add_argument("--model", choices=["logistic", "lgbm_calibrated"], default="lgbm_calibrated")
    ap.add_argument("--retrain-every", type=int, default=30)
    ap.add_argument("--ledger", default=str(ROOT / "results" / "paper_ledger.sqlite"))
    a = ap.parse_args()

    ledger = Ledger(Path(a.ledger))
    state: dict = {}
    if a.mode == "live":
        from cil.live import fetch_daily
        df = fetch_daily(days=900)
        day = df.index.get_level_values("date").max()
        step(ledger, df, day, a.horizon, a.model, 1, state, datetime.now(timezone.utc).isoformat())
    else:
        df = load_trendscan_history()
        days = pd.date_range(pd.Timestamp(a.start, tz="UTC"), pd.Timestamp(a.end, tz="UTC"), freq="D")
        for day in days:
            step(ledger, df, day, a.horizon, a.model, a.retrain_every, state,
                 f"replay:{day.date()}")

    ok, n = ledger.verify()
    tr = ledger.track_record()
    print(f"ledger chain valid={ok} rows={n} resolved={len(tr)}")
    if len(tr):
        s = score(tr.p_up.to_numpy(), tr.up.to_numpy(), np.full(len(tr), 0.5))
        print({k: (round(v, 4) if isinstance(v, float) else v) for k, v in s.items()})
        print(selective(tr.p_up.to_numpy(), tr.up.to_numpy()).round(3).to_string(index=False))


if __name__ == "__main__":
    main()
