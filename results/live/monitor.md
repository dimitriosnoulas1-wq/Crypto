# Live monitor (2026-10-20T13:07:50.695604+00:00)

## Alerts

- none

## Health

- **venue**: okx
- **symbols**: 61
- **universe_size**: 60
- **fetched_only_for_scoring**: ['RAY']
- **last_closed_bar**: 2026-10-20 12:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.7
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 106.9 instruments 61/61']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.12, 'recent_base_rate_7d': 0.125, 'momentum_24': 0.133, 'logistic': 0.128, 'lgbm_calibrated': 0.136, 'analog_k100': 0.114, 'derivatives': 0.123, 'orthosys': 0.12}
- **council_member_logloss_h1**: {'base_rate': 0.6932, 'recent_base_rate_7d': 0.6926, 'momentum_24': 0.6915, 'logistic': 0.6922, 'lgbm_calibrated': 0.6912, 'analog_k100': 0.695, 'derivatives': 0.6933, 'orthosys': 0.6933}
- **council_calls_h1**: 12
- **council_abstain_h1**: {'no_edge': 43, 'spoke': 12, 'extreme_volatility': 5}
- **council_weights_h4**: {'base_rate': 0.121, 'recent_base_rate_7d': 0.094, 'momentum_24': 0.121, 'logistic': 0.117, 'lgbm_calibrated': 0.14, 'analog_k100': 0.163, 'derivatives': 0.118, 'orthosys': 0.127}
- **council_member_logloss_h4**: {'base_rate': 0.6938, 'recent_base_rate_7d': 0.6988, 'momentum_24': 0.6937, 'logistic': 0.6944, 'lgbm_calibrated': 0.6908, 'analog_k100': 0.6851, 'derivatives': 0.6941, 'orthosys': 0.6928}
- **council_calls_h4**: 2
- **council_abstain_h4**: {'members_disagree': 31, 'no_edge': 22, 'extreme_volatility': 5, 'spoke': 2}
- **prediction_latency_min**: 7.7
- **price_snapshot_age_s**: 1.0
- **train_rows_h1**: 88998
- **orthosys_hist_hit_h1**: 0.5271
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0103
- **p_spread_logistic_h1**: 0.0176
- **p_spread_lgbm_calibrated_h1**: 0.0236
- **p_spread_analog_k100_h1**: 0.062
- **p_spread_derivatives_h1**: 0.0015
- **p_spread_orthosys_h1**: 0.007
- **p_spread_council_h1**: 0.0099
- **train_rows_h4**: 88815
- **orthosys_hist_hit_h4**: 0.5187
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0013
- **p_spread_logistic_h4**: 0.0335
- **p_spread_lgbm_calibrated_h4**: 0.0037
- **p_spread_analog_k100_h4**: 0.0785
- **p_spread_derivatives_h4**: 0.0075
- **p_spread_orthosys_h4**: 0.0048
- **p_spread_council_h4**: 0.0047
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 21840

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 960 | 16 | 960 | 0.503 | 0.47-0.53 | 0.505 | 0.477 | -0.0155 | 0.048 | 0.46 | -13.2 |
| analog_k100|h1|on_time | 960 | 16 | 960 | 0.503 | 0.47-0.53 | 0.505 | 0.477 | -0.0155 | 0.048 | 0.46 | -13.2 |
| analog_k100|h4|all | 780 | 13 | 780 | 0.532 | 0.50-0.57 | 0.433 | 0.454 | +0.0006 | 0.042 | 0.60 | -12.8 |
| analog_k100|h4|on_time | 780 | 13 | 780 | 0.532 | 0.50-0.57 | 0.433 | 0.454 | +0.0006 | 0.042 | 0.60 | -12.8 |
| base_rate|h1|all | 1260 | 21 | 1260 | 0.494 | 0.47-0.52 | 0.506 | 0.498 | +0.0000 | 0.007 | 0.00 | - |
| base_rate|h1|on_time | 1200 | 20 | 1200 | 0.502 | 0.47-0.53 | 0.498 | 0.498 | +0.0000 | 0.000 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 1080 | 18 | 1080 | 0.477 | 0.45-0.51 | 0.477 | 0.503 | +0.0000 | 0.026 | 0.00 | - |
| base_rate|h4|on_time | 1080 | 18 | 1080 | 0.477 | 0.45-0.51 | 0.477 | 0.503 | +0.0000 | 0.026 | 0.00 | - |
| council|h1|all | 960 | 16 | 106 | 0.547 | 0.45-0.64 | 0.505 | 0.497 | +0.0009 | 0.013 | 0.00 | - |
| council|h1|on_time | 960 | 16 | 106 | 0.547 | 0.45-0.64 | 0.505 | 0.497 | +0.0009 | 0.013 | 0.00 | - |
| council|h4|all | 780 | 13 | 12 | 0.750 | 0.47-0.91 | 0.433 | 0.500 | +0.0027 | 0.066 | 0.00 | - |
| council|h4|on_time | 780 | 13 | 12 | 0.750 | 0.47-0.91 | 0.433 | 0.500 | +0.0027 | 0.066 | 0.00 | - |
| derivatives|h1|all | 960 | 16 | 960 | 0.489 | 0.46-0.52 | 0.505 | 0.498 | -0.0002 | 0.013 | 0.00 | - |
| derivatives|h1|on_time | 960 | 16 | 960 | 0.489 | 0.46-0.52 | 0.505 | 0.498 | -0.0002 | 0.013 | 0.00 | - |
| derivatives|h4|all | 780 | 13 | 780 | 0.455 | 0.42-0.49 | 0.433 | 0.502 | +0.0007 | 0.069 | 0.00 | -45.1 |
| derivatives|h4|on_time | 780 | 13 | 780 | 0.455 | 0.42-0.49 | 0.433 | 0.502 | +0.0007 | 0.069 | 0.00 | -45.1 |
| lgbm_calibrated|h1|all | 1260 | 21 | 1260 | 0.563 | 0.54-0.59 | 0.506 | 0.481 | +0.0062 | 0.041 | 0.07 | -33.2 |
| lgbm_calibrated|h1|on_time | 1200 | 20 | 1200 | 0.573 | 0.55-0.60 | 0.498 | 0.482 | +0.0084 | 0.053 | 0.07 | -33.2 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 1080 | 18 | 1080 | 0.521 | 0.49-0.55 | 0.477 | 0.462 | +0.0026 | 0.017 | 0.18 | -0.9 |
| lgbm_calibrated|h4|on_time | 1080 | 18 | 1080 | 0.521 | 0.49-0.55 | 0.477 | 0.462 | +0.0026 | 0.017 | 0.18 | -0.9 |
| logistic|h1|all | 1260 | 21 | 1260 | 0.539 | 0.51-0.57 | 0.506 | 0.493 | +0.0037 | 0.022 | 0.05 | -25.4 |
| logistic|h1|on_time | 1200 | 20 | 1200 | 0.527 | 0.50-0.55 | 0.498 | 0.492 | +0.0009 | 0.011 | 0.06 | -25.5 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 1080 | 18 | 1080 | 0.508 | 0.48-0.54 | 0.477 | 0.494 | +0.0009 | 0.022 | 0.14 | +43.6 |
| logistic|h4|on_time | 1080 | 18 | 1080 | 0.508 | 0.48-0.54 | 0.477 | 0.494 | +0.0009 | 0.022 | 0.14 | +43.6 |
| momentum_24|h1|all | 1260 | 21 | 1260 | 0.554 | 0.53-0.58 | 0.506 | 0.500 | +0.0038 | 0.044 | 0.00 | - |
| momentum_24|h1|on_time | 1200 | 20 | 1200 | 0.547 | 0.52-0.57 | 0.498 | 0.499 | +0.0033 | 0.037 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 1080 | 18 | 1080 | 0.477 | 0.45-0.51 | 0.477 | 0.503 | +0.0001 | 0.026 | 0.00 | - |
| momentum_24|h4|on_time | 1080 | 18 | 1080 | 0.477 | 0.45-0.51 | 0.477 | 0.503 | +0.0001 | 0.026 | 0.00 | - |
| orthosys|h1|all | 1260 | 21 | 53 | 0.491 | 0.36-0.62 | 0.506 | 0.499 | +0.0002 | 0.006 | 0.00 | - |
| orthosys|h1|on_time | 1200 | 20 | 52 | 0.481 | 0.35-0.61 | 0.498 | 0.499 | -0.0001 | 0.004 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 1080 | 18 | 45 | 0.644 | 0.50-0.77 | 0.477 | 0.500 | +0.0017 | 0.023 | 0.00 | - |
| orthosys|h4|on_time | 1080 | 18 | 45 | 0.644 | 0.50-0.77 | 0.477 | 0.500 | +0.0017 | 0.023 | 0.00 | - |
| recent_base_rate_7d|h1|all | 1200 | 20 | 1200 | 0.502 | 0.47-0.53 | 0.498 | 0.471 | -0.0025 | 0.027 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 1200 | 20 | 1200 | 0.502 | 0.47-0.53 | 0.498 | 0.471 | -0.0025 | 0.027 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1020 | 17 | 1020 | 0.513 | 0.48-0.54 | 0.487 | 0.437 | -0.0163 | 0.050 | 1.00 | -19.6 |
| recent_base_rate_7d|h4|on_time | 1020 | 17 | 1020 | 0.513 | 0.48-0.54 | 0.487 | 0.437 | -0.0163 | 0.050 | 1.00 | -19.6 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 981.55 | -1.85% | 446 | 159 | 16 |
| analog_k100|h4 | 996.93 | -0.31% | 467 | 221 | 13 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 21 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 18 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 16 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 13 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 16 |
| derivatives|h4 | 996.58 | -0.34% | 3 | 1 | 13 |
| lgbm_calibrated|h1 | 944.33 | -5.57% | 84 | 27 | 21 |
| lgbm_calibrated|h4 | 993.15 | -0.68% | 192 | 108 | 18 |
| logistic|h1 | 957.89 | -4.21% | 69 | 32 | 21 |
| logistic|h4 | 1028.29 | +2.83% | 149 | 72 | 18 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 21 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 18 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 21 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 18 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 20 |
| recent_base_rate_7d|h4 | 991.70 | -0.83% | 1020 | 462 | 17 |
| benchmark_long_all_coins|h1 | 992.17 | -0.78% | 1260 | 558 | 21 |
| benchmark_long_all_coins|h4 | 998.46 | -0.15% | 1080 | 476 | 18 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 16 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 13 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 16 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 13 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 16 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 13 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 20 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 17 |

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
