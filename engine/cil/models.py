"""Candidate models. Every model is fitted inside a walk-forward fold only.

All models expose `fit(X, y)` and `predict_proba(X) -> P(up)`.
Baselines come first: a model is only interesting if it beats them.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.impute import SimpleImputer
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


class BaseRate:
    """Always predicts the training frequency of 'up'. The climatology baseline."""
    name = "base_rate"

    def fit(self, X, y):
        self.p = float(np.mean(y))
        return self

    def predict_proba(self, X):
        return np.full(len(X), self.p)


class ConditionalFrequency:
    """P(up | bucket of one feature), estimated on the training fold."""

    def __init__(self, name, column, edges):
        self.name, self.column, self.edges = name, column, edges

    def _bucket(self, X):
        return np.digitize(X[self.column].to_numpy(), self.edges)

    def fit(self, X, y):
        b = self._bucket(X)
        y = np.asarray(y)
        self.base = float(y.mean())
        self.table = {k: (y[b == k].sum() + self.base * 20) / ((b == k).sum() + 20)  # shrinkage
                      for k in np.unique(b)}
        return self

    def predict_proba(self, X):
        b = self._bucket(X)
        nan = X[self.column].isna().to_numpy()
        p = np.array([self.table.get(k, self.base) for k in b])
        p[nan] = self.base
        return p


class Logistic:
    name = "logistic"

    def __init__(self, columns, C=0.05):
        self.columns, self.C = columns, C

    def fit(self, X, y):
        self.model = make_pipeline(SimpleImputer(strategy="median"), StandardScaler(),
                                   LogisticRegression(C=self.C, max_iter=2000))
        self.model.fit(X[self.columns], y)
        return self

    def predict_proba(self, X):
        return self.model.predict_proba(X[self.columns])[:, 1]


class GBM:
    """Small, heavily regularised LightGBM, optionally isotonic-calibrated on the
    most recent (purged) slice of the training window."""

    def __init__(self, columns, calibrate=True, seed=7):
        self.columns, self.calibrate, self.seed = columns, calibrate, seed
        self.name = "lgbm_calibrated" if calibrate else "lgbm"

    def _new(self):
        return LGBMClassifier(n_estimators=300, learning_rate=0.02, num_leaves=7,
                              min_child_samples=200, subsample=0.7, subsample_freq=1,
                              colsample_bytree=0.6, reg_lambda=5.0,
                              random_state=self.seed, verbose=-1)

    def fit(self, X, y, dates=None, horizon=1):
        X = X[self.columns]
        y = np.asarray(y)
        if not self.calibrate or dates is None:
            self.model = self._new().fit(X, y)
            self.iso = None
            return self
        dates = pd.DatetimeIndex(dates).as_unit("ns")
        cut = pd.Timestamp(int(np.quantile(dates.asi8, 0.8)), unit="ns", tz="UTC")
        # Purge: fitting rows whose label could reach into the calibration slice are dropped.
        fit_mask = np.asarray(dates < cut - pd.Timedelta(days=horizon))
        cal_mask = np.asarray(dates >= cut)
        self.model = self._new().fit(X[fit_mask], y[fit_mask])
        raw = self.model.predict_proba(X[cal_mask])[:, 1]
        self.iso = IsotonicRegression(out_of_bounds="clip", y_min=0.01, y_max=0.99).fit(raw, y[cal_mask])
        return self

    def predict_proba(self, X):
        raw = self.model.predict_proba(X[self.columns])[:, 1]
        return self.iso.predict(raw) if self.iso is not None else raw


def default_models(columns):
    return [
        BaseRate(),
        ConditionalFrequency("momentum_7d", "ret_7", [0.0]),
        ConditionalFrequency("trend_sma200", "dist_sma_200", [0.0]),
        ConditionalFrequency("rsi_meanrev", "rsi_14", [30, 70]),
        ConditionalFrequency("funding_crowding", "funding_z", [-2, 2]),
        Logistic(columns),
        GBM(columns, calibrate=False),
        GBM(columns, calibrate=True),
    ]
