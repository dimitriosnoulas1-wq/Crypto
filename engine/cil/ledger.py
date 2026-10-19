"""Append-only prediction ledger (SQLite).

- Predictions are written before their outcome is known.
- Each row stores the SHA-256 of its content plus the previous row's hash, so any
  later edit or deletion breaks the chain (`verify()` detects it).
- Outcomes go to a separate table; prediction rows are never updated.
- SQLite triggers reject UPDATE/DELETE on the predictions table.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS predictions (
  id INTEGER PRIMARY KEY,
  created_at TEXT NOT NULL,      -- wall clock when written (UTC ISO)
  asof TEXT NOT NULL,            -- market data time the prediction is based on
  symbol TEXT NOT NULL,
  horizon_days INTEGER NOT NULL,
  model TEXT NOT NULL,
  p_up REAL NOT NULL,
  ref_price REAL NOT NULL,
  meta TEXT NOT NULL,            -- JSON: reasons, data-quality flags, model version
  prev_hash TEXT NOT NULL,
  row_hash TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS outcomes (
  prediction_id INTEGER PRIMARY KEY REFERENCES predictions(id),
  resolved_at TEXT NOT NULL,
  exit_price REAL NOT NULL,
  fwd_ret REAL NOT NULL,
  up INTEGER NOT NULL
);
CREATE TRIGGER IF NOT EXISTS no_update BEFORE UPDATE ON predictions
BEGIN SELECT RAISE(ABORT, 'predictions are append-only'); END;
CREATE TRIGGER IF NOT EXISTS no_delete BEFORE DELETE ON predictions
BEGIN SELECT RAISE(ABORT, 'predictions are append-only'); END;
"""

FIELDS = ("created_at", "asof", "symbol", "horizon_days", "model", "p_up", "ref_price", "meta")


def _hash(prev: str, row: dict) -> str:
    payload = json.dumps([prev] + [row[f] for f in FIELDS], sort_keys=True, default=str)
    return hashlib.sha256(payload.encode()).hexdigest()


class Ledger:
    def __init__(self, path: Path):
        self.db = sqlite3.connect(str(path))
        self.db.executescript(SCHEMA)

    def _last_hash(self) -> str:
        r = self.db.execute("SELECT row_hash FROM predictions ORDER BY id DESC LIMIT 1").fetchone()
        return r[0] if r else "GENESIS"

    def append(self, **row) -> int:
        row["meta"] = json.dumps(row.get("meta", {}), sort_keys=True)
        row["p_up"] = round(float(row["p_up"]), 6)
        row["ref_price"] = float(row["ref_price"])
        prev = self._last_hash()
        h = _hash(prev, row)
        cur = self.db.execute(
            f"INSERT INTO predictions ({','.join(FIELDS)}, prev_hash, row_hash) VALUES ({','.join('?' * (len(FIELDS) + 2))})",
            [row[f] for f in FIELDS] + [prev, h])
        self.db.commit()
        return cur.lastrowid

    def resolve(self, prediction_id, resolved_at, exit_price, fwd_ret):
        self.db.execute("INSERT OR IGNORE INTO outcomes VALUES (?,?,?,?,?)",
                        (prediction_id, resolved_at, float(exit_price), float(fwd_ret), int(fwd_ret > 0)))
        self.db.commit()

    def unresolved(self):
        return self.db.execute(
            "SELECT p.id, p.asof, p.symbol, p.horizon_days, p.ref_price FROM predictions p "
            "LEFT JOIN outcomes o ON o.prediction_id = p.id WHERE o.prediction_id IS NULL").fetchall()

    def verify(self) -> tuple[bool, int]:
        prev = "GENESIS"
        n = 0
        cols = ",".join(FIELDS)
        for r in self.db.execute(f"SELECT {cols}, prev_hash, row_hash FROM predictions ORDER BY id"):
            row = dict(zip(FIELDS, r[:len(FIELDS)]))
            if r[-2] != prev or _hash(prev, row) != r[-1]:
                return False, n
            prev = r[-1]
            n += 1
        return True, n

    def track_record(self):
        import pandas as pd
        return pd.read_sql_query(
            "SELECT p.asof, p.symbol, p.horizon_days, p.model, p.p_up, o.fwd_ret, o.up "
            "FROM predictions p JOIN outcomes o ON o.prediction_id = p.id ORDER BY p.id", self.db)
