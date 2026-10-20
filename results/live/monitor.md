# Live monitor (2026-10-20T14:08:07.571238+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h1 = 0.0011 (same probability for every coin)

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['ASTER', 'RAY']
- **last_closed_bar**: 2026-10-20 13:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 6.0
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 111.5 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.123, 'recent_base_rate_7d': 0.115, 'momentum_24': 0.139, 'logistic': 0.138, 'lgbm_calibrated': 0.15, 'analog_k100': 0.086, 'derivatives': 0.126, 'orthosys': 0.124}
- **council_member_logloss_h1**: {'base_rate': 0.6933, 'recent_base_rate_7d': 0.6945, 'momentum_24': 0.6914, 'logistic': 0.6915, 'lgbm_calibrated': 0.6902, 'analog_k100': 0.7014, 'derivatives': 0.6934, 'orthosys': 0.6932}
- **council_calls_h1**: 29
- **council_abstain_h1**: {'spoke': 29, 'no_edge': 26, 'extreme_volatility': 5}
- **council_weights_h4**: {'base_rate': 0.129, 'recent_base_rate_7d': 0.085, 'momentum_24': 0.129, 'logistic': 0.131, 'lgbm_calibrated': 0.138, 'analog_k100': 0.125, 'derivatives': 0.127, 'orthosys': 0.135}
- **council_member_logloss_h4**: {'base_rate': 0.6936, 'recent_base_rate_7d': 0.7017, 'momentum_24': 0.6936, 'logistic': 0.6933, 'lgbm_calibrated': 0.6923, 'analog_k100': 0.6941, 'derivatives': 0.6938, 'orthosys': 0.6928}
- **council_calls_h4**: 3
- **council_abstain_h4**: {'no_edge': 32, 'members_disagree': 20, 'extreme_volatility': 5, 'spoke': 3}
- **prediction_latency_min**: 8.0
- **price_snapshot_age_s**: 0.9
- **train_rows_h1**: 90557
- **orthosys_hist_hit_h1**: 0.5269
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0104
- **p_spread_logistic_h1**: 0.0216
- **p_spread_lgbm_calibrated_h1**: 0.0011
- **p_spread_analog_k100_h1**: 0.0654
- **p_spread_derivatives_h1**: 0.001
- **p_spread_orthosys_h1**: 0.009
- **p_spread_council_h1**: 0.0133
- **train_rows_h4**: 90371
- **orthosys_hist_hit_h4**: 0.5166
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0013
- **p_spread_logistic_h4**: 0.0414
- **p_spread_lgbm_calibrated_h4**: 0.0029
- **p_spread_analog_k100_h4**: 0.0815
- **p_spread_derivatives_h4**: 0.0042
- **p_spread_orthosys_h4**: 0.0056
- **p_spread_council_h4**: 0.0059
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 22920

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1020 | 17 | 1020 | 0.487 | 0.46-0.52 | 0.530 | 0.476 | -0.0271 | 0.065 | 0.47 | -21.1 |
| analog_k100|h1|on_time | 1020 | 17 | 1020 | 0.487 | 0.46-0.52 | 0.530 | 0.476 | -0.0271 | 0.065 | 0.47 | -21.1 |
| analog_k100|h4|all | 840 | 14 | 840 | 0.508 | 0.47-0.54 | 0.468 | 0.451 | -0.0270 | 0.068 | 0.62 | -26.6 |
| analog_k100|h4|on_time | 840 | 14 | 840 | 0.508 | 0.47-0.54 | 0.468 | 0.451 | -0.0270 | 0.068 | 0.62 | -26.6 |
| base_rate|h1|all | 1320 | 22 | 1320 | 0.475 | 0.45-0.50 | 0.525 | 0.498 | +0.0000 | 0.027 | 0.00 | - |
| base_rate|h1|on_time | 1260 | 21 | 1260 | 0.481 | 0.45-0.51 | 0.519 | 0.498 | +0.0000 | 0.021 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 1140 | 19 | 1140 | 0.500 | 0.47-0.53 | 0.500 | 0.503 | +0.0000 | 0.003 | 0.00 | - |
| base_rate|h4|on_time | 1140 | 19 | 1140 | 0.500 | 0.47-0.53 | 0.500 | 0.503 | +0.0000 | 0.003 | 0.00 | - |
| council|h1|all | 1020 | 17 | 118 | 0.492 | 0.40-0.58 | 0.530 | 0.497 | +0.0001 | 0.033 | 0.00 | - |
| council|h1|on_time | 1020 | 17 | 118 | 0.492 | 0.40-0.58 | 0.530 | 0.497 | +0.0001 | 0.033 | 0.00 | - |
| council|h4|all | 840 | 14 | 12 | 0.750 | 0.47-0.91 | 0.468 | 0.500 | +0.0020 | 0.032 | 0.00 | - |
| council|h4|on_time | 840 | 14 | 12 | 0.750 | 0.47-0.91 | 0.468 | 0.500 | +0.0020 | 0.032 | 0.00 | - |
| derivatives|h1|all | 1020 | 17 | 1020 | 0.466 | 0.44-0.50 | 0.530 | 0.498 | -0.0002 | 0.036 | 0.00 | - |
| derivatives|h1|on_time | 1020 | 17 | 1020 | 0.466 | 0.44-0.50 | 0.530 | 0.498 | -0.0002 | 0.036 | 0.00 | - |
| derivatives|h4|all | 840 | 14 | 840 | 0.485 | 0.45-0.52 | 0.468 | 0.502 | +0.0004 | 0.035 | 0.00 | -45.1 |
| derivatives|h4|on_time | 840 | 14 | 840 | 0.485 | 0.45-0.52 | 0.468 | 0.502 | +0.0004 | 0.035 | 0.00 | -45.1 |
| lgbm_calibrated|h1|all | 1320 | 22 | 1320 | 0.561 | 0.53-0.59 | 0.525 | 0.481 | +0.0035 | 0.044 | 0.06 | -33.2 |
| lgbm_calibrated|h1|on_time | 1260 | 21 | 1260 | 0.571 | 0.54-0.60 | 0.519 | 0.482 | +0.0054 | 0.051 | 0.07 | -33.2 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 1140 | 19 | 1140 | 0.499 | 0.47-0.53 | 0.500 | 0.462 | -0.0051 | 0.039 | 0.17 | -6.6 |
| lgbm_calibrated|h4|on_time | 1140 | 19 | 1140 | 0.499 | 0.47-0.53 | 0.500 | 0.462 | -0.0051 | 0.039 | 0.17 | -6.6 |
| logistic|h1|all | 1320 | 22 | 1320 | 0.524 | 0.50-0.55 | 0.525 | 0.493 | +0.0015 | 0.033 | 0.05 | -22.5 |
| logistic|h1|on_time | 1260 | 21 | 1260 | 0.512 | 0.48-0.54 | 0.519 | 0.491 | -0.0012 | 0.029 | 0.05 | -22.6 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 1140 | 19 | 1140 | 0.529 | 0.50-0.56 | 0.500 | 0.496 | +0.0061 | 0.005 | 0.14 | +51.3 |
| logistic|h4|on_time | 1140 | 19 | 1140 | 0.529 | 0.50-0.56 | 0.500 | 0.496 | +0.0061 | 0.005 | 0.14 | +51.3 |
| momentum_24|h1|all | 1320 | 22 | 1320 | 0.562 | 0.54-0.59 | 0.525 | 0.500 | +0.0046 | 0.052 | 0.00 | - |
| momentum_24|h1|on_time | 1260 | 21 | 1260 | 0.556 | 0.53-0.58 | 0.519 | 0.500 | +0.0041 | 0.046 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 1140 | 19 | 1140 | 0.500 | 0.47-0.53 | 0.500 | 0.503 | +0.0001 | 0.003 | 0.00 | - |
| momentum_24|h4|on_time | 1140 | 19 | 1140 | 0.500 | 0.47-0.53 | 0.500 | 0.503 | +0.0001 | 0.003 | 0.00 | - |
| orthosys|h1|all | 1320 | 22 | 57 | 0.491 | 0.37-0.62 | 0.525 | 0.499 | +0.0004 | 0.026 | 0.00 | - |
| orthosys|h1|on_time | 1260 | 21 | 56 | 0.482 | 0.36-0.61 | 0.519 | 0.499 | +0.0002 | 0.020 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 1140 | 19 | 48 | 0.604 | 0.46-0.73 | 0.500 | 0.500 | +0.0010 | 0.011 | 0.00 | - |
| orthosys|h4|on_time | 1140 | 19 | 48 | 0.604 | 0.46-0.73 | 0.500 | 0.500 | +0.0010 | 0.011 | 0.00 | - |
| recent_base_rate_7d|h1|all | 1260 | 21 | 1260 | 0.481 | 0.45-0.51 | 0.519 | 0.471 | -0.0062 | 0.048 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 1260 | 21 | 1260 | 0.481 | 0.45-0.51 | 0.519 | 0.471 | -0.0062 | 0.048 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1080 | 18 | 1080 | 0.489 | 0.46-0.52 | 0.511 | 0.437 | -0.0296 | 0.074 | 1.00 | -29.2 |
| recent_base_rate_7d|h4|on_time | 1080 | 18 | 1080 | 0.489 | 0.46-0.52 | 0.511 | 0.437 | -0.0296 | 0.074 | 1.00 | -29.2 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 969.28 | -3.07% | 480 | 163 | 17 |
| analog_k100|h4 | 993.05 | -0.69% | 517 | 229 | 14 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 22 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 19 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 17 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 14 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 17 |
| derivatives|h4 | 996.58 | -0.34% | 3 | 1 | 14 |
| lgbm_calibrated|h1 | 944.33 | -5.57% | 84 | 27 | 22 |
| lgbm_calibrated|h4 | 966.09 | -3.39% | 193 | 108 | 19 |
| logistic|h1 | 965.07 | -3.49% | 71 | 33 | 22 |
| logistic|h4 | 1034.55 | +3.45% | 155 | 78 | 19 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 22 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 19 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 22 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 19 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 21 |
| recent_base_rate_7d|h4 | 986.90 | -1.31% | 1080 | 468 | 18 |
| benchmark_long_all_coins|h1 | 1006.87 | +0.69% | 1320 | 616 | 22 |
| benchmark_long_all_coins|h4 | 1002.79 | +0.28% | 1140 | 530 | 19 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 17 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 14 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 19 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 17 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 14 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 17 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 14 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 19 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 19 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 19 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 19 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 18 |

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
