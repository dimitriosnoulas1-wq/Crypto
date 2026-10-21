# Live monitor (2026-10-21T11:07:10.897764+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.57 (ECE 0.131)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.467
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.496
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.494
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.58 (ECE 0.118)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.444
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.499
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.58 (ECE 0.141)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.438

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['CASHCAT', 'GRASS']
- **last_closed_bar**: 2026-10-21 10:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.1
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 102.9 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.127, 'recent_base_rate_7d': 0.088, 'momentum_24': 0.143, 'logistic': 0.198, 'lgbm_calibrated': 0.147, 'analog_k100': 0.035, 'derivatives': 0.13, 'orthosys': 0.132}
- **council_member_logloss_h1**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.6963, 'momentum_24': 0.6924, 'logistic': 0.6898, 'lgbm_calibrated': 0.6922, 'analog_k100': 0.7053, 'derivatives': 0.6934, 'orthosys': 0.693}
- **council_calls_h1**: 6
- **council_abstain_h1**: {'no_edge': 50, 'spoke': 6, 'extreme_volatility': 4}
- **council_weights_h4**: {'base_rate': 0.198, 'recent_base_rate_7d': 0.007, 'momentum_24': 0.198, 'logistic': 0.181, 'lgbm_calibrated': 0.038, 'analog_k100': 0.003, 'derivatives': 0.198, 'orthosys': 0.177}
- **council_member_logloss_h4**: {'base_rate': 0.6925, 'recent_base_rate_7d': 0.7211, 'momentum_24': 0.6925, 'logistic': 0.6933, 'lgbm_calibrated': 0.7066, 'analog_k100': 0.7321, 'derivatives': 0.6922, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 54, 'extreme_volatility': 4, 'members_disagree': 2}
- **prediction_latency_min**: 7.0
- **price_snapshot_age_s**: 0.4
- **train_rows_h1**: 91395
- **orthosys_hist_hit_h1**: 0.5293
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0083
- **p_spread_logistic_h1**: 0.0245
- **p_spread_lgbm_calibrated_h1**: 0.0279
- **p_spread_analog_k100_h1**: 0.057
- **p_spread_derivatives_h1**: 0.0122
- **p_spread_orthosys_h1**: 0.0066
- **p_spread_council_h1**: 0.0076
- **train_rows_h4**: 91209
- **orthosys_hist_hit_h4**: 0.5121
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0002
- **p_spread_logistic_h4**: 0.0577
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0726
- **p_spread_derivatives_h4**: 0.0353
- **p_spread_orthosys_h4**: 0.0027
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 45600

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 2280 | 38 | 2280 | 0.500 | 0.48-0.52 | 0.525 | 0.465 | -0.0245 | 0.066 | 0.52 | -15.1 |
| analog_k100|h1|on_time | 2280 | 38 | 2280 | 0.500 | 0.48-0.52 | 0.525 | 0.465 | -0.0245 | 0.066 | 0.52 | -15.1 |
| analog_k100|h4|all | 2100 | 35 | 2100 | 0.446 | 0.42-0.47 | 0.573 | 0.451 | -0.0783 | 0.131 | 0.64 | -38.6 |
| analog_k100|h4|on_time | 2100 | 35 | 2100 | 0.446 | 0.42-0.47 | 0.573 | 0.451 | -0.0783 | 0.131 | 0.64 | -38.6 |
| base_rate|h1|all | 2580 | 43 | 2580 | 0.477 | 0.46-0.50 | 0.523 | 0.498 | +0.0000 | 0.025 | 0.00 | - |
| base_rate|h1|on_time | 2520 | 42 | 2520 | 0.480 | 0.46-0.50 | 0.520 | 0.498 | +0.0000 | 0.022 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 2400 | 40 | 2400 | 0.575 | 0.56-0.60 | 0.575 | 0.503 | +0.0000 | 0.072 | 0.00 | - |
| base_rate|h4|on_time | 2400 | 40 | 2400 | 0.575 | 0.56-0.60 | 0.575 | 0.503 | +0.0000 | 0.072 | 0.00 | - |
| council|h1|all | 2280 | 38 | 406 | 0.549 | 0.50-0.60 | 0.525 | 0.495 | +0.0023 | 0.039 | 0.00 | +18.3 |
| council|h1|on_time | 2280 | 38 | 406 | 0.549 | 0.50-0.60 | 0.525 | 0.495 | +0.0023 | 0.039 | 0.00 | +18.3 |
| council|h4|all | 2100 | 35 | 21 | 0.571 | 0.37-0.76 | 0.573 | 0.500 | -0.0013 | 0.074 | 0.00 | - |
| council|h4|on_time | 2100 | 35 | 21 | 0.571 | 0.37-0.76 | 0.573 | 0.500 | -0.0013 | 0.074 | 0.00 | - |
| derivatives|h1|all | 2280 | 38 | 2280 | 0.473 | 0.45-0.49 | 0.525 | 0.498 | +0.0002 | 0.029 | 0.00 | +74.6 |
| derivatives|h1|on_time | 2280 | 38 | 2280 | 0.473 | 0.45-0.49 | 0.525 | 0.498 | +0.0002 | 0.029 | 0.00 | +74.6 |
| derivatives|h4|all | 2100 | 35 | 2100 | 0.573 | 0.55-0.59 | 0.573 | 0.502 | +0.0008 | 0.072 | 0.00 | +70.9 |
| derivatives|h4|on_time | 2100 | 35 | 2100 | 0.573 | 0.55-0.59 | 0.573 | 0.502 | +0.0008 | 0.072 | 0.00 | +70.9 |
| lgbm_calibrated|h1|all | 2580 | 43 | 2580 | 0.534 | 0.52-0.55 | 0.523 | 0.473 | +0.0002 | 0.051 | 0.15 | +3.3 |
| lgbm_calibrated|h1|on_time | 2520 | 42 | 2520 | 0.539 | 0.52-0.56 | 0.520 | 0.473 | +0.0010 | 0.047 | 0.16 | +3.3 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 2400 | 40 | 2400 | 0.424 | 0.40-0.44 | 0.575 | 0.460 | -0.0289 | 0.118 | 0.20 | -50.2 |
| lgbm_calibrated|h4|on_time | 2400 | 40 | 2400 | 0.424 | 0.40-0.44 | 0.575 | 0.460 | -0.0289 | 0.118 | 0.20 | -50.2 |
| logistic|h1|all | 2580 | 43 | 2580 | 0.535 | 0.52-0.55 | 0.523 | 0.490 | +0.0070 | 0.036 | 0.09 | -6.4 |
| logistic|h1|on_time | 2520 | 42 | 2520 | 0.529 | 0.51-0.55 | 0.520 | 0.489 | +0.0058 | 0.033 | 0.09 | -6.2 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 2400 | 40 | 2400 | 0.521 | 0.50-0.54 | 0.575 | 0.496 | -0.0010 | 0.079 | 0.20 | -1.6 |
| logistic|h4|on_time | 2400 | 40 | 2400 | 0.521 | 0.50-0.54 | 0.575 | 0.496 | -0.0010 | 0.079 | 0.20 | -1.6 |
| momentum_24|h1|all | 2580 | 43 | 2580 | 0.527 | 0.51-0.55 | 0.523 | 0.496 | +0.0018 | 0.027 | 0.00 | - |
| momentum_24|h1|on_time | 2520 | 42 | 2520 | 0.523 | 0.50-0.54 | 0.520 | 0.496 | +0.0015 | 0.024 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 2400 | 40 | 2400 | 0.575 | 0.56-0.60 | 0.575 | 0.503 | -0.0000 | 0.072 | 0.00 | - |
| momentum_24|h4|on_time | 2400 | 40 | 2400 | 0.575 | 0.56-0.60 | 0.575 | 0.503 | -0.0000 | 0.072 | 0.00 | - |
| orthosys|h1|all | 2580 | 43 | 190 | 0.537 | 0.47-0.61 | 0.523 | 0.499 | +0.0008 | 0.027 | 0.00 | - |
| orthosys|h1|on_time | 2520 | 42 | 189 | 0.534 | 0.46-0.60 | 0.520 | 0.499 | +0.0007 | 0.023 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 2400 | 40 | 187 | 0.439 | 0.37-0.51 | 0.575 | 0.499 | -0.0021 | 0.076 | 0.00 | - |
| orthosys|h4|on_time | 2400 | 40 | 187 | 0.439 | 0.37-0.51 | 0.575 | 0.499 | -0.0021 | 0.076 | 0.00 | - |
| recent_base_rate_7d|h1|all | 2520 | 42 | 2520 | 0.480 | 0.46-0.50 | 0.520 | 0.474 | -0.0067 | 0.047 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 2520 | 42 | 2520 | 0.480 | 0.46-0.50 | 0.520 | 0.474 | -0.0067 | 0.047 | 0.00 | - |
| recent_base_rate_7d|h4|all | 2340 | 39 | 2340 | 0.418 | 0.40-0.44 | 0.582 | 0.442 | -0.0583 | 0.141 | 0.87 | -69.8 |
| recent_base_rate_7d|h4|on_time | 2340 | 39 | 2340 | 0.418 | 0.40-0.44 | 0.582 | 0.442 | -0.0583 | 0.141 | 0.87 | -69.8 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 942.33 | -5.77% | 1195 | 465 | 38 |
| analog_k100|h4 | 970.67 | -2.93% | 1336 | 531 | 35 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 43 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 40 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 38 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 35 |
| derivatives|h1 | 1014.98 | +1.50% | 2 | 2 | 38 |
| derivatives|h4 | 1014.05 | +1.40% | 8 | 4 | 35 |
| lgbm_calibrated|h1 | 949.71 | -5.03% | 392 | 187 | 43 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 40 |
| logistic|h1 | 943.71 | -5.63% | 242 | 132 | 43 |
| logistic|h4 | 1025.49 | +2.55% | 472 | 234 | 40 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 43 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 40 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 43 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 40 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 42 |
| recent_base_rate_7d|h4 | 942.21 | -5.78% | 2040 | 763 | 39 |
| benchmark_long_all_coins|h1 | 1019.22 | +1.92% | 2580 | 1220 | 43 |
| benchmark_long_all_coins|h4 | 1044.59 | +4.46% | 2400 | 1296 | 40 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 39 |

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
