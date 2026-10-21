# Live monitor (2026-10-21T18:06:32.189361+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.59 (ECE 0.149)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.456
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.489
- MISCALIBRATED: base_rate|h4|all says 0.50 on average, reality 0.59 (ECE 0.090)
- MISCALIBRATED: council|h4|all says 0.50 on average, reality 0.59 (ECE 0.094)
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.487
- MISCALIBRATED: derivatives|h4|all says 0.50 on average, reality 0.59 (ECE 0.093)
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.59 (ECE 0.133)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.425
- MISCALIBRATED: logistic|h4|all says 0.50 on average, reality 0.59 (ECE 0.100)
- MISCALIBRATED: momentum_24|h4|all says 0.50 on average, reality 0.59 (ECE 0.090)
- MISCALIBRATED: orthosys|h4|all says 0.50 on average, reality 0.59 (ECE 0.094)
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.492
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.492
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.60 (ECE 0.156)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.419

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['AERO', 'HBAR']
- **last_closed_bar**: 2026-10-21 17:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.5
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 103.9 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.144, 'recent_base_rate_7d': 0.09, 'momentum_24': 0.158, 'logistic': 0.173, 'lgbm_calibrated': 0.108, 'analog_k100': 0.022, 'derivatives': 0.152, 'orthosys': 0.152}
- **council_member_logloss_h1**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.6968, 'momentum_24': 0.6928, 'logistic': 0.6922, 'lgbm_calibrated': 0.6954, 'analog_k100': 0.7079, 'derivatives': 0.6933, 'orthosys': 0.6931}
- **council_calls_h1**: 6
- **council_abstain_h1**: {'no_edge': 49, 'spoke': 6, 'extreme_volatility': 5}
- **council_weights_h4**: {'base_rate': 0.222, 'recent_base_rate_7d': 0.004, 'momentum_24': 0.221, 'logistic': 0.131, 'lgbm_calibrated': 0.027, 'analog_k100': 0.001, 'derivatives': 0.211, 'orthosys': 0.183}
- **council_member_logloss_h4**: {'base_rate': 0.6921, 'recent_base_rate_7d': 0.7222, 'momentum_24': 0.6921, 'logistic': 0.6959, 'lgbm_calibrated': 0.7072, 'analog_k100': 0.7376, 'derivatives': 0.6922, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 53, 'extreme_volatility': 5, 'members_disagree': 2}
- **prediction_latency_min**: 6.4
- **price_snapshot_age_s**: 1.1
- **train_rows_h1**: 92164
- **orthosys_hist_hit_h1**: 0.5306
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0063
- **p_spread_logistic_h1**: 0.0352
- **p_spread_lgbm_calibrated_h1**: 0.0265
- **p_spread_analog_k100_h1**: 0.0509
- **p_spread_derivatives_h1**: 0.0227
- **p_spread_orthosys_h1**: 0.0089
- **p_spread_council_h1**: 0.0078
- **train_rows_h4**: 91978
- **orthosys_hist_hit_h4**: 0.5115
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0008
- **p_spread_logistic_h4**: 0.0711
- **p_spread_lgbm_calibrated_h4**: 0.0021
- **p_spread_analog_k100_h4**: 0.094
- **p_spread_derivatives_h4**: 0.0378
- **p_spread_orthosys_h4**: 0.0033
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 53160

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 2700 | 45 | 2700 | 0.494 | 0.47-0.51 | 0.531 | 0.465 | -0.0312 | 0.072 | 0.52 | -14.1 |
| analog_k100|h1|on_time | 2700 | 45 | 2700 | 0.494 | 0.47-0.51 | 0.531 | 0.465 | -0.0312 | 0.072 | 0.52 | -14.1 |
| analog_k100|h4|all | 2520 | 42 | 2520 | 0.437 | 0.42-0.46 | 0.594 | 0.450 | -0.0899 | 0.149 | 0.63 | -33.0 |
| analog_k100|h4|on_time | 2520 | 42 | 2520 | 0.437 | 0.42-0.46 | 0.594 | 0.450 | -0.0899 | 0.149 | 0.63 | -33.0 |
| base_rate|h1|all | 3000 | 50 | 3000 | 0.471 | 0.45-0.49 | 0.529 | 0.498 | +0.0000 | 0.031 | 0.00 | - |
| base_rate|h1|on_time | 2940 | 49 | 2940 | 0.473 | 0.46-0.49 | 0.527 | 0.498 | +0.0000 | 0.029 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 2820 | 47 | 2820 | 0.593 | 0.58-0.61 | 0.593 | 0.503 | +0.0000 | 0.090 | 0.00 | - |
| base_rate|h4|on_time | 2820 | 47 | 2820 | 0.593 | 0.58-0.61 | 0.593 | 0.503 | +0.0000 | 0.090 | 0.00 | - |
| council|h1|all | 2700 | 45 | 472 | 0.508 | 0.46-0.55 | 0.531 | 0.495 | +0.0009 | 0.036 | 0.00 | +18.3 |
| council|h1|on_time | 2700 | 45 | 472 | 0.508 | 0.46-0.55 | 0.531 | 0.495 | +0.0009 | 0.036 | 0.00 | +18.3 |
| council|h4|all | 2520 | 42 | 22 | 0.591 | 0.39-0.77 | 0.594 | 0.500 | -0.0023 | 0.094 | 0.00 | - |
| council|h4|on_time | 2520 | 42 | 22 | 0.591 | 0.39-0.77 | 0.594 | 0.500 | -0.0023 | 0.094 | 0.00 | - |
| derivatives|h1|all | 2700 | 45 | 2700 | 0.469 | 0.45-0.49 | 0.531 | 0.498 | +0.0003 | 0.034 | 0.00 | -128.4 |
| derivatives|h1|on_time | 2700 | 45 | 2700 | 0.469 | 0.45-0.49 | 0.531 | 0.498 | +0.0003 | 0.034 | 0.00 | -128.4 |
| derivatives|h4|all | 2520 | 42 | 2520 | 0.596 | 0.58-0.62 | 0.594 | 0.502 | +0.0003 | 0.093 | 0.01 | +469.9 |
| derivatives|h4|on_time | 2520 | 42 | 2520 | 0.596 | 0.58-0.62 | 0.594 | 0.502 | +0.0003 | 0.093 | 0.01 | +469.9 |
| lgbm_calibrated|h1|all | 3000 | 50 | 3000 | 0.524 | 0.51-0.54 | 0.529 | 0.473 | -0.0044 | 0.056 | 0.16 | -3.6 |
| lgbm_calibrated|h1|on_time | 2940 | 49 | 2940 | 0.527 | 0.51-0.55 | 0.527 | 0.473 | -0.0037 | 0.053 | 0.16 | -3.6 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 2820 | 47 | 2820 | 0.406 | 0.39-0.42 | 0.593 | 0.462 | -0.0314 | 0.133 | 0.17 | -50.2 |
| lgbm_calibrated|h4|on_time | 2820 | 47 | 2820 | 0.406 | 0.39-0.42 | 0.593 | 0.462 | -0.0314 | 0.133 | 0.17 | -50.2 |
| logistic|h1|all | 3000 | 50 | 3000 | 0.524 | 0.51-0.54 | 0.529 | 0.490 | +0.0028 | 0.041 | 0.10 | -27.6 |
| logistic|h1|on_time | 2940 | 49 | 2940 | 0.518 | 0.50-0.54 | 0.527 | 0.489 | +0.0016 | 0.039 | 0.10 | -27.7 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 2820 | 47 | 2820 | 0.515 | 0.50-0.53 | 0.593 | 0.495 | -0.0086 | 0.100 | 0.21 | -33.8 |
| logistic|h4|on_time | 2820 | 47 | 2820 | 0.515 | 0.50-0.53 | 0.593 | 0.495 | -0.0086 | 0.100 | 0.21 | -33.8 |
| momentum_24|h1|all | 3000 | 50 | 3000 | 0.515 | 0.50-0.53 | 0.529 | 0.496 | +0.0009 | 0.033 | 0.00 | - |
| momentum_24|h1|on_time | 2940 | 49 | 2940 | 0.511 | 0.49-0.53 | 0.527 | 0.496 | +0.0006 | 0.031 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 2820 | 47 | 2820 | 0.593 | 0.58-0.61 | 0.593 | 0.503 | -0.0000 | 0.090 | 0.00 | - |
| momentum_24|h4|on_time | 2820 | 47 | 2820 | 0.593 | 0.58-0.61 | 0.593 | 0.503 | -0.0000 | 0.090 | 0.00 | - |
| orthosys|h1|all | 3000 | 50 | 216 | 0.532 | 0.47-0.60 | 0.529 | 0.499 | +0.0008 | 0.032 | 0.00 | - |
| orthosys|h1|on_time | 2940 | 49 | 215 | 0.530 | 0.46-0.60 | 0.527 | 0.499 | +0.0008 | 0.030 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 2820 | 47 | 203 | 0.424 | 0.36-0.49 | 0.593 | 0.499 | -0.0030 | 0.094 | 0.00 | - |
| orthosys|h4|on_time | 2820 | 47 | 203 | 0.424 | 0.36-0.49 | 0.593 | 0.499 | -0.0030 | 0.094 | 0.00 | - |
| recent_base_rate_7d|h1|all | 2940 | 49 | 2940 | 0.473 | 0.46-0.49 | 0.527 | 0.475 | -0.0071 | 0.052 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 2940 | 49 | 2940 | 0.473 | 0.46-0.49 | 0.527 | 0.475 | -0.0071 | 0.052 | 0.00 | - |
| recent_base_rate_7d|h4|all | 2760 | 46 | 2760 | 0.400 | 0.38-0.42 | 0.600 | 0.444 | -0.0611 | 0.156 | 0.76 | -68.7 |
| recent_base_rate_7d|h4|on_time | 2760 | 46 | 2760 | 0.400 | 0.38-0.42 | 0.600 | 0.444 | -0.0611 | 0.156 | 0.76 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 947.08 | -5.29% | 1397 | 541 | 45 |
| analog_k100|h4 | 971.65 | -2.84% | 1587 | 601 | 42 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 50 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 47 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 45 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 42 |
| derivatives|h1 | 921.25 | -7.87% | 9 | 4 | 45 |
| derivatives|h4 | 1070.46 | +7.05% | 20 | 10 | 42 |
| lgbm_calibrated|h1 | 924.47 | -7.55% | 473 | 210 | 50 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 47 |
| logistic|h1 | 839.93 | -16.01% | 302 | 152 | 50 |
| logistic|h4 | 985.14 | -1.49% | 585 | 275 | 47 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 50 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 47 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 50 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 47 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 49 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 46 |
| benchmark_long_all_coins|h1 | 1017.95 | +1.79% | 3000 | 1428 | 50 |
| benchmark_long_all_coins|h4 | 1054.61 | +5.46% | 2820 | 1594 | 47 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 46 |

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
