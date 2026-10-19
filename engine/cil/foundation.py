"""Pre-trained time-series foundation models as council members (optional).

NOT YET TESTED: the weights are hosted on Hugging Face, which this environment's network
policy blocks. `available()` returns False until both the package and the weights load, and
the live cycle then simply runs without these members.

ChronosAgent: Amazon Chronos-Bolt forecasts quantiles of the next `h` closes from the recent
close history of each coin; P(up) is the share of the predictive distribution above the
current close (interpolated between quantile levels). Zero-shot: nothing is fitted on our data.
These models were pre-trained on historical data that may overlap past periods, so they are
only judged on live predictions in the ledger.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

MODEL_ID = "amazon/chronos-bolt-small"
CONTEXT = 512
_pipeline = None
_error = None


def available() -> tuple[bool, str]:
    global _pipeline, _error
    if _pipeline is not None:
        return True, "ok"
    if _error is not None:
        return False, _error
    try:
        import torch  # noqa: F401
        from chronos import BaseChronosPipeline
        _pipeline = BaseChronosPipeline.from_pretrained(MODEL_ID, device_map="cpu")
        return True, "ok"
    except Exception as e:  # missing package or Hugging Face unreachable
        _error = f"{type(e).__name__}: {str(e)[:160]}"
        return False, _error


class ChronosAgent:
    name = "chronos_bolt"

    def __init__(self, df: pd.DataFrame, horizon: int):
        self.df, self.h = df, horizon

    def fit(self, X, y):
        return self  # zero-shot

    def predict_proba(self, X):
        import torch
        out = []
        for d, sym in X.index:
            c = self.df.xs(sym, level="symbol")["close"]
            c = c[c.index <= d].tail(CONTEXT)
            if len(c) < 64:
                out.append(0.5)
                continue
            q, _ = _pipeline.predict_quantiles(torch.tensor(np.log(c.to_numpy())), prediction_length=self.h,
                                               quantile_levels=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
            qh = q[0, -1, :].numpy()                      # quantiles of log close at step h
            levels = np.linspace(0.1, 0.9, 9)
            now = np.log(c.iloc[-1])
            # P(close_h > now) = 1 - CDF(now), CDF interpolated over the quantiles.
            cdf = float(np.interp(now, qh, levels, left=0.05, right=0.95))
            out.append(1 - cdf)
        return np.array(out)
