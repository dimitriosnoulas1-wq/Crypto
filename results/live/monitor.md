# Live monitor (2026-10-21T22:06:08.213606+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.58 (ECE 0.140)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.466
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.496
- MISCALIBRATED: council|h4|all says 0.50 on average, reality 0.58 (ECE 0.081)
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.495
- MISCALIBRATED: derivatives|h4|all says 0.50 on average, reality 0.58 (ECE 0.080)
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.58 (ECE 0.121)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.436
- MISCALIBRATED: logistic|h4|all says 0.49 on average, reality 0.58 (ECE 0.094)
- MISCALIBRATED: orthosys|h4|all says 0.50 on average, reality 0.58 (ECE 0.082)
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.491
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.499
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.45 on average, reality 0.59 (ECE 0.140)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.431

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['COMP', 'RAY']
- **last_closed_bar**: 2026-10-21 21:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.1
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 103.6 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.146, 'recent_base_rate_7d': 0.091, 'momentum_24': 0.159, 'logistic': 0.17, 'lgbm_calibrated': 0.118, 'analog_k100': 0.016, 'derivatives': 0.148, 'orthosys': 0.153}
- **council_member_logloss_h1**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.6965, 'momentum_24': 0.6928, 'logistic': 0.6924, 'lgbm_calibrated': 0.6947, 'analog_k100': 0.7091, 'derivatives': 0.6935, 'orthosys': 0.6931}
- **council_calls_h1**: 3
- **council_abstain_h1**: {'no_edge': 51, 'extreme_volatility': 6, 'spoke': 3}
- **council_weights_h4**: {'base_rate': 0.23, 'recent_base_rate_7d': 0.004, 'momentum_24': 0.23, 'logistic': 0.093, 'lgbm_calibrated': 0.024, 'analog_k100': 0.001, 'derivatives': 0.231, 'orthosys': 0.188}
- **council_member_logloss_h4**: {'base_rate': 0.6921, 'recent_base_rate_7d': 0.7205, 'momentum_24': 0.6921, 'logistic': 0.6982, 'lgbm_calibrated': 0.7072, 'analog_k100': 0.7366, 'derivatives': 0.6918, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 54, 'extreme_volatility': 6}
- **prediction_latency_min**: 6.0
- **price_snapshot_age_s**: 0.7
- **train_rows_h1**: 92414
- **orthosys_hist_hit_h1**: 0.5309
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.008
- **p_spread_logistic_h1**: 0.0316
- **p_spread_lgbm_calibrated_h1**: 0.0099
- **p_spread_analog_k100_h1**: 0.0517
- **p_spread_derivatives_h1**: 0.0149
- **p_spread_orthosys_h1**: 0.0069
- **p_spread_council_h1**: 0.0053
- **train_rows_h4**: 92228
- **orthosys_hist_hit_h4**: 0.5117
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0005
- **p_spread_logistic_h4**: 0.0662
- **p_spread_lgbm_calibrated_h4**: 0.0062
- **p_spread_analog_k100_h4**: 0.0696
- **p_spread_derivatives_h4**: 0.0488
- **p_spread_orthosys_h4**: 0.0026
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 57480

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 2940 | 49 | 2940 | 0.490 | 0.47-0.51 | 0.522 | 0.466 | -0.0301 | 0.067 | 0.51 | -16.2 |
| analog_k100|h1|on_time | 2940 | 49 | 2940 | 0.490 | 0.47-0.51 | 0.522 | 0.466 | -0.0301 | 0.067 | 0.51 | -16.2 |
| analog_k100|h4|all | 2760 | 46 | 2760 | 0.447 | 0.43-0.47 | 0.580 | 0.446 | -0.0830 | 0.140 | 0.64 | -31.9 |
| analog_k100|h4|on_time | 2760 | 46 | 2760 | 0.447 | 0.43-0.47 | 0.580 | 0.446 | -0.0830 | 0.140 | 0.64 | -31.9 |
| base_rate|h1|all | 3240 | 54 | 3240 | 0.479 | 0.46-0.50 | 0.521 | 0.498 | +0.0000 | 0.023 | 0.00 | - |
| base_rate|h1|on_time | 3180 | 53 | 3180 | 0.481 | 0.46-0.50 | 0.519 | 0.498 | +0.0000 | 0.021 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 3060 | 51 | 3060 | 0.581 | 0.56-0.60 | 0.581 | 0.504 | +0.0000 | 0.077 | 0.00 | - |
| base_rate|h4|on_time | 3060 | 51 | 3060 | 0.581 | 0.56-0.60 | 0.581 | 0.504 | +0.0000 | 0.077 | 0.00 | - |
| council|h1|all | 2940 | 49 | 483 | 0.507 | 0.46-0.55 | 0.522 | 0.496 | +0.0007 | 0.027 | 0.00 | +18.3 |
| council|h1|on_time | 2940 | 49 | 483 | 0.507 | 0.46-0.55 | 0.522 | 0.496 | +0.0007 | 0.027 | 0.00 | +18.3 |
| council|h4|all | 2760 | 46 | 25 | 0.600 | 0.41-0.77 | 0.580 | 0.500 | -0.0018 | 0.081 | 0.00 | - |
| council|h4|on_time | 2760 | 46 | 25 | 0.600 | 0.41-0.77 | 0.580 | 0.500 | -0.0018 | 0.081 | 0.00 | - |
| derivatives|h1|all | 2940 | 49 | 2940 | 0.477 | 0.46-0.50 | 0.522 | 0.497 | -0.0003 | 0.026 | 0.01 | -262.5 |
| derivatives|h1|on_time | 2940 | 49 | 2940 | 0.477 | 0.46-0.50 | 0.522 | 0.497 | -0.0003 | 0.026 | 0.01 | -262.5 |
| derivatives|h4|all | 2760 | 46 | 2760 | 0.584 | 0.57-0.60 | 0.580 | 0.501 | -0.0002 | 0.080 | 0.01 | +267.0 |
| derivatives|h4|on_time | 2760 | 46 | 2760 | 0.584 | 0.57-0.60 | 0.580 | 0.501 | -0.0002 | 0.080 | 0.01 | +267.0 |
| lgbm_calibrated|h1|all | 3240 | 54 | 3239 | 0.527 | 0.51-0.54 | 0.521 | 0.473 | -0.0029 | 0.048 | 0.16 | -0.0 |
| lgbm_calibrated|h1|on_time | 3180 | 53 | 3179 | 0.530 | 0.51-0.55 | 0.519 | 0.473 | -0.0022 | 0.045 | 0.16 | -0.0 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 3060 | 51 | 3060 | 0.419 | 0.40-0.44 | 0.581 | 0.462 | -0.0291 | 0.121 | 0.17 | -48.0 |
| lgbm_calibrated|h4|on_time | 3060 | 51 | 3060 | 0.419 | 0.40-0.44 | 0.581 | 0.462 | -0.0291 | 0.121 | 0.17 | -48.0 |
| logistic|h1|all | 3240 | 54 | 3240 | 0.523 | 0.51-0.54 | 0.521 | 0.490 | +0.0015 | 0.033 | 0.10 | -36.8 |
| logistic|h1|on_time | 3180 | 53 | 3180 | 0.519 | 0.50-0.54 | 0.519 | 0.489 | +0.0004 | 0.031 | 0.10 | -36.9 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 3060 | 51 | 3060 | 0.511 | 0.49-0.53 | 0.581 | 0.493 | -0.0121 | 0.094 | 0.23 | -36.5 |
| logistic|h4|on_time | 3060 | 51 | 3060 | 0.511 | 0.49-0.53 | 0.581 | 0.493 | -0.0121 | 0.094 | 0.23 | -36.5 |
| momentum_24|h1|all | 3240 | 54 | 3240 | 0.518 | 0.50-0.54 | 0.521 | 0.496 | +0.0011 | 0.025 | 0.00 | - |
| momentum_24|h1|on_time | 3180 | 53 | 3180 | 0.515 | 0.50-0.53 | 0.519 | 0.495 | +0.0009 | 0.023 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 3060 | 51 | 3060 | 0.581 | 0.56-0.60 | 0.581 | 0.504 | -0.0000 | 0.077 | 0.00 | - |
| momentum_24|h4|on_time | 3060 | 51 | 3060 | 0.581 | 0.56-0.60 | 0.581 | 0.504 | -0.0000 | 0.077 | 0.00 | - |
| orthosys|h1|all | 3240 | 54 | 232 | 0.526 | 0.46-0.59 | 0.521 | 0.499 | +0.0006 | 0.025 | 0.00 | - |
| orthosys|h1|on_time | 3180 | 53 | 231 | 0.524 | 0.46-0.59 | 0.519 | 0.499 | +0.0005 | 0.022 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 3060 | 51 | 221 | 0.425 | 0.36-0.49 | 0.581 | 0.499 | -0.0026 | 0.082 | 0.00 | - |
| orthosys|h4|on_time | 3060 | 51 | 221 | 0.425 | 0.36-0.49 | 0.581 | 0.499 | -0.0026 | 0.082 | 0.00 | - |
| recent_base_rate_7d|h1|all | 3180 | 53 | 3180 | 0.481 | 0.46-0.50 | 0.519 | 0.476 | -0.0061 | 0.043 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 3180 | 53 | 3180 | 0.481 | 0.46-0.50 | 0.519 | 0.476 | -0.0061 | 0.043 | 0.00 | - |
| recent_base_rate_7d|h4|all | 3000 | 50 | 3000 | 0.413 | 0.40-0.43 | 0.587 | 0.447 | -0.0552 | 0.140 | 0.70 | -68.7 |
| recent_base_rate_7d|h4|on_time | 3000 | 50 | 3000 | 0.413 | 0.40-0.43 | 0.587 | 0.447 | -0.0552 | 0.140 | 0.70 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 926.52 | -7.35% | 1488 | 575 | 49 |
| analog_k100|h4 | 969.50 | -3.05% | 1772 | 695 | 46 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 54 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 51 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 49 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 46 |
| derivatives|h1 | 805.33 | -19.47% | 18 | 4 | 49 |
| derivatives|h4 | 1059.26 | +5.93% | 32 | 14 | 46 |
| lgbm_calibrated|h1 | 924.76 | -7.52% | 521 | 244 | 54 |
| lgbm_calibrated|h4 | 916.34 | -8.37% | 523 | 218 | 51 |
| logistic|h1 | 802.13 | -19.79% | 334 | 164 | 54 |
| logistic|h4 | 979.70 | -2.03% | 704 | 327 | 51 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 54 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 51 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 54 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 51 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 53 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 50 |
| benchmark_long_all_coins|h1 | 1016.59 | +1.66% | 3240 | 1536 | 54 |
| benchmark_long_all_coins|h4 | 1052.52 | +5.25% | 3060 | 1693 | 51 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 50 |

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
