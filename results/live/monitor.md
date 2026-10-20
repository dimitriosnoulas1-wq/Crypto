# Live monitor (2026-10-20T19:08:23.585237+00:00)

## Alerts

- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.497
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.55 (ECE 0.098)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.472

## Health

- **venue**: okx
- **symbols**: 63
- **universe_size**: 60
- **fetched_only_for_scoring**: ['A', 'S', 'WLFI']
- **last_closed_bar**: 2026-10-20 18:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 6.3
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 107.6 instruments 63/63']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.128, 'recent_base_rate_7d': 0.091, 'momentum_24': 0.146, 'logistic': 0.164, 'lgbm_calibrated': 0.152, 'analog_k100': 0.059, 'derivatives': 0.131, 'orthosys': 0.128}
- **council_member_logloss_h1**: {'base_rate': 0.6936, 'recent_base_rate_7d': 0.6981, 'momentum_24': 0.6919, 'logistic': 0.6904, 'lgbm_calibrated': 0.6914, 'analog_k100': 0.7063, 'derivatives': 0.6937, 'orthosys': 0.6936}
- **council_calls_h1**: 2
- **council_abstain_h1**: {'no_edge': 55, 'extreme_volatility': 3, 'spoke': 2}
- **council_weights_h4**: {'base_rate': 0.17, 'recent_base_rate_7d': 0.02, 'momentum_24': 0.171, 'logistic': 0.227, 'lgbm_calibrated': 0.068, 'analog_k100': 0.015, 'derivatives': 0.163, 'orthosys': 0.167}
- **council_member_logloss_h4**: {'base_rate': 0.6928, 'recent_base_rate_7d': 0.7254, 'momentum_24': 0.6927, 'logistic': 0.6886, 'lgbm_calibrated': 0.7061, 'analog_k100': 0.7377, 'derivatives': 0.6931, 'orthosys': 0.693}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 47, 'members_disagree': 10, 'extreme_volatility': 3}
- **prediction_latency_min**: 8.3
- **price_snapshot_age_s**: 0.6
- **train_rows_h1**: 92361
- **orthosys_hist_hit_h1**: 0.5265
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0064
- **p_spread_logistic_h1**: 0.0229
- **p_spread_lgbm_calibrated_h1**: 0.0122
- **p_spread_analog_k100_h1**: 0.0593
- **p_spread_derivatives_h1**: 0.0014
- **p_spread_orthosys_h1**: 0.01
- **p_spread_council_h1**: 0.0046
- **train_rows_h4**: 92172
- **orthosys_hist_hit_h4**: 0.515
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0006
- **p_spread_logistic_h4**: 0.0496
- **p_spread_lgbm_calibrated_h4**: 0.0046
- **p_spread_analog_k100_h4**: 0.076
- **p_spread_derivatives_h4**: 0.0049
- **p_spread_orthosys_h4**: 0.0056
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 28320

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1320 | 22 | 1320 | 0.502 | 0.47-0.53 | 0.532 | 0.471 | -0.0184 | 0.065 | 0.50 | -10.1 |
| analog_k100|h1|on_time | 1320 | 22 | 1320 | 0.502 | 0.47-0.53 | 0.532 | 0.471 | -0.0184 | 0.065 | 0.50 | -10.1 |
| analog_k100|h4|all | 1140 | 19 | 1140 | 0.458 | 0.43-0.49 | 0.544 | 0.446 | -0.0745 | 0.121 | 0.63 | -58.7 |
| analog_k100|h4|on_time | 1140 | 19 | 1140 | 0.458 | 0.43-0.49 | 0.544 | 0.446 | -0.0745 | 0.121 | 0.63 | -58.7 |
| base_rate|h1|all | 1620 | 27 | 1620 | 0.473 | 0.45-0.50 | 0.527 | 0.498 | +0.0000 | 0.029 | 0.00 | - |
| base_rate|h1|on_time | 1560 | 26 | 1560 | 0.478 | 0.45-0.50 | 0.522 | 0.498 | +0.0000 | 0.024 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 1440 | 24 | 1440 | 0.553 | 0.53-0.58 | 0.553 | 0.503 | +0.0000 | 0.050 | 0.00 | - |
| base_rate|h4|on_time | 1440 | 24 | 1440 | 0.553 | 0.53-0.58 | 0.553 | 0.503 | +0.0000 | 0.050 | 0.00 | - |
| council|h1|all | 1320 | 22 | 243 | 0.535 | 0.47-0.60 | 0.532 | 0.495 | +0.0025 | 0.040 | 0.00 | +64.4 |
| council|h1|on_time | 1320 | 22 | 243 | 0.535 | 0.47-0.60 | 0.532 | 0.495 | +0.0025 | 0.040 | 0.00 | +64.4 |
| council|h4|all | 1140 | 19 | 18 | 0.556 | 0.34-0.75 | 0.544 | 0.500 | +0.0000 | 0.045 | 0.00 | - |
| council|h4|on_time | 1140 | 19 | 18 | 0.556 | 0.34-0.75 | 0.544 | 0.500 | +0.0000 | 0.045 | 0.00 | - |
| derivatives|h1|all | 1320 | 22 | 1320 | 0.465 | 0.44-0.49 | 0.532 | 0.498 | -0.0001 | 0.037 | 0.00 | - |
| derivatives|h1|on_time | 1320 | 22 | 1320 | 0.465 | 0.44-0.49 | 0.532 | 0.498 | -0.0001 | 0.037 | 0.00 | - |
| derivatives|h4|all | 1140 | 19 | 1140 | 0.542 | 0.51-0.57 | 0.544 | 0.502 | -0.0002 | 0.042 | 0.00 | -117.6 |
| derivatives|h4|on_time | 1140 | 19 | 1140 | 0.542 | 0.51-0.57 | 0.544 | 0.502 | -0.0002 | 0.042 | 0.00 | -117.6 |
| lgbm_calibrated|h1|all | 1620 | 27 | 1620 | 0.565 | 0.54-0.59 | 0.527 | 0.478 | +0.0060 | 0.054 | 0.09 | +33.6 |
| lgbm_calibrated|h1|on_time | 1560 | 26 | 1560 | 0.573 | 0.55-0.60 | 0.522 | 0.478 | +0.0077 | 0.049 | 0.10 | +33.6 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 1440 | 24 | 1440 | 0.446 | 0.42-0.47 | 0.553 | 0.459 | -0.0163 | 0.098 | 0.15 | -1.8 |
| lgbm_calibrated|h4|on_time | 1440 | 24 | 1440 | 0.446 | 0.42-0.47 | 0.553 | 0.459 | -0.0163 | 0.098 | 0.15 | -1.8 |
| logistic|h1|all | 1620 | 27 | 1620 | 0.534 | 0.51-0.56 | 0.527 | 0.490 | +0.0070 | 0.041 | 0.12 | -6.9 |
| logistic|h1|on_time | 1560 | 26 | 1560 | 0.524 | 0.50-0.55 | 0.522 | 0.489 | +0.0051 | 0.038 | 0.12 | -6.7 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 1440 | 24 | 1440 | 0.550 | 0.52-0.58 | 0.553 | 0.495 | +0.0134 | 0.060 | 0.17 | +44.0 |
| logistic|h4|on_time | 1440 | 24 | 1440 | 0.550 | 0.52-0.58 | 0.553 | 0.495 | +0.0134 | 0.060 | 0.17 | +44.0 |
| momentum_24|h1|all | 1620 | 27 | 1620 | 0.557 | 0.53-0.58 | 0.527 | 0.498 | +0.0042 | 0.047 | 0.00 | - |
| momentum_24|h1|on_time | 1560 | 26 | 1560 | 0.552 | 0.53-0.58 | 0.522 | 0.498 | +0.0038 | 0.042 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 1440 | 24 | 1440 | 0.553 | 0.53-0.58 | 0.553 | 0.503 | +0.0003 | 0.051 | 0.00 | - |
| momentum_24|h4|on_time | 1440 | 24 | 1440 | 0.553 | 0.53-0.58 | 0.553 | 0.503 | +0.0003 | 0.051 | 0.00 | - |
| orthosys|h1|all | 1620 | 27 | 163 | 0.552 | 0.48-0.63 | 0.527 | 0.498 | +0.0014 | 0.033 | 0.00 | - |
| orthosys|h1|on_time | 1560 | 26 | 162 | 0.549 | 0.47-0.62 | 0.522 | 0.498 | +0.0013 | 0.028 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 1440 | 24 | 87 | 0.609 | 0.50-0.71 | 0.553 | 0.499 | +0.0004 | 0.065 | 0.00 | - |
| orthosys|h4|on_time | 1440 | 24 | 87 | 0.609 | 0.50-0.71 | 0.553 | 0.499 | +0.0004 | 0.065 | 0.00 | - |
| recent_base_rate_7d|h1|all | 1560 | 26 | 1560 | 0.478 | 0.45-0.50 | 0.522 | 0.472 | -0.0072 | 0.050 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 1560 | 26 | 1560 | 0.478 | 0.45-0.50 | 0.522 | 0.472 | -0.0072 | 0.050 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1380 | 23 | 1380 | 0.436 | 0.41-0.46 | 0.564 | 0.437 | -0.0569 | 0.127 | 1.00 | -69.2 |
| recent_base_rate_7d|h4|on_time | 1380 | 23 | 1380 | 0.436 | 0.41-0.46 | 0.564 | 0.437 | -0.0569 | 0.127 | 1.00 | -69.2 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 973.79 | -2.62% | 656 | 259 | 22 |
| analog_k100|h4 | 974.94 | -2.51% | 715 | 290 | 19 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 27 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 24 |
| council|h1 | 1006.44 | +0.64% | 3 | 2 | 22 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 19 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 22 |
| derivatives|h4 | 985.33 | -1.47% | 5 | 1 | 19 |
| lgbm_calibrated|h1 | 951.51 | -4.85% | 150 | 81 | 27 |
| lgbm_calibrated|h4 | 926.57 | -7.34% | 219 | 127 | 24 |
| logistic|h1 | 953.42 | -4.66% | 196 | 101 | 27 |
| logistic|h4 | 1039.59 | +3.96% | 244 | 143 | 24 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 27 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 24 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 27 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 24 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 26 |
| recent_base_rate_7d|h4 | 960.86 | -3.91% | 1380 | 548 | 23 |
| benchmark_long_all_coins|h1 | 1004.81 | +0.48% | 1620 | 756 | 27 |
| benchmark_long_all_coins|h4 | 1027.18 | +2.72% | 1440 | 740 | 24 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 19 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 19 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 19 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 23 |

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
