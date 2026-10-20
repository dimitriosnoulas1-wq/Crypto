# Live monitor (2026-10-20T21:06:33.172056+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h1|all says 0.47 on average, reality 0.55 (ECE 0.084)
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.482
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.474
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.57 (ECE 0.112)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.458
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.486
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.58 (ECE 0.139)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.449

## Health

- **venue**: okx
- **symbols**: 61
- **universe_size**: 60
- **fetched_only_for_scoring**: ['A']
- **last_closed_bar**: 2026-10-20 20:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.6
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 103.6 instruments 61/61']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.123, 'recent_base_rate_7d': 0.091, 'momentum_24': 0.144, 'logistic': 0.165, 'lgbm_calibrated': 0.155, 'analog_k100': 0.066, 'derivatives': 0.126, 'orthosys': 0.129}
- **council_member_logloss_h1**: {'base_rate': 0.6935, 'recent_base_rate_7d': 0.6972, 'momentum_24': 0.6916, 'logistic': 0.69, 'lgbm_calibrated': 0.6907, 'analog_k100': 0.703, 'derivatives': 0.6936, 'orthosys': 0.6929}
- **council_calls_h1**: 28
- **council_abstain_h1**: {'no_edge': 29, 'spoke': 28, 'extreme_volatility': 2, 'members_disagree': 1}
- **council_weights_h4**: {'base_rate': 0.163, 'recent_base_rate_7d': 0.02, 'momentum_24': 0.164, 'logistic': 0.236, 'lgbm_calibrated': 0.082, 'analog_k100': 0.015, 'derivatives': 0.157, 'orthosys': 0.162}
- **council_member_logloss_h4**: {'base_rate': 0.6929, 'recent_base_rate_7d': 0.7216, 'momentum_24': 0.6928, 'logistic': 0.6879, 'lgbm_calibrated': 0.702, 'analog_k100': 0.7321, 'derivatives': 0.6931, 'orthosys': 0.693}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 53, 'members_disagree': 5, 'extreme_volatility': 2}
- **prediction_latency_min**: 6.5
- **price_snapshot_age_s**: 0.9
- **train_rows_h1**: 89437
- **orthosys_hist_hit_h1**: 0.5257
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0049
- **p_spread_logistic_h1**: 0.0171
- **p_spread_lgbm_calibrated_h1**: 0.0579
- **p_spread_analog_k100_h1**: 0.0531
- **p_spread_derivatives_h1**: 0.0009
- **p_spread_orthosys_h1**: 0.0046
- **p_spread_council_h1**: 0.0166
- **train_rows_h4**: 89254
- **orthosys_hist_hit_h4**: 0.5142
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0002
- **p_spread_logistic_h4**: 0.0371
- **p_spread_lgbm_calibrated_h4**: 0.0121
- **p_spread_analog_k100_h4**: 0.0783
- **p_spread_derivatives_h4**: 0.006
- **p_spread_orthosys_h4**: 0.0026
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 30480

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1440 | 24 | 1440 | 0.496 | 0.47-0.52 | 0.549 | 0.470 | -0.0251 | 0.084 | 0.50 | -15.3 |
| analog_k100|h1|on_time | 1440 | 24 | 1440 | 0.496 | 0.47-0.52 | 0.549 | 0.470 | -0.0251 | 0.084 | 0.50 | -15.3 |
| analog_k100|h4|all | 1260 | 21 | 1260 | 0.448 | 0.42-0.48 | 0.560 | 0.445 | -0.0846 | 0.132 | 0.64 | -55.8 |
| analog_k100|h4|on_time | 1260 | 21 | 1260 | 0.448 | 0.42-0.48 | 0.560 | 0.445 | -0.0846 | 0.132 | 0.64 | -55.8 |
| base_rate|h1|all | 1740 | 29 | 1740 | 0.458 | 0.43-0.48 | 0.542 | 0.498 | +0.0000 | 0.044 | 0.00 | - |
| base_rate|h1|on_time | 1680 | 28 | 1680 | 0.462 | 0.44-0.49 | 0.538 | 0.498 | +0.0000 | 0.040 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 1560 | 26 | 1560 | 0.566 | 0.54-0.59 | 0.566 | 0.503 | +0.0000 | 0.063 | 0.00 | - |
| base_rate|h4|on_time | 1560 | 26 | 1560 | 0.566 | 0.54-0.59 | 0.566 | 0.503 | +0.0000 | 0.063 | 0.00 | - |
| council|h1|all | 1440 | 24 | 254 | 0.528 | 0.47-0.59 | 0.549 | 0.495 | +0.0024 | 0.055 | 0.00 | +64.4 |
| council|h1|on_time | 1440 | 24 | 254 | 0.528 | 0.47-0.59 | 0.549 | 0.495 | +0.0024 | 0.055 | 0.00 | +64.4 |
| council|h4|all | 1260 | 21 | 18 | 0.556 | 0.34-0.75 | 0.560 | 0.500 | -0.0005 | 0.062 | 0.00 | - |
| council|h4|on_time | 1260 | 21 | 18 | 0.556 | 0.34-0.75 | 0.560 | 0.500 | -0.0005 | 0.062 | 0.00 | - |
| derivatives|h1|all | 1440 | 24 | 1440 | 0.448 | 0.42-0.47 | 0.549 | 0.498 | -0.0001 | 0.054 | 0.00 | - |
| derivatives|h1|on_time | 1440 | 24 | 1440 | 0.448 | 0.42-0.47 | 0.549 | 0.498 | -0.0001 | 0.054 | 0.00 | - |
| derivatives|h4|all | 1260 | 21 | 1260 | 0.560 | 0.53-0.59 | 0.560 | 0.502 | +0.0001 | 0.058 | 0.00 | -117.6 |
| derivatives|h4|on_time | 1260 | 21 | 1260 | 0.560 | 0.53-0.59 | 0.560 | 0.502 | +0.0001 | 0.058 | 0.00 | -117.6 |
| lgbm_calibrated|h1|all | 1740 | 29 | 1740 | 0.544 | 0.52-0.57 | 0.542 | 0.478 | +0.0026 | 0.069 | 0.10 | +19.3 |
| lgbm_calibrated|h1|on_time | 1680 | 28 | 1680 | 0.551 | 0.53-0.57 | 0.538 | 0.478 | +0.0041 | 0.065 | 0.10 | +19.3 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 1560 | 26 | 1560 | 0.433 | 0.41-0.46 | 0.566 | 0.458 | -0.0241 | 0.112 | 0.22 | -25.4 |
| lgbm_calibrated|h4|on_time | 1560 | 26 | 1560 | 0.433 | 0.41-0.46 | 0.566 | 0.458 | -0.0241 | 0.112 | 0.22 | -25.4 |
| logistic|h1|all | 1740 | 29 | 1740 | 0.530 | 0.51-0.55 | 0.542 | 0.491 | +0.0070 | 0.055 | 0.12 | -8.9 |
| logistic|h1|on_time | 1680 | 28 | 1680 | 0.521 | 0.50-0.54 | 0.538 | 0.490 | +0.0052 | 0.052 | 0.12 | -8.7 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 1560 | 26 | 1560 | 0.532 | 0.51-0.56 | 0.566 | 0.493 | +0.0027 | 0.073 | 0.19 | +16.6 |
| logistic|h4|on_time | 1560 | 26 | 1560 | 0.532 | 0.51-0.56 | 0.566 | 0.493 | +0.0027 | 0.073 | 0.19 | +16.6 |
| momentum_24|h1|all | 1740 | 29 | 1740 | 0.541 | 0.52-0.56 | 0.542 | 0.498 | +0.0029 | 0.044 | 0.00 | - |
| momentum_24|h1|on_time | 1680 | 28 | 1680 | 0.535 | 0.51-0.56 | 0.538 | 0.498 | +0.0025 | 0.041 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 1560 | 26 | 1560 | 0.566 | 0.54-0.59 | 0.566 | 0.503 | +0.0001 | 0.063 | 0.00 | - |
| momentum_24|h4|on_time | 1560 | 26 | 1560 | 0.566 | 0.54-0.59 | 0.566 | 0.503 | +0.0001 | 0.063 | 0.00 | - |
| orthosys|h1|all | 1740 | 29 | 173 | 0.543 | 0.47-0.62 | 0.542 | 0.498 | +0.0014 | 0.046 | 0.00 | - |
| orthosys|h1|on_time | 1680 | 28 | 172 | 0.541 | 0.47-0.61 | 0.538 | 0.498 | +0.0013 | 0.042 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 1560 | 26 | 134 | 0.463 | 0.38-0.55 | 0.566 | 0.499 | -0.0013 | 0.067 | 0.00 | - |
| orthosys|h4|on_time | 1560 | 26 | 134 | 0.463 | 0.38-0.55 | 0.566 | 0.499 | -0.0013 | 0.067 | 0.00 | - |
| recent_base_rate_7d|h1|all | 1680 | 28 | 1680 | 0.462 | 0.44-0.49 | 0.538 | 0.473 | -0.0100 | 0.065 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 1680 | 28 | 1680 | 0.462 | 0.44-0.49 | 0.538 | 0.473 | -0.0100 | 0.065 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1500 | 25 | 1500 | 0.423 | 0.40-0.45 | 0.577 | 0.438 | -0.0607 | 0.139 | 0.96 | -67.9 |
| recent_base_rate_7d|h4|on_time | 1500 | 25 | 1500 | 0.423 | 0.40-0.45 | 0.577 | 0.438 | -0.0607 | 0.139 | 0.96 | -67.9 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 962.07 | -3.79% | 726 | 277 | 24 |
| analog_k100|h4 | 973.42 | -2.66% | 801 | 320 | 21 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 29 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 26 |
| council|h1 | 1006.44 | +0.64% | 3 | 2 | 24 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 21 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 24 |
| derivatives|h4 | 985.33 | -1.47% | 5 | 1 | 21 |
| lgbm_calibrated|h1 | 941.35 | -5.86% | 167 | 83 | 29 |
| lgbm_calibrated|h4 | 923.39 | -7.66% | 337 | 167 | 26 |
| logistic|h1 | 942.01 | -5.80% | 205 | 106 | 29 |
| logistic|h4 | 1034.57 | +3.46% | 303 | 159 | 26 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 29 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 26 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 29 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 26 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 28 |
| recent_base_rate_7d|h4 | 959.92 | -4.01% | 1440 | 577 | 25 |
| benchmark_long_all_coins|h1 | 1015.79 | +1.58% | 1740 | 849 | 29 |
| benchmark_long_all_coins|h4 | 1029.74 | +2.97% | 1560 | 811 | 26 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 25 |

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
