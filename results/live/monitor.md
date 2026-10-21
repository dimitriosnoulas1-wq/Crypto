# Live monitor (2026-10-21T04:06:37.185503+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0009 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.58 (ECE 0.146)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.460
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.497
- MISCALIBRATED: base_rate|h4|all says 0.50 on average, reality 0.58 (ECE 0.081)
- MISCALIBRATED: council|h4|all says 0.50 on average, reality 0.58 (ECE 0.084)
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.493
- MISCALIBRATED: derivatives|h4|all says 0.50 on average, reality 0.58 (ECE 0.081)
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.58 (ECE 0.130)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.437
- MISCALIBRATED: logistic|h4|all says 0.49 on average, reality 0.58 (ECE 0.092)
- MISCALIBRATED: momentum_24|h4|all says 0.50 on average, reality 0.58 (ECE 0.081)
- MISCALIBRATED: orthosys|h4|all says 0.50 on average, reality 0.58 (ECE 0.086)
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.59 (ECE 0.153)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.429

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['DASH', 'ENSO']
- **last_closed_bar**: 2026-10-21 03:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.6
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 103.7 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.127, 'recent_base_rate_7d': 0.085, 'momentum_24': 0.146, 'logistic': 0.193, 'lgbm_calibrated': 0.146, 'analog_k100': 0.037, 'derivatives': 0.131, 'orthosys': 0.135}
- **council_member_logloss_h1**: {'base_rate': 0.6935, 'recent_base_rate_7d': 0.6975, 'momentum_24': 0.6922, 'logistic': 0.6896, 'lgbm_calibrated': 0.6922, 'analog_k100': 0.7075, 'derivatives': 0.6936, 'orthosys': 0.6929}
- **council_calls_h1**: 0
- **council_abstain_h1**: {'no_edge': 57, 'extreme_volatility': 3}
- **council_weights_h4**: {'base_rate': 0.204, 'recent_base_rate_7d': 0.009, 'momentum_24': 0.205, 'logistic': 0.161, 'lgbm_calibrated': 0.039, 'analog_k100': 0.004, 'derivatives': 0.197, 'orthosys': 0.181}
- **council_member_logloss_h4**: {'base_rate': 0.6923, 'recent_base_rate_7d': 0.7255, 'momentum_24': 0.6923, 'logistic': 0.6948, 'lgbm_calibrated': 0.7096, 'analog_k100': 0.7398, 'derivatives': 0.6924, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 57, 'extreme_volatility': 3}
- **prediction_latency_min**: 6.5
- **price_snapshot_age_s**: 0.8
- **train_rows_h1**: 90992
- **orthosys_hist_hit_h1**: 0.5274
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0058
- **p_spread_logistic_h1**: 0.0221
- **p_spread_lgbm_calibrated_h1**: 0.0102
- **p_spread_analog_k100_h1**: 0.0586
- **p_spread_derivatives_h1**: 0.0006
- **p_spread_orthosys_h1**: 0.0035
- **p_spread_council_h1**: 0.0
- **train_rows_h4**: 90806
- **orthosys_hist_hit_h4**: 0.5135
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0005
- **p_spread_logistic_h4**: 0.043
- **p_spread_lgbm_calibrated_h4**: 0.0009
- **p_spread_analog_k100_h4**: 0.0746
- **p_spread_derivatives_h4**: 0.0019
- **p_spread_orthosys_h4**: 0.0017
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 38040

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1860 | 31 | 1860 | 0.503 | 0.48-0.53 | 0.527 | 0.465 | -0.0231 | 0.067 | 0.53 | -14.6 |
| analog_k100|h1|on_time | 1860 | 31 | 1860 | 0.503 | 0.48-0.53 | 0.527 | 0.465 | -0.0231 | 0.067 | 0.53 | -14.6 |
| analog_k100|h4|all | 1680 | 28 | 1680 | 0.436 | 0.41-0.46 | 0.583 | 0.446 | -0.0894 | 0.146 | 0.65 | -52.4 |
| analog_k100|h4|on_time | 1680 | 28 | 1680 | 0.436 | 0.41-0.46 | 0.583 | 0.446 | -0.0894 | 0.146 | 0.65 | -52.4 |
| base_rate|h1|all | 2160 | 36 | 2160 | 0.475 | 0.45-0.50 | 0.525 | 0.498 | +0.0000 | 0.026 | 0.00 | - |
| base_rate|h1|on_time | 2100 | 35 | 2100 | 0.479 | 0.46-0.50 | 0.521 | 0.498 | +0.0000 | 0.023 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 1980 | 33 | 1980 | 0.584 | 0.56-0.61 | 0.584 | 0.503 | +0.0000 | 0.081 | 0.00 | - |
| base_rate|h4|on_time | 1980 | 33 | 1980 | 0.584 | 0.56-0.61 | 0.584 | 0.503 | +0.0000 | 0.081 | 0.00 | - |
| council|h1|all | 1860 | 31 | 338 | 0.550 | 0.50-0.60 | 0.527 | 0.495 | +0.0024 | 0.041 | 0.00 | +18.3 |
| council|h1|on_time | 1860 | 31 | 338 | 0.550 | 0.50-0.60 | 0.527 | 0.495 | +0.0024 | 0.041 | 0.00 | +18.3 |
| council|h4|all | 1680 | 28 | 20 | 0.600 | 0.39-0.78 | 0.583 | 0.500 | -0.0014 | 0.084 | 0.00 | - |
| council|h4|on_time | 1680 | 28 | 20 | 0.600 | 0.39-0.78 | 0.583 | 0.500 | -0.0014 | 0.084 | 0.00 | - |
| derivatives|h1|all | 1860 | 31 | 1860 | 0.470 | 0.45-0.49 | 0.527 | 0.498 | -0.0001 | 0.032 | 0.00 | - |
| derivatives|h1|on_time | 1860 | 31 | 1860 | 0.470 | 0.45-0.49 | 0.527 | 0.498 | -0.0001 | 0.032 | 0.00 | - |
| derivatives|h4|all | 1680 | 28 | 1680 | 0.581 | 0.56-0.60 | 0.583 | 0.502 | -0.0001 | 0.081 | 0.00 | -117.6 |
| derivatives|h4|on_time | 1680 | 28 | 1680 | 0.581 | 0.56-0.60 | 0.583 | 0.502 | -0.0001 | 0.081 | 0.00 | -117.6 |
| lgbm_calibrated|h1|all | 2160 | 36 | 2160 | 0.545 | 0.52-0.57 | 0.525 | 0.474 | +0.0041 | 0.051 | 0.13 | +5.9 |
| lgbm_calibrated|h1|on_time | 2100 | 35 | 2100 | 0.550 | 0.53-0.57 | 0.521 | 0.474 | +0.0053 | 0.047 | 0.13 | +5.9 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 1980 | 33 | 1980 | 0.415 | 0.39-0.44 | 0.584 | 0.457 | -0.0339 | 0.130 | 0.25 | -50.2 |
| lgbm_calibrated|h4|on_time | 1980 | 33 | 1980 | 0.415 | 0.39-0.44 | 0.584 | 0.457 | -0.0339 | 0.130 | 0.25 | -50.2 |
| logistic|h1|all | 2160 | 36 | 2160 | 0.533 | 0.51-0.55 | 0.525 | 0.491 | +0.0073 | 0.037 | 0.10 | +2.2 |
| logistic|h1|on_time | 2100 | 35 | 2100 | 0.526 | 0.50-0.55 | 0.521 | 0.490 | +0.0058 | 0.034 | 0.10 | +2.5 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 1980 | 33 | 1980 | 0.508 | 0.49-0.53 | 0.584 | 0.493 | -0.0056 | 0.092 | 0.20 | -0.2 |
| logistic|h4|on_time | 1980 | 33 | 1980 | 0.508 | 0.49-0.53 | 0.584 | 0.493 | -0.0056 | 0.092 | 0.20 | -0.2 |
| momentum_24|h1|all | 2160 | 36 | 2160 | 0.541 | 0.52-0.56 | 0.525 | 0.496 | +0.0028 | 0.031 | 0.00 | - |
| momentum_24|h1|on_time | 2100 | 35 | 2100 | 0.536 | 0.51-0.56 | 0.521 | 0.496 | +0.0025 | 0.026 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 1980 | 33 | 1980 | 0.584 | 0.56-0.61 | 0.584 | 0.503 | +0.0000 | 0.081 | 0.00 | - |
| momentum_24|h4|on_time | 1980 | 33 | 1980 | 0.584 | 0.56-0.61 | 0.584 | 0.503 | +0.0000 | 0.081 | 0.00 | - |
| orthosys|h1|all | 2160 | 36 | 183 | 0.541 | 0.47-0.61 | 0.525 | 0.498 | +0.0010 | 0.029 | 0.00 | - |
| orthosys|h1|on_time | 2100 | 35 | 182 | 0.538 | 0.47-0.61 | 0.521 | 0.498 | +0.0008 | 0.025 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 1980 | 33 | 178 | 0.438 | 0.37-0.51 | 0.584 | 0.499 | -0.0024 | 0.086 | 0.00 | - |
| orthosys|h4|on_time | 1980 | 33 | 178 | 0.438 | 0.37-0.51 | 0.584 | 0.499 | -0.0024 | 0.086 | 0.00 | - |
| recent_base_rate_7d|h1|all | 2100 | 35 | 2100 | 0.479 | 0.46-0.50 | 0.521 | 0.474 | -0.0068 | 0.047 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 2100 | 35 | 2100 | 0.479 | 0.46-0.50 | 0.521 | 0.474 | -0.0068 | 0.047 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1920 | 32 | 1920 | 0.407 | 0.39-0.43 | 0.593 | 0.440 | -0.0646 | 0.153 | 0.94 | -70.0 |
| recent_base_rate_7d|h4|on_time | 1920 | 32 | 1920 | 0.407 | 0.39-0.43 | 0.593 | 0.440 | -0.0646 | 0.153 | 0.94 | -70.0 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 954.09 | -4.59% | 977 | 383 | 31 |
| analog_k100|h4 | 966.58 | -3.34% | 1095 | 421 | 28 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 36 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 33 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 31 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 28 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 31 |
| derivatives|h4 | 985.33 | -1.47% | 5 | 1 | 28 |
| lgbm_calibrated|h1 | 933.77 | -6.62% | 274 | 135 | 36 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 33 |
| logistic|h1 | 1001.31 | +0.13% | 219 | 116 | 36 |
| logistic|h4 | 1025.84 | +2.58% | 404 | 195 | 33 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 36 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 33 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 36 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 33 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 35 |
| recent_base_rate_7d|h4 | 948.69 | -5.13% | 1800 | 696 | 32 |
| benchmark_long_all_coins|h1 | 1019.24 | +1.92% | 2160 | 1036 | 36 |
| benchmark_long_all_coins|h4 | 1040.82 | +4.08% | 1980 | 1079 | 33 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 32 |

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
