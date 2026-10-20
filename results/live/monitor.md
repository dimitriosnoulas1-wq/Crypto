# Live monitor (2026-10-20T07:07:27.762947+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0019 (same probability for every coin)

## Health

- **venue**: okx
- **symbols**: 63
- **universe_size**: 60
- **fetched_only_for_scoring**: ['ETHFI', 'STX', 'USELESS']
- **last_closed_bar**: 2026-10-20 06:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.3
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 107.0 instruments 63/63']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.122, 'recent_base_rate_7d': 0.11, 'momentum_24': 0.138, 'logistic': 0.131, 'lgbm_calibrated': 0.135, 'analog_k100': 0.115, 'derivatives': 0.125, 'orthosys': 0.124}
- **council_member_logloss_h1**: {'base_rate': 0.6935, 'recent_base_rate_7d': 0.6964, 'momentum_24': 0.6907, 'logistic': 0.6918, 'lgbm_calibrated': 0.691, 'analog_k100': 0.6969, 'derivatives': 0.6937, 'orthosys': 0.6932}
- **council_calls_h1**: 6
- **council_abstain_h1**: {'no_edge': 51, 'spoke': 6, 'extreme_volatility': 3}
- **council_weights_h4**: {'base_rate': 0.155, 'recent_base_rate_7d': 0.044, 'momentum_24': 0.155, 'logistic': 0.122, 'lgbm_calibrated': 0.091, 'analog_k100': 0.13, 'derivatives': 0.152, 'orthosys': 0.149}
- **council_member_logloss_h4**: {'base_rate': 0.6922, 'recent_base_rate_7d': 0.7338, 'momentum_24': 0.6922, 'logistic': 0.6994, 'lgbm_calibrated': 0.7082, 'analog_k100': 0.7001, 'derivatives': 0.6917, 'orthosys': 0.6933}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 49, 'members_disagree': 8, 'extreme_volatility': 3}
- **prediction_latency_min**: 7.3
- **price_snapshot_age_s**: 1.1
- **train_rows_h1**: 91678
- **orthosys_hist_hit_h1**: 0.5279
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.011
- **p_spread_logistic_h1**: 0.0177
- **p_spread_lgbm_calibrated_h1**: 0.0152
- **p_spread_analog_k100_h1**: 0.0542
- **p_spread_derivatives_h1**: 0.0014
- **p_spread_orthosys_h1**: 0.0087
- **p_spread_council_h1**: 0.0082
- **train_rows_h4**: 91489
- **orthosys_hist_hit_h4**: 0.5178
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0007
- **p_spread_logistic_h4**: 0.0235
- **p_spread_lgbm_calibrated_h4**: 0.0019
- **p_spread_analog_k100_h4**: 0.0851
- **p_spread_derivatives_h4**: 0.0077
- **p_spread_orthosys_h4**: 0.0056
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 15360

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 600 | 10 | 600 | 0.508 | 0.47-0.55 | 0.558 | 0.491 | -0.0093 | 0.077 | 0.41 | -2.4 |
| analog_k100|h1|on_time | 600 | 10 | 600 | 0.508 | 0.47-0.55 | 0.558 | 0.491 | -0.0093 | 0.077 | 0.41 | -2.4 |
| analog_k100|h4|all | 420 | 7 | 420 | 0.521 | 0.47-0.57 | 0.552 | 0.462 | -0.0169 | 0.096 | 0.59 | +1.7 |
| analog_k100|h4|on_time | 420 | 7 | 420 | 0.521 | 0.47-0.57 | 0.552 | 0.462 | -0.0169 | 0.096 | 0.59 | +1.7 |
| base_rate|h1|all | 900 | 15 | 900 | 0.459 | 0.43-0.49 | 0.541 | 0.498 | +0.0000 | 0.043 | 0.00 | - |
| base_rate|h1|on_time | 840 | 14 | 840 | 0.467 | 0.43-0.50 | 0.533 | 0.498 | +0.0000 | 0.035 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 720 | 12 | 720 | 0.568 | 0.53-0.60 | 0.568 | 0.503 | +0.0000 | 0.065 | 0.00 | - |
| base_rate|h4|on_time | 720 | 12 | 720 | 0.568 | 0.53-0.60 | 0.568 | 0.503 | +0.0000 | 0.065 | 0.00 | - |
| council|h1|all | 600 | 10 | 70 | 0.514 | 0.40-0.63 | 0.558 | 0.497 | +0.0012 | 0.061 | 0.00 | - |
| council|h1|on_time | 600 | 10 | 70 | 0.514 | 0.40-0.63 | 0.558 | 0.497 | +0.0012 | 0.061 | 0.00 | - |
| council|h4|all | 420 | 7 | 12 | 0.750 | 0.47-0.91 | 0.552 | 0.499 | +0.0002 | 0.066 | 0.00 | - |
| council|h4|on_time | 420 | 7 | 12 | 0.750 | 0.47-0.91 | 0.552 | 0.499 | +0.0002 | 0.066 | 0.00 | - |
| derivatives|h1|all | 600 | 10 | 600 | 0.432 | 0.39-0.47 | 0.558 | 0.498 | -0.0003 | 0.070 | 0.00 | - |
| derivatives|h1|on_time | 600 | 10 | 600 | 0.432 | 0.39-0.47 | 0.558 | 0.498 | -0.0003 | 0.070 | 0.00 | - |
| derivatives|h4|all | 420 | 7 | 420 | 0.571 | 0.52-0.62 | 0.552 | 0.503 | +0.0011 | 0.067 | 0.00 | - |
| derivatives|h4|on_time | 420 | 7 | 420 | 0.571 | 0.52-0.62 | 0.552 | 0.503 | +0.0011 | 0.067 | 0.00 | - |
| lgbm_calibrated|h1|all | 900 | 15 | 900 | 0.517 | 0.48-0.55 | 0.541 | 0.476 | +0.0042 | 0.065 | 0.08 | -20.6 |
| lgbm_calibrated|h1|on_time | 840 | 14 | 840 | 0.529 | 0.49-0.56 | 0.533 | 0.476 | +0.0072 | 0.057 | 0.09 | -20.6 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 720 | 12 | 720 | 0.429 | 0.39-0.47 | 0.568 | 0.460 | -0.0259 | 0.111 | 0.22 | -10.0 |
| lgbm_calibrated|h4|on_time | 720 | 12 | 720 | 0.429 | 0.39-0.47 | 0.568 | 0.460 | -0.0259 | 0.111 | 0.22 | -10.0 |
| logistic|h1|all | 900 | 15 | 900 | 0.561 | 0.53-0.59 | 0.541 | 0.489 | +0.0076 | 0.054 | 0.06 | -28.5 |
| logistic|h1|on_time | 840 | 14 | 840 | 0.545 | 0.51-0.58 | 0.533 | 0.487 | +0.0040 | 0.048 | 0.06 | -28.9 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 720 | 12 | 720 | 0.499 | 0.46-0.54 | 0.568 | 0.489 | -0.0073 | 0.079 | 0.15 | -8.8 |
| logistic|h4|on_time | 720 | 12 | 720 | 0.499 | 0.46-0.54 | 0.568 | 0.489 | -0.0073 | 0.079 | 0.15 | -8.8 |
| momentum_24|h1|all | 900 | 15 | 900 | 0.571 | 0.54-0.60 | 0.541 | 0.500 | +0.0052 | 0.062 | 0.00 | - |
| momentum_24|h1|on_time | 840 | 14 | 840 | 0.562 | 0.53-0.60 | 0.533 | 0.500 | +0.0045 | 0.053 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 720 | 12 | 720 | 0.568 | 0.53-0.60 | 0.568 | 0.503 | -0.0001 | 0.065 | 0.00 | - |
| momentum_24|h4|on_time | 720 | 12 | 720 | 0.568 | 0.53-0.60 | 0.568 | 0.503 | -0.0001 | 0.065 | 0.00 | - |
| orthosys|h1|all | 900 | 15 | 32 | 0.531 | 0.36-0.69 | 0.541 | 0.499 | +0.0010 | 0.045 | 0.00 | - |
| orthosys|h1|on_time | 840 | 14 | 31 | 0.516 | 0.35-0.68 | 0.533 | 0.499 | +0.0008 | 0.036 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 720 | 12 | 21 | 0.429 | 0.24-0.63 | 0.568 | 0.500 | -0.0017 | 0.068 | 0.00 | - |
| orthosys|h4|on_time | 720 | 12 | 21 | 0.429 | 0.24-0.63 | 0.568 | 0.500 | -0.0017 | 0.068 | 0.00 | - |
| recent_base_rate_7d|h1|all | 840 | 14 | 840 | 0.467 | 0.43-0.50 | 0.533 | 0.472 | -0.0113 | 0.061 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 840 | 14 | 840 | 0.467 | 0.43-0.50 | 0.533 | 0.472 | -0.0113 | 0.061 | 0.00 | - |
| recent_base_rate_7d|h4|all | 660 | 11 | 660 | 0.408 | 0.37-0.45 | 0.592 | 0.435 | -0.0702 | 0.157 | 1.00 | -36.8 |
| recent_base_rate_7d|h4|on_time | 660 | 11 | 660 | 0.408 | 0.37-0.45 | 0.592 | 0.435 | -0.0702 | 0.157 | 1.00 | -36.8 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 996.78 | -0.32% | 249 | 114 | 10 |
| analog_k100|h4 | 1000.86 | +0.09% | 246 | 118 | 7 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 15 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 12 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 10 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 7 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 10 |
| derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 7 |
| lgbm_calibrated|h1 | 972.16 | -2.78% | 75 | 23 | 15 |
| lgbm_calibrated|h4 | 992.01 | -0.80% | 161 | 82 | 12 |
| logistic|h1 | 949.42 | -5.06% | 55 | 27 | 15 |
| logistic|h4 | 1001.64 | +0.16% | 105 | 46 | 12 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 15 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 12 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 15 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 12 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 14 |
| recent_base_rate_7d|h4 | 989.93 | -1.01% | 660 | 246 | 11 |
| benchmark_long_all_coins|h1 | 991.48 | -0.85% | 900 | 379 | 15 |
| benchmark_long_all_coins|h4 | 1003.26 | +0.33% | 720 | 361 | 12 |

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
