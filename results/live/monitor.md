# Live monitor (2026-10-21T08:07:26.181034+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.56 (ECE 0.129)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.471
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.492
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.489
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.56 (ECE 0.108)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.455
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.495
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.57 (ECE 0.131)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.449

## Health

- **venue**: okx
- **symbols**: 61
- **universe_size**: 60
- **fetched_only_for_scoring**: ['CAP']
- **last_closed_bar**: 2026-10-21 07:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.4
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 105.6 instruments 61/61']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.126, 'recent_base_rate_7d': 0.09, 'momentum_24': 0.145, 'logistic': 0.194, 'lgbm_calibrated': 0.144, 'analog_k100': 0.04, 'derivatives': 0.13, 'orthosys': 0.132}
- **council_member_logloss_h1**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.6963, 'momentum_24': 0.6922, 'logistic': 0.6897, 'lgbm_calibrated': 0.6923, 'analog_k100': 0.705, 'derivatives': 0.6934, 'orthosys': 0.693}
- **council_calls_h1**: 29
- **council_abstain_h1**: {'spoke': 29, 'no_edge': 29, 'extreme_volatility': 2}
- **council_weights_h4**: {'base_rate': 0.202, 'recent_base_rate_7d': 0.013, 'momentum_24': 0.202, 'logistic': 0.148, 'lgbm_calibrated': 0.05, 'analog_k100': 0.005, 'derivatives': 0.196, 'orthosys': 0.185}
- **council_member_logloss_h4**: {'base_rate': 0.6927, 'recent_base_rate_7d': 0.7186, 'momentum_24': 0.6927, 'logistic': 0.6956, 'lgbm_calibrated': 0.7057, 'analog_k100': 0.7327, 'derivatives': 0.6928, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 57, 'extreme_volatility': 2, 'members_disagree': 1}
- **prediction_latency_min**: 7.3
- **price_snapshot_age_s**: 0.4
- **train_rows_h1**: 89718
- **orthosys_hist_hit_h1**: 0.5277
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.006
- **p_spread_logistic_h1**: 0.0218
- **p_spread_lgbm_calibrated_h1**: 0.0081
- **p_spread_analog_k100_h1**: 0.0611
- **p_spread_derivatives_h1**: 0.0068
- **p_spread_orthosys_h1**: 0.0036
- **p_spread_council_h1**: 0.0129
- **train_rows_h4**: 89535
- **orthosys_hist_hit_h4**: 0.5135
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0003
- **p_spread_logistic_h4**: 0.0444
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0842
- **p_spread_derivatives_h4**: 0.0184
- **p_spread_orthosys_h4**: 0.0017
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 42360

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 2100 | 35 | 2100 | 0.496 | 0.47-0.52 | 0.531 | 0.464 | -0.0265 | 0.072 | 0.53 | -14.9 |
| analog_k100|h1|on_time | 2100 | 35 | 2100 | 0.496 | 0.47-0.52 | 0.531 | 0.464 | -0.0265 | 0.072 | 0.53 | -14.9 |
| analog_k100|h4|all | 1920 | 32 | 1920 | 0.448 | 0.43-0.47 | 0.561 | 0.450 | -0.0758 | 0.129 | 0.64 | -41.7 |
| analog_k100|h4|on_time | 1920 | 32 | 1920 | 0.448 | 0.43-0.47 | 0.561 | 0.450 | -0.0758 | 0.129 | 0.64 | -41.7 |
| base_rate|h1|all | 2400 | 40 | 2400 | 0.472 | 0.45-0.49 | 0.528 | 0.498 | +0.0000 | 0.030 | 0.00 | - |
| base_rate|h1|on_time | 2340 | 39 | 2340 | 0.475 | 0.46-0.50 | 0.525 | 0.498 | +0.0000 | 0.027 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 2220 | 37 | 2220 | 0.565 | 0.54-0.59 | 0.565 | 0.503 | +0.0000 | 0.062 | 0.00 | - |
| base_rate|h4|on_time | 2220 | 37 | 2220 | 0.565 | 0.54-0.59 | 0.565 | 0.503 | +0.0000 | 0.062 | 0.00 | - |
| council|h1|all | 2100 | 35 | 367 | 0.526 | 0.47-0.58 | 0.531 | 0.495 | +0.0016 | 0.036 | 0.00 | +18.3 |
| council|h1|on_time | 2100 | 35 | 367 | 0.526 | 0.47-0.58 | 0.531 | 0.495 | +0.0016 | 0.036 | 0.00 | +18.3 |
| council|h4|all | 1920 | 32 | 21 | 0.571 | 0.37-0.76 | 0.561 | 0.500 | -0.0009 | 0.062 | 0.00 | - |
| council|h4|on_time | 1920 | 32 | 21 | 0.571 | 0.37-0.76 | 0.561 | 0.500 | -0.0009 | 0.062 | 0.00 | - |
| derivatives|h1|all | 2100 | 35 | 2100 | 0.467 | 0.45-0.49 | 0.531 | 0.498 | -0.0000 | 0.035 | 0.00 | - |
| derivatives|h1|on_time | 2100 | 35 | 2100 | 0.467 | 0.45-0.49 | 0.531 | 0.498 | -0.0000 | 0.035 | 0.00 | - |
| derivatives|h4|all | 1920 | 32 | 1920 | 0.561 | 0.54-0.58 | 0.561 | 0.503 | -0.0000 | 0.058 | 0.00 | -117.6 |
| derivatives|h4|on_time | 1920 | 32 | 1920 | 0.561 | 0.54-0.58 | 0.561 | 0.503 | -0.0000 | 0.058 | 0.00 | -117.6 |
| lgbm_calibrated|h1|all | 2400 | 40 | 2400 | 0.535 | 0.51-0.55 | 0.528 | 0.474 | -0.0006 | 0.054 | 0.13 | +2.3 |
| lgbm_calibrated|h1|on_time | 2340 | 39 | 2340 | 0.539 | 0.52-0.56 | 0.525 | 0.474 | +0.0003 | 0.051 | 0.13 | +2.3 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 2220 | 37 | 2220 | 0.435 | 0.41-0.46 | 0.565 | 0.459 | -0.0272 | 0.108 | 0.22 | -50.2 |
| lgbm_calibrated|h4|on_time | 2220 | 37 | 2220 | 0.435 | 0.41-0.46 | 0.565 | 0.459 | -0.0272 | 0.108 | 0.22 | -50.2 |
| logistic|h1|all | 2400 | 40 | 2400 | 0.532 | 0.51-0.55 | 0.528 | 0.491 | +0.0059 | 0.040 | 0.09 | +6.6 |
| logistic|h1|on_time | 2340 | 39 | 2340 | 0.526 | 0.51-0.55 | 0.525 | 0.490 | +0.0046 | 0.037 | 0.10 | +7.0 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 2220 | 37 | 2220 | 0.509 | 0.49-0.53 | 0.565 | 0.495 | -0.0041 | 0.070 | 0.20 | +0.6 |
| logistic|h4|on_time | 2220 | 37 | 2220 | 0.509 | 0.49-0.53 | 0.565 | 0.495 | -0.0041 | 0.070 | 0.20 | +0.6 |
| momentum_24|h1|all | 2400 | 40 | 2400 | 0.528 | 0.51-0.55 | 0.528 | 0.496 | +0.0019 | 0.032 | 0.00 | - |
| momentum_24|h1|on_time | 2340 | 39 | 2340 | 0.524 | 0.50-0.54 | 0.525 | 0.496 | +0.0016 | 0.029 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 2220 | 37 | 2220 | 0.565 | 0.54-0.59 | 0.565 | 0.503 | -0.0000 | 0.062 | 0.00 | - |
| momentum_24|h4|on_time | 2220 | 37 | 2220 | 0.565 | 0.54-0.59 | 0.565 | 0.503 | -0.0000 | 0.062 | 0.00 | - |
| orthosys|h1|all | 2400 | 40 | 187 | 0.540 | 0.47-0.61 | 0.528 | 0.498 | +0.0010 | 0.032 | 0.00 | - |
| orthosys|h1|on_time | 2340 | 39 | 186 | 0.538 | 0.47-0.61 | 0.525 | 0.498 | +0.0009 | 0.028 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 2220 | 37 | 184 | 0.446 | 0.38-0.52 | 0.565 | 0.499 | -0.0017 | 0.066 | 0.00 | - |
| orthosys|h4|on_time | 2220 | 37 | 184 | 0.446 | 0.38-0.52 | 0.565 | 0.499 | -0.0017 | 0.066 | 0.00 | - |
| recent_base_rate_7d|h1|all | 2340 | 39 | 2340 | 0.475 | 0.46-0.50 | 0.525 | 0.474 | -0.0075 | 0.051 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 2340 | 39 | 2340 | 0.475 | 0.46-0.50 | 0.525 | 0.474 | -0.0075 | 0.051 | 0.00 | - |
| recent_base_rate_7d|h4|all | 2160 | 36 | 2160 | 0.428 | 0.41-0.45 | 0.572 | 0.441 | -0.0540 | 0.131 | 0.86 | -71.2 |
| recent_base_rate_7d|h4|on_time | 2160 | 36 | 2160 | 0.428 | 0.41-0.45 | 0.572 | 0.441 | -0.0540 | 0.131 | 0.86 | -71.2 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 946.85 | -5.31% | 1116 | 436 | 35 |
| analog_k100|h4 | 970.87 | -2.91% | 1229 | 493 | 32 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 40 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 37 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 35 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 32 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 35 |
| derivatives|h4 | 985.33 | -1.47% | 5 | 1 | 32 |
| lgbm_calibrated|h1 | 950.42 | -4.96% | 302 | 143 | 40 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 37 |
| logistic|h1 | 1063.82 | +6.38% | 226 | 122 | 40 |
| logistic|h4 | 1027.50 | +2.75% | 446 | 216 | 37 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 40 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 37 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 40 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 37 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 39 |
| recent_base_rate_7d|h4 | 946.20 | -5.38% | 1860 | 708 | 36 |
| benchmark_long_all_coins|h1 | 1019.39 | +1.94% | 2400 | 1145 | 40 |
| benchmark_long_all_coins|h4 | 1041.76 | +4.18% | 2220 | 1178 | 37 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 36 |

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
