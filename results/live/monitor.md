# Live monitor (2026-10-21T00:06:14.992509+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h4|all says 0.44 on average, reality 0.58 (ECE 0.152)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.453
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.490
- MISCALIBRATED: base_rate|h4|all says 0.50 on average, reality 0.59 (ECE 0.082)
- MISCALIBRATED: council|h4|all says 0.50 on average, reality 0.58 (ECE 0.085)
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.485
- MISCALIBRATED: derivatives|h4|all says 0.50 on average, reality 0.58 (ECE 0.082)
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.59 (ECE 0.131)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.438
- MISCALIBRATED: logistic|h4|all says 0.49 on average, reality 0.59 (ECE 0.094)
- MISCALIBRATED: momentum_24|h4|all says 0.50 on average, reality 0.59 (ECE 0.082)
- MISCALIBRATED: orthosys|h4|all says 0.50 on average, reality 0.59 (ECE 0.086)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.494
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.60 (ECE 0.156)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.428

## Health

- **venue**: okx
- **symbols**: 61
- **universe_size**: 60
- **fetched_only_for_scoring**: ['GRASS']
- **last_closed_bar**: 2026-10-20 23:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.3
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 102.6 instruments 61/61']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.129, 'recent_base_rate_7d': 0.085, 'momentum_24': 0.147, 'logistic': 0.18, 'lgbm_calibrated': 0.137, 'analog_k100': 0.051, 'derivatives': 0.133, 'orthosys': 0.138}
- **council_member_logloss_h1**: {'base_rate': 0.6936, 'recent_base_rate_7d': 0.6982, 'momentum_24': 0.6922, 'logistic': 0.69, 'lgbm_calibrated': 0.693, 'analog_k100': 0.706, 'derivatives': 0.6937, 'orthosys': 0.6929}
- **council_calls_h1**: 5
- **council_abstain_h1**: {'no_edge': 54, 'spoke': 5, 'extreme_volatility': 1}
- **council_weights_h4**: {'base_rate': 0.196, 'recent_base_rate_7d': 0.014, 'momentum_24': 0.196, 'logistic': 0.166, 'lgbm_calibrated': 0.053, 'analog_k100': 0.006, 'derivatives': 0.19, 'orthosys': 0.178}
- **council_member_logloss_h4**: {'base_rate': 0.6925, 'recent_base_rate_7d': 0.7246, 'momentum_24': 0.6925, 'logistic': 0.6945, 'lgbm_calibrated': 0.7082, 'analog_k100': 0.7424, 'derivatives': 0.6925, 'orthosys': 0.6936}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 59, 'extreme_volatility': 1}
- **prediction_latency_min**: 6.2
- **price_snapshot_age_s**: 0.4
- **train_rows_h1**: 89631
- **orthosys_hist_hit_h1**: 0.5284
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0044
- **p_spread_logistic_h1**: 0.0131
- **p_spread_lgbm_calibrated_h1**: 0.0128
- **p_spread_analog_k100_h1**: 0.0729
- **p_spread_derivatives_h1**: 0.0005
- **p_spread_orthosys_h1**: 0.0037
- **p_spread_council_h1**: 0.0064
- **train_rows_h4**: 89448
- **orthosys_hist_hit_h4**: 0.5141
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0003
- **p_spread_logistic_h4**: 0.0255
- **p_spread_lgbm_calibrated_h4**: 0.0021
- **p_spread_analog_k100_h4**: 0.0758
- **p_spread_derivatives_h4**: 0.0018
- **p_spread_orthosys_h4**: 0.0018
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 33720

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1620 | 27 | 1620 | 0.502 | 0.48-0.53 | 0.537 | 0.467 | -0.0210 | 0.075 | 0.52 | -14.7 |
| analog_k100|h1|on_time | 1620 | 27 | 1620 | 0.502 | 0.48-0.53 | 0.537 | 0.467 | -0.0210 | 0.075 | 0.52 | -14.7 |
| analog_k100|h4|all | 1440 | 24 | 1440 | 0.428 | 0.40-0.45 | 0.584 | 0.444 | -0.1006 | 0.152 | 0.65 | -61.2 |
| analog_k100|h4|on_time | 1440 | 24 | 1440 | 0.428 | 0.40-0.45 | 0.584 | 0.444 | -0.1006 | 0.152 | 0.65 | -61.2 |
| base_rate|h1|all | 1920 | 32 | 1920 | 0.468 | 0.45-0.49 | 0.532 | 0.498 | +0.0000 | 0.034 | 0.00 | - |
| base_rate|h1|on_time | 1860 | 31 | 1860 | 0.472 | 0.45-0.49 | 0.528 | 0.498 | +0.0000 | 0.030 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 1740 | 29 | 1740 | 0.585 | 0.56-0.61 | 0.585 | 0.503 | +0.0000 | 0.082 | 0.00 | - |
| base_rate|h4|on_time | 1740 | 29 | 1740 | 0.585 | 0.56-0.61 | 0.585 | 0.503 | +0.0000 | 0.082 | 0.00 | - |
| council|h1|all | 1620 | 27 | 316 | 0.557 | 0.50-0.61 | 0.537 | 0.495 | +0.0031 | 0.055 | 0.00 | +18.3 |
| council|h1|on_time | 1620 | 27 | 316 | 0.557 | 0.50-0.61 | 0.537 | 0.495 | +0.0031 | 0.055 | 0.00 | +18.3 |
| council|h4|all | 1440 | 24 | 20 | 0.600 | 0.39-0.78 | 0.584 | 0.500 | -0.0012 | 0.085 | 0.00 | - |
| council|h4|on_time | 1440 | 24 | 20 | 0.600 | 0.39-0.78 | 0.584 | 0.500 | -0.0012 | 0.085 | 0.00 | - |
| derivatives|h1|all | 1620 | 27 | 1620 | 0.460 | 0.44-0.48 | 0.537 | 0.498 | -0.0001 | 0.041 | 0.00 | - |
| derivatives|h1|on_time | 1620 | 27 | 1620 | 0.460 | 0.44-0.48 | 0.537 | 0.498 | -0.0001 | 0.041 | 0.00 | - |
| derivatives|h4|all | 1440 | 24 | 1440 | 0.581 | 0.56-0.61 | 0.584 | 0.502 | +0.0000 | 0.082 | 0.00 | -117.6 |
| derivatives|h4|on_time | 1440 | 24 | 1440 | 0.581 | 0.56-0.61 | 0.584 | 0.502 | +0.0000 | 0.082 | 0.00 | -117.6 |
| lgbm_calibrated|h1|all | 1920 | 32 | 1920 | 0.545 | 0.52-0.57 | 0.532 | 0.475 | +0.0033 | 0.058 | 0.14 | +6.3 |
| lgbm_calibrated|h1|on_time | 1860 | 31 | 1860 | 0.552 | 0.53-0.57 | 0.528 | 0.475 | +0.0046 | 0.054 | 0.14 | +6.3 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 1740 | 29 | 1740 | 0.414 | 0.39-0.44 | 0.585 | 0.457 | -0.0340 | 0.131 | 0.26 | -50.8 |
| lgbm_calibrated|h4|on_time | 1740 | 29 | 1740 | 0.414 | 0.39-0.44 | 0.585 | 0.457 | -0.0340 | 0.131 | 0.26 | -50.8 |
| logistic|h1|all | 1920 | 32 | 1920 | 0.538 | 0.52-0.56 | 0.532 | 0.490 | +0.0082 | 0.046 | 0.11 | -8.1 |
| logistic|h1|on_time | 1860 | 31 | 1860 | 0.530 | 0.51-0.55 | 0.528 | 0.489 | +0.0066 | 0.043 | 0.11 | -8.0 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 1740 | 29 | 1740 | 0.511 | 0.49-0.53 | 0.585 | 0.491 | -0.0053 | 0.094 | 0.21 | -0.0 |
| logistic|h4|on_time | 1740 | 29 | 1740 | 0.511 | 0.49-0.53 | 0.585 | 0.491 | -0.0053 | 0.094 | 0.21 | -0.0 |
| momentum_24|h1|all | 1920 | 32 | 1920 | 0.543 | 0.52-0.57 | 0.532 | 0.497 | +0.0030 | 0.035 | 0.00 | - |
| momentum_24|h1|on_time | 1860 | 31 | 1860 | 0.538 | 0.52-0.56 | 0.528 | 0.497 | +0.0027 | 0.032 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 1740 | 29 | 1740 | 0.585 | 0.56-0.61 | 0.585 | 0.503 | +0.0000 | 0.082 | 0.00 | - |
| momentum_24|h4|on_time | 1740 | 29 | 1740 | 0.585 | 0.56-0.61 | 0.585 | 0.503 | +0.0000 | 0.082 | 0.00 | - |
| orthosys|h1|all | 1920 | 32 | 177 | 0.542 | 0.47-0.61 | 0.532 | 0.498 | +0.0012 | 0.036 | 0.00 | - |
| orthosys|h1|on_time | 1860 | 31 | 176 | 0.540 | 0.47-0.61 | 0.528 | 0.498 | +0.0011 | 0.032 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 1740 | 29 | 173 | 0.428 | 0.36-0.50 | 0.585 | 0.499 | -0.0024 | 0.086 | 0.00 | - |
| orthosys|h4|on_time | 1740 | 29 | 173 | 0.428 | 0.36-0.50 | 0.585 | 0.499 | -0.0024 | 0.086 | 0.00 | - |
| recent_base_rate_7d|h1|all | 1860 | 31 | 1860 | 0.472 | 0.45-0.49 | 0.528 | 0.473 | -0.0082 | 0.055 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 1860 | 31 | 1860 | 0.472 | 0.45-0.49 | 0.528 | 0.473 | -0.0082 | 0.055 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1680 | 28 | 1680 | 0.405 | 0.38-0.43 | 0.595 | 0.439 | -0.0671 | 0.156 | 0.93 | -73.1 |
| recent_base_rate_7d|h4|on_time | 1680 | 28 | 1680 | 0.405 | 0.38-0.43 | 0.595 | 0.439 | -0.0671 | 0.156 | 0.93 | -73.1 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 958.89 | -4.11% | 836 | 329 | 27 |
| analog_k100|h4 | 966.51 | -3.35% | 930 | 347 | 24 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 32 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 29 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 27 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 24 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 27 |
| derivatives|h4 | 985.33 | -1.47% | 5 | 1 | 24 |
| lgbm_calibrated|h1 | 934.27 | -6.57% | 263 | 129 | 32 |
| lgbm_calibrated|h4 | 917.65 | -8.24% | 453 | 189 | 29 |
| logistic|h1 | 938.48 | -6.15% | 212 | 111 | 32 |
| logistic|h4 | 1028.95 | +2.90% | 370 | 181 | 29 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 32 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 29 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 32 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 29 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 31 |
| recent_base_rate_7d|h4 | 953.43 | -4.66% | 1560 | 601 | 28 |
| benchmark_long_all_coins|h1 | 1011.99 | +1.20% | 1920 | 917 | 32 |
| benchmark_long_all_coins|h4 | 1037.73 | +3.77% | 1740 | 948 | 29 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 28 |

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
