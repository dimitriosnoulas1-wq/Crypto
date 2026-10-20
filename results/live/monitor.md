# Live monitor (2026-10-20T08:06:53.145597+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.001 (same probability for every coin)

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['ETHFI', 'STX']
- **last_closed_bar**: 2026-10-20 07:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.8
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 107.0 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.123, 'recent_base_rate_7d': 0.098, 'momentum_24': 0.138, 'logistic': 0.146, 'lgbm_calibrated': 0.135, 'analog_k100': 0.109, 'derivatives': 0.126, 'orthosys': 0.126}
- **council_member_logloss_h1**: {'base_rate': 0.6936, 'recent_base_rate_7d': 0.6992, 'momentum_24': 0.691, 'logistic': 0.6898, 'lgbm_calibrated': 0.6915, 'analog_k100': 0.6985, 'derivatives': 0.6939, 'orthosys': 0.6931}
- **council_calls_h1**: 7
- **council_abstain_h1**: {'no_edge': 48, 'spoke': 7, 'extreme_volatility': 5}
- **council_weights_h4**: {'base_rate': 0.152, 'recent_base_rate_7d': 0.048, 'momentum_24': 0.152, 'logistic': 0.133, 'lgbm_calibrated': 0.096, 'analog_k100': 0.122, 'derivatives': 0.15, 'orthosys': 0.148}
- **council_member_logloss_h4**: {'base_rate': 0.6925, 'recent_base_rate_7d': 0.7274, 'momentum_24': 0.6925, 'logistic': 0.6962, 'lgbm_calibrated': 0.7054, 'analog_k100': 0.7015, 'derivatives': 0.692, 'orthosys': 0.6933}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 42, 'members_disagree': 13, 'extreme_volatility': 5}
- **prediction_latency_min**: 6.8
- **price_snapshot_age_s**: 0.4
- **train_rows_h1**: 90227
- **orthosys_hist_hit_h1**: 0.5275
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0109
- **p_spread_logistic_h1**: 0.0212
- **p_spread_lgbm_calibrated_h1**: 0.0133
- **p_spread_analog_k100_h1**: 0.0563
- **p_spread_derivatives_h1**: 0.0015
- **p_spread_orthosys_h1**: 0.0077
- **p_spread_council_h1**: 0.0081
- **train_rows_h4**: 90041
- **orthosys_hist_hit_h4**: 0.5183
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.001
- **p_spread_logistic_h4**: 0.0324
- **p_spread_lgbm_calibrated_h4**: 0.001
- **p_spread_analog_k100_h4**: 0.0754
- **p_spread_derivatives_h4**: 0.0053
- **p_spread_orthosys_h4**: 0.0051
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 16440

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 660 | 11 | 660 | 0.500 | 0.46-0.54 | 0.523 | 0.491 | -0.0125 | 0.045 | 0.41 | -2.7 |
| analog_k100|h1|on_time | 660 | 11 | 660 | 0.500 | 0.46-0.54 | 0.523 | 0.491 | -0.0125 | 0.045 | 0.41 | -2.7 |
| analog_k100|h4|all | 480 | 8 | 480 | 0.550 | 0.51-0.59 | 0.498 | 0.460 | -0.0022 | 0.053 | 0.59 | +8.1 |
| analog_k100|h4|on_time | 480 | 8 | 480 | 0.550 | 0.51-0.59 | 0.498 | 0.460 | -0.0022 | 0.053 | 0.59 | +8.1 |
| base_rate|h1|all | 960 | 16 | 960 | 0.482 | 0.45-0.51 | 0.518 | 0.498 | +0.0000 | 0.020 | 0.00 | - |
| base_rate|h1|on_time | 900 | 15 | 900 | 0.491 | 0.46-0.52 | 0.509 | 0.498 | +0.0000 | 0.011 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 780 | 13 | 780 | 0.533 | 0.50-0.57 | 0.533 | 0.503 | +0.0000 | 0.030 | 0.00 | - |
| base_rate|h4|on_time | 780 | 13 | 780 | 0.533 | 0.50-0.57 | 0.533 | 0.503 | +0.0000 | 0.030 | 0.00 | - |
| council|h1|all | 660 | 11 | 76 | 0.500 | 0.39-0.61 | 0.523 | 0.497 | +0.0003 | 0.026 | 0.00 | - |
| council|h1|on_time | 660 | 11 | 76 | 0.500 | 0.39-0.61 | 0.523 | 0.497 | +0.0003 | 0.026 | 0.00 | - |
| council|h4|all | 480 | 8 | 12 | 0.750 | 0.47-0.91 | 0.498 | 0.500 | +0.0015 | 0.010 | 0.00 | - |
| council|h4|on_time | 480 | 8 | 12 | 0.750 | 0.47-0.91 | 0.498 | 0.500 | +0.0015 | 0.010 | 0.00 | - |
| derivatives|h1|all | 660 | 11 | 660 | 0.470 | 0.43-0.51 | 0.523 | 0.498 | -0.0002 | 0.032 | 0.00 | - |
| derivatives|h1|on_time | 660 | 11 | 660 | 0.470 | 0.43-0.51 | 0.523 | 0.498 | -0.0002 | 0.032 | 0.00 | - |
| derivatives|h4|all | 480 | 8 | 480 | 0.519 | 0.47-0.56 | 0.498 | 0.503 | +0.0012 | 0.015 | 0.00 | - |
| derivatives|h4|on_time | 480 | 8 | 480 | 0.519 | 0.47-0.56 | 0.498 | 0.503 | +0.0012 | 0.015 | 0.00 | - |
| lgbm_calibrated|h1|all | 960 | 16 | 960 | 0.536 | 0.50-0.57 | 0.518 | 0.477 | +0.0045 | 0.041 | 0.08 | -28.5 |
| lgbm_calibrated|h1|on_time | 900 | 15 | 900 | 0.549 | 0.52-0.58 | 0.509 | 0.477 | +0.0073 | 0.032 | 0.09 | -28.5 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 780 | 13 | 780 | 0.464 | 0.43-0.50 | 0.533 | 0.460 | -0.0140 | 0.076 | 0.25 | -0.9 |
| lgbm_calibrated|h4|on_time | 780 | 13 | 780 | 0.464 | 0.43-0.50 | 0.533 | 0.460 | -0.0140 | 0.076 | 0.25 | -0.9 |
| logistic|h1|all | 960 | 16 | 960 | 0.566 | 0.53-0.60 | 0.518 | 0.489 | +0.0072 | 0.049 | 0.06 | -38.7 |
| logistic|h1|on_time | 900 | 15 | 900 | 0.551 | 0.52-0.58 | 0.509 | 0.487 | +0.0038 | 0.035 | 0.06 | -39.7 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 780 | 13 | 780 | 0.529 | 0.49-0.56 | 0.533 | 0.487 | +0.0019 | 0.046 | 0.15 | -2.9 |
| logistic|h4|on_time | 780 | 13 | 780 | 0.529 | 0.49-0.56 | 0.533 | 0.487 | +0.0019 | 0.046 | 0.15 | -2.9 |
| momentum_24|h1|all | 960 | 16 | 960 | 0.566 | 0.53-0.60 | 0.518 | 0.500 | +0.0047 | 0.056 | 0.00 | - |
| momentum_24|h1|on_time | 900 | 15 | 900 | 0.557 | 0.52-0.59 | 0.509 | 0.500 | +0.0040 | 0.047 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 780 | 13 | 780 | 0.533 | 0.50-0.57 | 0.533 | 0.503 | +0.0001 | 0.030 | 0.00 | - |
| momentum_24|h4|on_time | 780 | 13 | 780 | 0.533 | 0.50-0.57 | 0.533 | 0.503 | +0.0001 | 0.030 | 0.00 | - |
| orthosys|h1|all | 960 | 16 | 38 | 0.526 | 0.37-0.68 | 0.518 | 0.499 | +0.0007 | 0.020 | 0.00 | - |
| orthosys|h1|on_time | 900 | 15 | 37 | 0.514 | 0.36-0.67 | 0.509 | 0.499 | +0.0004 | 0.010 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 780 | 13 | 26 | 0.538 | 0.35-0.71 | 0.533 | 0.500 | -0.0003 | 0.039 | 0.00 | - |
| orthosys|h4|on_time | 780 | 13 | 26 | 0.538 | 0.35-0.71 | 0.533 | 0.500 | -0.0003 | 0.039 | 0.00 | - |
| recent_base_rate_7d|h1|all | 900 | 15 | 900 | 0.491 | 0.46-0.52 | 0.509 | 0.472 | -0.0056 | 0.037 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 900 | 15 | 900 | 0.491 | 0.46-0.52 | 0.509 | 0.472 | -0.0056 | 0.037 | 0.00 | - |
| recent_base_rate_7d|h4|all | 720 | 12 | 720 | 0.447 | 0.41-0.48 | 0.553 | 0.436 | -0.0510 | 0.116 | 1.00 | -28.1 |
| recent_base_rate_7d|h4|on_time | 720 | 12 | 720 | 0.447 | 0.41-0.48 | 0.553 | 0.436 | -0.0510 | 0.116 | 1.00 | -28.1 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 996.23 | -0.38% | 272 | 122 | 11 |
| analog_k100|h4 | 1002.19 | +0.22% | 281 | 143 | 8 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 16 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 13 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 11 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 8 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 11 |
| derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 8 |
| lgbm_calibrated|h1 | 959.78 | -4.02% | 81 | 26 | 16 |
| lgbm_calibrated|h4 | 993.15 | -0.68% | 192 | 108 | 13 |
| logistic|h1 | 932.38 | -6.76% | 59 | 28 | 16 |
| logistic|h4 | 1003.27 | +0.33% | 114 | 53 | 13 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 16 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 13 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 16 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 13 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 15 |
| recent_base_rate_7d|h4 | 991.59 | -0.84% | 720 | 296 | 12 |
| benchmark_long_all_coins|h1 | 989.03 | -1.10% | 960 | 391 | 16 |
| benchmark_long_all_coins|h4 | 1001.08 | +0.11% | 780 | 367 | 13 |

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
