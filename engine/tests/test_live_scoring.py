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


def test_wallet_accounting():
    from live_cycle import wallets, FEE_BPS
    tr = pd.DataFrame({
        "asof": ["b1", "b1", "b2"], "model_name": ["m", "m", "m"], "horizon_days": [1, 1, 1],
        "p_up": [0.6, 0.4, 0.5], "live_price": [100.0, 100.0, 100.0], "exit_px": [110.0, 90.0, 120.0]})
    w = wallets(tr)["m|h1"]
    fee = 2 * FEE_BPS / 1e4
    assert w["trades"] == 2 and w["wins"] == 2                     # bar b2: p=0.5 -> no position
    assert w["value"] == pytest.approx(1000 * (1 + (0.10 - fee)), abs=0.01)   # long +10%, short +10%


def test_pro_wallet_needs_live_evidence():
    import numpy as np
    import pandas as pd
    import live_cycle as L
    rng = np.random.default_rng(0)
    rows = []
    for i in range(120):
        asof = pd.Timestamp("2026-10-19", tz="UTC") + pd.Timedelta(hours=i)
        for c in range(20):
            up = rng.random() < 0.5
            for name, p in (("oracle", 0.7 if up else 0.3), ("coin", 0.7 if rng.random() < 0.5 else 0.3)):
                rows.append(dict(asof=asof, model_name=name, horizon_days=1, symbol=str(c), p_up=p,
                                 live_price=100.0, exit_px=100.5 if up else 99.5, up=up))
    w = L.pro_wallets(pd.DataFrame(rows))
    assert w["PRO_oracle|h1"]["trades"] > 0 and w["PRO_oracle|h1"]["value"] > 1000
    first = w["PRO_oracle|h1"]["scored_bars"] - w["PRO_oracle|h1"]["licensed_bars"]
    assert first >= L.LICENSE_MIN_BARS            # never trades before it has a record
    assert w["PRO_coin|h1"]["value"] <= 1000.0 + 1e-9 or w["PRO_coin|h1"]["trades"] < w["PRO_oracle|h1"]["trades"]
