# Live monitor (2026-10-20T22:06:52.278117+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h1|all says 0.47 on average, reality 0.55 (ECE 0.083)
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.483
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.475
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.57 (ECE 0.118)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.451
- MISCALIBRATED: logistic|h4|all says 0.49 on average, reality 0.57 (ECE 0.080)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.487
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.58 (ECE 0.144)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.442

## Health

- **venue**: okx
- **symbols**: 61
- **universe_size**: 60
- **fetched_only_for_scoring**: ['A']
- **last_closed_bar**: 2026-10-20 21:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.9
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 104.1 instruments 61/61']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.129, 'recent_base_rate_7d': 0.085, 'momentum_24': 0.146, 'logistic': 0.175, 'lgbm_calibrated': 0.145, 'analog_k100': 0.052, 'derivatives': 0.132, 'orthosys': 0.137}
- **council_member_logloss_h1**: {'base_rate': 0.6936, 'recent_base_rate_7d': 0.6986, 'momentum_24': 0.6921, 'logistic': 0.6901, 'lgbm_calibrated': 0.6922, 'analog_k100': 0.7066, 'derivatives': 0.6937, 'orthosys': 0.6929}
- **council_calls_h1**: 7
- **council_abstain_h1**: {'no_edge': 51, 'spoke': 7, 'extreme_volatility': 2}
- **council_weights_h4**: {'base_rate': 0.179, 'recent_base_rate_7d': 0.018, 'momentum_24': 0.18, 'logistic': 0.197, 'lgbm_calibrated': 0.071, 'analog_k100': 0.011, 'derivatives': 0.174, 'orthosys': 0.17}
- **council_member_logloss_h4**: {'base_rate': 0.6927, 'recent_base_rate_7d': 0.7231, 'momentum_24': 0.6927, 'logistic': 0.6915, 'lgbm_calibrated': 0.7046, 'analog_k100': 0.737, 'derivatives': 0.6928, 'orthosys': 0.6934}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 58, 'extreme_volatility': 2}
- **prediction_latency_min**: 6.8
- **price_snapshot_age_s**: 0.2
- **train_rows_h1**: 89498
- **orthosys_hist_hit_h1**: 0.5257
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0053
- **p_spread_logistic_h1**: 0.0191
- **p_spread_lgbm_calibrated_h1**: 0.0203
- **p_spread_analog_k100_h1**: 0.0717
- **p_spread_derivatives_h1**: 0.0012
- **p_spread_orthosys_h1**: 0.0033
- **p_spread_council_h1**: 0.007
- **train_rows_h4**: 89315
- **orthosys_hist_hit_h4**: 0.5131
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0003
- **p_spread_logistic_h4**: 0.0279
- **p_spread_lgbm_calibrated_h4**: 0.0025
- **p_spread_analog_k100_h4**: 0.0744
- **p_spread_derivatives_h4**: 0.0043
- **p_spread_orthosys_h4**: 0.0017
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 31560

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1500 | 25 | 1500 | 0.499 | 0.47-0.52 | 0.547 | 0.469 | -0.0229 | 0.083 | 0.51 | -15.9 |
| analog_k100|h1|on_time | 1500 | 25 | 1500 | 0.499 | 0.47-0.52 | 0.547 | 0.469 | -0.0229 | 0.083 | 0.51 | -15.9 |
| analog_k100|h4|all | 1320 | 22 | 1320 | 0.442 | 0.42-0.47 | 0.568 | 0.444 | -0.0891 | 0.138 | 0.64 | -55.3 |
| analog_k100|h4|on_time | 1320 | 22 | 1320 | 0.442 | 0.42-0.47 | 0.568 | 0.444 | -0.0891 | 0.138 | 0.64 | -55.3 |
| base_rate|h1|all | 1800 | 30 | 1800 | 0.459 | 0.44-0.48 | 0.541 | 0.498 | +0.0000 | 0.042 | 0.00 | - |
| base_rate|h1|on_time | 1740 | 29 | 1740 | 0.463 | 0.44-0.49 | 0.537 | 0.498 | +0.0000 | 0.039 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 1620 | 27 | 1620 | 0.572 | 0.55-0.60 | 0.572 | 0.503 | +0.0000 | 0.069 | 0.00 | - |
| base_rate|h4|on_time | 1620 | 27 | 1620 | 0.572 | 0.55-0.60 | 0.572 | 0.503 | +0.0000 | 0.069 | 0.00 | - |
| council|h1|all | 1500 | 25 | 282 | 0.528 | 0.47-0.59 | 0.547 | 0.495 | +0.0023 | 0.053 | 0.00 | +18.3 |
| council|h1|on_time | 1500 | 25 | 282 | 0.528 | 0.47-0.59 | 0.547 | 0.495 | +0.0023 | 0.053 | 0.00 | +18.3 |
| council|h4|all | 1320 | 22 | 19 | 0.579 | 0.36-0.77 | 0.568 | 0.500 | -0.0007 | 0.069 | 0.00 | - |
| council|h4|on_time | 1320 | 22 | 19 | 0.579 | 0.36-0.77 | 0.568 | 0.500 | -0.0007 | 0.069 | 0.00 | - |
| derivatives|h1|all | 1500 | 25 | 1500 | 0.450 | 0.42-0.48 | 0.547 | 0.498 | -0.0001 | 0.052 | 0.00 | - |
| derivatives|h1|on_time | 1500 | 25 | 1500 | 0.450 | 0.42-0.48 | 0.547 | 0.498 | -0.0001 | 0.052 | 0.00 | - |
| derivatives|h4|all | 1320 | 22 | 1320 | 0.567 | 0.54-0.59 | 0.568 | 0.502 | +0.0001 | 0.066 | 0.00 | -117.6 |
| derivatives|h4|on_time | 1320 | 22 | 1320 | 0.567 | 0.54-0.59 | 0.568 | 0.502 | +0.0001 | 0.066 | 0.00 | -117.6 |
| lgbm_calibrated|h1|all | 1800 | 30 | 1800 | 0.542 | 0.52-0.57 | 0.541 | 0.476 | +0.0006 | 0.065 | 0.10 | +11.4 |
| lgbm_calibrated|h1|on_time | 1740 | 29 | 1740 | 0.549 | 0.53-0.57 | 0.537 | 0.477 | +0.0019 | 0.060 | 0.11 | +11.4 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 1620 | 27 | 1620 | 0.427 | 0.40-0.45 | 0.572 | 0.457 | -0.0277 | 0.118 | 0.24 | -36.3 |
| lgbm_calibrated|h4|on_time | 1620 | 27 | 1620 | 0.427 | 0.40-0.45 | 0.572 | 0.457 | -0.0277 | 0.118 | 0.24 | -36.3 |
| logistic|h1|all | 1800 | 30 | 1800 | 0.531 | 0.51-0.55 | 0.541 | 0.490 | +0.0070 | 0.054 | 0.12 | -6.6 |
| logistic|h1|on_time | 1740 | 29 | 1740 | 0.522 | 0.50-0.55 | 0.537 | 0.489 | +0.0052 | 0.051 | 0.12 | -6.4 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 1620 | 27 | 1620 | 0.526 | 0.50-0.55 | 0.572 | 0.492 | -0.0010 | 0.080 | 0.20 | +6.1 |
| logistic|h4|on_time | 1620 | 27 | 1620 | 0.526 | 0.50-0.55 | 0.572 | 0.492 | -0.0010 | 0.080 | 0.20 | +6.1 |
| momentum_24|h1|all | 1800 | 30 | 1800 | 0.539 | 0.52-0.56 | 0.541 | 0.497 | +0.0028 | 0.043 | 0.00 | - |
| momentum_24|h1|on_time | 1740 | 29 | 1740 | 0.533 | 0.51-0.56 | 0.537 | 0.497 | +0.0024 | 0.039 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 1620 | 27 | 1620 | 0.572 | 0.55-0.60 | 0.572 | 0.503 | +0.0001 | 0.069 | 0.00 | - |
| momentum_24|h4|on_time | 1620 | 27 | 1620 | 0.572 | 0.55-0.60 | 0.572 | 0.503 | +0.0001 | 0.069 | 0.00 | - |
| orthosys|h1|all | 1800 | 30 | 175 | 0.543 | 0.47-0.61 | 0.541 | 0.498 | +0.0014 | 0.045 | 0.00 | - |
| orthosys|h1|on_time | 1740 | 29 | 174 | 0.540 | 0.47-0.61 | 0.537 | 0.498 | +0.0013 | 0.040 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 1620 | 27 | 163 | 0.429 | 0.36-0.51 | 0.572 | 0.499 | -0.0020 | 0.074 | 0.00 | - |
| orthosys|h4|on_time | 1620 | 27 | 163 | 0.429 | 0.36-0.51 | 0.572 | 0.499 | -0.0020 | 0.074 | 0.00 | - |
| recent_base_rate_7d|h1|all | 1740 | 29 | 1740 | 0.463 | 0.44-0.49 | 0.537 | 0.473 | -0.0097 | 0.064 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 1740 | 29 | 1740 | 0.463 | 0.44-0.49 | 0.537 | 0.473 | -0.0097 | 0.064 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1560 | 26 | 1560 | 0.417 | 0.39-0.44 | 0.583 | 0.439 | -0.0626 | 0.144 | 0.92 | -67.9 |
| recent_base_rate_7d|h4|on_time | 1560 | 26 | 1560 | 0.417 | 0.39-0.44 | 0.583 | 0.439 | -0.0626 | 0.144 | 0.92 | -67.9 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 959.32 | -4.07% | 762 | 294 | 25 |
| analog_k100|h4 | 972.31 | -2.77% | 844 | 329 | 22 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 30 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 27 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 25 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 22 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 25 |
| derivatives|h4 | 985.33 | -1.47% | 5 | 1 | 22 |
| lgbm_calibrated|h1 | 935.12 | -6.49% | 184 | 87 | 30 |
| lgbm_calibrated|h4 | 921.09 | -7.89% | 395 | 178 | 27 |
| logistic|h1 | 955.91 | -4.41% | 208 | 108 | 30 |
| logistic|h4 | 1031.44 | +3.14% | 328 | 165 | 27 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 30 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 27 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 30 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 27 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 29 |
| recent_base_rate_7d|h4 | 959.92 | -4.01% | 1440 | 577 | 26 |
| benchmark_long_all_coins|h1 | 1015.27 | +1.53% | 1800 | 879 | 30 |
| benchmark_long_all_coins|h4 | 1031.77 | +3.18% | 1620 | 855 | 27 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 26 |

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
