# Live monitor (2026-10-22T02:05:56.727208+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h4|all says 0.44 on average, reality 0.54 (ECE 0.112)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.487
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.55 (ECE 0.087)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.469
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.485
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.45 on average, reality 0.55 (ECE 0.103)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.465

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['DASH', 'HBAR']
- **last_closed_bar**: 2026-10-22 01:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.0
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 103.1 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.034
- **council_weights_h1**: {'base_rate': 0.141, 'recent_base_rate_7d': 0.095, 'momentum_24': 0.162, 'logistic': 0.158, 'lgbm_calibrated': 0.131, 'analog_k100': 0.018, 'derivatives': 0.15, 'orthosys': 0.144}
- **council_member_logloss_h1**: {'base_rate': 0.6933, 'recent_base_rate_7d': 0.6957, 'momentum_24': 0.6925, 'logistic': 0.6926, 'lgbm_calibrated': 0.6937, 'analog_k100': 0.7067, 'derivatives': 0.6931, 'orthosys': 0.6932}
- **council_calls_h1**: 3
- **council_abstain_h1**: {'no_edge': 49, 'extreme_volatility': 7, 'spoke': 3, 'missing_inputs': 1}
- **council_weights_h4**: {'base_rate': 0.219, 'recent_base_rate_7d': 0.005, 'momentum_24': 0.217, 'logistic': 0.089, 'lgbm_calibrated': 0.036, 'analog_k100': 0.001, 'derivatives': 0.24, 'orthosys': 0.193}
- **council_member_logloss_h4**: {'base_rate': 0.6927, 'recent_base_rate_7d': 0.717, 'momentum_24': 0.6928, 'logistic': 0.6983, 'lgbm_calibrated': 0.7038, 'analog_k100': 0.7287, 'derivatives': 0.6919, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 51, 'extreme_volatility': 7, 'missing_inputs': 1, 'members_disagree': 1}
- **prediction_latency_min**: 5.8
- **price_snapshot_age_s**: 0.3
- **train_rows_h1**: 91087
- **orthosys_hist_hit_h1**: 0.5298
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.008
- **p_spread_logistic_h1**: 0.0497
- **p_spread_lgbm_calibrated_h1**: 0.0194
- **p_spread_analog_k100_h1**: 0.0897
- **p_spread_derivatives_h1**: 0.028
- **p_spread_orthosys_h1**: 0.0102
- **p_spread_council_h1**: 0.0052
- **train_rows_h4**: 90901
- **orthosys_hist_hit_h4**: 0.5099
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0006
- **p_spread_logistic_h4**: 0.08
- **p_spread_lgbm_calibrated_h4**: 0.004
- **p_spread_analog_k100_h4**: 0.106
- **p_spread_derivatives_h4**: 0.0579
- **p_spread_orthosys_h4**: 0.0034
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 61800

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 3180 | 53 | 3180 | 0.498 | 0.48-0.52 | 0.500 | 0.466 | -0.0227 | 0.058 | 0.51 | -12.6 |
| analog_k100|h1|on_time | 3180 | 53 | 3180 | 0.498 | 0.48-0.52 | 0.500 | 0.466 | -0.0227 | 0.058 | 0.51 | -12.6 |
| analog_k100|h4|all | 3000 | 50 | 3000 | 0.469 | 0.45-0.49 | 0.543 | 0.444 | -0.0606 | 0.112 | 0.65 | -19.0 |
| analog_k100|h4|on_time | 3000 | 50 | 3000 | 0.469 | 0.45-0.49 | 0.543 | 0.444 | -0.0606 | 0.112 | 0.65 | -19.0 |
| base_rate|h1|all | 3480 | 58 | 3480 | 0.499 | 0.48-0.52 | 0.501 | 0.498 | +0.0000 | 0.003 | 0.00 | - |
| base_rate|h1|on_time | 3420 | 57 | 3420 | 0.502 | 0.49-0.52 | 0.498 | 0.498 | +0.0000 | 0.000 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 3300 | 55 | 3300 | 0.548 | 0.53-0.56 | 0.548 | 0.504 | +0.0000 | 0.044 | 0.00 | - |
| base_rate|h4|on_time | 3300 | 55 | 3300 | 0.548 | 0.53-0.56 | 0.548 | 0.504 | +0.0000 | 0.044 | 0.00 | - |
| council|h1|all | 3180 | 53 | 489 | 0.513 | 0.47-0.56 | 0.500 | 0.496 | +0.0003 | 0.004 | 0.00 | +18.3 |
| council|h1|on_time | 3180 | 53 | 489 | 0.513 | 0.47-0.56 | 0.500 | 0.496 | +0.0003 | 0.004 | 0.00 | +18.3 |
| council|h4|all | 3000 | 50 | 25 | 0.600 | 0.41-0.77 | 0.543 | 0.500 | -0.0003 | 0.044 | 0.00 | - |
| council|h4|on_time | 3000 | 50 | 25 | 0.600 | 0.41-0.77 | 0.543 | 0.500 | -0.0003 | 0.044 | 0.00 | - |
| derivatives|h1|all | 3180 | 53 | 3180 | 0.500 | 0.48-0.52 | 0.500 | 0.497 | +0.0000 | 0.003 | 0.01 | -60.3 |
| derivatives|h1|on_time | 3180 | 53 | 3180 | 0.500 | 0.48-0.52 | 0.500 | 0.497 | +0.0000 | 0.003 | 0.01 | -60.3 |
| derivatives|h4|all | 3000 | 50 | 3000 | 0.553 | 0.54-0.57 | 0.543 | 0.501 | +0.0022 | 0.048 | 0.02 | +543.5 |
| derivatives|h4|on_time | 3000 | 50 | 3000 | 0.553 | 0.54-0.57 | 0.543 | 0.501 | +0.0022 | 0.048 | 0.02 | +543.5 |
| lgbm_calibrated|h1|all | 3480 | 58 | 3479 | 0.545 | 0.53-0.56 | 0.501 | 0.474 | -0.0003 | 0.026 | 0.15 | -2.5 |
| lgbm_calibrated|h1|on_time | 3420 | 57 | 3419 | 0.548 | 0.53-0.56 | 0.498 | 0.475 | +0.0003 | 0.024 | 0.15 | -2.5 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 3300 | 55 | 3300 | 0.452 | 0.44-0.47 | 0.548 | 0.463 | -0.0190 | 0.087 | 0.16 | -48.0 |
| lgbm_calibrated|h4|on_time | 3300 | 55 | 3300 | 0.452 | 0.44-0.47 | 0.548 | 0.463 | -0.0190 | 0.087 | 0.16 | -48.0 |
| logistic|h1|all | 3480 | 58 | 3480 | 0.522 | 0.51-0.54 | 0.501 | 0.490 | +0.0007 | 0.012 | 0.11 | -27.5 |
| logistic|h1|on_time | 3420 | 57 | 3420 | 0.517 | 0.50-0.53 | 0.498 | 0.490 | -0.0003 | 0.010 | 0.11 | -27.6 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 3300 | 55 | 3300 | 0.509 | 0.49-0.53 | 0.548 | 0.493 | -0.0103 | 0.062 | 0.23 | -16.4 |
| logistic|h4|on_time | 3300 | 55 | 3300 | 0.509 | 0.49-0.53 | 0.548 | 0.493 | -0.0103 | 0.062 | 0.23 | -16.4 |
| momentum_24|h1|all | 3480 | 58 | 3480 | 0.526 | 0.51-0.54 | 0.501 | 0.496 | +0.0016 | 0.016 | 0.00 | - |
| momentum_24|h1|on_time | 3420 | 57 | 3420 | 0.523 | 0.51-0.54 | 0.498 | 0.495 | +0.0014 | 0.013 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 3300 | 55 | 3300 | 0.548 | 0.53-0.56 | 0.548 | 0.504 | -0.0002 | 0.044 | 0.00 | - |
| momentum_24|h4|on_time | 3300 | 55 | 3300 | 0.548 | 0.53-0.56 | 0.548 | 0.504 | -0.0002 | 0.044 | 0.00 | - |
| orthosys|h1|all | 3480 | 58 | 250 | 0.512 | 0.45-0.57 | 0.501 | 0.499 | -0.0001 | 0.005 | 0.00 | - |
| orthosys|h1|on_time | 3420 | 57 | 249 | 0.510 | 0.45-0.57 | 0.498 | 0.499 | -0.0002 | 0.002 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 3300 | 55 | 235 | 0.421 | 0.36-0.49 | 0.548 | 0.499 | -0.0012 | 0.048 | 0.00 | - |
| orthosys|h4|on_time | 3300 | 55 | 235 | 0.421 | 0.36-0.49 | 0.548 | 0.499 | -0.0012 | 0.048 | 0.00 | - |
| recent_base_rate_7d|h1|all | 3420 | 57 | 3420 | 0.502 | 0.49-0.52 | 0.498 | 0.477 | -0.0040 | 0.021 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 3420 | 57 | 3420 | 0.502 | 0.49-0.52 | 0.498 | 0.477 | -0.0040 | 0.021 | 0.00 | - |
| recent_base_rate_7d|h4|all | 3240 | 54 | 3240 | 0.448 | 0.43-0.47 | 0.552 | 0.449 | -0.0461 | 0.103 | 0.65 | -68.7 |
| recent_base_rate_7d|h4|on_time | 3240 | 54 | 3240 | 0.448 | 0.43-0.47 | 0.552 | 0.449 | -0.0461 | 0.103 | 0.65 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 938.18 | -6.18% | 1614 | 662 | 53 |
| analog_k100|h4 | 981.10 | -1.89% | 1941 | 827 | 50 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 58 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 55 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 53 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 50 |
| derivatives|h1 | 1040.09 | +4.01% | 23 | 8 | 53 |
| derivatives|h4 | 1188.01 | +18.80% | 47 | 28 | 50 |
| lgbm_calibrated|h1 | 907.89 | -9.21% | 530 | 247 | 58 |
| lgbm_calibrated|h4 | 916.34 | -8.37% | 523 | 218 | 55 |
| logistic|h1 | 817.73 | -18.23% | 378 | 182 | 58 |
| logistic|h4 | 998.12 | -0.19% | 772 | 361 | 55 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 58 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 55 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 58 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 55 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 57 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 54 |
| benchmark_long_all_coins|h1 | 985.00 | -1.50% | 3480 | 1573 | 58 |
| benchmark_long_all_coins|h4 | 1029.71 | +2.97% | 3300 | 1723 | 55 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 58 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 58 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 58 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 58 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 58 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 57 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 54 |

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
