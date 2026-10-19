"""Outcome alignment and exactly-once scoring for the live ledger."""
import sqlite3
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cil.ledger import Ledger  # noqa: E402
from live_cycle import resolve_pending  # noqa: E402

H = pd.Timedelta(hours=1)
T0 = pd.Timestamp("2026-10-19 15:00", tz="UTC")


def closes(n_bars):
    idx = pd.MultiIndex.from_tuples([(T0 + i * H, "BTC") for i in range(n_bars)], names=["date", "symbol"])
    return pd.Series([100.0 + i for i in range(n_bars)], index=idx)  # close(T0+i) = 100+i


@pytest.fixture
def ledger(tmp_path):
    led = Ledger(tmp_path / "l.db")
    for h in (1, 4):
        led.append(created_at="w", asof=str(T0), symbol="BTC", horizon_days=h, model="m", p_up=0.6,
                   ref_price=100.0, meta={})
    return led


def test_not_scored_before_horizon_bar_closes(ledger):
    assert resolve_pending(ledger, closes(1), H) == 0          # only the prediction bar itself


def test_h1_uses_next_bar_close_and_h4_the_fourth(ledger):
    assert resolve_pending(ledger, closes(2), H) == 1          # bar T0+1h closed -> h1 only
    assert resolve_pending(ledger, closes(5), H) == 1          # bar T0+4h closed -> h4
    rows = dict(ledger.db.execute("SELECT p.horizon_days, o.exit_price FROM outcomes o "
                                  "JOIN predictions p ON p.id = o.prediction_id").fetchall())
    assert rows == {1: 101.0, 4: 104.0}
    fwd = dict(ledger.db.execute("SELECT p.horizon_days, o.fwd_ret FROM outcomes o "
                                 "JOIN predictions p ON p.id = o.prediction_id").fetchall())
    assert fwd[1] == pytest.approx(np.log(101 / 100))


def test_rerun_never_rescores(ledger):
    resolve_pending(ledger, closes(5), H)
    assert resolve_pending(ledger, closes(5), H) == 0
    assert resolve_pending(ledger, closes(9), H) == 0
    assert ledger.db.execute("SELECT COUNT(*) FROM outcomes").fetchone()[0] == 2
    assert ledger.resolve(1, "x", 999.0, 1.0) is False           # direct second insert is ignored


def test_outcomes_are_append_only(ledger):
    resolve_pending(ledger, closes(5), H)
    with pytest.raises(sqlite3.DatabaseError):
        ledger.db.execute("UPDATE outcomes SET exit_price = 1")
    with pytest.raises(sqlite3.DatabaseError):
        ledger.db.execute("DELETE FROM outcomes")
    assert ledger.verify() == (True, 2)


def test_recent_base_rate_uses_only_last_days():
    from cil.models import RecentBaseRate
    idx = pd.MultiIndex.from_tuples([(T0 + i * pd.Timedelta(days=1), "BTC") for i in range(20)], names=["date", "symbol"])
    y = np.array([1] * 10 + [0] * 10)
    m = RecentBaseRate(7).fit(pd.DataFrame(index=idx), y)
    assert m.p == 0.0                       # the last 8 days (inclusive window) are all 0
