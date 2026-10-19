"""Cost-aware daily portfolio simulation from 1-day-horizon predictions.

Position rule per coin and day: long if p >= t, short if p <= 1 - t (when allowed),
flat otherwise. Active positions are equally weighted (gross exposure 1).
Costs: `fee_bps` per side on every change of weight, and funding: longs pay the
day's funding rate, shorts receive it (Binance USD-M convention).
Entry at the close of the signal day, exit at the next close (fwd_ret is close-to-close).
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def simulate(preds: pd.DataFrame, funding: pd.Series, threshold=0.55, fee_bps=10.0,
             allow_short=True) -> pd.DataFrame:
    df = preds.copy()
    df["side"] = np.where(df["p"] >= threshold, 1.0,
                          np.where((df["p"] <= 1 - threshold) & allow_short, -1.0, 0.0))
    active = df.groupby("date")["side"].transform(lambda s: (s != 0).sum())
    df["w"] = np.where(active > 0, df["side"] / active.replace(0, 1), 0.0)
    # Funding paid over the holding day: the funding of the *next* day.
    fnext = funding.groupby(level="symbol").shift(-1).rename("fund_next")
    df = df.join(fnext, on=["date", "symbol"])
    df["fund_next"] = df["fund_next"].fillna(0.0)

    wide_w = df.pivot(index="date", columns="symbol", values="w").fillna(0.0).sort_index()
    wide_r = df.pivot(index="date", columns="symbol", values="fwd_ret").reindex_like(wide_w).fillna(0.0)
    wide_f = df.pivot(index="date", columns="symbol", values="fund_next").reindex_like(wide_w).fillna(0.0)

    simple = np.expm1(wide_r)
    gross = (wide_w * simple).sum(axis=1)
    turnover = wide_w.diff().abs().sum(axis=1).fillna(wide_w.abs().sum(axis=1))
    fees = turnover * fee_bps / 1e4
    funding_cost = (wide_w * wide_f).sum(axis=1)
    net = gross - fees - funding_cost
    return pd.DataFrame({"gross": gross, "fees": fees, "funding": funding_cost, "net": net,
                         "exposure": wide_w.abs().sum(axis=1), "turnover": turnover})


def summary(daily: pd.Series) -> dict:
    daily = daily.fillna(0.0)
    equity = (1 + daily).cumprod()
    years = len(daily) / 365.0
    dd = equity / equity.cummax() - 1
    sd = daily.std()
    return {
        "days": len(daily),
        "total_return": float(equity.iloc[-1] - 1),
        "cagr": float(equity.iloc[-1] ** (1 / years) - 1) if years > 0 else float("nan"),
        "sharpe": float(daily.mean() / sd * np.sqrt(365)) if sd > 0 else float("nan"),
        "max_drawdown": float(dd.min()),
        "win_days": float((daily > 0).mean()),
    }
