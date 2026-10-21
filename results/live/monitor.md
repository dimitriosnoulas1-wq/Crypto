# Live monitor (2026-10-21T05:06:03.188564+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0011 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.57 (ECE 0.138)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.464
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.500
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.58 (ECE 0.121)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.445
- MISCALIBRATED: logistic|h4|all says 0.49 on average, reality 0.58 (ECE 0.083)
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.58 (ECE 0.144)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.437

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['DASH', 'ENSO']
- **last_closed_bar**: 2026-10-21 04:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.1
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 101.8 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.125, 'recent_base_rate_7d': 0.088, 'momentum_24': 0.145, 'logistic': 0.185, 'lgbm_calibrated': 0.156, 'analog_k100': 0.042, 'derivatives': 0.128, 'orthosys': 0.131}
- **council_member_logloss_h1**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.6968, 'momentum_24': 0.692, 'logistic': 0.6898, 'lgbm_calibrated': 0.6913, 'analog_k100': 0.7054, 'derivatives': 0.6935, 'orthosys': 0.6929}
- **council_calls_h1**: 4
- **council_abstain_h1**: {'no_edge': 53, 'spoke': 4, 'extreme_volatility': 3}
- **council_weights_h4**: {'base_rate': 0.206, 'recent_base_rate_7d': 0.009, 'momentum_24': 0.206, 'logistic': 0.154, 'lgbm_calibrated': 0.039, 'analog_k100': 0.004, 'derivatives': 0.199, 'orthosys': 0.183}
- **council_member_logloss_h4**: {'base_rate': 0.6923, 'recent_base_rate_7d': 0.7246, 'momentum_24': 0.6923, 'logistic': 0.6953, 'lgbm_calibrated': 0.7092, 'analog_k100': 0.7387, 'derivatives': 0.6924, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 56, 'extreme_volatility': 3, 'members_disagree': 1}
- **prediction_latency_min**: 6.0
- **price_snapshot_age_s**: 1.0
- **train_rows_h1**: 91054
- **orthosys_hist_hit_h1**: 0.5273
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0082
- **p_spread_logistic_h1**: 0.0195
- **p_spread_lgbm_calibrated_h1**: 0.017
- **p_spread_analog_k100_h1**: 0.0638
- **p_spread_derivatives_h1**: 0.0013
- **p_spread_orthosys_h1**: 0.0035
- **p_spread_council_h1**: 0.0059
- **train_rows_h4**: 90868
- **orthosys_hist_hit_h4**: 0.5135
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0006
- **p_spread_logistic_h4**: 0.0361
- **p_spread_lgbm_calibrated_h4**: 0.0011
- **p_spread_analog_k100_h4**: 0.0747
- **p_spread_derivatives_h4**: 0.0168
- **p_spread_orthosys_h4**: 0.0017
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 39120

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1920 | 32 | 1920 | 0.509 | 0.49-0.53 | 0.520 | 0.465 | -0.0195 | 0.060 | 0.53 | -14.2 |
| analog_k100|h1|on_time | 1920 | 32 | 1920 | 0.509 | 0.49-0.53 | 0.520 | 0.465 | -0.0195 | 0.060 | 0.53 | -14.2 |
| analog_k100|h4|all | 1740 | 29 | 1740 | 0.440 | 0.42-0.46 | 0.574 | 0.447 | -0.0860 | 0.138 | 0.65 | -48.9 |
| analog_k100|h4|on_time | 1740 | 29 | 1740 | 0.440 | 0.42-0.46 | 0.574 | 0.447 | -0.0860 | 0.138 | 0.65 | -48.9 |
| base_rate|h1|all | 2220 | 37 | 2220 | 0.482 | 0.46-0.50 | 0.518 | 0.498 | +0.0000 | 0.020 | 0.00 | - |
| base_rate|h1|on_time | 2160 | 36 | 2160 | 0.485 | 0.46-0.51 | 0.515 | 0.498 | +0.0000 | 0.017 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 2040 | 34 | 2040 | 0.576 | 0.55-0.60 | 0.576 | 0.503 | +0.0000 | 0.073 | 0.00 | - |
| base_rate|h4|on_time | 2040 | 34 | 2040 | 0.576 | 0.55-0.60 | 0.576 | 0.503 | +0.0000 | 0.073 | 0.00 | - |
| council|h1|all | 1920 | 32 | 338 | 0.550 | 0.50-0.60 | 0.520 | 0.495 | +0.0022 | 0.034 | 0.00 | +18.3 |
| council|h1|on_time | 1920 | 32 | 338 | 0.550 | 0.50-0.60 | 0.520 | 0.495 | +0.0022 | 0.034 | 0.00 | +18.3 |
| council|h4|all | 1740 | 29 | 20 | 0.600 | 0.39-0.78 | 0.574 | 0.500 | -0.0012 | 0.075 | 0.00 | - |
| council|h4|on_time | 1740 | 29 | 20 | 0.600 | 0.39-0.78 | 0.574 | 0.500 | -0.0012 | 0.075 | 0.00 | - |
| derivatives|h1|all | 1920 | 32 | 1920 | 0.478 | 0.46-0.50 | 0.520 | 0.498 | -0.0001 | 0.024 | 0.00 | - |
| derivatives|h1|on_time | 1920 | 32 | 1920 | 0.478 | 0.46-0.50 | 0.520 | 0.498 | -0.0001 | 0.024 | 0.00 | - |
| derivatives|h4|all | 1740 | 29 | 1740 | 0.573 | 0.55-0.60 | 0.574 | 0.502 | -0.0001 | 0.072 | 0.00 | -117.6 |
| derivatives|h4|on_time | 1740 | 29 | 1740 | 0.573 | 0.55-0.60 | 0.574 | 0.502 | -0.0001 | 0.072 | 0.00 | -117.6 |
| lgbm_calibrated|h1|all | 2220 | 37 | 2220 | 0.549 | 0.53-0.57 | 0.518 | 0.474 | +0.0044 | 0.045 | 0.12 | +5.9 |
| lgbm_calibrated|h1|on_time | 2160 | 36 | 2160 | 0.555 | 0.53-0.58 | 0.515 | 0.474 | +0.0055 | 0.041 | 0.13 | +5.9 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 2040 | 34 | 2040 | 0.423 | 0.40-0.44 | 0.576 | 0.458 | -0.0314 | 0.121 | 0.24 | -50.2 |
| lgbm_calibrated|h4|on_time | 2040 | 34 | 2040 | 0.423 | 0.40-0.44 | 0.576 | 0.458 | -0.0314 | 0.121 | 0.24 | -50.2 |
| logistic|h1|all | 2220 | 37 | 2220 | 0.535 | 0.51-0.56 | 0.518 | 0.491 | +0.0069 | 0.031 | 0.10 | +3.0 |
| logistic|h1|on_time | 2160 | 36 | 2160 | 0.528 | 0.51-0.55 | 0.515 | 0.490 | +0.0055 | 0.028 | 0.10 | +3.4 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 2040 | 34 | 2040 | 0.505 | 0.48-0.53 | 0.576 | 0.493 | -0.0055 | 0.083 | 0.20 | +0.1 |
| logistic|h4|on_time | 2040 | 34 | 2040 | 0.505 | 0.48-0.53 | 0.576 | 0.493 | -0.0055 | 0.083 | 0.20 | +0.1 |
| momentum_24|h1|all | 2220 | 37 | 2220 | 0.543 | 0.52-0.56 | 0.518 | 0.496 | +0.0029 | 0.033 | 0.00 | - |
| momentum_24|h1|on_time | 2160 | 36 | 2160 | 0.539 | 0.52-0.56 | 0.515 | 0.496 | +0.0026 | 0.029 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 2040 | 34 | 2040 | 0.576 | 0.55-0.60 | 0.576 | 0.503 | +0.0000 | 0.073 | 0.00 | - |
| momentum_24|h4|on_time | 2040 | 34 | 2040 | 0.576 | 0.55-0.60 | 0.576 | 0.503 | +0.0000 | 0.073 | 0.00 | - |
| orthosys|h1|all | 2220 | 37 | 184 | 0.538 | 0.47-0.61 | 0.518 | 0.498 | +0.0008 | 0.023 | 0.00 | - |
| orthosys|h1|on_time | 2160 | 36 | 183 | 0.536 | 0.46-0.61 | 0.515 | 0.498 | +0.0006 | 0.019 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 2040 | 34 | 179 | 0.441 | 0.37-0.51 | 0.576 | 0.499 | -0.0021 | 0.078 | 0.00 | - |
| orthosys|h4|on_time | 2040 | 34 | 179 | 0.441 | 0.37-0.51 | 0.576 | 0.499 | -0.0021 | 0.078 | 0.00 | - |
| recent_base_rate_7d|h1|all | 2160 | 36 | 2160 | 0.485 | 0.46-0.51 | 0.515 | 0.474 | -0.0056 | 0.041 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 2160 | 36 | 2160 | 0.485 | 0.46-0.51 | 0.515 | 0.474 | -0.0056 | 0.041 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1980 | 33 | 1980 | 0.415 | 0.39-0.44 | 0.585 | 0.441 | -0.0605 | 0.144 | 0.91 | -70.0 |
| recent_base_rate_7d|h4|on_time | 1980 | 33 | 1980 | 0.415 | 0.39-0.44 | 0.585 | 0.441 | -0.0605 | 0.144 | 0.91 | -70.0 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 953.84 | -4.62% | 1008 | 397 | 32 |
| analog_k100|h4 | 968.20 | -3.18% | 1128 | 439 | 29 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 37 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 34 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 32 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 29 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 32 |
| derivatives|h4 | 985.33 | -1.47% | 5 | 1 | 29 |
| lgbm_calibrated|h1 | 933.77 | -6.62% | 274 | 135 | 37 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 34 |
| logistic|h1 | 1011.03 | +1.10% | 221 | 118 | 37 |
| logistic|h4 | 1026.43 | +2.64% | 410 | 197 | 34 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 37 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 34 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 37 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 34 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 36 |
| recent_base_rate_7d|h4 | 948.69 | -5.13% | 1800 | 696 | 33 |
| benchmark_long_all_coins|h1 | 1017.10 | +1.71% | 2220 | 1047 | 37 |
| benchmark_long_all_coins|h4 | 1041.40 | +4.14% | 2040 | 1101 | 34 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 29 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 33 |

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
