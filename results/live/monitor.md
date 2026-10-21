# Live monitor (2026-10-21T15:06:54.232650+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.58 (ECE 0.132)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.469
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.492
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.491
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.58 (ECE 0.119)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.440
- MISCALIBRATED: logistic|h4|all says 0.50 on average, reality 0.58 (ECE 0.082)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.494
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.58 (ECE 0.142)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.434

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['DASH', 'HBAR']
- **last_closed_bar**: 2026-10-21 14:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.8
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 104.6 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.132, 'recent_base_rate_7d': 0.089, 'momentum_24': 0.144, 'logistic': 0.192, 'lgbm_calibrated': 0.14, 'analog_k100': 0.031, 'derivatives': 0.135, 'orthosys': 0.136}
- **council_member_logloss_h1**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.6963, 'momentum_24': 0.6927, 'logistic': 0.6906, 'lgbm_calibrated': 0.6929, 'analog_k100': 0.7052, 'derivatives': 0.6934, 'orthosys': 0.6931}
- **council_calls_h1**: 35
- **council_abstain_h1**: {'spoke': 35, 'no_edge': 20, 'extreme_volatility': 5}
- **council_weights_h4**: {'base_rate': 0.204, 'recent_base_rate_7d': 0.006, 'momentum_24': 0.203, 'logistic': 0.175, 'lgbm_calibrated': 0.035, 'analog_k100': 0.002, 'derivatives': 0.197, 'orthosys': 0.178}
- **council_member_logloss_h4**: {'base_rate': 0.6924, 'recent_base_rate_7d': 0.7203, 'momentum_24': 0.6924, 'logistic': 0.6936, 'lgbm_calibrated': 0.7061, 'analog_k100': 0.7321, 'derivatives': 0.6925, 'orthosys': 0.6935}
- **council_calls_h4**: 2
- **council_abstain_h4**: {'no_edge': 48, 'extreme_volatility': 5, 'members_disagree': 5, 'spoke': 2}
- **prediction_latency_min**: 6.8
- **price_snapshot_age_s**: 0.8
- **train_rows_h1**: 91978
- **orthosys_hist_hit_h1**: 0.5305
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0068
- **p_spread_logistic_h1**: 0.0353
- **p_spread_lgbm_calibrated_h1**: 0.0129
- **p_spread_analog_k100_h1**: 0.0577
- **p_spread_derivatives_h1**: 0.0061
- **p_spread_orthosys_h1**: 0.0069
- **p_spread_council_h1**: 0.0128
- **train_rows_h4**: 91792
- **orthosys_hist_hit_h4**: 0.5119
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0006
- **p_spread_logistic_h4**: 0.0831
- **p_spread_lgbm_calibrated_h4**: 0.0574
- **p_spread_analog_k100_h4**: 0.1027
- **p_spread_derivatives_h4**: 0.0388
- **p_spread_orthosys_h4**: 0.0027
- **p_spread_council_h4**: 0.0042
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 49920

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 2520 | 42 | 2520 | 0.500 | 0.48-0.52 | 0.529 | 0.465 | -0.0259 | 0.068 | 0.52 | -12.2 |
| analog_k100|h1|on_time | 2520 | 42 | 2520 | 0.500 | 0.48-0.52 | 0.529 | 0.465 | -0.0259 | 0.068 | 0.52 | -12.2 |
| analog_k100|h4|all | 2340 | 39 | 2340 | 0.449 | 0.43-0.47 | 0.577 | 0.451 | -0.0795 | 0.132 | 0.63 | -26.7 |
| analog_k100|h4|on_time | 2340 | 39 | 2340 | 0.449 | 0.43-0.47 | 0.577 | 0.451 | -0.0795 | 0.132 | 0.63 | -26.7 |
| base_rate|h1|all | 2820 | 47 | 2820 | 0.473 | 0.45-0.49 | 0.527 | 0.498 | +0.0000 | 0.029 | 0.00 | - |
| base_rate|h1|on_time | 2760 | 46 | 2760 | 0.476 | 0.46-0.49 | 0.524 | 0.498 | +0.0000 | 0.026 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 2640 | 44 | 2640 | 0.578 | 0.56-0.60 | 0.578 | 0.503 | +0.0000 | 0.075 | 0.00 | - |
| base_rate|h4|on_time | 2640 | 44 | 2640 | 0.578 | 0.56-0.60 | 0.578 | 0.503 | +0.0000 | 0.075 | 0.00 | - |
| council|h1|all | 2520 | 42 | 434 | 0.539 | 0.49-0.59 | 0.529 | 0.495 | +0.0019 | 0.039 | 0.00 | +18.3 |
| council|h1|on_time | 2520 | 42 | 434 | 0.539 | 0.49-0.59 | 0.529 | 0.495 | +0.0019 | 0.039 | 0.00 | +18.3 |
| council|h4|all | 2340 | 39 | 21 | 0.571 | 0.37-0.76 | 0.577 | 0.500 | -0.0016 | 0.078 | 0.00 | - |
| council|h4|on_time | 2340 | 39 | 21 | 0.571 | 0.37-0.76 | 0.577 | 0.500 | -0.0016 | 0.078 | 0.00 | - |
| derivatives|h1|all | 2520 | 42 | 2520 | 0.471 | 0.45-0.49 | 0.529 | 0.498 | +0.0002 | 0.032 | 0.00 | -11.5 |
| derivatives|h1|on_time | 2520 | 42 | 2520 | 0.471 | 0.45-0.49 | 0.529 | 0.498 | +0.0002 | 0.032 | 0.00 | -11.5 |
| derivatives|h4|all | 2340 | 39 | 2340 | 0.577 | 0.56-0.60 | 0.577 | 0.502 | -0.0006 | 0.075 | 0.01 | -199.6 |
| derivatives|h4|on_time | 2340 | 39 | 2340 | 0.577 | 0.56-0.60 | 0.577 | 0.502 | -0.0006 | 0.075 | 0.01 | -199.6 |
| lgbm_calibrated|h1|all | 2820 | 47 | 2820 | 0.530 | 0.51-0.55 | 0.527 | 0.473 | -0.0017 | 0.054 | 0.15 | +2.0 |
| lgbm_calibrated|h1|on_time | 2760 | 46 | 2760 | 0.534 | 0.52-0.55 | 0.524 | 0.474 | -0.0009 | 0.051 | 0.15 | +2.0 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 2640 | 44 | 2640 | 0.421 | 0.40-0.44 | 0.578 | 0.461 | -0.0285 | 0.119 | 0.19 | -50.2 |
| lgbm_calibrated|h4|on_time | 2640 | 44 | 2640 | 0.421 | 0.40-0.44 | 0.578 | 0.461 | -0.0285 | 0.119 | 0.19 | -50.2 |
| logistic|h1|all | 2820 | 47 | 2820 | 0.529 | 0.51-0.55 | 0.527 | 0.490 | +0.0046 | 0.038 | 0.09 | -29.7 |
| logistic|h1|on_time | 2760 | 46 | 2760 | 0.524 | 0.50-0.54 | 0.524 | 0.489 | +0.0035 | 0.036 | 0.10 | -29.8 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 2640 | 44 | 2640 | 0.522 | 0.50-0.54 | 0.578 | 0.496 | -0.0037 | 0.082 | 0.20 | -43.5 |
| logistic|h4|on_time | 2640 | 44 | 2640 | 0.522 | 0.50-0.54 | 0.578 | 0.496 | -0.0037 | 0.082 | 0.20 | -43.5 |
| momentum_24|h1|all | 2820 | 47 | 2820 | 0.520 | 0.50-0.54 | 0.527 | 0.496 | +0.0013 | 0.031 | 0.00 | - |
| momentum_24|h1|on_time | 2760 | 46 | 2760 | 0.516 | 0.50-0.53 | 0.524 | 0.496 | +0.0010 | 0.029 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 2640 | 44 | 2640 | 0.578 | 0.56-0.60 | 0.578 | 0.503 | -0.0000 | 0.075 | 0.00 | - |
| momentum_24|h4|on_time | 2640 | 44 | 2640 | 0.578 | 0.56-0.60 | 0.578 | 0.503 | -0.0000 | 0.075 | 0.00 | - |
| orthosys|h1|all | 2820 | 47 | 203 | 0.527 | 0.46-0.59 | 0.527 | 0.499 | +0.0007 | 0.029 | 0.00 | - |
| orthosys|h1|on_time | 2760 | 46 | 202 | 0.525 | 0.46-0.59 | 0.524 | 0.499 | +0.0006 | 0.026 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 2640 | 44 | 193 | 0.430 | 0.36-0.50 | 0.578 | 0.499 | -0.0023 | 0.079 | 0.00 | - |
| orthosys|h4|on_time | 2640 | 44 | 193 | 0.430 | 0.36-0.50 | 0.578 | 0.499 | -0.0023 | 0.079 | 0.00 | - |
| recent_base_rate_7d|h1|all | 2760 | 46 | 2760 | 0.476 | 0.46-0.49 | 0.524 | 0.474 | -0.0070 | 0.050 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 2760 | 46 | 2760 | 0.476 | 0.46-0.49 | 0.524 | 0.474 | -0.0070 | 0.050 | 0.00 | - |
| recent_base_rate_7d|h4|all | 2580 | 43 | 2580 | 0.415 | 0.40-0.43 | 0.585 | 0.443 | -0.0575 | 0.142 | 0.81 | -68.7 |
| recent_base_rate_7d|h4|on_time | 2580 | 43 | 2580 | 0.415 | 0.40-0.43 | 0.585 | 0.443 | -0.0575 | 0.142 | 0.81 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 954.75 | -4.53% | 1306 | 518 | 42 |
| analog_k100|h4 | 979.98 | -2.00% | 1472 | 578 | 39 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 47 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 44 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 42 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 39 |
| derivatives|h1 | 975.90 | -2.41% | 6 | 3 | 42 |
| derivatives|h4 | 967.75 | -3.22% | 13 | 4 | 39 |
| lgbm_calibrated|h1 | 936.90 | -6.31% | 416 | 198 | 47 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 44 |
| logistic|h1 | 833.24 | -16.68% | 266 | 141 | 47 |
| logistic|h4 | 980.87 | -1.91% | 525 | 254 | 44 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 47 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 44 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 47 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 44 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 46 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 43 |
| benchmark_long_all_coins|h1 | 1023.28 | +2.33% | 2820 | 1331 | 47 |
| benchmark_long_all_coins|h4 | 1051.65 | +5.17% | 2640 | 1452 | 44 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 43 |

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
