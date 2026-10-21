# Live monitor (2026-10-21T10:08:18.763900+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.57 (ECE 0.131)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.467
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.499
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.57 (ECE 0.115)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.447
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.58 (ECE 0.138)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.441

## Health

- **venue**: okx
- **symbols**: 63
- **universe_size**: 60
- **fetched_only_for_scoring**: ['CAP', 'CASHCAT', 'GRASS']
- **last_closed_bar**: 2026-10-21 09:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 6.3
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 104.1 instruments 63/63']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.125, 'recent_base_rate_7d': 0.087, 'momentum_24': 0.144, 'logistic': 0.202, 'lgbm_calibrated': 0.147, 'analog_k100': 0.034, 'derivatives': 0.129, 'orthosys': 0.131}
- **council_member_logloss_h1**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.6964, 'momentum_24': 0.6922, 'logistic': 0.6895, 'lgbm_calibrated': 0.692, 'analog_k100': 0.7058, 'derivatives': 0.6933, 'orthosys': 0.693}
- **council_calls_h1**: 9
- **council_abstain_h1**: {'no_edge': 47, 'spoke': 9, 'extreme_volatility': 4}
- **council_weights_h4**: {'base_rate': 0.199, 'recent_base_rate_7d': 0.009, 'momentum_24': 0.199, 'logistic': 0.171, 'lgbm_calibrated': 0.041, 'analog_k100': 0.004, 'derivatives': 0.197, 'orthosys': 0.18}
- **council_member_logloss_h4**: {'base_rate': 0.6925, 'recent_base_rate_7d': 0.7201, 'momentum_24': 0.6925, 'logistic': 0.6939, 'lgbm_calibrated': 0.7063, 'analog_k100': 0.7318, 'derivatives': 0.6924, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 55, 'extreme_volatility': 4, 'members_disagree': 1}
- **prediction_latency_min**: 8.2
- **price_snapshot_age_s**: 0.4
- **train_rows_h1**: 92873
- **orthosys_hist_hit_h1**: 0.5289
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0076
- **p_spread_logistic_h1**: 0.0269
- **p_spread_lgbm_calibrated_h1**: 0.0092
- **p_spread_analog_k100_h1**: 0.0589
- **p_spread_derivatives_h1**: 0.0108
- **p_spread_orthosys_h1**: 0.0037
- **p_spread_council_h1**: 0.0095
- **train_rows_h4**: 92684
- **orthosys_hist_hit_h4**: 0.5124
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0002
- **p_spread_logistic_h4**: 0.0576
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0705
- **p_spread_derivatives_h4**: 0.027
- **p_spread_orthosys_h4**: 0.0016
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 44520

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 2220 | 37 | 2220 | 0.503 | 0.48-0.52 | 0.521 | 0.465 | -0.0231 | 0.061 | 0.53 | -13.9 |
| analog_k100|h1|on_time | 2220 | 37 | 2220 | 0.503 | 0.48-0.52 | 0.521 | 0.465 | -0.0231 | 0.061 | 0.53 | -13.9 |
| analog_k100|h4|all | 2040 | 34 | 2040 | 0.446 | 0.42-0.47 | 0.570 | 0.451 | -0.0764 | 0.131 | 0.64 | -39.6 |
| analog_k100|h4|on_time | 2040 | 34 | 2040 | 0.446 | 0.42-0.47 | 0.570 | 0.451 | -0.0764 | 0.131 | 0.64 | -39.6 |
| base_rate|h1|all | 2520 | 42 | 2520 | 0.481 | 0.46-0.50 | 0.519 | 0.498 | +0.0000 | 0.021 | 0.00 | - |
| base_rate|h1|on_time | 2460 | 41 | 2460 | 0.484 | 0.46-0.50 | 0.516 | 0.498 | +0.0000 | 0.018 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 2340 | 39 | 2340 | 0.573 | 0.55-0.59 | 0.573 | 0.503 | +0.0000 | 0.069 | 0.00 | - |
| base_rate|h4|on_time | 2340 | 39 | 2340 | 0.573 | 0.55-0.59 | 0.573 | 0.503 | +0.0000 | 0.069 | 0.00 | - |
| council|h1|all | 2220 | 37 | 397 | 0.549 | 0.50-0.60 | 0.521 | 0.495 | +0.0022 | 0.034 | 0.00 | +18.3 |
| council|h1|on_time | 2220 | 37 | 397 | 0.549 | 0.50-0.60 | 0.521 | 0.495 | +0.0022 | 0.034 | 0.00 | +18.3 |
| council|h4|all | 2040 | 34 | 21 | 0.571 | 0.37-0.76 | 0.570 | 0.500 | -0.0012 | 0.071 | 0.00 | - |
| council|h4|on_time | 2040 | 34 | 21 | 0.571 | 0.37-0.76 | 0.570 | 0.500 | -0.0012 | 0.071 | 0.00 | - |
| derivatives|h1|all | 2220 | 37 | 2220 | 0.478 | 0.46-0.50 | 0.521 | 0.498 | +0.0000 | 0.024 | 0.00 | +57.8 |
| derivatives|h1|on_time | 2220 | 37 | 2220 | 0.478 | 0.46-0.50 | 0.521 | 0.498 | +0.0000 | 0.024 | 0.00 | +57.8 |
| derivatives|h4|all | 2040 | 34 | 2040 | 0.570 | 0.55-0.59 | 0.570 | 0.502 | +0.0005 | 0.068 | 0.00 | +35.4 |
| derivatives|h4|on_time | 2040 | 34 | 2040 | 0.570 | 0.55-0.59 | 0.570 | 0.502 | +0.0005 | 0.068 | 0.00 | +35.4 |
| lgbm_calibrated|h1|all | 2520 | 42 | 2520 | 0.540 | 0.52-0.56 | 0.519 | 0.473 | +0.0023 | 0.046 | 0.14 | +6.3 |
| lgbm_calibrated|h1|on_time | 2460 | 41 | 2460 | 0.545 | 0.52-0.56 | 0.516 | 0.474 | +0.0033 | 0.042 | 0.15 | +6.3 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 2340 | 39 | 2340 | 0.427 | 0.41-0.45 | 0.573 | 0.460 | -0.0285 | 0.115 | 0.21 | -50.2 |
| lgbm_calibrated|h4|on_time | 2340 | 39 | 2340 | 0.427 | 0.41-0.45 | 0.573 | 0.460 | -0.0285 | 0.115 | 0.21 | -50.2 |
| logistic|h1|all | 2520 | 42 | 2520 | 0.537 | 0.52-0.56 | 0.519 | 0.490 | +0.0071 | 0.031 | 0.09 | -8.4 |
| logistic|h1|on_time | 2460 | 41 | 2460 | 0.531 | 0.51-0.55 | 0.516 | 0.489 | +0.0058 | 0.029 | 0.10 | -8.3 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 2340 | 39 | 2340 | 0.521 | 0.50-0.54 | 0.573 | 0.496 | -0.0014 | 0.076 | 0.20 | -0.8 |
| logistic|h4|on_time | 2340 | 39 | 2340 | 0.521 | 0.50-0.54 | 0.573 | 0.496 | -0.0014 | 0.076 | 0.20 | -0.8 |
| momentum_24|h1|all | 2520 | 42 | 2520 | 0.530 | 0.51-0.55 | 0.519 | 0.496 | +0.0020 | 0.023 | 0.00 | - |
| momentum_24|h1|on_time | 2460 | 41 | 2460 | 0.526 | 0.51-0.55 | 0.516 | 0.496 | +0.0017 | 0.020 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 2340 | 39 | 2340 | 0.573 | 0.55-0.59 | 0.573 | 0.503 | -0.0000 | 0.069 | 0.00 | - |
| momentum_24|h4|on_time | 2340 | 39 | 2340 | 0.573 | 0.55-0.59 | 0.573 | 0.503 | -0.0000 | 0.069 | 0.00 | - |
| orthosys|h1|all | 2520 | 42 | 189 | 0.534 | 0.46-0.60 | 0.519 | 0.499 | +0.0007 | 0.023 | 0.00 | - |
| orthosys|h1|on_time | 2460 | 41 | 188 | 0.532 | 0.46-0.60 | 0.516 | 0.499 | +0.0006 | 0.019 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 2340 | 39 | 186 | 0.441 | 0.37-0.51 | 0.573 | 0.499 | -0.0020 | 0.074 | 0.00 | - |
| orthosys|h4|on_time | 2340 | 39 | 186 | 0.441 | 0.37-0.51 | 0.573 | 0.499 | -0.0020 | 0.074 | 0.00 | - |
| recent_base_rate_7d|h1|all | 2460 | 41 | 2460 | 0.484 | 0.46-0.50 | 0.516 | 0.474 | -0.0060 | 0.042 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 2460 | 41 | 2460 | 0.484 | 0.46-0.50 | 0.516 | 0.474 | -0.0060 | 0.042 | 0.00 | - |
| recent_base_rate_7d|h4|all | 2280 | 38 | 2280 | 0.420 | 0.40-0.44 | 0.580 | 0.442 | -0.0573 | 0.138 | 0.87 | -69.9 |
| recent_base_rate_7d|h4|on_time | 2280 | 38 | 2280 | 0.420 | 0.40-0.44 | 0.580 | 0.442 | -0.0573 | 0.138 | 0.87 | -69.9 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 948.61 | -5.14% | 1167 | 462 | 37 |
| analog_k100|h4 | 970.84 | -2.92% | 1296 | 518 | 34 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 42 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 39 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 37 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 34 |
| derivatives|h1 | 1005.78 | +0.58% | 1 | 1 | 37 |
| derivatives|h4 | 1006.01 | +0.60% | 7 | 3 | 34 |
| lgbm_calibrated|h1 | 952.95 | -4.71% | 362 | 183 | 42 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 39 |
| logistic|h1 | 932.98 | -6.70% | 238 | 129 | 42 |
| logistic|h4 | 1027.19 | +2.72% | 466 | 229 | 39 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 42 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 39 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 42 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 39 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 41 |
| recent_base_rate_7d|h4 | 943.80 | -5.62% | 1980 | 745 | 38 |
| benchmark_long_all_coins|h1 | 1017.55 | +1.76% | 2520 | 1177 | 42 |
| benchmark_long_all_coins|h4 | 1043.35 | +4.34% | 2340 | 1255 | 39 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 38 |

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
