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
