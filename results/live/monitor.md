# Live monitor (2026-10-21T06:08:31.242095+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.56 (ECE 0.132)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.470
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.57 (ECE 0.110)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.456
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.57 (ECE 0.132)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.449

## Health

- **venue**: okx
- **symbols**: 61
- **universe_size**: 60
- **fetched_only_for_scoring**: ['ENSO']
- **last_closed_bar**: 2026-10-21 05:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 6.5
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 101.8 instruments 61/61']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.123, 'recent_base_rate_7d': 0.092, 'momentum_24': 0.145, 'logistic': 0.181, 'lgbm_calibrated': 0.157, 'analog_k100': 0.048, 'derivatives': 0.126, 'orthosys': 0.128}
- **council_member_logloss_h1**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.6961, 'momentum_24': 0.6919, 'logistic': 0.6899, 'lgbm_calibrated': 0.6911, 'analog_k100': 0.7035, 'derivatives': 0.6934, 'orthosys': 0.693}
- **council_calls_h1**: 8
- **council_abstain_h1**: {'no_edge': 50, 'spoke': 8, 'extreme_volatility': 2}
- **council_weights_h4**: {'base_rate': 0.205, 'recent_base_rate_7d': 0.01, 'momentum_24': 0.205, 'logistic': 0.153, 'lgbm_calibrated': 0.042, 'analog_k100': 0.004, 'derivatives': 0.198, 'orthosys': 0.184}
- **council_member_logloss_h4**: {'base_rate': 0.6924, 'recent_base_rate_7d': 0.7227, 'momentum_24': 0.6924, 'logistic': 0.6953, 'lgbm_calibrated': 0.7081, 'analog_k100': 0.7371, 'derivatives': 0.6925, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 57, 'extreme_volatility': 2, 'members_disagree': 1}
- **prediction_latency_min**: 8.4
- **price_snapshot_age_s**: 0.7
- **train_rows_h1**: 89581
- **orthosys_hist_hit_h1**: 0.527
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0078
- **p_spread_logistic_h1**: 0.0218
- **p_spread_lgbm_calibrated_h1**: 0.0153
- **p_spread_analog_k100_h1**: 0.0633
- **p_spread_derivatives_h1**: 0.0037
- **p_spread_orthosys_h1**: 0.0035
- **p_spread_council_h1**: 0.0078
- **train_rows_h4**: 89398
- **orthosys_hist_hit_h4**: 0.5134
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0003
- **p_spread_logistic_h4**: 0.0464
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0776
- **p_spread_derivatives_h4**: 0.0117
- **p_spread_orthosys_h4**: 0.0017
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 40200

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1980 | 33 | 1980 | 0.512 | 0.49-0.53 | 0.512 | 0.465 | -0.0165 | 0.051 | 0.53 | -12.0 |
| analog_k100|h1|on_time | 1980 | 33 | 1980 | 0.512 | 0.49-0.53 | 0.512 | 0.465 | -0.0165 | 0.051 | 0.53 | -12.0 |
| analog_k100|h4|all | 1800 | 30 | 1800 | 0.447 | 0.42-0.47 | 0.561 | 0.447 | -0.0804 | 0.132 | 0.65 | -45.5 |
| analog_k100|h4|on_time | 1800 | 30 | 1800 | 0.447 | 0.42-0.47 | 0.561 | 0.447 | -0.0804 | 0.132 | 0.65 | -45.5 |
| base_rate|h1|all | 2280 | 38 | 2280 | 0.489 | 0.47-0.51 | 0.511 | 0.498 | +0.0000 | 0.013 | 0.00 | - |
| base_rate|h1|on_time | 2220 | 37 | 2220 | 0.493 | 0.47-0.51 | 0.507 | 0.498 | +0.0000 | 0.009 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 2100 | 35 | 2100 | 0.565 | 0.54-0.59 | 0.565 | 0.503 | +0.0000 | 0.062 | 0.00 | - |
| base_rate|h4|on_time | 2100 | 35 | 2100 | 0.565 | 0.54-0.59 | 0.565 | 0.503 | +0.0000 | 0.062 | 0.00 | - |
| council|h1|all | 1980 | 33 | 342 | 0.550 | 0.50-0.60 | 0.512 | 0.495 | +0.0019 | 0.025 | 0.00 | +18.3 |
| council|h1|on_time | 1980 | 33 | 342 | 0.550 | 0.50-0.60 | 0.512 | 0.495 | +0.0019 | 0.025 | 0.00 | +18.3 |
| council|h4|all | 1800 | 30 | 20 | 0.600 | 0.39-0.78 | 0.561 | 0.500 | -0.0008 | 0.062 | 0.00 | - |
| council|h4|on_time | 1800 | 30 | 20 | 0.600 | 0.39-0.78 | 0.561 | 0.500 | -0.0008 | 0.062 | 0.00 | - |
| derivatives|h1|all | 1980 | 33 | 1980 | 0.486 | 0.46-0.51 | 0.512 | 0.498 | -0.0001 | 0.016 | 0.00 | - |
| derivatives|h1|on_time | 1980 | 33 | 1980 | 0.486 | 0.46-0.51 | 0.512 | 0.498 | -0.0001 | 0.016 | 0.00 | - |
| derivatives|h4|all | 1800 | 30 | 1800 | 0.562 | 0.54-0.58 | 0.561 | 0.503 | -0.0000 | 0.059 | 0.00 | -117.6 |
| derivatives|h4|on_time | 1800 | 30 | 1800 | 0.562 | 0.54-0.58 | 0.561 | 0.503 | -0.0000 | 0.059 | 0.00 | -117.6 |
| lgbm_calibrated|h1|all | 2280 | 38 | 2280 | 0.555 | 0.53-0.58 | 0.511 | 0.475 | +0.0045 | 0.037 | 0.12 | +6.3 |
| lgbm_calibrated|h1|on_time | 2220 | 37 | 2220 | 0.560 | 0.54-0.58 | 0.507 | 0.475 | +0.0056 | 0.034 | 0.12 | +6.3 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 2100 | 35 | 2100 | 0.434 | 0.41-0.46 | 0.565 | 0.458 | -0.0280 | 0.110 | 0.23 | -50.2 |
| lgbm_calibrated|h4|on_time | 2100 | 35 | 2100 | 0.434 | 0.41-0.46 | 0.565 | 0.458 | -0.0280 | 0.110 | 0.23 | -50.2 |
| logistic|h1|all | 2280 | 38 | 2280 | 0.539 | 0.52-0.56 | 0.511 | 0.491 | +0.0071 | 0.023 | 0.10 | +2.3 |
| logistic|h1|on_time | 2220 | 37 | 2220 | 0.532 | 0.51-0.55 | 0.507 | 0.490 | +0.0057 | 0.021 | 0.10 | +2.6 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 2100 | 35 | 2100 | 0.505 | 0.48-0.53 | 0.565 | 0.494 | -0.0051 | 0.072 | 0.20 | -3.9 |
| logistic|h4|on_time | 2100 | 35 | 2100 | 0.505 | 0.48-0.53 | 0.565 | 0.494 | -0.0051 | 0.072 | 0.20 | -3.9 |
| momentum_24|h1|all | 2280 | 38 | 2280 | 0.539 | 0.52-0.56 | 0.511 | 0.496 | +0.0026 | 0.028 | 0.00 | - |
| momentum_24|h1|on_time | 2220 | 37 | 2220 | 0.534 | 0.51-0.55 | 0.507 | 0.496 | +0.0023 | 0.024 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 2100 | 35 | 2100 | 0.565 | 0.54-0.59 | 0.565 | 0.503 | -0.0000 | 0.062 | 0.00 | - |
| momentum_24|h4|on_time | 2100 | 35 | 2100 | 0.565 | 0.54-0.59 | 0.565 | 0.503 | -0.0000 | 0.062 | 0.00 | - |
| orthosys|h1|all | 2280 | 38 | 185 | 0.535 | 0.46-0.61 | 0.511 | 0.498 | +0.0005 | 0.015 | 0.00 | - |
| orthosys|h1|on_time | 2220 | 37 | 184 | 0.533 | 0.46-0.60 | 0.507 | 0.498 | +0.0004 | 0.011 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 2100 | 35 | 182 | 0.445 | 0.37-0.52 | 0.565 | 0.499 | -0.0017 | 0.066 | 0.00 | - |
| orthosys|h4|on_time | 2100 | 35 | 182 | 0.445 | 0.37-0.52 | 0.565 | 0.499 | -0.0017 | 0.066 | 0.00 | - |
| recent_base_rate_7d|h1|all | 2220 | 37 | 2220 | 0.493 | 0.47-0.51 | 0.507 | 0.474 | -0.0041 | 0.034 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 2220 | 37 | 2220 | 0.493 | 0.47-0.51 | 0.507 | 0.474 | -0.0041 | 0.034 | 0.00 | - |
| recent_base_rate_7d|h4|all | 2040 | 34 | 2040 | 0.427 | 0.41-0.45 | 0.573 | 0.441 | -0.0550 | 0.132 | 0.88 | -70.0 |
| recent_base_rate_7d|h4|on_time | 2040 | 34 | 2040 | 0.427 | 0.41-0.45 | 0.573 | 0.441 | -0.0550 | 0.132 | 0.88 | -70.0 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 958.45 | -4.16% | 1046 | 425 | 33 |
| analog_k100|h4 | 969.77 | -3.02% | 1163 | 461 | 30 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 38 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 35 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 33 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 30 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 33 |
| derivatives|h4 | 985.33 | -1.47% | 5 | 1 | 30 |
| lgbm_calibrated|h1 | 945.98 | -5.40% | 275 | 136 | 38 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 35 |
| logistic|h1 | 1002.56 | +0.26% | 223 | 119 | 38 |
| logistic|h4 | 1022.54 | +2.25% | 421 | 201 | 35 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 38 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 35 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 38 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 35 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 37 |
| recent_base_rate_7d|h4 | 948.69 | -5.13% | 1800 | 696 | 34 |
| benchmark_long_all_coins|h1 | 1013.00 | +1.30% | 2280 | 1053 | 38 |
| benchmark_long_all_coins|h4 | 1039.50 | +3.95% | 2100 | 1110 | 35 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 33 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 38 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 34 |

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
