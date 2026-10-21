# Live monitor (2026-10-21T23:06:59.177934+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.57 (ECE 0.134)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.468
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.57 (ECE 0.114)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.443
- MISCALIBRATED: logistic|h4|all says 0.49 on average, reality 0.57 (ECE 0.088)
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.492
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.45 on average, reality 0.58 (ECE 0.132)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.438

## Health

- **venue**: okx
- **symbols**: 63
- **universe_size**: 60
- **fetched_only_for_scoring**: ['COMP', 'HBAR', 'RAY']
- **last_closed_bar**: 2026-10-21 22:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.9
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 107.9 instruments 63/63']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.147, 'recent_base_rate_7d': 0.091, 'momentum_24': 0.161, 'logistic': 0.166, 'lgbm_calibrated': 0.117, 'analog_k100': 0.016, 'derivatives': 0.148, 'orthosys': 0.154}
- **council_member_logloss_h1**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.6964, 'momentum_24': 0.6928, 'logistic': 0.6927, 'lgbm_calibrated': 0.6948, 'analog_k100': 0.7089, 'derivatives': 0.6936, 'orthosys': 0.6931}
- **council_calls_h1**: 0
- **council_abstain_h1**: {'no_edge': 53, 'extreme_volatility': 7}
- **council_weights_h4**: {'base_rate': 0.234, 'recent_base_rate_7d': 0.004, 'momentum_24': 0.233, 'logistic': 0.087, 'lgbm_calibrated': 0.025, 'analog_k100': 0.001, 'derivatives': 0.223, 'orthosys': 0.192}
- **council_member_logloss_h4**: {'base_rate': 0.6922, 'recent_base_rate_7d': 0.7198, 'momentum_24': 0.6922, 'logistic': 0.6986, 'lgbm_calibrated': 0.7067, 'analog_k100': 0.7354, 'derivatives': 0.6923, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 53, 'extreme_volatility': 7}
- **prediction_latency_min**: 6.9
- **price_snapshot_age_s**: 0.7
- **train_rows_h1**: 93974
- **orthosys_hist_hit_h1**: 0.5307
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0083
- **p_spread_logistic_h1**: 0.0338
- **p_spread_lgbm_calibrated_h1**: 0.0217
- **p_spread_analog_k100_h1**: 0.064
- **p_spread_derivatives_h1**: 0.021
- **p_spread_orthosys_h1**: 0.0079
- **p_spread_council_h1**: 0.0
- **train_rows_h4**: 93785
- **orthosys_hist_hit_h4**: 0.5128
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0004
- **p_spread_logistic_h4**: 0.0725
- **p_spread_lgbm_calibrated_h4**: 0.0112
- **p_spread_analog_k100_h4**: 0.1099
- **p_spread_derivatives_h4**: 0.0539
- **p_spread_orthosys_h4**: 0.0033
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 58560

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 3000 | 50 | 3000 | 0.490 | 0.47-0.51 | 0.514 | 0.466 | -0.0290 | 0.066 | 0.50 | -15.4 |
| analog_k100|h1|on_time | 3000 | 50 | 3000 | 0.490 | 0.47-0.51 | 0.514 | 0.466 | -0.0290 | 0.066 | 0.50 | -15.4 |
| analog_k100|h4|all | 2820 | 47 | 2820 | 0.450 | 0.43-0.47 | 0.573 | 0.445 | -0.0793 | 0.134 | 0.64 | -29.1 |
| analog_k100|h4|on_time | 2820 | 47 | 2820 | 0.450 | 0.43-0.47 | 0.573 | 0.445 | -0.0793 | 0.134 | 0.64 | -29.1 |
| base_rate|h1|all | 3300 | 55 | 3300 | 0.486 | 0.47-0.50 | 0.514 | 0.498 | +0.0000 | 0.016 | 0.00 | - |
| base_rate|h1|on_time | 3240 | 54 | 3240 | 0.489 | 0.47-0.51 | 0.511 | 0.498 | +0.0000 | 0.013 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 3120 | 52 | 3120 | 0.574 | 0.56-0.59 | 0.574 | 0.504 | +0.0000 | 0.071 | 0.00 | - |
| base_rate|h4|on_time | 3120 | 52 | 3120 | 0.574 | 0.56-0.59 | 0.574 | 0.504 | +0.0000 | 0.071 | 0.00 | - |
| council|h1|all | 3000 | 50 | 486 | 0.510 | 0.47-0.55 | 0.514 | 0.496 | +0.0006 | 0.019 | 0.00 | +18.3 |
| council|h1|on_time | 3000 | 50 | 486 | 0.510 | 0.47-0.55 | 0.514 | 0.496 | +0.0006 | 0.019 | 0.00 | +18.3 |
| council|h4|all | 2820 | 47 | 25 | 0.600 | 0.41-0.77 | 0.573 | 0.500 | -0.0015 | 0.073 | 0.00 | - |
| council|h4|on_time | 2820 | 47 | 25 | 0.600 | 0.41-0.77 | 0.573 | 0.500 | -0.0015 | 0.073 | 0.00 | - |
| derivatives|h1|all | 3000 | 50 | 3000 | 0.485 | 0.47-0.50 | 0.514 | 0.497 | -0.0001 | 0.018 | 0.01 | -124.1 |
| derivatives|h1|on_time | 3000 | 50 | 3000 | 0.485 | 0.47-0.50 | 0.514 | 0.497 | -0.0001 | 0.018 | 0.01 | -124.1 |
| derivatives|h4|all | 2820 | 47 | 2820 | 0.578 | 0.56-0.60 | 0.573 | 0.501 | +0.0007 | 0.074 | 0.01 | +330.2 |
| derivatives|h4|on_time | 2820 | 47 | 2820 | 0.578 | 0.56-0.60 | 0.573 | 0.501 | +0.0007 | 0.074 | 0.01 | +330.2 |
| lgbm_calibrated|h1|all | 3300 | 55 | 3299 | 0.533 | 0.52-0.55 | 0.514 | 0.473 | -0.0006 | 0.041 | 0.16 | -0.0 |
| lgbm_calibrated|h1|on_time | 3240 | 54 | 3239 | 0.537 | 0.52-0.55 | 0.511 | 0.473 | +0.0000 | 0.038 | 0.16 | -0.0 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 3120 | 52 | 3120 | 0.425 | 0.41-0.44 | 0.574 | 0.462 | -0.0269 | 0.114 | 0.17 | -48.0 |
| lgbm_calibrated|h4|on_time | 3120 | 52 | 3120 | 0.425 | 0.41-0.44 | 0.574 | 0.462 | -0.0269 | 0.114 | 0.17 | -48.0 |
| logistic|h1|all | 3300 | 55 | 3300 | 0.526 | 0.51-0.54 | 0.514 | 0.489 | +0.0026 | 0.026 | 0.10 | -23.8 |
| logistic|h1|on_time | 3240 | 54 | 3240 | 0.522 | 0.50-0.54 | 0.511 | 0.489 | +0.0016 | 0.024 | 0.10 | -23.8 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 3120 | 52 | 3120 | 0.512 | 0.49-0.53 | 0.574 | 0.493 | -0.0116 | 0.088 | 0.23 | -31.7 |
| logistic|h4|on_time | 3120 | 52 | 3120 | 0.512 | 0.49-0.53 | 0.574 | 0.493 | -0.0116 | 0.088 | 0.23 | -31.7 |
| momentum_24|h1|all | 3300 | 55 | 3300 | 0.523 | 0.51-0.54 | 0.514 | 0.496 | +0.0015 | 0.018 | 0.00 | - |
| momentum_24|h1|on_time | 3240 | 54 | 3240 | 0.520 | 0.50-0.54 | 0.511 | 0.495 | +0.0012 | 0.016 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 3120 | 52 | 3120 | 0.574 | 0.56-0.59 | 0.574 | 0.504 | -0.0001 | 0.071 | 0.00 | - |
| momentum_24|h4|on_time | 3120 | 52 | 3120 | 0.574 | 0.56-0.59 | 0.574 | 0.504 | -0.0001 | 0.071 | 0.00 | - |
| orthosys|h1|all | 3300 | 55 | 235 | 0.523 | 0.46-0.59 | 0.514 | 0.499 | +0.0004 | 0.018 | 0.00 | - |
| orthosys|h1|on_time | 3240 | 54 | 234 | 0.521 | 0.46-0.58 | 0.511 | 0.499 | +0.0004 | 0.015 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 3120 | 52 | 227 | 0.427 | 0.36-0.49 | 0.574 | 0.499 | -0.0023 | 0.075 | 0.00 | - |
| orthosys|h4|on_time | 3120 | 52 | 227 | 0.427 | 0.36-0.49 | 0.574 | 0.499 | -0.0023 | 0.075 | 0.00 | - |
| recent_base_rate_7d|h1|all | 3240 | 54 | 3240 | 0.489 | 0.47-0.51 | 0.511 | 0.476 | -0.0055 | 0.035 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 3240 | 54 | 3240 | 0.489 | 0.47-0.51 | 0.511 | 0.476 | -0.0055 | 0.035 | 0.00 | - |
| recent_base_rate_7d|h4|all | 3060 | 51 | 3060 | 0.420 | 0.40-0.44 | 0.580 | 0.447 | -0.0532 | 0.132 | 0.69 | -68.7 |
| recent_base_rate_7d|h4|on_time | 3060 | 51 | 3060 | 0.420 | 0.40-0.44 | 0.580 | 0.447 | -0.0532 | 0.132 | 0.69 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 930.36 | -6.96% | 1511 | 589 | 50 |
| analog_k100|h4 | 971.62 | -2.84% | 1814 | 722 | 47 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 55 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 52 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 50 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 47 |
| derivatives|h1 | 995.90 | -0.41% | 19 | 5 | 50 |
| derivatives|h4 | 1081.40 | +8.14% | 36 | 18 | 47 |
| lgbm_calibrated|h1 | 924.76 | -7.52% | 521 | 244 | 55 |
| lgbm_calibrated|h4 | 916.34 | -8.37% | 523 | 218 | 52 |
| logistic|h1 | 838.88 | -16.11% | 343 | 171 | 55 |
| logistic|h4 | 983.50 | -1.65% | 722 | 336 | 52 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 55 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 52 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 55 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 52 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 54 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 51 |
| benchmark_long_all_coins|h1 | 1004.54 | +0.45% | 3300 | 1542 | 55 |
| benchmark_long_all_coins|h4 | 1048.47 | +4.85% | 3120 | 1706 | 52 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 51 |

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
