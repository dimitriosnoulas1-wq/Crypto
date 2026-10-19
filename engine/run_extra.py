"""Experiments for the reference-repository ideas not yet tested.

A. TrendScan OrthoSys composite: replicate their walk-forward hit-rate claim
   (TRAIN 2022-01..2023-06, VAL 2023-07..2024-06, OOS 2024-07..2025-07, 20 bps round trip).
B. ml-crypto-forecast event targets (>= +10% within N days): their random split
   versus a purged walk-forward, same features and model family.
C. crypto-scanner / Argus anomaly alerts: do volume, funding and idiosyncratic-move
   spikes predict the next 1/3/7 days?
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

from cil.data import load_trendscan_history
from cil.features import build_features
from cil.labels import build_labels
from cil.metrics import block_bootstrap_bss, score, wilson
from cil.models import GBM, BaseRate, Logistic
from cil.orthosys import DEFAULT, TRENDSCAN_DAILY, orthosys_panel
from cil.validate import walk_forward

OUT = Path(__file__).resolve().parent.parent / "results"
PERIODS = {"train": ("2022-01-01", "2023-06-30"), "val": ("2023-07-01", "2024-06-30"),
           "oos": ("2024-07-01", "2025-07-31")}


def cluster_ci(values: pd.Series, n_boot=2000, seed=3):
    """95% CI of the mean, resampling whole dates (signals on one day are correlated)."""
    rng = np.random.default_rng(seed)
    by_day = values.groupby(level="date").agg(["sum", "count"])
    s, c = by_day["sum"].to_numpy(), by_day["count"].to_numpy()
    idx = rng.integers(0, len(s), (n_boot, len(s)))
    means = s[idx].sum(1) / c[idx].sum(1)
    return (float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5)))


def xs_excess(ret: pd.Series) -> pd.Series:
    """Forward return minus the same-date mean of the OTHER coins (no future information)."""
    g = ret.groupby(level="date")
    tot, cnt = g.transform("sum"), g.transform("count")
    return ret - (tot - ret) / (cnt - 1).replace(0, np.nan)


def in_period(idx, a, b):
    d = idx.get_level_values("date")
    return (d >= pd.Timestamp(a, tz="UTC")) & (d <= pd.Timestamp(b, tz="UTC"))


def fwd(df, h):
    return build_labels(df, h)["fwd_ret"]


def experiment_a(df):
    res = {}
    for pname, params in (("pine_default", DEFAULT), ("trendscan_daily_tuned", TRENDSCAN_DAILY)):
        o = orthosys_panel(df, params)
        res[pname] = {}
        for h in (1, 3, 5, 10, 20):
            r = fwd(df, h)
            x = o.join(r.rename("r")).dropna(subset=["r"])
            x = x[x.position != 0]
            row = {}
            for per, (a, b) in PERIODS.items():
                s = x[in_period(x.index, a, b)]
                if s.empty:
                    continue
                hit = (np.sign(s.r) == s.position)
                net = s.position * np.expm1(s.r) - 0.002  # 20 bps round trip, like their report
                k, n = int(hit.sum()), len(s)
                allr = r[in_period(r.index, a, b)].dropna()
                p_up = float((allr > 0).mean())
                share_long = float((s.position > 0).mean())
                row[per] = {"signals": n, "signal_days": int(s.index.get_level_values("date").nunique()),
                            "longs": int((s.position > 0).sum()),
                            "hit_rate": k / n, "hit_ci95_by_day": cluster_ci(hit.astype(float)),
                            # Chance level for the same long/short mix in that period.
                            "chance_hit": share_long * p_up + (1 - share_long) * (1 - p_up),
                            "avg_net_ret": float(net.mean()),
                            "net_ci95_by_day": cluster_ci(net)}
            res[pname][f"h{h}"] = row
    return res


def experiment_b(df, feats):
    out = {}
    cols = list(feats.columns)
    for n_days, thresh in ((7, 0.10), (30, 0.10), (30, 0.20)):
        lab = build_labels(df, n_days)
        lab["up"] = (lab["fwd_ret"] >= np.log1p(thresh)).astype(float).where(lab["fwd_ret"].notna())
        data = feats.join(lab).dropna(subset=["up"])
        key = f">=+{int(thresh * 100)}%_in_{n_days}d"
        # 1) Their method: random stratified 70/30 split over all rows.
        X = data[cols].fillna(data[cols].median())
        Xtr, Xte, ytr, yte = train_test_split(X, data["up"], test_size=0.3, stratify=data["up"], random_state=45)
        rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=5, n_jobs=-1, random_state=0).fit(Xtr, ytr)
        p_rand = rf.predict_proba(Xte)[:, 1]
        rand = {"auc": float(roc_auc_score(yte, p_rand)),
                "accuracy": float(((p_rand >= 0.5) == yte).mean()), "n_test": len(yte)}
        # 2) Honest: purged walk-forward, 2023-01..2025-07.
        models = [BaseRate(), Logistic(cols), GBM(cols, calibrate=False)]
        wf = walk_forward(feats, lab, models, n_days, "2023-01-01", "2025-07-01")
        ref = wf[wf.model == "base_rate"].set_index(["date", "symbol"])["p"]
        honest = {}
        for name, g in wf.groupby("model"):
            g = g.set_index(["date", "symbol"])
            pr = ref.reindex(g.index).to_numpy()
            s = score(g.p, g.y, pr)
            top = g.p >= g.p.quantile(0.9)
            s["precision_top10pct"] = float(g.y[top].mean())
            s["base_rate_test"] = float(g.y.mean())
            s["bss_ci95"] = block_bootstrap_bss(g.p.to_numpy(), g.y.to_numpy(), pr,
                                                g.index.get_level_values("date").strftime("%Y-%m"), 300)
            honest[name] = s
        out[key] = {"random_split_like_repo": rand, "purged_walk_forward": honest,
                    "positive_rate_all": float(data["up"].mean())}
    return out


def experiment_c(df, feats):
    r = {h: fwd(df, h) for h in (1, 3, 7)}
    f = feats.copy()
    vol = f["vol_30"]
    idio1 = (f["ret_1"] - f["beta_60"] * f["btc_ret_1"]) / vol
    events = {
        "volume_spike_z>3": f["qvol_z"] > 3,
        "volume_spike_z>3_up_day": (f["qvol_z"] > 3) & (f["ret_1"] > 0),
        "volume_spike_z>3_down_day": (f["qvol_z"] > 3) & (f["ret_1"] < 0),
        "funding_annualized>+100%": f["funding_1d"] * 365 > 1.0,
        "funding_annualized<-30%": f["funding_1d"] * 365 < -0.3,
        "funding_z>3": f["funding_z"] > 3,
        "funding_z<-3": f["funding_z"] < -3,
        "idiosyncratic_up_move>3sigma": idio1 > 3,
        "idiosyncratic_down_move<-3sigma": idio1 < -3,
        "rsi<25": f["rsi_14"] < 25,
        "rsi>80": f["rsi_14"] > 80,
    }
    out = {}
    for name, mask in events.items():
        mask = mask.fillna(False)
        row = {"events": int(mask.sum())}
        for h, ret in r.items():
            ev = ret[mask.reindex(ret.index, fill_value=False)].dropna()
            if len(ev) < 20:
                continue
            excess = xs_excess(ret).reindex(ev.index).dropna()
            row[f"h{h}"] = {"n": len(ev), "days": int(ev.index.get_level_values("date").nunique()),
                            "mean_ret": float(ev.mean()), "up_share": float((ev > 0).mean()),
                            "mean_excess_vs_other_coins_same_day": float(excess.mean()),
                            "excess_ci95_by_day": cluster_ci(excess),
                            "beat_other_coins_share": float((excess > 0).mean())}
        out[name] = row
    return out


def main():
    df = load_trendscan_history()
    feats = build_features(df)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report = {"generated_at": stamp,
              "A_orthosys": experiment_a(df),
              "B_event_targets": experiment_b(df, feats),
              "C_anomaly_events": experiment_c(df, feats)}
    (OUT / f"extra_{stamp}.json").write_text(json.dumps(report, indent=1, default=str))
    (OUT / "extra_latest.json").write_text(json.dumps(report, indent=1, default=str))
    print(OUT / f"extra_{stamp}.json")


if __name__ == "__main__":
    main()
