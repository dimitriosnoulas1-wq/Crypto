"""Look-ahead checks (idea from Freqtrade's lookahead-analysis, reimplemented).

1. Features at dates <= D must be identical whether or not data after D exists.
2. Labels at date D must use only closes after D.
3. The ledger must reject edits and detect tampering.
"""
import sqlite3
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from cil.data import load_trendscan_history
from cil.features import build_features
from cil.labels import build_labels
from cil.ledger import Ledger


@pytest.fixture(scope="module")
def df():
    return load_trendscan_history()


@pytest.mark.parametrize("cut", ["2023-03-15", "2024-06-30", "2025-01-10"])
def test_features_do_not_look_ahead(df, cut):
    cut = pd.Timestamp(cut, tz="UTC")
    full = build_features(df)
    trunc = build_features(df[df.index.get_level_values("date") <= cut])
    a = full[full.index.get_level_values("date") <= cut].sort_index()
    b = trunc.sort_index()
    pd.testing.assert_frame_equal(a, b, check_exact=False, rtol=1e-9, atol=1e-12)


def test_labels_use_only_future(df):
    lab = build_labels(df, 3)
    btc = df.xs("BTC", level="symbol")["close"]
    d = btc.index[100]
    expected = np.log(btc.iloc[103]) - np.log(btc.iloc[100])
    assert lab.loc[(d, "BTC"), "fwd_ret"] == pytest.approx(expected)
    # The last 3 rows of each symbol have no label yet.
    assert lab.xs("BTC", level="symbol")["fwd_ret"].iloc[-3:].isna().all()


def test_ledger_is_append_only_and_tamper_evident():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "l.db"
        led = Ledger(path)
        for i in range(3):
            led.append(created_at="t", asof=f"d{i}", symbol="BTC", horizon_days=1,
                       model="m", p_up=0.6, ref_price=100 + i, meta={})
        assert led.verify() == (True, 3)
        with pytest.raises(sqlite3.DatabaseError):
            led.db.execute("UPDATE predictions SET p_up = 0.99 WHERE id = 2")
        # Bypass the trigger the way an attacker with file access could, then detect it.
        led.db.execute("DROP TRIGGER no_update")
        led.db.execute("UPDATE predictions SET p_up = 0.99 WHERE id = 2")
        led.db.commit()
        ok, n = led.verify()
        assert not ok and n == 1


def test_orthosys_does_not_look_ahead(df):
    from cil.orthosys import orthosys_panel
    cut = pd.Timestamp("2024-03-01", tz="UTC")
    full = orthosys_panel(df)
    trunc = orthosys_panel(df[df.index.get_level_values("date") <= cut])
    a = full[full.index.get_level_values("date") <= cut].sort_index()
    pd.testing.assert_frame_equal(a, trunc.sort_index(), check_exact=False, rtol=1e-9, atol=1e-12)
