# Live monitor (2026-10-21T14:08:48.700401+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.57 (ECE 0.126)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.472
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.500
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.500
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.57 (ECE 0.113)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.446
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.58 (ECE 0.137)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.440

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['DASH', 'HBAR']
- **last_closed_bar**: 2026-10-21 13:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 6.5
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 114.8 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.133, 'recent_base_rate_7d': 0.085, 'momentum_24': 0.145, 'logistic': 0.197, 'lgbm_calibrated': 0.133, 'analog_k100': 0.031, 'derivatives': 0.136, 'orthosys': 0.14}
- **council_member_logloss_h1**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.6968, 'momentum_24': 0.6928, 'logistic': 0.6905, 'lgbm_calibrated': 0.6934, 'analog_k100': 0.7058, 'derivatives': 0.6935, 'orthosys': 0.693}
- **council_calls_h1**: 9
- **council_abstain_h1**: {'no_edge': 46, 'spoke': 9, 'extreme_volatility': 5}
- **council_weights_h4**: {'base_rate': 0.201, 'recent_base_rate_7d': 0.006, 'momentum_24': 0.201, 'logistic': 0.179, 'lgbm_calibrated': 0.035, 'analog_k100': 0.002, 'derivatives': 0.2, 'orthosys': 0.176}
- **council_member_logloss_h4**: {'base_rate': 0.6924, 'recent_base_rate_7d': 0.7207, 'momentum_24': 0.6924, 'logistic': 0.6934, 'lgbm_calibrated': 0.7063, 'analog_k100': 0.7321, 'derivatives': 0.6922, 'orthosys': 0.6935}
- **council_calls_h4**: 1
- **council_abstain_h4**: {'no_edge': 51, 'extreme_volatility': 5, 'members_disagree': 3, 'spoke': 1}
- **prediction_latency_min**: 8.7
- **price_snapshot_age_s**: 0.5
- **train_rows_h1**: 91916
- **orthosys_hist_hit_h1**: 0.5306
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0081
- **p_spread_logistic_h1**: 0.0357
- **p_spread_lgbm_calibrated_h1**: 0.013
- **p_spread_analog_k100_h1**: 0.0637
- **p_spread_derivatives_h1**: 0.0125
- **p_spread_orthosys_h1**: 0.0069
- **p_spread_council_h1**: 0.0099
- **train_rows_h4**: 91730
- **orthosys_hist_hit_h4**: 0.5119
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0005
- **p_spread_logistic_h4**: 0.0781
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0728
- **p_spread_derivatives_h4**: 0.0263
- **p_spread_orthosys_h4**: 0.0027
- **p_spread_council_h4**: 0.003
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 48840

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 2460 | 41 | 2460 | 0.503 | 0.48-0.52 | 0.520 | 0.466 | -0.0230 | 0.059 | 0.52 | -8.2 |
| analog_k100|h1|on_time | 2460 | 41 | 2460 | 0.503 | 0.48-0.52 | 0.520 | 0.466 | -0.0230 | 0.059 | 0.52 | -8.2 |
| analog_k100|h4|all | 2280 | 38 | 2280 | 0.451 | 0.43-0.47 | 0.570 | 0.451 | -0.0764 | 0.126 | 0.63 | -28.8 |
| analog_k100|h4|on_time | 2280 | 38 | 2280 | 0.451 | 0.43-0.47 | 0.570 | 0.451 | -0.0764 | 0.126 | 0.63 | -28.8 |
| base_rate|h1|all | 2760 | 46 | 2760 | 0.481 | 0.46-0.50 | 0.519 | 0.498 | +0.0000 | 0.021 | 0.00 | - |
| base_rate|h1|on_time | 2700 | 45 | 2700 | 0.484 | 0.47-0.50 | 0.516 | 0.498 | +0.0000 | 0.018 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 2580 | 43 | 2580 | 0.572 | 0.55-0.59 | 0.572 | 0.503 | +0.0000 | 0.069 | 0.00 | - |
| base_rate|h4|on_time | 2580 | 43 | 2580 | 0.572 | 0.55-0.59 | 0.572 | 0.503 | +0.0000 | 0.069 | 0.00 | - |
| council|h1|all | 2460 | 41 | 425 | 0.546 | 0.50-0.59 | 0.520 | 0.495 | +0.0020 | 0.032 | 0.00 | +18.3 |
| council|h1|on_time | 2460 | 41 | 425 | 0.546 | 0.50-0.59 | 0.520 | 0.495 | +0.0020 | 0.032 | 0.00 | +18.3 |
| council|h4|all | 2280 | 38 | 21 | 0.571 | 0.37-0.76 | 0.570 | 0.500 | -0.0013 | 0.071 | 0.00 | - |
| council|h4|on_time | 2280 | 38 | 21 | 0.571 | 0.37-0.76 | 0.570 | 0.500 | -0.0013 | 0.071 | 0.00 | - |
| derivatives|h1|all | 2460 | 41 | 2460 | 0.480 | 0.46-0.50 | 0.520 | 0.498 | -0.0000 | 0.023 | 0.00 | -99.5 |
| derivatives|h1|on_time | 2460 | 41 | 2460 | 0.480 | 0.46-0.50 | 0.520 | 0.498 | -0.0000 | 0.023 | 0.00 | -99.5 |
| derivatives|h4|all | 2280 | 38 | 2280 | 0.571 | 0.55-0.59 | 0.570 | 0.502 | -0.0000 | 0.068 | 0.01 | -206.9 |
| derivatives|h4|on_time | 2280 | 38 | 2280 | 0.571 | 0.55-0.59 | 0.570 | 0.502 | -0.0000 | 0.068 | 0.01 | -206.9 |
| lgbm_calibrated|h1|all | 2760 | 46 | 2760 | 0.539 | 0.52-0.56 | 0.519 | 0.474 | +0.0009 | 0.045 | 0.15 | +6.6 |
| lgbm_calibrated|h1|on_time | 2700 | 45 | 2700 | 0.543 | 0.52-0.56 | 0.516 | 0.474 | +0.0017 | 0.042 | 0.15 | +6.6 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 2580 | 43 | 2580 | 0.427 | 0.41-0.45 | 0.572 | 0.461 | -0.0275 | 0.113 | 0.19 | -50.2 |
| lgbm_calibrated|h4|on_time | 2580 | 43 | 2580 | 0.427 | 0.41-0.45 | 0.572 | 0.461 | -0.0275 | 0.113 | 0.19 | -50.2 |
| logistic|h1|all | 2760 | 46 | 2760 | 0.534 | 0.52-0.55 | 0.519 | 0.490 | +0.0055 | 0.030 | 0.09 | -28.5 |
| logistic|h1|on_time | 2700 | 45 | 2700 | 0.529 | 0.51-0.55 | 0.516 | 0.489 | +0.0043 | 0.028 | 0.09 | -28.6 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 2580 | 43 | 2580 | 0.524 | 0.50-0.54 | 0.572 | 0.496 | -0.0020 | 0.076 | 0.20 | -31.5 |
| logistic|h4|on_time | 2580 | 43 | 2580 | 0.524 | 0.50-0.54 | 0.572 | 0.496 | -0.0020 | 0.076 | 0.20 | -31.5 |
| momentum_24|h1|all | 2760 | 46 | 2760 | 0.521 | 0.50-0.54 | 0.519 | 0.496 | +0.0013 | 0.023 | 0.00 | - |
| momentum_24|h1|on_time | 2700 | 45 | 2700 | 0.517 | 0.50-0.54 | 0.516 | 0.496 | +0.0010 | 0.020 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 2580 | 43 | 2580 | 0.572 | 0.55-0.59 | 0.572 | 0.503 | -0.0000 | 0.069 | 0.00 | - |
| momentum_24|h4|on_time | 2580 | 43 | 2580 | 0.572 | 0.55-0.59 | 0.572 | 0.503 | -0.0000 | 0.069 | 0.00 | - |
| orthosys|h1|all | 2760 | 46 | 200 | 0.525 | 0.46-0.59 | 0.519 | 0.499 | +0.0005 | 0.021 | 0.00 | - |
| orthosys|h1|on_time | 2700 | 45 | 199 | 0.523 | 0.45-0.59 | 0.516 | 0.499 | +0.0004 | 0.018 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 2580 | 43 | 190 | 0.432 | 0.36-0.50 | 0.572 | 0.499 | -0.0021 | 0.073 | 0.00 | - |
| orthosys|h4|on_time | 2580 | 43 | 190 | 0.432 | 0.36-0.50 | 0.572 | 0.499 | -0.0021 | 0.073 | 0.00 | - |
| recent_base_rate_7d|h1|all | 2700 | 45 | 2700 | 0.484 | 0.47-0.50 | 0.516 | 0.474 | -0.0059 | 0.042 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 2700 | 45 | 2700 | 0.484 | 0.47-0.50 | 0.516 | 0.474 | -0.0059 | 0.042 | 0.00 | - |
| recent_base_rate_7d|h4|all | 2520 | 42 | 2520 | 0.421 | 0.40-0.44 | 0.579 | 0.442 | -0.0557 | 0.137 | 0.83 | -68.7 |
| recent_base_rate_7d|h4|on_time | 2520 | 42 | 2520 | 0.421 | 0.40-0.44 | 0.579 | 0.442 | -0.0557 | 0.137 | 0.83 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 969.98 | -3.00% | 1271 | 511 | 41 |
| analog_k100|h4 | 978.49 | -2.15% | 1438 | 569 | 38 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 46 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 43 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 41 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 38 |
| derivatives|h1 | 960.09 | -3.99% | 4 | 2 | 41 |
| derivatives|h4 | 970.47 | -2.95% | 12 | 4 | 38 |
| lgbm_calibrated|h1 | 959.55 | -4.05% | 408 | 197 | 46 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 43 |
| logistic|h1 | 838.49 | -16.15% | 257 | 138 | 46 |
| logistic|h4 | 992.09 | -0.79% | 510 | 250 | 43 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 46 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 43 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 46 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 43 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 45 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 42 |
| benchmark_long_all_coins|h1 | 1012.24 | +1.22% | 2760 | 1277 | 46 |
| benchmark_long_all_coins|h4 | 1049.58 | +4.96% | 2580 | 1404 | 43 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 42 |

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
