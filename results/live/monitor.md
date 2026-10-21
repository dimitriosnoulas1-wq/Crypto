# Live monitor (2026-10-21T02:05:52.829160+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h1|all says 0.47 on average, reality 0.54 (ECE 0.083)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.59 (ECE 0.153)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.458
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.483
- MISCALIBRATED: base_rate|h4|all says 0.50 on average, reality 0.59 (ECE 0.087)
- MISCALIBRATED: council|h4|all says 0.50 on average, reality 0.59 (ECE 0.091)
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.477
- MISCALIBRATED: derivatives|h4|all says 0.50 on average, reality 0.59 (ECE 0.087)
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.59 (ECE 0.136)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.432
- MISCALIBRATED: logistic|h4|all says 0.49 on average, reality 0.59 (ECE 0.098)
- MISCALIBRATED: momentum_24|h4|all says 0.50 on average, reality 0.59 (ECE 0.087)
- MISCALIBRATED: orthosys|h4|all says 0.50 on average, reality 0.59 (ECE 0.091)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.487
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.60 (ECE 0.160)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.423

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['DASH', 'GRASS']
- **last_closed_bar**: 2026-10-21 01:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 3.9
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 107.1 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.129, 'recent_base_rate_7d': 0.084, 'momentum_24': 0.146, 'logistic': 0.19, 'lgbm_calibrated': 0.142, 'analog_k100': 0.038, 'derivatives': 0.132, 'orthosys': 0.138}
- **council_member_logloss_h1**: {'base_rate': 0.6936, 'recent_base_rate_7d': 0.698, 'momentum_24': 0.6923, 'logistic': 0.6897, 'lgbm_calibrated': 0.6926, 'analog_k100': 0.7084, 'derivatives': 0.6936, 'orthosys': 0.6929}
- **council_calls_h1**: 6
- **council_abstain_h1**: {'no_edge': 52, 'spoke': 6, 'extreme_volatility': 2}
- **council_weights_h4**: {'base_rate': 0.204, 'recent_base_rate_7d': 0.011, 'momentum_24': 0.204, 'logistic': 0.155, 'lgbm_calibrated': 0.043, 'analog_k100': 0.004, 'derivatives': 0.197, 'orthosys': 0.182}
- **council_member_logloss_h4**: {'base_rate': 0.6924, 'recent_base_rate_7d': 0.7259, 'momentum_24': 0.6923, 'logistic': 0.6954, 'lgbm_calibrated': 0.7097, 'analog_k100': 0.7431, 'derivatives': 0.6924, 'orthosys': 0.6936}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 58, 'extreme_volatility': 2}
- **prediction_latency_min**: 5.8
- **price_snapshot_age_s**: 1.0
- **train_rows_h1**: 90903
- **orthosys_hist_hit_h1**: 0.5268
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0038
- **p_spread_logistic_h1**: 0.0186
- **p_spread_lgbm_calibrated_h1**: 0.0156
- **p_spread_analog_k100_h1**: 0.0601
- **p_spread_derivatives_h1**: 0.0009
- **p_spread_orthosys_h1**: 0.006
- **p_spread_council_h1**: 0.0067
- **train_rows_h4**: 90717
- **orthosys_hist_hit_h4**: 0.5141
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0001
- **p_spread_logistic_h4**: 0.033
- **p_spread_lgbm_calibrated_h4**: 0.0065
- **p_spread_analog_k100_h4**: 0.0761
- **p_spread_derivatives_h4**: 0.0033
- **p_spread_orthosys_h4**: 0.0032
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 35880

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1740 | 29 | 1740 | 0.491 | 0.47-0.51 | 0.544 | 0.466 | -0.0305 | 0.083 | 0.52 | -14.4 |
| analog_k100|h1|on_time | 1740 | 29 | 1740 | 0.491 | 0.47-0.51 | 0.544 | 0.466 | -0.0305 | 0.083 | 0.52 | -14.4 |
| analog_k100|h4|all | 1560 | 26 | 1560 | 0.433 | 0.41-0.46 | 0.590 | 0.446 | -0.0935 | 0.153 | 0.65 | -53.5 |
| analog_k100|h4|on_time | 1560 | 26 | 1560 | 0.433 | 0.41-0.46 | 0.590 | 0.446 | -0.0935 | 0.153 | 0.65 | -53.5 |
| base_rate|h1|all | 2040 | 34 | 2040 | 0.461 | 0.44-0.48 | 0.539 | 0.498 | +0.0000 | 0.041 | 0.00 | - |
| base_rate|h1|on_time | 1980 | 33 | 1980 | 0.465 | 0.44-0.49 | 0.535 | 0.498 | +0.0000 | 0.037 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 1860 | 31 | 1860 | 0.590 | 0.57-0.61 | 0.590 | 0.503 | +0.0000 | 0.087 | 0.00 | - |
| base_rate|h4|on_time | 1860 | 31 | 1860 | 0.590 | 0.57-0.61 | 0.590 | 0.503 | +0.0000 | 0.087 | 0.00 | - |
| council|h1|all | 1740 | 29 | 330 | 0.542 | 0.49-0.60 | 0.544 | 0.495 | +0.0026 | 0.056 | 0.00 | +18.3 |
| council|h1|on_time | 1740 | 29 | 330 | 0.542 | 0.49-0.60 | 0.544 | 0.495 | +0.0026 | 0.056 | 0.00 | +18.3 |
| council|h4|all | 1560 | 26 | 20 | 0.600 | 0.39-0.78 | 0.590 | 0.500 | -0.0016 | 0.091 | 0.00 | - |
| council|h4|on_time | 1560 | 26 | 20 | 0.600 | 0.39-0.78 | 0.590 | 0.500 | -0.0016 | 0.091 | 0.00 | - |
| derivatives|h1|all | 1740 | 29 | 1740 | 0.453 | 0.43-0.48 | 0.544 | 0.498 | -0.0001 | 0.049 | 0.00 | - |
| derivatives|h1|on_time | 1740 | 29 | 1740 | 0.453 | 0.43-0.48 | 0.544 | 0.498 | -0.0001 | 0.049 | 0.00 | - |
| derivatives|h4|all | 1560 | 26 | 1560 | 0.587 | 0.56-0.61 | 0.590 | 0.502 | -0.0001 | 0.087 | 0.00 | -117.6 |
| derivatives|h4|on_time | 1560 | 26 | 1560 | 0.587 | 0.56-0.61 | 0.590 | 0.502 | -0.0001 | 0.087 | 0.00 | -117.6 |
| lgbm_calibrated|h1|all | 2040 | 34 | 2040 | 0.535 | 0.51-0.56 | 0.539 | 0.474 | +0.0009 | 0.065 | 0.13 | +6.3 |
| lgbm_calibrated|h1|on_time | 1980 | 33 | 1980 | 0.540 | 0.52-0.56 | 0.535 | 0.475 | +0.0020 | 0.061 | 0.13 | +6.3 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 1860 | 31 | 1860 | 0.410 | 0.39-0.43 | 0.590 | 0.457 | -0.0359 | 0.136 | 0.26 | -50.2 |
| lgbm_calibrated|h4|on_time | 1860 | 31 | 1860 | 0.410 | 0.39-0.43 | 0.590 | 0.457 | -0.0359 | 0.136 | 0.26 | -50.2 |
| logistic|h1|all | 2040 | 34 | 2040 | 0.531 | 0.51-0.55 | 0.539 | 0.490 | +0.0074 | 0.052 | 0.10 | -8.0 |
| logistic|h1|on_time | 1980 | 33 | 1980 | 0.523 | 0.50-0.55 | 0.535 | 0.489 | +0.0058 | 0.049 | 0.11 | -7.8 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 1860 | 31 | 1860 | 0.516 | 0.49-0.54 | 0.590 | 0.492 | -0.0045 | 0.098 | 0.21 | +2.2 |
| logistic|h4|on_time | 1860 | 31 | 1860 | 0.516 | 0.49-0.54 | 0.590 | 0.492 | -0.0045 | 0.098 | 0.21 | +2.2 |
| momentum_24|h1|all | 2040 | 34 | 2040 | 0.531 | 0.51-0.55 | 0.539 | 0.497 | +0.0022 | 0.042 | 0.00 | - |
| momentum_24|h1|on_time | 1980 | 33 | 1980 | 0.526 | 0.50-0.55 | 0.535 | 0.497 | +0.0018 | 0.039 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 1860 | 31 | 1860 | 0.590 | 0.57-0.61 | 0.590 | 0.503 | +0.0000 | 0.087 | 0.00 | - |
| momentum_24|h4|on_time | 1860 | 31 | 1860 | 0.590 | 0.57-0.61 | 0.590 | 0.503 | +0.0000 | 0.087 | 0.00 | - |
| orthosys|h1|all | 2040 | 34 | 179 | 0.542 | 0.47-0.61 | 0.539 | 0.498 | +0.0013 | 0.042 | 0.00 | - |
| orthosys|h1|on_time | 1980 | 33 | 178 | 0.539 | 0.47-0.61 | 0.535 | 0.498 | +0.0012 | 0.038 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 1860 | 31 | 176 | 0.432 | 0.36-0.51 | 0.590 | 0.499 | -0.0026 | 0.091 | 0.00 | - |
| orthosys|h4|on_time | 1860 | 31 | 176 | 0.432 | 0.36-0.51 | 0.590 | 0.499 | -0.0026 | 0.091 | 0.00 | - |
| recent_base_rate_7d|h1|all | 1980 | 33 | 1980 | 0.465 | 0.44-0.49 | 0.535 | 0.473 | -0.0092 | 0.062 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 1980 | 33 | 1980 | 0.465 | 0.44-0.49 | 0.535 | 0.473 | -0.0092 | 0.062 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1800 | 30 | 1800 | 0.401 | 0.38-0.42 | 0.599 | 0.440 | -0.0681 | 0.160 | 0.93 | -72.0 |
| recent_base_rate_7d|h4|on_time | 1800 | 30 | 1800 | 0.401 | 0.38-0.42 | 0.599 | 0.440 | -0.0681 | 0.160 | 0.93 | -72.0 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 957.72 | -4.23% | 909 | 345 | 29 |
| analog_k100|h4 | 968.49 | -3.15% | 1008 | 382 | 26 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 34 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 31 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 29 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 26 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 29 |
| derivatives|h4 | 985.33 | -1.47% | 5 | 1 | 26 |
| lgbm_calibrated|h1 | 934.27 | -6.57% | 263 | 129 | 34 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 31 |
| logistic|h1 | 939.45 | -6.05% | 214 | 112 | 34 |
| logistic|h4 | 1031.13 | +3.11% | 394 | 191 | 31 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 34 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 31 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 34 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 31 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 33 |
| recent_base_rate_7d|h4 | 950.73 | -4.93% | 1680 | 641 | 30 |
| benchmark_long_all_coins|h1 | 1023.33 | +2.33% | 2040 | 1003 | 34 |
| benchmark_long_all_coins|h4 | 1039.63 | +3.96% | 1860 | 1020 | 31 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 30 |

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
