# Live monitor (2026-10-21T09:06:35.112180+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0013 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.56 (ECE 0.131)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.468
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.498
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.57 (ECE 0.111)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.452
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.58 (ECE 0.134)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.445

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['CAP', 'GRASS']
- **last_closed_bar**: 2026-10-21 08:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.5
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 108.8 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.133, 'recent_base_rate_7d': 0.087, 'momentum_24': 0.15, 'logistic': 0.191, 'lgbm_calibrated': 0.129, 'analog_k100': 0.033, 'derivatives': 0.137, 'orthosys': 0.141}
- **council_member_logloss_h1**: {'base_rate': 0.6935, 'recent_base_rate_7d': 0.6972, 'momentum_24': 0.6925, 'logistic': 0.6905, 'lgbm_calibrated': 0.6938, 'analog_k100': 0.7071, 'derivatives': 0.6935, 'orthosys': 0.693}
- **council_calls_h1**: 1
- **council_abstain_h1**: {'no_edge': 55, 'extreme_volatility': 4, 'spoke': 1}
- **council_weights_h4**: {'base_rate': 0.202, 'recent_base_rate_7d': 0.011, 'momentum_24': 0.202, 'logistic': 0.158, 'lgbm_calibrated': 0.045, 'analog_k100': 0.004, 'derivatives': 0.196, 'orthosys': 0.183}
- **council_member_logloss_h4**: {'base_rate': 0.6926, 'recent_base_rate_7d': 0.7196, 'momentum_24': 0.6926, 'logistic': 0.6948, 'lgbm_calibrated': 0.7061, 'analog_k100': 0.732, 'derivatives': 0.6926, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 55, 'extreme_volatility': 4, 'members_disagree': 1}
- **prediction_latency_min**: 6.5
- **price_snapshot_age_s**: 0.3
- **train_rows_h1**: 91277
- **orthosys_hist_hit_h1**: 0.5285
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0078
- **p_spread_logistic_h1**: 0.0234
- **p_spread_lgbm_calibrated_h1**: 0.026
- **p_spread_analog_k100_h1**: 0.0579
- **p_spread_derivatives_h1**: 0.0049
- **p_spread_orthosys_h1**: 0.0037
- **p_spread_council_h1**: 0.0027
- **train_rows_h4**: 91091
- **orthosys_hist_hit_h4**: 0.5142
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0002
- **p_spread_logistic_h4**: 0.0562
- **p_spread_lgbm_calibrated_h4**: 0.0013
- **p_spread_analog_k100_h4**: 0.0711
- **p_spread_derivatives_h4**: 0.0317
- **p_spread_orthosys_h4**: 0.0018
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 43440

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 2160 | 36 | 2160 | 0.500 | 0.48-0.52 | 0.521 | 0.464 | -0.0241 | 0.062 | 0.53 | -14.5 |
| analog_k100|h1|on_time | 2160 | 36 | 2160 | 0.500 | 0.48-0.52 | 0.521 | 0.464 | -0.0241 | 0.062 | 0.53 | -14.5 |
| analog_k100|h4|all | 1980 | 33 | 1980 | 0.446 | 0.42-0.47 | 0.565 | 0.451 | -0.0756 | 0.131 | 0.64 | -40.6 |
| analog_k100|h4|on_time | 1980 | 33 | 1980 | 0.446 | 0.42-0.47 | 0.565 | 0.451 | -0.0756 | 0.131 | 0.64 | -40.6 |
| base_rate|h1|all | 2460 | 41 | 2460 | 0.480 | 0.46-0.50 | 0.520 | 0.498 | +0.0000 | 0.022 | 0.00 | - |
| base_rate|h1|on_time | 2400 | 40 | 2400 | 0.484 | 0.46-0.50 | 0.516 | 0.498 | +0.0000 | 0.018 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 2280 | 38 | 2280 | 0.568 | 0.55-0.59 | 0.568 | 0.503 | +0.0000 | 0.065 | 0.00 | - |
| base_rate|h4|on_time | 2280 | 38 | 2280 | 0.568 | 0.55-0.59 | 0.568 | 0.503 | +0.0000 | 0.065 | 0.00 | - |
| council|h1|all | 2160 | 36 | 396 | 0.548 | 0.50-0.60 | 0.521 | 0.495 | +0.0022 | 0.034 | 0.00 | +18.3 |
| council|h1|on_time | 2160 | 36 | 396 | 0.548 | 0.50-0.60 | 0.521 | 0.495 | +0.0022 | 0.034 | 0.00 | +18.3 |
| council|h4|all | 1980 | 33 | 21 | 0.571 | 0.37-0.76 | 0.565 | 0.500 | -0.0010 | 0.065 | 0.00 | - |
| council|h4|on_time | 1980 | 33 | 21 | 0.571 | 0.37-0.76 | 0.565 | 0.500 | -0.0010 | 0.065 | 0.00 | - |
| derivatives|h1|all | 2160 | 36 | 2160 | 0.477 | 0.46-0.50 | 0.521 | 0.498 | +0.0001 | 0.025 | 0.00 | +57.8 |
| derivatives|h1|on_time | 2160 | 36 | 2160 | 0.477 | 0.46-0.50 | 0.521 | 0.498 | +0.0001 | 0.025 | 0.00 | +57.8 |
| derivatives|h4|all | 1980 | 33 | 1980 | 0.565 | 0.54-0.59 | 0.565 | 0.502 | +0.0003 | 0.063 | 0.00 | +0.8 |
| derivatives|h4|on_time | 1980 | 33 | 1980 | 0.565 | 0.54-0.59 | 0.565 | 0.502 | +0.0003 | 0.063 | 0.00 | +0.8 |
| lgbm_calibrated|h1|all | 2460 | 41 | 2460 | 0.541 | 0.52-0.56 | 0.520 | 0.473 | +0.0026 | 0.047 | 0.15 | +6.3 |
| lgbm_calibrated|h1|on_time | 2400 | 40 | 2400 | 0.546 | 0.53-0.57 | 0.516 | 0.473 | +0.0036 | 0.043 | 0.15 | +6.3 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 2280 | 38 | 2280 | 0.432 | 0.41-0.45 | 0.568 | 0.459 | -0.0277 | 0.111 | 0.22 | -50.2 |
| lgbm_calibrated|h4|on_time | 2280 | 38 | 2280 | 0.432 | 0.41-0.45 | 0.568 | 0.459 | -0.0277 | 0.111 | 0.22 | -50.2 |
| logistic|h1|all | 2460 | 41 | 2460 | 0.539 | 0.52-0.56 | 0.520 | 0.490 | +0.0077 | 0.032 | 0.10 | +7.5 |
| logistic|h1|on_time | 2400 | 40 | 2400 | 0.533 | 0.51-0.55 | 0.516 | 0.489 | +0.0065 | 0.030 | 0.10 | +7.8 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 2280 | 38 | 2280 | 0.515 | 0.49-0.54 | 0.568 | 0.496 | -0.0025 | 0.072 | 0.20 | +2.6 |
| logistic|h4|on_time | 2280 | 38 | 2280 | 0.515 | 0.49-0.54 | 0.568 | 0.496 | -0.0025 | 0.072 | 0.20 | +2.6 |
| momentum_24|h1|all | 2460 | 41 | 2460 | 0.534 | 0.51-0.55 | 0.520 | 0.496 | +0.0023 | 0.024 | 0.00 | - |
| momentum_24|h1|on_time | 2400 | 40 | 2400 | 0.530 | 0.51-0.55 | 0.516 | 0.496 | +0.0020 | 0.020 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 2280 | 38 | 2280 | 0.568 | 0.55-0.59 | 0.568 | 0.503 | -0.0000 | 0.065 | 0.00 | - |
| momentum_24|h4|on_time | 2280 | 38 | 2280 | 0.568 | 0.55-0.59 | 0.568 | 0.503 | -0.0000 | 0.065 | 0.00 | - |
| orthosys|h1|all | 2460 | 41 | 188 | 0.537 | 0.47-0.61 | 0.520 | 0.498 | +0.0008 | 0.023 | 0.00 | - |
| orthosys|h1|on_time | 2400 | 40 | 187 | 0.535 | 0.46-0.60 | 0.516 | 0.498 | +0.0007 | 0.020 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 2280 | 38 | 185 | 0.443 | 0.37-0.52 | 0.568 | 0.499 | -0.0018 | 0.069 | 0.00 | - |
| orthosys|h4|on_time | 2280 | 38 | 185 | 0.443 | 0.37-0.52 | 0.568 | 0.499 | -0.0018 | 0.069 | 0.00 | - |
| recent_base_rate_7d|h1|all | 2400 | 40 | 2400 | 0.484 | 0.46-0.50 | 0.516 | 0.474 | -0.0061 | 0.043 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 2400 | 40 | 2400 | 0.484 | 0.46-0.50 | 0.516 | 0.474 | -0.0061 | 0.043 | 0.00 | - |
| recent_base_rate_7d|h4|all | 2220 | 37 | 2220 | 0.425 | 0.40-0.45 | 0.575 | 0.442 | -0.0552 | 0.134 | 0.86 | -69.7 |
| recent_base_rate_7d|h4|on_time | 2220 | 37 | 2220 | 0.425 | 0.40-0.45 | 0.575 | 0.442 | -0.0552 | 0.134 | 0.86 | -69.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 947.23 | -5.28% | 1140 | 449 | 36 |
| analog_k100|h4 | 970.91 | -2.91% | 1261 | 506 | 33 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 41 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 38 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 36 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 33 |
| derivatives|h1 | 1005.78 | +0.58% | 1 | 1 | 36 |
| derivatives|h4 | 999.94 | -0.01% | 6 | 2 | 33 |
| lgbm_calibrated|h1 | 952.95 | -4.71% | 362 | 183 | 41 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 38 |
| logistic|h1 | 1066.86 | +6.69% | 235 | 129 | 41 |
| logistic|h4 | 1030.51 | +3.05% | 454 | 222 | 38 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 41 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 38 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 41 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 38 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 40 |
| recent_base_rate_7d|h4 | 945.58 | -5.44% | 1920 | 730 | 37 |
| benchmark_long_all_coins|h1 | 1014.64 | +1.46% | 2460 | 1158 | 41 |
| benchmark_long_all_coins|h4 | 1041.92 | +4.19% | 2280 | 1211 | 38 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 37 |

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
