"""Council: weights earned from the ledger, abstention, risk veto."""
import numpy as np
import pandas as pd

from cil.council import convene, hedge_weights, risk_veto

IDX = pd.MultiIndex.from_tuples([("t", "A"), ("t", "B"), ("t", "C")], names=["date", "symbol"])


def test_hedge_rewards_the_member_that_was_right():
    rows = []
    for b in range(10):
        for m, p in (("good", 0.7), ("bad", 0.3)):
            rows.append({"asof": f"b{b}", "model": m, "p_up": p, "up": 1})
    w, ll = hedge_weights(pd.DataFrame(rows), ["good", "bad"])
    assert w["good"] > 0.99 and ll["good"] < ll["bad"]


def test_no_history_means_equal_weights():
    w, _ = hedge_weights(pd.DataFrame(columns=["asof", "model", "p_up", "up"]), ["a", "b"])
    assert w == {"a": 0.5, "b": 0.5}


def test_abstains_when_members_disagree_and_on_veto():
    preds = {"x": pd.Series([0.7, 0.7, 0.515], index=IDX), "y": pd.Series([0.3, 0.7, 0.515], index=IDX)}
    veto = pd.Series(["", "extreme_volatility", ""], index=IDX)
    p, meta = convene(preds, {"x": 0.5, "y": 0.5}, veto)
    assert p.loc[("t", "A")] == 0.5 and meta[0]["abstain"] in ("no_edge", "members_disagree")
    assert p.loc[("t", "B")] == 0.5 and meta[1]["abstain"] == "extreme_volatility"
    assert p.loc[("t", "C")] == 0.5 and meta[2]["abstain"] == "no_edge"


def test_speaks_when_trusted_members_agree():
    preds = {"x": pd.Series([0.7, 0.7, 0.7], index=IDX), "y": pd.Series([0.65, 0.6, 0.62], index=IDX)}
    p, meta = convene(preds, {"x": 0.5, "y": 0.5}, pd.Series("", index=IDX))
    assert (p > 0.55).all() and all(m["abstain"] == "" for m in meta)


def test_veto_flags_extreme_volatility():
    f = pd.DataFrame({"vol_30": [0.01] * 9 + [0.2], "ret_1": 0.0, "rsi_14": 50.0},
                     index=pd.MultiIndex.from_tuples([("t", str(i)) for i in range(10)], names=["date", "symbol"]))
    v = risk_veto(f)
    assert v.iloc[-1] == "extreme_volatility" and (v.iloc[:-1] == "").all()


def test_new_member_is_not_penalised_for_bars_before_it_existed():
    rows = []
    for b in range(10):
        rows.append({"asof": f"b{b}", "model": "old", "p_up": 0.6, "up": 1})
        rows.append({"asof": f"b{b}", "model": "other", "p_up": 0.4, "up": 1})
    rows.append({"asof": "b9", "model": "new", "p_up": 0.6, "up": 1})  # joined at the last bar
    w, ll = hedge_weights(pd.DataFrame(rows), ["old", "other", "new"])
    assert w["new"] > w["other"]          # neutral history, then as good as "old" on its own bar
    assert abs(ll["new"] - ll["old"]) < 1e-9
