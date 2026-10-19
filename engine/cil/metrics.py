"""Scoring of probabilistic predictions. No metric is reported without its sample size."""
from __future__ import annotations

import math

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (c - h, c + h)


def brier(p, y):
    return float(np.mean((np.asarray(p) - np.asarray(y)) ** 2))


def logloss(p, y):
    p = np.clip(np.asarray(p), 1e-6, 1 - 1e-6)
    y = np.asarray(y)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def ece(p, y, bins=10):
    p, y = np.asarray(p), np.asarray(y)
    idx = np.minimum((p * bins).astype(int), bins - 1)
    total = 0.0
    for b in range(bins):
        m = idx == b
        if m.any():
            total += m.mean() * abs(p[m].mean() - y[m].mean())
    return float(total)


def score(p, y, p_ref=None) -> dict:
    p, y = np.asarray(p), np.asarray(y)
    calls = (p >= 0.5).astype(int)
    k = int((calls == y).sum())
    out = {
        "n": len(y),
        "up_rate": float(y.mean()),
        "accuracy": k / len(y),
        "accuracy_ci95": wilson(k, len(y)),
        "brier": brier(p, y),
        "logloss": logloss(p, y),
        "ece": ece(p, y),
        "auc": float(roc_auc_score(y, p)) if len(np.unique(y)) == 2 and np.std(p) > 0 else float("nan"),
    }
    if p_ref is not None:
        out["brier_skill"] = 1 - out["brier"] / brier(p_ref, y)
    return out


def selective(p, y, thresholds=(0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.9)) -> pd.DataFrame:
    """Accuracy when the model only speaks if confident: max(p, 1-p) >= t."""
    p, y = np.asarray(p), np.asarray(y)
    conf = np.maximum(p, 1 - p)
    rows = []
    for t in thresholds:
        m = conf >= t
        n = int(m.sum())
        k = int(((p[m] >= 0.5).astype(int) == y[m]).sum()) if n else 0
        lo, hi = wilson(k, n)
        rows.append({"threshold": t, "calls": n, "coverage": n / len(p),
                     "hit_rate": k / n if n else float("nan"), "ci95_low": lo, "ci95_high": hi})
    return pd.DataFrame(rows)


def block_bootstrap_bss(p, y, p_ref, blocks, n_boot=1000, seed=0):
    """95% CI of Brier skill score, resampling whole calendar months (keeps dependence)."""
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({"p": p, "y": y, "r": p_ref, "b": blocks})
    groups = [g for _, g in df.groupby("b")]
    vals = []
    for _ in range(n_boot):
        s = pd.concat([groups[i] for i in rng.integers(0, len(groups), len(groups))])
        vals.append(1 - brier(s.p, s.y) / brier(s.r, s.y))
    return (float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5)))
