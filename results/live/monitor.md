# Live monitor (2026-10-20T09:06:52.263442+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0017 (same probability for every coin)

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['ETHFI', 'STX']
- **last_closed_bar**: 2026-10-20 08:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.8
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 106.5 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.122, 'recent_base_rate_7d': 0.108, 'momentum_24': 0.137, 'logistic': 0.145, 'lgbm_calibrated': 0.136, 'analog_k100': 0.102, 'derivatives': 0.125, 'orthosys': 0.124}
- **council_member_logloss_h1**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.6962, 'momentum_24': 0.6911, 'logistic': 0.6898, 'lgbm_calibrated': 0.6912, 'analog_k100': 0.6999, 'derivatives': 0.6936, 'orthosys': 0.6931}
- **council_calls_h1**: 6
- **council_abstain_h1**: {'no_edge': 49, 'spoke': 6, 'extreme_volatility': 5}
- **council_weights_h4**: {'base_rate': 0.141, 'recent_base_rate_7d': 0.056, 'momentum_24': 0.141, 'logistic': 0.145, 'lgbm_calibrated': 0.107, 'analog_k100': 0.131, 'derivatives': 0.139, 'orthosys': 0.14}
- **council_member_logloss_h4**: {'base_rate': 0.6929, 'recent_base_rate_7d': 0.7184, 'momentum_24': 0.6929, 'logistic': 0.6921, 'lgbm_calibrated': 0.6999, 'analog_k100': 0.6949, 'derivatives': 0.6927, 'orthosys': 0.6931}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 37, 'members_disagree': 18, 'extreme_volatility': 5}
- **prediction_latency_min**: 6.7
- **price_snapshot_age_s**: 0.8
- **train_rows_h1**: 90289
- **orthosys_hist_hit_h1**: 0.5275
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0112
- **p_spread_logistic_h1**: 0.0173
- **p_spread_lgbm_calibrated_h1**: 0.0163
- **p_spread_analog_k100_h1**: 0.0501
- **p_spread_derivatives_h1**: 0.0022
- **p_spread_orthosys_h1**: 0.005
- **p_spread_council_h1**: 0.0069
- **train_rows_h4**: 90103
- **orthosys_hist_hit_h4**: 0.5183
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0011
- **p_spread_logistic_h4**: 0.0298
- **p_spread_lgbm_calibrated_h4**: 0.0017
- **p_spread_analog_k100_h4**: 0.0805
- **p_spread_derivatives_h4**: 0.0098
- **p_spread_orthosys_h4**: 0.0033
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 17520

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 720 | 12 | 720 | 0.512 | 0.48-0.55 | 0.500 | 0.487 | -0.0044 | 0.034 | 0.42 | -6.3 |
| analog_k100|h1|on_time | 720 | 12 | 720 | 0.512 | 0.48-0.55 | 0.500 | 0.487 | -0.0044 | 0.034 | 0.42 | -6.3 |
| analog_k100|h4|all | 540 | 9 | 540 | 0.543 | 0.50-0.58 | 0.467 | 0.462 | -0.0032 | 0.027 | 0.58 | +1.9 |
| analog_k100|h4|on_time | 540 | 9 | 540 | 0.543 | 0.50-0.58 | 0.467 | 0.462 | -0.0032 | 0.027 | 0.58 | +1.9 |
| base_rate|h1|all | 1020 | 17 | 1020 | 0.498 | 0.47-0.53 | 0.502 | 0.498 | +0.0000 | 0.004 | 0.00 | - |
| base_rate|h1|on_time | 960 | 16 | 960 | 0.507 | 0.48-0.54 | 0.493 | 0.498 | +0.0000 | 0.005 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 840 | 14 | 840 | 0.511 | 0.48-0.54 | 0.511 | 0.503 | +0.0000 | 0.007 | 0.00 | - |
| base_rate|h4|on_time | 840 | 14 | 840 | 0.511 | 0.48-0.54 | 0.511 | 0.503 | +0.0000 | 0.007 | 0.00 | - |
| council|h1|all | 720 | 12 | 83 | 0.530 | 0.42-0.63 | 0.500 | 0.497 | +0.0005 | 0.004 | 0.00 | - |
| council|h1|on_time | 720 | 12 | 83 | 0.530 | 0.42-0.63 | 0.500 | 0.497 | +0.0005 | 0.004 | 0.00 | - |
| council|h4|all | 540 | 9 | 12 | 0.750 | 0.47-0.91 | 0.467 | 0.500 | +0.0023 | 0.033 | 0.00 | - |
| council|h4|on_time | 540 | 9 | 12 | 0.750 | 0.47-0.91 | 0.467 | 0.500 | +0.0023 | 0.033 | 0.00 | - |
| derivatives|h1|all | 720 | 12 | 720 | 0.493 | 0.46-0.53 | 0.500 | 0.498 | -0.0002 | 0.009 | 0.00 | - |
| derivatives|h1|on_time | 720 | 12 | 720 | 0.493 | 0.46-0.53 | 0.500 | 0.498 | -0.0002 | 0.009 | 0.00 | - |
| derivatives|h4|all | 540 | 9 | 540 | 0.487 | 0.45-0.53 | 0.467 | 0.503 | +0.0008 | 0.036 | 0.00 | -325.5 |
| derivatives|h4|on_time | 540 | 9 | 540 | 0.487 | 0.45-0.53 | 0.467 | 0.503 | +0.0008 | 0.036 | 0.00 | -325.5 |
| lgbm_calibrated|h1|all | 1020 | 17 | 1020 | 0.547 | 0.52-0.58 | 0.502 | 0.477 | +0.0040 | 0.024 | 0.08 | -33.2 |
| lgbm_calibrated|h1|on_time | 960 | 16 | 960 | 0.559 | 0.53-0.59 | 0.493 | 0.478 | +0.0066 | 0.037 | 0.09 | -33.2 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 840 | 14 | 840 | 0.487 | 0.45-0.52 | 0.511 | 0.460 | -0.0070 | 0.053 | 0.23 | -0.9 |
| lgbm_calibrated|h4|on_time | 840 | 14 | 840 | 0.487 | 0.45-0.52 | 0.511 | 0.460 | -0.0070 | 0.053 | 0.23 | -0.9 |
| logistic|h1|all | 1020 | 17 | 1020 | 0.548 | 0.52-0.58 | 0.502 | 0.490 | +0.0035 | 0.031 | 0.06 | -44.2 |
| logistic|h1|on_time | 960 | 16 | 960 | 0.533 | 0.50-0.56 | 0.493 | 0.489 | +0.0001 | 0.017 | 0.06 | -45.4 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 840 | 14 | 840 | 0.537 | 0.50-0.57 | 0.511 | 0.487 | +0.0045 | 0.023 | 0.14 | +4.3 |
| logistic|h4|on_time | 840 | 14 | 840 | 0.537 | 0.50-0.57 | 0.511 | 0.487 | +0.0045 | 0.023 | 0.14 | +4.3 |
| momentum_24|h1|all | 1020 | 17 | 1020 | 0.567 | 0.54-0.60 | 0.502 | 0.500 | +0.0048 | 0.057 | 0.00 | - |
| momentum_24|h1|on_time | 960 | 16 | 960 | 0.558 | 0.53-0.59 | 0.493 | 0.500 | +0.0042 | 0.049 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 840 | 14 | 840 | 0.511 | 0.48-0.54 | 0.511 | 0.503 | +0.0001 | 0.007 | 0.00 | - |
| momentum_24|h4|on_time | 840 | 14 | 840 | 0.511 | 0.48-0.54 | 0.511 | 0.503 | +0.0001 | 0.007 | 0.00 | - |
| orthosys|h1|all | 1020 | 17 | 43 | 0.535 | 0.39-0.67 | 0.502 | 0.499 | +0.0005 | 0.005 | 0.00 | - |
| orthosys|h1|on_time | 960 | 16 | 42 | 0.524 | 0.38-0.67 | 0.493 | 0.499 | +0.0003 | 0.007 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 840 | 14 | 30 | 0.533 | 0.36-0.70 | 0.511 | 0.500 | +0.0003 | 0.017 | 0.00 | - |
| orthosys|h4|on_time | 840 | 14 | 30 | 0.533 | 0.36-0.70 | 0.511 | 0.500 | +0.0003 | 0.017 | 0.00 | - |
| recent_base_rate_7d|h1|all | 960 | 16 | 960 | 0.507 | 0.48-0.54 | 0.493 | 0.472 | -0.0016 | 0.021 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 960 | 16 | 960 | 0.507 | 0.48-0.54 | 0.493 | 0.472 | -0.0016 | 0.021 | 0.00 | - |
| recent_base_rate_7d|h4|all | 780 | 13 | 780 | 0.473 | 0.44-0.51 | 0.527 | 0.437 | -0.0380 | 0.090 | 1.00 | -23.8 |
| recent_base_rate_7d|h4|on_time | 780 | 13 | 780 | 0.473 | 0.44-0.51 | 0.527 | 0.437 | -0.0380 | 0.090 | 1.00 | -23.8 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 992.39 | -0.76% | 303 | 124 | 12 |
| analog_k100|h4 | 1000.83 | +0.08% | 312 | 158 | 9 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 17 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 14 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 12 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 9 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 12 |
| derivatives|h4 | 991.86 | -0.81% | 1 | 0 | 9 |
| lgbm_calibrated|h1 | 944.33 | -5.57% | 84 | 27 | 17 |
| lgbm_calibrated|h4 | 993.15 | -0.68% | 192 | 108 | 14 |
| logistic|h1 | 913.25 | -8.68% | 61 | 28 | 17 |
| logistic|h4 | 1006.80 | +0.68% | 120 | 56 | 14 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 17 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 14 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 17 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 14 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 16 |
| recent_base_rate_7d|h4 | 992.28 | -0.77% | 780 | 340 | 13 |
| benchmark_long_all_coins|h1 | 991.68 | -0.83% | 1020 | 432 | 17 |
| benchmark_long_all_coins|h4 | 999.88 | -0.01% | 840 | 380 | 14 |

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
