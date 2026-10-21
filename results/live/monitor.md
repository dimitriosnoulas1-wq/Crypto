# Live monitor (2026-10-21T01:06:19.972036+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h1|all says 0.47 on average, reality 0.54 (ECE 0.081)
- MISCALIBRATED: analog_k100|h4|all says 0.44 on average, reality 0.59 (ECE 0.152)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.453
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.485
- MISCALIBRATED: base_rate|h4|all says 0.50 on average, reality 0.59 (ECE 0.083)
- MISCALIBRATED: council|h4|all says 0.50 on average, reality 0.59 (ECE 0.086)
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.479
- MISCALIBRATED: derivatives|h4|all says 0.50 on average, reality 0.59 (ECE 0.083)
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.59 (ECE 0.133)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.436
- MISCALIBRATED: logistic|h4|all says 0.49 on average, reality 0.59 (ECE 0.096)
- MISCALIBRATED: momentum_24|h4|all says 0.50 on average, reality 0.59 (ECE 0.083)
- MISCALIBRATED: orthosys|h4|all says 0.50 on average, reality 0.59 (ECE 0.087)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.489
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.60 (ECE 0.156)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.427

## Health

- **venue**: okx
- **symbols**: 61
- **universe_size**: 60
- **fetched_only_for_scoring**: ['GRASS']
- **last_closed_bar**: 2026-10-21 00:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.4
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 102.6 instruments 61/61']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.125, 'recent_base_rate_7d': 0.086, 'momentum_24': 0.144, 'logistic': 0.185, 'lgbm_calibrated': 0.146, 'analog_k100': 0.053, 'derivatives': 0.128, 'orthosys': 0.132}
- **council_member_logloss_h1**: {'base_rate': 0.6935, 'recent_base_rate_7d': 0.6976, 'momentum_24': 0.692, 'logistic': 0.6894, 'lgbm_calibrated': 0.6919, 'analog_k100': 0.7044, 'derivatives': 0.6936, 'orthosys': 0.6929}
- **council_calls_h1**: 9
- **council_abstain_h1**: {'no_edge': 49, 'spoke': 9, 'extreme_volatility': 2}
- **council_weights_h4**: {'base_rate': 0.201, 'recent_base_rate_7d': 0.012, 'momentum_24': 0.201, 'logistic': 0.158, 'lgbm_calibrated': 0.046, 'analog_k100': 0.005, 'derivatives': 0.196, 'orthosys': 0.181}
- **council_member_logloss_h4**: {'base_rate': 0.6924, 'recent_base_rate_7d': 0.726, 'momentum_24': 0.6924, 'logistic': 0.6952, 'lgbm_calibrated': 0.7093, 'analog_k100': 0.7447, 'derivatives': 0.6924, 'orthosys': 0.6936}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 58, 'extreme_volatility': 2}
- **prediction_latency_min**: 6.3
- **price_snapshot_age_s**: 0.8
- **train_rows_h1**: 89692
- **orthosys_hist_hit_h1**: 0.5284
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0048
- **p_spread_logistic_h1**: 0.0182
- **p_spread_lgbm_calibrated_h1**: 0.0151
- **p_spread_analog_k100_h1**: 0.06
- **p_spread_derivatives_h1**: 0.0003
- **p_spread_orthosys_h1**: 0.0037
- **p_spread_council_h1**: 0.008
- **train_rows_h4**: 89509
- **orthosys_hist_hit_h4**: 0.5141
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0004
- **p_spread_logistic_h4**: 0.0295
- **p_spread_lgbm_calibrated_h4**: 0.0031
- **p_spread_analog_k100_h4**: 0.0767
- **p_spread_derivatives_h4**: 0.0045
- **p_spread_orthosys_h4**: 0.0018
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 34800

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1680 | 28 | 1680 | 0.495 | 0.47-0.52 | 0.542 | 0.466 | -0.0286 | 0.081 | 0.52 | -15.7 |
| analog_k100|h1|on_time | 1680 | 28 | 1680 | 0.495 | 0.47-0.52 | 0.542 | 0.466 | -0.0286 | 0.081 | 0.52 | -15.7 |
| analog_k100|h4|all | 1500 | 25 | 1500 | 0.428 | 0.40-0.45 | 0.585 | 0.444 | -0.0977 | 0.152 | 0.65 | -59.0 |
| analog_k100|h4|on_time | 1500 | 25 | 1500 | 0.428 | 0.40-0.45 | 0.585 | 0.444 | -0.0977 | 0.152 | 0.65 | -59.0 |
| base_rate|h1|all | 1980 | 33 | 1980 | 0.463 | 0.44-0.49 | 0.537 | 0.498 | +0.0000 | 0.039 | 0.00 | - |
| base_rate|h1|on_time | 1920 | 32 | 1920 | 0.467 | 0.44-0.49 | 0.533 | 0.498 | +0.0000 | 0.035 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 1800 | 30 | 1800 | 0.586 | 0.56-0.61 | 0.586 | 0.503 | +0.0000 | 0.083 | 0.00 | - |
| base_rate|h4|on_time | 1800 | 30 | 1800 | 0.586 | 0.56-0.61 | 0.586 | 0.503 | +0.0000 | 0.083 | 0.00 | - |
| council|h1|all | 1680 | 28 | 321 | 0.551 | 0.50-0.60 | 0.542 | 0.495 | +0.0029 | 0.057 | 0.00 | +18.3 |
| council|h1|on_time | 1680 | 28 | 321 | 0.551 | 0.50-0.60 | 0.542 | 0.495 | +0.0029 | 0.057 | 0.00 | +18.3 |
| council|h4|all | 1500 | 25 | 20 | 0.600 | 0.39-0.78 | 0.585 | 0.500 | -0.0014 | 0.086 | 0.00 | - |
| council|h4|on_time | 1500 | 25 | 20 | 0.600 | 0.39-0.78 | 0.585 | 0.500 | -0.0014 | 0.086 | 0.00 | - |
| derivatives|h1|all | 1680 | 28 | 1680 | 0.455 | 0.43-0.48 | 0.542 | 0.498 | -0.0001 | 0.047 | 0.00 | - |
| derivatives|h1|on_time | 1680 | 28 | 1680 | 0.455 | 0.43-0.48 | 0.542 | 0.498 | -0.0001 | 0.047 | 0.00 | - |
| derivatives|h4|all | 1500 | 25 | 1500 | 0.583 | 0.56-0.61 | 0.585 | 0.502 | -0.0001 | 0.083 | 0.00 | -117.6 |
| derivatives|h4|on_time | 1500 | 25 | 1500 | 0.583 | 0.56-0.61 | 0.585 | 0.502 | -0.0001 | 0.083 | 0.00 | -117.6 |
| lgbm_calibrated|h1|all | 1980 | 33 | 1980 | 0.538 | 0.52-0.56 | 0.537 | 0.475 | +0.0019 | 0.062 | 0.13 | +6.3 |
| lgbm_calibrated|h1|on_time | 1920 | 32 | 1920 | 0.544 | 0.52-0.57 | 0.533 | 0.475 | +0.0032 | 0.059 | 0.14 | +6.3 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 1800 | 30 | 1800 | 0.413 | 0.39-0.44 | 0.586 | 0.456 | -0.0349 | 0.133 | 0.27 | -50.2 |
| lgbm_calibrated|h4|on_time | 1800 | 30 | 1800 | 0.413 | 0.39-0.44 | 0.586 | 0.456 | -0.0349 | 0.133 | 0.27 | -50.2 |
| logistic|h1|all | 1980 | 33 | 1980 | 0.534 | 0.51-0.56 | 0.537 | 0.490 | +0.0077 | 0.050 | 0.11 | -8.1 |
| logistic|h1|on_time | 1920 | 32 | 1920 | 0.526 | 0.50-0.55 | 0.533 | 0.489 | +0.0062 | 0.047 | 0.11 | -8.0 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 1800 | 30 | 1800 | 0.512 | 0.49-0.53 | 0.586 | 0.491 | -0.0058 | 0.096 | 0.21 | +3.2 |
| logistic|h4|on_time | 1800 | 30 | 1800 | 0.512 | 0.49-0.53 | 0.586 | 0.491 | -0.0058 | 0.096 | 0.21 | +3.2 |
| momentum_24|h1|all | 1980 | 33 | 1980 | 0.535 | 0.51-0.56 | 0.537 | 0.497 | +0.0025 | 0.040 | 0.00 | - |
| momentum_24|h1|on_time | 1920 | 32 | 1920 | 0.530 | 0.51-0.55 | 0.533 | 0.497 | +0.0021 | 0.037 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 1800 | 30 | 1800 | 0.586 | 0.56-0.61 | 0.586 | 0.503 | +0.0000 | 0.083 | 0.00 | - |
| momentum_24|h4|on_time | 1800 | 30 | 1800 | 0.586 | 0.56-0.61 | 0.586 | 0.503 | +0.0000 | 0.083 | 0.00 | - |
| orthosys|h1|all | 1980 | 33 | 178 | 0.545 | 0.47-0.62 | 0.537 | 0.498 | +0.0013 | 0.041 | 0.00 | - |
| orthosys|h1|on_time | 1920 | 32 | 177 | 0.542 | 0.47-0.61 | 0.533 | 0.498 | +0.0012 | 0.037 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 1800 | 30 | 175 | 0.429 | 0.36-0.50 | 0.586 | 0.499 | -0.0025 | 0.087 | 0.00 | - |
| orthosys|h4|on_time | 1800 | 30 | 175 | 0.429 | 0.36-0.50 | 0.586 | 0.499 | -0.0025 | 0.087 | 0.00 | - |
| recent_base_rate_7d|h1|all | 1920 | 32 | 1920 | 0.467 | 0.44-0.49 | 0.533 | 0.473 | -0.0090 | 0.060 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 1920 | 32 | 1920 | 0.467 | 0.44-0.49 | 0.533 | 0.473 | -0.0090 | 0.060 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1740 | 29 | 1740 | 0.404 | 0.38-0.43 | 0.596 | 0.440 | -0.0670 | 0.156 | 0.93 | -71.8 |
| recent_base_rate_7d|h4|on_time | 1740 | 29 | 1740 | 0.404 | 0.38-0.43 | 0.596 | 0.440 | -0.0670 | 0.156 | 0.93 | -71.8 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 955.48 | -4.45% | 878 | 339 | 28 |
| analog_k100|h4 | 966.32 | -3.37% | 971 | 363 | 25 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 33 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 30 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 28 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 25 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 28 |
| derivatives|h4 | 985.33 | -1.47% | 5 | 1 | 25 |
| lgbm_calibrated|h1 | 934.27 | -6.57% | 263 | 129 | 33 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 30 |
| logistic|h1 | 938.48 | -6.15% | 212 | 111 | 33 |
| logistic|h4 | 1031.81 | +3.18% | 381 | 184 | 30 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 33 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 30 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 33 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 30 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 32 |
| recent_base_rate_7d|h4 | 952.56 | -4.74% | 1620 | 622 | 29 |
| benchmark_long_all_coins|h1 | 1013.50 | +1.35% | 1980 | 953 | 33 |
| benchmark_long_all_coins|h4 | 1038.16 | +3.82% | 1800 | 983 | 30 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 29 |

## Unverified (pending, not scored)

- analog_k100|h1: 60
- analog_k100|h4: 240
- base_rate|h1: 60
- base_rate|h4: 240
- council|h1: 60
- council|h4: 240
- derivatives|h1: 60
- derivatives|h4: 240
- lgbm_calibrated|h1: 60
- lgbm_calibrated|h4: 240
- logistic|h1: 60
- logistic|h4: 240
- momentum_24|h1: 60
- momentum_24|h4: 240
- orthosys|h1: 60
- orthosys|h4: 240
- recent_base_rate_7d|h1: 60
- recent_base_rate_7d|h4: 240
