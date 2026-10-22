# Live monitor (2026-10-22T05:06:02.916695+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h4|all says 0.44 on average, reality 0.52 (ECE 0.100)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.494
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.466
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.491

## Health

- **venue**: okx
- **symbols**: 61
- **universe_size**: 60
- **fetched_only_for_scoring**: ['APR']
- **last_closed_bar**: 2026-10-22 04:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.1
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 98.6 instruments 61/61']
- **feature_nan_share_latest_bar**: 0.034
- **council_weights_h1**: {'base_rate': 0.155, 'recent_base_rate_7d': 0.122, 'momentum_24': 0.172, 'logistic': 0.105, 'lgbm_calibrated': 0.121, 'analog_k100': 0.015, 'derivatives': 0.165, 'orthosys': 0.146}
- **council_member_logloss_h1**: {'base_rate': 0.693, 'recent_base_rate_7d': 0.6944, 'momentum_24': 0.6924, 'logistic': 0.6952, 'lgbm_calibrated': 0.6944, 'analog_k100': 0.7074, 'derivatives': 0.6928, 'orthosys': 0.6933}
- **council_calls_h1**: 0
- **council_abstain_h1**: {'no_edge': 52, 'extreme_volatility': 7, 'missing_inputs': 1}
- **council_weights_h4**: {'base_rate': 0.206, 'recent_base_rate_7d': 0.006, 'momentum_24': 0.203, 'logistic': 0.071, 'lgbm_calibrated': 0.057, 'analog_k100': 0.004, 'derivatives': 0.26, 'orthosys': 0.192}
- **council_member_logloss_h4**: {'base_rate': 0.6931, 'recent_base_rate_7d': 0.7138, 'momentum_24': 0.6932, 'logistic': 0.6993, 'lgbm_calibrated': 0.7006, 'analog_k100': 0.7183, 'derivatives': 0.6915, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 50, 'extreme_volatility': 7, 'members_disagree': 2, 'missing_inputs': 1}
- **prediction_latency_min**: 5.9
- **price_snapshot_age_s**: 0.6
- **train_rows_h1**: 89714
- **orthosys_hist_hit_h1**: 0.5298
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0059
- **p_spread_logistic_h1**: 0.0442
- **p_spread_lgbm_calibrated_h1**: 0.0108
- **p_spread_analog_k100_h1**: 0.0693
- **p_spread_derivatives_h1**: 0.029
- **p_spread_orthosys_h1**: 0.013
- **p_spread_council_h1**: 0.0
- **train_rows_h4**: 89531
- **orthosys_hist_hit_h4**: 0.5091
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0003
- **p_spread_logistic_h4**: 0.0931
- **p_spread_lgbm_calibrated_h4**: 0.0453
- **p_spread_analog_k100_h4**: 0.1182
- **p_spread_derivatives_h4**: 0.0541
- **p_spread_orthosys_h4**: 0.004
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 65040

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 3360 | 56 | 3360 | 0.492 | 0.47-0.51 | 0.487 | 0.469 | -0.0287 | 0.065 | 0.51 | -13.5 |
| analog_k100|h1|on_time | 3360 | 56 | 3360 | 0.492 | 0.47-0.51 | 0.487 | 0.469 | -0.0287 | 0.065 | 0.51 | -13.5 |
| analog_k100|h4|all | 3180 | 53 | 3180 | 0.483 | 0.47-0.50 | 0.516 | 0.442 | -0.0422 | 0.100 | 0.65 | -10.3 |
| analog_k100|h4|on_time | 3180 | 53 | 3180 | 0.483 | 0.47-0.50 | 0.516 | 0.442 | -0.0422 | 0.100 | 0.65 | -10.3 |
| base_rate|h1|all | 3660 | 61 | 3660 | 0.511 | 0.50-0.53 | 0.489 | 0.498 | +0.0000 | 0.009 | 0.00 | - |
| base_rate|h1|on_time | 3600 | 60 | 3600 | 0.514 | 0.50-0.53 | 0.486 | 0.498 | +0.0000 | 0.012 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 3480 | 58 | 3480 | 0.522 | 0.51-0.54 | 0.522 | 0.504 | +0.0000 | 0.018 | 0.00 | - |
| base_rate|h4|on_time | 3480 | 58 | 3480 | 0.522 | 0.51-0.54 | 0.522 | 0.504 | +0.0000 | 0.018 | 0.00 | - |
| council|h1|all | 3360 | 56 | 492 | 0.510 | 0.47-0.55 | 0.487 | 0.496 | -0.0001 | 0.013 | 0.00 | +18.3 |
| council|h1|on_time | 3360 | 56 | 492 | 0.510 | 0.47-0.55 | 0.487 | 0.496 | -0.0001 | 0.013 | 0.00 | +18.3 |
| council|h4|all | 3180 | 53 | 25 | 0.600 | 0.41-0.77 | 0.516 | 0.500 | +0.0005 | 0.016 | 0.00 | - |
| council|h4|on_time | 3180 | 53 | 25 | 0.600 | 0.41-0.77 | 0.516 | 0.500 | +0.0005 | 0.016 | 0.00 | - |
| derivatives|h1|all | 3360 | 56 | 3360 | 0.512 | 0.50-0.53 | 0.487 | 0.497 | +0.0006 | 0.010 | 0.01 | -25.7 |
| derivatives|h1|on_time | 3360 | 56 | 3360 | 0.512 | 0.50-0.53 | 0.487 | 0.497 | +0.0006 | 0.010 | 0.01 | -25.7 |
| derivatives|h4|all | 3180 | 53 | 3180 | 0.530 | 0.51-0.55 | 0.516 | 0.500 | +0.0035 | 0.024 | 0.02 | +497.5 |
| derivatives|h4|on_time | 3180 | 53 | 3180 | 0.530 | 0.51-0.55 | 0.516 | 0.500 | +0.0035 | 0.024 | 0.02 | +497.5 |
| lgbm_calibrated|h1|all | 3660 | 61 | 3659 | 0.536 | 0.52-0.55 | 0.489 | 0.476 | -0.0025 | 0.013 | 0.14 | -2.5 |
| lgbm_calibrated|h1|on_time | 3600 | 60 | 3599 | 0.540 | 0.52-0.56 | 0.486 | 0.476 | -0.0019 | 0.012 | 0.15 | -2.5 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 3480 | 58 | 3480 | 0.477 | 0.46-0.49 | 0.522 | 0.463 | -0.0130 | 0.061 | 0.15 | -48.0 |
| lgbm_calibrated|h4|on_time | 3480 | 58 | 3480 | 0.477 | 0.46-0.49 | 0.522 | 0.463 | -0.0130 | 0.061 | 0.15 | -48.0 |
| logistic|h1|all | 3660 | 61 | 3660 | 0.511 | 0.50-0.53 | 0.489 | 0.492 | -0.0045 | 0.014 | 0.13 | -31.9 |
| logistic|h1|on_time | 3600 | 60 | 3600 | 0.507 | 0.49-0.52 | 0.486 | 0.492 | -0.0056 | 0.018 | 0.13 | -32.0 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 3480 | 58 | 3480 | 0.498 | 0.48-0.51 | 0.522 | 0.494 | -0.0127 | 0.041 | 0.24 | -22.1 |
| logistic|h4|on_time | 3480 | 58 | 3480 | 0.498 | 0.48-0.51 | 0.522 | 0.494 | -0.0127 | 0.041 | 0.24 | -22.1 |
| momentum_24|h1|all | 3660 | 61 | 3660 | 0.519 | 0.50-0.54 | 0.489 | 0.496 | +0.0011 | 0.009 | 0.00 | - |
| momentum_24|h1|on_time | 3600 | 60 | 3600 | 0.516 | 0.50-0.53 | 0.486 | 0.496 | +0.0009 | 0.010 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 3480 | 58 | 3480 | 0.522 | 0.51-0.54 | 0.522 | 0.504 | -0.0002 | 0.018 | 0.00 | - |
| momentum_24|h4|on_time | 3480 | 58 | 3480 | 0.522 | 0.51-0.54 | 0.522 | 0.504 | -0.0002 | 0.018 | 0.00 | - |
| orthosys|h1|all | 3660 | 61 | 284 | 0.507 | 0.45-0.56 | 0.489 | 0.499 | -0.0005 | 0.011 | 0.00 | - |
| orthosys|h1|on_time | 3600 | 60 | 283 | 0.505 | 0.45-0.56 | 0.486 | 0.499 | -0.0006 | 0.013 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 3480 | 58 | 250 | 0.404 | 0.35-0.47 | 0.522 | 0.499 | -0.0006 | 0.023 | 0.00 | - |
| orthosys|h4|on_time | 3480 | 58 | 250 | 0.404 | 0.35-0.47 | 0.522 | 0.499 | -0.0006 | 0.023 | 0.00 | - |
| recent_base_rate_7d|h1|all | 3600 | 60 | 3600 | 0.514 | 0.50-0.53 | 0.486 | 0.477 | -0.0025 | 0.009 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 3600 | 60 | 3600 | 0.514 | 0.50-0.53 | 0.486 | 0.477 | -0.0025 | 0.009 | 0.00 | - |
| recent_base_rate_7d|h4|all | 3420 | 57 | 3420 | 0.474 | 0.46-0.49 | 0.526 | 0.451 | -0.0387 | 0.075 | 0.61 | -68.7 |
| recent_base_rate_7d|h4|on_time | 3420 | 57 | 3420 | 0.474 | 0.46-0.49 | 0.526 | 0.451 | -0.0387 | 0.075 | 0.61 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 931.12 | -6.89% | 1711 | 686 | 56 |
| analog_k100|h4 | 989.99 | -1.00% | 2070 | 932 | 53 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 61 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 58 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 56 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 53 |
| derivatives|h1 | 1116.26 | +11.63% | 26 | 11 | 56 |
| derivatives|h4 | 1210.96 | +21.10% | 56 | 36 | 53 |
| lgbm_calibrated|h1 | 907.89 | -9.21% | 530 | 247 | 61 |
| lgbm_calibrated|h4 | 916.34 | -8.37% | 523 | 218 | 58 |
| logistic|h1 | 806.68 | -19.33% | 458 | 193 | 61 |
| logistic|h4 | 991.68 | -0.83% | 840 | 385 | 58 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 61 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 58 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 61 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 58 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 60 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 57 |
| benchmark_long_all_coins|h1 | 968.24 | -3.18% | 3660 | 1601 | 61 |
| benchmark_long_all_coins|h4 | 1010.53 | +1.05% | 3480 | 1732 | 58 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 61 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 58 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 61 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 58 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 61 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 58 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 61 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 58 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 61 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 58 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 60 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 57 |

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
