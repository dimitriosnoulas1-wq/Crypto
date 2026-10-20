import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import attention_log as A


class _R:
    status_code = 200

    def json(self):
        return {"coins": [{"item": {"symbol": "ABC", "id": "abc", "score": 0, "market_cap_rank": 5,
                                    "data": {"price": 2.0, "price_change_percentage_24h": {"usd": 12.5}}}},
                          {"item": {"symbol": "XYZ", "id": "xyz", "score": 1, "market_cap_rank": None, "data": None}}],
                "categories": [{"name": "AI"}]}


def test_parse_and_append(tmp_path):
    p = tmp_path / "a.jsonl"
    rec = A.snapshot(path=p, get=lambda *a, **k: _R())
    assert rec["coins"][0] == {"symbol": "ABC", "id": "abc", "score": 0, "mcap_rank": 5, "price": 2.0, "chg24h_pct": 12.5}
    assert rec["coins"][1]["chg24h_pct"] is None and rec["categories"] == ["AI"]
    A.snapshot(path=p, get=lambda *a, **k: _R())
    assert len(p.read_text().splitlines()) == 2                    # append-only


def test_http_error_writes_nothing(tmp_path):
    class Bad:
        status_code = 429
    p = tmp_path / "a.jsonl"
    assert A.snapshot(path=p, get=lambda *a, **k: Bad()) is None and not p.exists()
