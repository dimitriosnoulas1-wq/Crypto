import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import xs_paper as X


def test_legs_are_lowest_and_highest_vol():
    vol = pd.Series(np.arange(50, dtype=float), index=[f"C{i}" for i in range(50)])
    lo, hi = X.pick_legs(vol)
    assert len(lo) == len(hi) == 10
    assert set(lo) == {f"C{i}" for i in range(10)} and set(hi) == {f"C{i}" for i in range(40, 50)}


def test_book_return_long_up_short_down_pays_and_costs_20bps():
    rec = {"long": ["A"], "short": ["B"], "entry_px": {"A": 100.0, "B": 100.0}}
    r = X.book_return(rec, {"A": 101.0, "B": 99.0})
    assert abs(r["gross_bps"] - 200.0) < 1e-6 and abs(r["net_bps"] - 180.0) < 1e-6
    assert X.book_return(rec, {"A": 101.0}) is None            # missing price: never invent a result


def test_chain_detects_tampering(tmp_path):
    p = tmp_path / "b.jsonl"
    X.append({"type": "open", "id": "d1", "x": 1}, p)
    X.append({"type": "open", "id": "d2", "x": 2}, p)
    assert X.verify(X.read_book(p))
    txt = p.read_text().replace('"x": 1', '"x": 9')
    p.write_text(txt)
    assert not X.verify(X.read_book(p))


def test_trend_weights_follow_sign_and_scale_inverse_to_vol():
    rng = np.random.default_rng(0)
    n = 120
    idx = pd.date_range("2024-01-01", periods=n, freq="D")
    up_calm = pd.Series(100 * np.exp(np.cumsum(np.full(n, 0.004) + rng.normal(0, 0.005, n))), index=idx)
    down_wild = pd.Series(100 * np.exp(np.cumsum(np.full(n, -0.004) + rng.normal(0, 0.05, n))), index=idx)
    w = X.trend_weights(pd.DataFrame({"UP": up_calm, "DN": down_wild}))
    assert w["UP"] > 0 > w["DN"]                                   # long the uptrend, short the downtrend
    assert abs(w["UP"]) > abs(w["DN"])                             # calmer coin gets the larger size (vol targeting)
    assert abs(w["UP"]) <= X.LEV_CAP / 2 + 1e-9                    # leverage cap, spread over 2 coins


def test_trend_book_return_and_cost(tmp_path):
    p = tmp_path / "t.jsonl"
    X.append({"type": "open", "id": "d1", "weights": {"A": 0.5, "B": -0.5}, "entry_px": {"A": 100.0, "B": 100.0}}, p)
    recs = X.read_book(p)
    prev = recs[0]
    px = {"A": 102.0, "B": 99.0}
    gross = sum(w * (px[s] / prev["entry_px"][s] - 1) for s, w in prev["weights"].items())
    assert abs(gross - 0.015) < 1e-9                               # 0.5*2% + 0.5*1%
    assert X.trend_summary(recs)["equity"] == X.CAPITAL            # nothing closed yet: equity unchanged
