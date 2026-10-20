# Live monitor (2026-10-20T06:06:54.797081+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.001 (same probability for every coin)

## Health

- **venue**: okx
- **symbols**: 63
- **universe_size**: 60
- **fetched_only_for_scoring**: ['ETHFI', 'USELESS', 'W']
- **last_closed_bar**: 2026-10-20 05:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.8
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 105.8 instruments 63/63']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.125, 'recent_base_rate_7d': 0.101, 'momentum_24': 0.141, 'logistic': 0.132, 'lgbm_calibrated': 0.129, 'analog_k100': 0.117, 'derivatives': 0.128, 'orthosys': 0.127}
- **council_member_logloss_h1**: {'base_rate': 0.6936, 'recent_base_rate_7d': 0.6998, 'momentum_24': 0.6906, 'logistic': 0.6923, 'lgbm_calibrated': 0.6929, 'analog_k100': 0.6979, 'derivatives': 0.694, 'orthosys': 0.6932}
- **council_calls_h1**: 3
- **council_abstain_h1**: {'no_edge': 54, 'spoke': 3, 'extreme_volatility': 3}
- **council_weights_h4**: {'base_rate': 0.16, 'recent_base_rate_7d': 0.042, 'momentum_24': 0.16, 'logistic': 0.117, 'lgbm_calibrated': 0.09, 'analog_k100': 0.122, 'derivatives': 0.156, 'orthosys': 0.153}
- **council_member_logloss_h4**: {'base_rate': 0.6919, 'recent_base_rate_7d': 0.741, 'momentum_24': 0.6919, 'logistic': 0.7024, 'lgbm_calibrated': 0.7112, 'analog_k100': 0.7079, 'derivatives': 0.6912, 'orthosys': 0.6934}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 48, 'members_disagree': 9, 'extreme_volatility': 3}
- **prediction_latency_min**: 6.8
- **price_snapshot_age_s**: 0.8
- **train_rows_h1**: 91624
- **orthosys_hist_hit_h1**: 0.5292
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0104
- **p_spread_logistic_h1**: 0.0226
- **p_spread_lgbm_calibrated_h1**: 0.011
- **p_spread_analog_k100_h1**: 0.0511
- **p_spread_derivatives_h1**: 0.0015
- **p_spread_orthosys_h1**: 0.0053
- **p_spread_council_h1**: 0.0062
- **train_rows_h4**: 91435
- **orthosys_hist_hit_h4**: 0.5161
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0005
- **p_spread_logistic_h4**: 0.0286
- **p_spread_lgbm_calibrated_h4**: 0.001
- **p_spread_analog_k100_h4**: 0.0866
- **p_spread_derivatives_h4**: 0.0048
- **p_spread_orthosys_h4**: 0.0029
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 14280

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 540 | 9 | 540 | 0.519 | 0.48-0.56 | 0.530 | 0.492 | -0.0064 | 0.048 | 0.43 | -0.4 |
| analog_k100|h1|on_time | 540 | 9 | 540 | 0.519 | 0.48-0.56 | 0.530 | 0.492 | -0.0064 | 0.048 | 0.43 | -0.4 |
| analog_k100|h4|all | 360 | 6 | 360 | 0.528 | 0.48-0.58 | 0.589 | 0.459 | -0.0153 | 0.133 | 0.59 | -1.7 |
| analog_k100|h4|on_time | 360 | 6 | 360 | 0.528 | 0.48-0.58 | 0.589 | 0.459 | -0.0153 | 0.133 | 0.59 | -1.7 |
| base_rate|h1|all | 840 | 14 | 840 | 0.479 | 0.44-0.51 | 0.521 | 0.498 | +0.0000 | 0.023 | 0.00 | - |
| base_rate|h1|on_time | 780 | 13 | 780 | 0.488 | 0.45-0.52 | 0.512 | 0.498 | +0.0000 | 0.013 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 660 | 11 | 660 | 0.589 | 0.55-0.63 | 0.589 | 0.503 | +0.0000 | 0.086 | 0.00 | - |
| base_rate|h4|on_time | 660 | 11 | 660 | 0.589 | 0.55-0.63 | 0.589 | 0.503 | +0.0000 | 0.086 | 0.00 | - |
| council|h1|all | 540 | 9 | 67 | 0.507 | 0.39-0.62 | 0.530 | 0.497 | +0.0008 | 0.033 | 0.00 | - |
| council|h1|on_time | 540 | 9 | 67 | 0.507 | 0.39-0.62 | 0.530 | 0.497 | +0.0008 | 0.033 | 0.00 | - |
| council|h4|all | 360 | 6 | 12 | 0.750 | 0.47-0.91 | 0.589 | 0.499 | -0.0006 | 0.105 | 0.00 | - |
| council|h4|on_time | 360 | 6 | 12 | 0.750 | 0.47-0.91 | 0.589 | 0.499 | -0.0006 | 0.105 | 0.00 | - |
| derivatives|h1|all | 540 | 9 | 540 | 0.459 | 0.42-0.50 | 0.530 | 0.498 | -0.0003 | 0.042 | 0.00 | - |
| derivatives|h1|on_time | 540 | 9 | 540 | 0.459 | 0.42-0.50 | 0.530 | 0.498 | -0.0003 | 0.042 | 0.00 | - |
| derivatives|h4|all | 360 | 6 | 360 | 0.603 | 0.55-0.65 | 0.589 | 0.503 | +0.0007 | 0.099 | 0.00 | - |
| derivatives|h4|on_time | 360 | 6 | 360 | 0.603 | 0.55-0.65 | 0.589 | 0.503 | +0.0007 | 0.099 | 0.00 | - |
| lgbm_calibrated|h1|all | 840 | 14 | 840 | 0.501 | 0.47-0.53 | 0.521 | 0.474 | +0.0049 | 0.047 | 0.09 | -20.6 |
| lgbm_calibrated|h1|on_time | 780 | 13 | 780 | 0.513 | 0.48-0.55 | 0.512 | 0.475 | +0.0081 | 0.037 | 0.10 | -20.6 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 660 | 11 | 660 | 0.408 | 0.37-0.45 | 0.589 | 0.459 | -0.0322 | 0.133 | 0.24 | -10.0 |
| lgbm_calibrated|h4|on_time | 660 | 11 | 660 | 0.408 | 0.37-0.45 | 0.589 | 0.459 | -0.0322 | 0.133 | 0.24 | -10.0 |
| logistic|h1|all | 840 | 14 | 840 | 0.544 | 0.51-0.58 | 0.521 | 0.487 | +0.0034 | 0.036 | 0.06 | -30.9 |
| logistic|h1|on_time | 780 | 13 | 780 | 0.526 | 0.49-0.56 | 0.512 | 0.484 | -0.0008 | 0.029 | 0.06 | -31.5 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 660 | 11 | 660 | 0.473 | 0.43-0.51 | 0.589 | 0.491 | -0.0141 | 0.099 | 0.14 | -30.2 |
| logistic|h4|on_time | 660 | 11 | 660 | 0.473 | 0.43-0.51 | 0.589 | 0.491 | -0.0141 | 0.099 | 0.14 | -30.2 |
| momentum_24|h1|all | 840 | 14 | 840 | 0.577 | 0.54-0.61 | 0.521 | 0.500 | +0.0056 | 0.068 | 0.00 | - |
| momentum_24|h1|on_time | 780 | 13 | 780 | 0.568 | 0.53-0.60 | 0.512 | 0.500 | +0.0049 | 0.059 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 660 | 11 | 660 | 0.589 | 0.55-0.63 | 0.589 | 0.503 | -0.0000 | 0.086 | 0.00 | - |
| momentum_24|h4|on_time | 660 | 11 | 660 | 0.589 | 0.55-0.63 | 0.589 | 0.503 | -0.0000 | 0.086 | 0.00 | - |
| orthosys|h1|all | 840 | 14 | 30 | 0.500 | 0.33-0.67 | 0.521 | 0.500 | +0.0006 | 0.023 | 0.00 | - |
| orthosys|h1|on_time | 780 | 13 | 29 | 0.483 | 0.31-0.66 | 0.512 | 0.500 | +0.0003 | 0.012 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 660 | 11 | 19 | 0.421 | 0.23-0.64 | 0.589 | 0.500 | -0.0023 | 0.090 | 0.00 | - |
| orthosys|h4|on_time | 660 | 11 | 19 | 0.421 | 0.23-0.64 | 0.589 | 0.500 | -0.0023 | 0.090 | 0.00 | - |
| recent_base_rate_7d|h1|all | 780 | 13 | 780 | 0.488 | 0.45-0.52 | 0.512 | 0.472 | -0.0059 | 0.039 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 780 | 13 | 780 | 0.488 | 0.45-0.52 | 0.512 | 0.472 | -0.0059 | 0.039 | 0.00 | - |
| recent_base_rate_7d|h4|all | 600 | 10 | 600 | 0.382 | 0.34-0.42 | 0.618 | 0.434 | -0.0838 | 0.184 | 1.00 | -43.1 |
| recent_base_rate_7d|h4|on_time | 600 | 10 | 600 | 0.382 | 0.34-0.42 | 0.618 | 0.434 | -0.0838 | 0.184 | 1.00 | -43.1 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 999.44 | -0.06% | 230 | 107 | 9 |
| analog_k100|h4 | 1000.27 | +0.03% | 213 | 99 | 6 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 14 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 11 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 9 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 6 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 9 |
| derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 6 |
| lgbm_calibrated|h1 | 972.16 | -2.78% | 75 | 23 | 14 |
| lgbm_calibrated|h4 | 992.01 | -0.80% | 161 | 82 | 11 |
| logistic|h1 | 948.23 | -5.18% | 52 | 25 | 14 |
| logistic|h4 | 997.29 | -0.27% | 94 | 37 | 11 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 14 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 11 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 14 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 11 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 13 |
| recent_base_rate_7d|h4 | 989.28 | -1.07% | 600 | 205 | 10 |
| benchmark_long_all_coins|h1 | 986.98 | -1.30% | 840 | 328 | 14 |
| benchmark_long_all_coins|h4 | 1004.42 | +0.44% | 660 | 347 | 11 |

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
