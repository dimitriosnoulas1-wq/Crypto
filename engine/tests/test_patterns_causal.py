import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import run_patterns as P


def _series(n=400, seed=1):
    rng = np.random.default_rng(seed)
    c = pd.Series(100 * np.exp(np.cumsum(rng.normal(0, 0.02, n))), index=pd.date_range("2024-01-01", periods=n, freq="D"))
    h, l = c * (1 + rng.uniform(0, 0.01, n)), c * (1 - rng.uniform(0, 0.01, n))
    return h, l, c


def test_pivot_patterns_never_use_future_bars():
    h, l, c = _series()
    full = P.pivot_patterns(h, l, c, k=3)
    for T in (150, 250, 399):                     # truncating the future must not change any earlier signal
        cut = P.pivot_patterns(h[:T], l[:T], c[:T], k=3)
        for name in full:
            assert (full[name].iloc[:T].to_numpy() == cut[name].to_numpy()).all(), (name, T)
    assert sum(float((s != 0).sum()) for s in full.values()) > 0   # the detectors do fire


def test_rsi_divergence_never_uses_future_bars():
    h, l, c = _series(seed=2)
    H, L, C = h.to_frame("X"), l.to_frame("X"), c.to_frame("X")
    full = P.rsi_divergence(L, H, C, P.rsi(C), 3)
    T = 300
    cut = P.rsi_divergence(L[:T], H[:T], C[:T], P.rsi(C[:T]), 3)
    for name in full:
        assert (full[name].iloc[:T].to_numpy() == cut[name].to_numpy()).all()
