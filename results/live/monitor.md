# Live monitor (2026-10-22T06:10:19.264371+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h4|all says 0.44 on average, reality 0.51 (ECE 0.103)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.497
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.460
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.498

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['APR', 'CHIP']
- **last_closed_bar**: 2026-10-22 05:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 8.3
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 100.9 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.033
- **council_weights_h1**: {'base_rate': 0.154, 'recent_base_rate_7d': 0.124, 'momentum_24': 0.171, 'logistic': 0.101, 'lgbm_calibrated': 0.123, 'analog_k100': 0.013, 'derivatives': 0.167, 'orthosys': 0.147}
- **council_member_logloss_h1**: {'base_rate': 0.693, 'recent_base_rate_7d': 0.6942, 'momentum_24': 0.6924, 'logistic': 0.6953, 'lgbm_calibrated': 0.6942, 'analog_k100': 0.7077, 'derivatives': 0.6927, 'orthosys': 0.6933}
- **council_calls_h1**: 2
- **council_abstain_h1**: {'no_edge': 50, 'extreme_volatility': 7, 'spoke': 2, 'missing_inputs': 1}
- **council_weights_h4**: {'base_rate': 0.202, 'recent_base_rate_7d': 0.007, 'momentum_24': 0.199, 'logistic': 0.064, 'lgbm_calibrated': 0.065, 'analog_k100': 0.006, 'derivatives': 0.265, 'orthosys': 0.191}
- **council_member_logloss_h4**: {'base_rate': 0.6932, 'recent_base_rate_7d': 0.7126, 'momentum_24': 0.6933, 'logistic': 0.6998, 'lgbm_calibrated': 0.6997, 'analog_k100': 0.7154, 'derivatives': 0.6914, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 50, 'extreme_volatility': 7, 'members_disagree': 2, 'missing_inputs': 1}
- **prediction_latency_min**: 10.2
- **price_snapshot_age_s**: 0.8
- **train_rows_h1**: 91335
- **orthosys_hist_hit_h1**: 0.5284
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0043
- **p_spread_logistic_h1**: 0.0399
- **p_spread_lgbm_calibrated_h1**: 0.0108
- **p_spread_analog_k100_h1**: 0.0681
- **p_spread_derivatives_h1**: 0.0279
- **p_spread_orthosys_h1**: 0.0143
- **p_spread_council_h1**: 0.0043
- **train_rows_h4**: 91149
- **orthosys_hist_hit_h4**: 0.508
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0002
- **p_spread_logistic_h4**: 0.0731
- **p_spread_lgbm_calibrated_h4**: 0.004
- **p_spread_analog_k100_h4**: 0.1114
- **p_spread_derivatives_h4**: 0.0494
- **p_spread_orthosys_h4**: 0.004
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 66120

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 3420 | 57 | 3420 | 0.490 | 0.47-0.51 | 0.481 | 0.470 | -0.0305 | 0.067 | 0.51 | -14.6 |
| analog_k100|h1|on_time | 3420 | 57 | 3420 | 0.490 | 0.47-0.51 | 0.481 | 0.470 | -0.0305 | 0.067 | 0.51 | -14.6 |
| analog_k100|h4|all | 3240 | 54 | 3240 | 0.479 | 0.46-0.50 | 0.508 | 0.444 | -0.0457 | 0.103 | 0.65 | -11.3 |
| analog_k100|h4|on_time | 3240 | 54 | 3240 | 0.479 | 0.46-0.50 | 0.508 | 0.444 | -0.0457 | 0.103 | 0.65 | -11.3 |
| base_rate|h1|all | 3720 | 62 | 3720 | 0.517 | 0.50-0.53 | 0.483 | 0.498 | +0.0000 | 0.015 | 0.00 | - |
| base_rate|h1|on_time | 3660 | 61 | 3660 | 0.520 | 0.50-0.54 | 0.480 | 0.498 | +0.0000 | 0.018 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 3540 | 59 | 3540 | 0.515 | 0.50-0.53 | 0.515 | 0.504 | +0.0000 | 0.011 | 0.00 | - |
| base_rate|h4|on_time | 3540 | 59 | 3540 | 0.515 | 0.50-0.53 | 0.515 | 0.504 | +0.0000 | 0.011 | 0.00 | - |
| council|h1|all | 3420 | 57 | 492 | 0.510 | 0.47-0.55 | 0.481 | 0.496 | -0.0004 | 0.020 | 0.00 | +18.3 |
| council|h1|on_time | 3420 | 57 | 492 | 0.510 | 0.47-0.55 | 0.481 | 0.496 | -0.0004 | 0.020 | 0.00 | +18.3 |
| council|h4|all | 3240 | 54 | 25 | 0.600 | 0.41-0.77 | 0.508 | 0.500 | +0.0006 | 0.008 | 0.00 | - |
| council|h4|on_time | 3240 | 54 | 25 | 0.600 | 0.41-0.77 | 0.508 | 0.500 | +0.0006 | 0.008 | 0.00 | - |
| derivatives|h1|all | 3420 | 57 | 3420 | 0.519 | 0.50-0.54 | 0.481 | 0.497 | +0.0008 | 0.016 | 0.01 | -20.5 |
| derivatives|h1|on_time | 3420 | 57 | 3420 | 0.519 | 0.50-0.54 | 0.481 | 0.497 | +0.0008 | 0.016 | 0.01 | -20.5 |
| derivatives|h4|all | 3240 | 54 | 3240 | 0.523 | 0.51-0.54 | 0.508 | 0.500 | +0.0038 | 0.017 | 0.02 | +481.8 |
| derivatives|h4|on_time | 3240 | 54 | 3240 | 0.523 | 0.51-0.54 | 0.508 | 0.500 | +0.0038 | 0.017 | 0.02 | +481.8 |
| lgbm_calibrated|h1|all | 3720 | 62 | 3719 | 0.542 | 0.53-0.56 | 0.483 | 0.476 | -0.0020 | 0.014 | 0.14 | -2.6 |
| lgbm_calibrated|h1|on_time | 3660 | 61 | 3659 | 0.545 | 0.53-0.56 | 0.480 | 0.476 | -0.0014 | 0.018 | 0.15 | -2.6 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 3540 | 59 | 3540 | 0.484 | 0.47-0.50 | 0.515 | 0.463 | -0.0103 | 0.054 | 0.15 | -48.0 |
| lgbm_calibrated|h4|on_time | 3540 | 59 | 3540 | 0.484 | 0.47-0.50 | 0.515 | 0.463 | -0.0103 | 0.054 | 0.15 | -48.0 |
| logistic|h1|all | 3720 | 62 | 3720 | 0.507 | 0.49-0.52 | 0.483 | 0.493 | -0.0056 | 0.018 | 0.13 | -31.7 |
| logistic|h1|on_time | 3660 | 61 | 3660 | 0.502 | 0.49-0.52 | 0.480 | 0.492 | -0.0066 | 0.023 | 0.13 | -31.8 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 3540 | 59 | 3540 | 0.494 | 0.48-0.51 | 0.515 | 0.494 | -0.0139 | 0.045 | 0.24 | -23.0 |
| logistic|h4|on_time | 3540 | 59 | 3540 | 0.494 | 0.48-0.51 | 0.515 | 0.494 | -0.0139 | 0.045 | 0.24 | -23.0 |
| momentum_24|h1|all | 3720 | 62 | 3720 | 0.514 | 0.50-0.53 | 0.483 | 0.496 | +0.0008 | 0.013 | 0.00 | - |
| momentum_24|h1|on_time | 3660 | 61 | 3660 | 0.511 | 0.49-0.53 | 0.480 | 0.496 | +0.0005 | 0.016 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 3540 | 59 | 3540 | 0.515 | 0.50-0.53 | 0.515 | 0.504 | -0.0001 | 0.011 | 0.00 | - |
| momentum_24|h4|on_time | 3540 | 59 | 3540 | 0.515 | 0.50-0.53 | 0.515 | 0.504 | -0.0001 | 0.011 | 0.00 | - |
| orthosys|h1|all | 3720 | 62 | 299 | 0.485 | 0.43-0.54 | 0.483 | 0.500 | -0.0012 | 0.017 | 0.00 | - |
| orthosys|h1|on_time | 3660 | 61 | 298 | 0.483 | 0.43-0.54 | 0.480 | 0.500 | -0.0013 | 0.020 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 3540 | 59 | 258 | 0.399 | 0.34-0.46 | 0.515 | 0.499 | -0.0005 | 0.015 | 0.00 | - |
| orthosys|h4|on_time | 3540 | 59 | 258 | 0.399 | 0.34-0.46 | 0.515 | 0.499 | -0.0005 | 0.015 | 0.00 | - |
| recent_base_rate_7d|h1|all | 3660 | 61 | 3660 | 0.520 | 0.50-0.54 | 0.480 | 0.477 | -0.0020 | 0.003 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 3660 | 61 | 3660 | 0.520 | 0.50-0.54 | 0.480 | 0.477 | -0.0020 | 0.003 | 0.00 | - |
| recent_base_rate_7d|h4|all | 3480 | 58 | 3480 | 0.481 | 0.46-0.50 | 0.519 | 0.451 | -0.0363 | 0.068 | 0.60 | -68.7 |
| recent_base_rate_7d|h4|on_time | 3480 | 58 | 3480 | 0.481 | 0.46-0.50 | 0.519 | 0.451 | -0.0363 | 0.068 | 0.60 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 924.96 | -7.50% | 1747 | 695 | 57 |
| analog_k100|h4 | 988.48 | -1.15% | 2112 | 942 | 54 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 62 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 59 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 57 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 54 |
| derivatives|h1 | 1128.94 | +12.89% | 27 | 12 | 57 |
| derivatives|h4 | 1216.65 | +21.67% | 59 | 38 | 54 |
| lgbm_calibrated|h1 | 905.66 | -9.43% | 531 | 247 | 62 |
| lgbm_calibrated|h4 | 916.34 | -8.37% | 523 | 218 | 59 |
| logistic|h1 | 804.76 | -19.52% | 469 | 198 | 62 |
| logistic|h4 | 990.38 | -0.96% | 866 | 390 | 59 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 62 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 59 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 62 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 59 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 61 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 58 |
| benchmark_long_all_coins|h1 | 959.85 | -4.01% | 3720 | 1607 | 62 |
| benchmark_long_all_coins|h4 | 1004.81 | +0.48% | 3540 | 1737 | 59 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 57 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 62 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 59 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 57 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 57 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 62 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 59 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 62 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 59 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 62 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 59 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 62 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 59 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 61 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 58 |

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
