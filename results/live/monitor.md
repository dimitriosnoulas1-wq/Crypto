# Live monitor (2026-10-21T07:08:09.963554+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.55 (ECE 0.130)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.471
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.499
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.56 (ECE 0.103)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.462
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.57 (ECE 0.125)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.455

## Health

- **venue**: okx
- **symbols**: 61
- **universe_size**: 60
- **fetched_only_for_scoring**: ['CAP']
- **last_closed_bar**: 2026-10-21 06:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 6.2
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 102.5 instruments 61/61']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.121, 'recent_base_rate_7d': 0.097, 'momentum_24': 0.141, 'logistic': 0.182, 'lgbm_calibrated': 0.157, 'analog_k100': 0.053, 'derivatives': 0.124, 'orthosys': 0.125}
- **council_member_logloss_h1**: {'base_rate': 0.6933, 'recent_base_rate_7d': 0.6953, 'momentum_24': 0.692, 'logistic': 0.6897, 'lgbm_calibrated': 0.691, 'analog_k100': 0.7019, 'derivatives': 0.6933, 'orthosys': 0.693}
- **council_calls_h1**: 17
- **council_abstain_h1**: {'no_edge': 41, 'spoke': 17, 'extreme_volatility': 2}
- **council_weights_h4**: {'base_rate': 0.202, 'recent_base_rate_7d': 0.012, 'momentum_24': 0.202, 'logistic': 0.153, 'lgbm_calibrated': 0.047, 'analog_k100': 0.005, 'derivatives': 0.196, 'orthosys': 0.184}
- **council_member_logloss_h4**: {'base_rate': 0.6926, 'recent_base_rate_7d': 0.7202, 'momentum_24': 0.6926, 'logistic': 0.6953, 'lgbm_calibrated': 0.7065, 'analog_k100': 0.7344, 'derivatives': 0.6927, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 57, 'extreme_volatility': 2, 'members_disagree': 1}
- **prediction_latency_min**: 8.1
- **price_snapshot_age_s**: 0.7
- **train_rows_h1**: 89657
- **orthosys_hist_hit_h1**: 0.5276
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0079
- **p_spread_logistic_h1**: 0.014
- **p_spread_lgbm_calibrated_h1**: 0.0176
- **p_spread_analog_k100_h1**: 0.0616
- **p_spread_derivatives_h1**: 0.0034
- **p_spread_orthosys_h1**: 0.0036
- **p_spread_council_h1**: 0.0106
- **train_rows_h4**: 89474
- **orthosys_hist_hit_h4**: 0.5134
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0002
- **p_spread_logistic_h4**: 0.0387
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0816
- **p_spread_derivatives_h4**: 0.022
- **p_spread_orthosys_h4**: 0.0017
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 41280

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 2040 | 34 | 2040 | 0.502 | 0.48-0.52 | 0.521 | 0.464 | -0.0224 | 0.062 | 0.53 | -13.1 |
| analog_k100|h1|on_time | 2040 | 34 | 2040 | 0.502 | 0.48-0.52 | 0.521 | 0.464 | -0.0224 | 0.062 | 0.53 | -13.1 |
| analog_k100|h4|all | 1860 | 31 | 1860 | 0.448 | 0.43-0.47 | 0.554 | 0.448 | -0.0768 | 0.130 | 0.64 | -41.8 |
| analog_k100|h4|on_time | 1860 | 31 | 1860 | 0.448 | 0.43-0.47 | 0.554 | 0.448 | -0.0768 | 0.130 | 0.64 | -41.8 |
| base_rate|h1|all | 2340 | 39 | 2340 | 0.481 | 0.46-0.50 | 0.519 | 0.498 | +0.0000 | 0.021 | 0.00 | - |
| base_rate|h1|on_time | 2280 | 38 | 2280 | 0.484 | 0.46-0.50 | 0.516 | 0.498 | +0.0000 | 0.018 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 2160 | 36 | 2160 | 0.559 | 0.54-0.58 | 0.559 | 0.503 | +0.0000 | 0.055 | 0.00 | - |
| base_rate|h4|on_time | 2160 | 36 | 2160 | 0.559 | 0.54-0.58 | 0.559 | 0.503 | +0.0000 | 0.055 | 0.00 | - |
| council|h1|all | 2040 | 34 | 350 | 0.546 | 0.49-0.60 | 0.521 | 0.495 | +0.0020 | 0.033 | 0.00 | +18.3 |
| council|h1|on_time | 2040 | 34 | 350 | 0.546 | 0.49-0.60 | 0.521 | 0.495 | +0.0020 | 0.033 | 0.00 | +18.3 |
| council|h4|all | 1860 | 31 | 21 | 0.571 | 0.37-0.76 | 0.554 | 0.500 | -0.0007 | 0.055 | 0.00 | - |
| council|h4|on_time | 1860 | 31 | 21 | 0.571 | 0.37-0.76 | 0.554 | 0.500 | -0.0007 | 0.055 | 0.00 | - |
| derivatives|h1|all | 2040 | 34 | 2040 | 0.477 | 0.46-0.50 | 0.521 | 0.498 | +0.0000 | 0.025 | 0.00 | - |
| derivatives|h1|on_time | 2040 | 34 | 2040 | 0.477 | 0.46-0.50 | 0.521 | 0.498 | +0.0000 | 0.025 | 0.00 | - |
| derivatives|h4|all | 1860 | 31 | 1860 | 0.555 | 0.53-0.58 | 0.554 | 0.503 | -0.0000 | 0.051 | 0.00 | -117.6 |
| derivatives|h4|on_time | 1860 | 31 | 1860 | 0.555 | 0.53-0.58 | 0.554 | 0.503 | -0.0000 | 0.051 | 0.00 | -117.6 |
| lgbm_calibrated|h1|all | 2340 | 39 | 2340 | 0.545 | 0.52-0.56 | 0.519 | 0.474 | +0.0022 | 0.045 | 0.12 | +8.4 |
| lgbm_calibrated|h1|on_time | 2280 | 38 | 2280 | 0.550 | 0.53-0.57 | 0.516 | 0.474 | +0.0032 | 0.042 | 0.12 | +8.4 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 2160 | 36 | 2160 | 0.441 | 0.42-0.46 | 0.559 | 0.458 | -0.0261 | 0.103 | 0.23 | -50.2 |
| lgbm_calibrated|h4|on_time | 2160 | 36 | 2160 | 0.441 | 0.42-0.46 | 0.559 | 0.458 | -0.0261 | 0.103 | 0.23 | -50.2 |
| logistic|h1|all | 2340 | 39 | 2340 | 0.541 | 0.52-0.56 | 0.519 | 0.491 | +0.0074 | 0.031 | 0.10 | +5.7 |
| logistic|h1|on_time | 2280 | 38 | 2280 | 0.535 | 0.51-0.56 | 0.516 | 0.490 | +0.0060 | 0.028 | 0.10 | +6.1 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 2160 | 36 | 2160 | 0.501 | 0.48-0.52 | 0.559 | 0.494 | -0.0056 | 0.065 | 0.20 | +3.4 |
| logistic|h4|on_time | 2160 | 36 | 2160 | 0.501 | 0.48-0.52 | 0.559 | 0.494 | -0.0056 | 0.065 | 0.20 | +3.4 |
| momentum_24|h1|all | 2340 | 39 | 2340 | 0.535 | 0.51-0.55 | 0.519 | 0.496 | +0.0023 | 0.024 | 0.00 | - |
| momentum_24|h1|on_time | 2280 | 38 | 2280 | 0.530 | 0.51-0.55 | 0.516 | 0.496 | +0.0020 | 0.020 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 2160 | 36 | 2160 | 0.559 | 0.54-0.58 | 0.559 | 0.503 | -0.0000 | 0.056 | 0.00 | - |
| momentum_24|h4|on_time | 2160 | 36 | 2160 | 0.559 | 0.54-0.58 | 0.559 | 0.503 | -0.0000 | 0.056 | 0.00 | - |
| orthosys|h1|all | 2340 | 39 | 186 | 0.538 | 0.47-0.61 | 0.519 | 0.498 | +0.0008 | 0.023 | 0.00 | - |
| orthosys|h1|on_time | 2280 | 38 | 185 | 0.535 | 0.46-0.61 | 0.516 | 0.498 | +0.0007 | 0.019 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 2160 | 36 | 183 | 0.443 | 0.37-0.52 | 0.559 | 0.499 | -0.0016 | 0.060 | 0.00 | - |
| orthosys|h4|on_time | 2160 | 36 | 183 | 0.443 | 0.37-0.52 | 0.559 | 0.499 | -0.0016 | 0.060 | 0.00 | - |
| recent_base_rate_7d|h1|all | 2280 | 38 | 2280 | 0.484 | 0.46-0.50 | 0.516 | 0.473 | -0.0060 | 0.042 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 2280 | 38 | 2280 | 0.484 | 0.46-0.50 | 0.516 | 0.473 | -0.0060 | 0.042 | 0.00 | - |
| recent_base_rate_7d|h4|all | 2100 | 35 | 2100 | 0.434 | 0.41-0.46 | 0.566 | 0.441 | -0.0517 | 0.125 | 0.86 | -70.0 |
| recent_base_rate_7d|h4|on_time | 2100 | 35 | 2100 | 0.434 | 0.41-0.46 | 0.566 | 0.441 | -0.0517 | 0.125 | 0.86 | -70.0 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 954.10 | -4.59% | 1084 | 431 | 34 |
| analog_k100|h4 | 971.83 | -2.82% | 1197 | 480 | 31 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 39 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 36 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 34 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 31 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 34 |
| derivatives|h4 | 985.33 | -1.47% | 5 | 1 | 31 |
| lgbm_calibrated|h1 | 957.62 | -4.24% | 280 | 140 | 39 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 36 |
| logistic|h1 | 1041.80 | +4.18% | 225 | 121 | 39 |
| logistic|h4 | 1029.76 | +2.98% | 432 | 206 | 36 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 39 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 36 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 39 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 36 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 38 |
| recent_base_rate_7d|h4 | 948.69 | -5.13% | 1800 | 696 | 35 |
| benchmark_long_all_coins|h1 | 1012.41 | +1.24% | 2340 | 1094 | 39 |
| benchmark_long_all_coins|h4 | 1039.54 | +3.95% | 2160 | 1131 | 36 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 35 |

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
