# Live monitor (2026-10-19T23:07:46.155352+00:00)

## Alerts

- LATENCY SLIPPAGE: analog_k100|h1|all live price differs from bar close by +25.6 bps on average
- MISCALIBRATED: base_rate|h1|all says 0.50 on average, reality 0.60 (ECE 0.100)
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.450
- LATENCY SLIPPAGE: base_rate|h1|all live price differs from bar close by +20.9 bps on average
- LATENCY SLIPPAGE: base_rate|h4|all live price differs from bar close by +18.1 bps on average
- LATENCY SLIPPAGE: council|h1|all live price differs from bar close by +25.6 bps on average
- LATENCY SLIPPAGE: derivatives|h1|all live price differs from bar close by +25.6 bps on average
- MISCALIBRATED: lgbm_calibrated|h1|all says 0.47 on average, reality 0.60 (ECE 0.124)
- LATENCY SLIPPAGE: lgbm_calibrated|h1|all live price differs from bar close by +20.9 bps on average
- LATENCY SLIPPAGE: lgbm_calibrated|h4|all live price differs from bar close by +18.1 bps on average
- MISCALIBRATED: logistic|h1|all says 0.49 on average, reality 0.60 (ECE 0.107)
- LATENCY SLIPPAGE: logistic|h1|all live price differs from bar close by +20.9 bps on average
- LATENCY SLIPPAGE: logistic|h4|all live price differs from bar close by +18.1 bps on average
- MISCALIBRATED: momentum_24|h1|all says 0.50 on average, reality 0.60 (ECE 0.095)
- LATENCY SLIPPAGE: momentum_24|h1|all live price differs from bar close by +20.9 bps on average
- LATENCY SLIPPAGE: momentum_24|h4|all live price differs from bar close by +18.1 bps on average
- MISCALIBRATED: orthosys|h1|all says 0.50 on average, reality 0.60 (ECE 0.098)
- LATENCY SLIPPAGE: orthosys|h1|all live price differs from bar close by +20.9 bps on average
- LATENCY SLIPPAGE: orthosys|h4|all live price differs from bar close by +18.1 bps on average
- MISCALIBRATED: recent_base_rate_7d|h1|all says 0.47 on average, reality 0.59 (ECE 0.121)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.463
- LATENCY SLIPPAGE: recent_base_rate_7d|h1|all live price differs from bar close by +19.6 bps on average

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['SHIB', 'XLM']
- **last_closed_bar**: 2026-10-19 22:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.8
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 105.8 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.126, 'recent_base_rate_7d': 0.12, 'momentum_24': 0.132, 'logistic': 0.141, 'lgbm_calibrated': 0.116, 'analog_k100': 0.107, 'derivatives': 0.13, 'orthosys': 0.127}
- **council_member_logloss_h1**: {'base_rate': 0.6936, 'recent_base_rate_7d': 0.6975, 'momentum_24': 0.6911, 'logistic': 0.6873, 'lgbm_calibrated': 0.6982, 'analog_k100': 0.7591, 'derivatives': 0.6957, 'orthosys': 0.6932}
- **council_calls_h1**: 4
- **council_abstain_h1**: {'no_edge': 53, 'spoke': 4, 'extreme_volatility': 3}
- **council_weights_h4**: {'base_rate': 0.123, 'recent_base_rate_7d': 0.12, 'momentum_24': 0.123, 'logistic': 0.111, 'lgbm_calibrated': 0.152, 'analog_k100': 0.123, 'derivatives': 0.123, 'orthosys': 0.124}
- **council_member_logloss_h4**: {'base_rate': 0.6945, 'recent_base_rate_7d': 0.6983, 'momentum_24': 0.6944, 'logistic': 0.7063, 'lgbm_calibrated': 0.6714, 'orthosys': 0.6934}
- **council_calls_h4**: 2
- **council_abstain_h4**: {'members_disagree': 37, 'no_edge': 18, 'extreme_volatility': 3, 'spoke': 2}
- **prediction_latency_min**: 7.7
- **price_snapshot_age_s**: 0.9
- **train_rows_h1**: 89710
- **orthosys_hist_hit_h1**: 0.5283
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0098
- **p_spread_logistic_h1**: 0.0222
- **p_spread_lgbm_calibrated_h1**: 0.0139
- **p_spread_analog_k100_h1**: 0.0492
- **p_spread_derivatives_h1**: 0.0005
- **p_spread_orthosys_h1**: 0.0052
- **p_spread_council_h1**: 0.007
- **train_rows_h4**: 89524
- **orthosys_hist_hit_h4**: 0.5149
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0001
- **p_spread_logistic_h4**: 0.0415
- **p_spread_lgbm_calibrated_h4**: 0.007
- **p_spread_analog_k100_h4**: 0.0677
- **p_spread_derivatives_h4**: 0.0039
- **p_spread_orthosys_h4**: 0.0027
- **p_spread_council_h4**: 0.0055
- **predictions_written**: 1080
- **resolved_this_cycle**: 900
- **ledger_chain_valid**: True
- **ledger_rows**: 6720

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 120 | 2 | 120 | 0.367 | 0.29-0.46 | 0.825 | 0.471 | -0.1086 | 0.366 | 0.43 | -37.5 |
| analog_k100|h1|on_time | 120 | 2 | 120 | 0.367 | 0.29-0.46 | 0.825 | 0.471 | -0.1086 | 0.366 | 0.43 | -37.5 |
| base_rate|h1|all | 420 | 7 | 420 | 0.402 | 0.36-0.45 | 0.598 | 0.498 | +0.0000 | 0.100 | 0.00 | - |
| base_rate|h1|on_time | 360 | 6 | 360 | 0.411 | 0.36-0.46 | 0.589 | 0.498 | +0.0000 | 0.091 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 240 | 4 | 240 | 0.525 | 0.46-0.59 | 0.525 | 0.503 | +0.0000 | 0.022 | 0.00 | - |
| base_rate|h4|on_time | 240 | 4 | 240 | 0.525 | 0.46-0.59 | 0.525 | 0.503 | +0.0000 | 0.022 | 0.00 | - |
| council|h1|all | 120 | 2 | 33 | 0.182 | 0.09-0.34 | 0.825 | 0.493 | -0.0129 | 0.332 | 0.00 | - |
| council|h1|on_time | 120 | 2 | 33 | 0.182 | 0.09-0.34 | 0.825 | 0.493 | -0.0129 | 0.332 | 0.00 | - |
| derivatives|h1|all | 120 | 2 | 120 | 0.150 | 0.10-0.22 | 0.825 | 0.498 | -0.0006 | 0.352 | 0.00 | - |
| derivatives|h1|on_time | 120 | 2 | 120 | 0.150 | 0.10-0.22 | 0.825 | 0.498 | -0.0006 | 0.352 | 0.00 | - |
| lgbm_calibrated|h1|all | 420 | 7 | 420 | 0.471 | 0.42-0.52 | 0.598 | 0.474 | -0.0138 | 0.124 | 0.15 | -33.8 |
| lgbm_calibrated|h1|on_time | 360 | 6 | 360 | 0.492 | 0.44-0.54 | 0.589 | 0.475 | -0.0099 | 0.114 | 0.17 | -33.8 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 240 | 4 | 240 | 0.475 | 0.41-0.54 | 0.525 | 0.455 | +0.0088 | 0.070 | 0.41 | +46.6 |
| lgbm_calibrated|h4|on_time | 240 | 4 | 240 | 0.475 | 0.41-0.54 | 0.525 | 0.455 | +0.0088 | 0.070 | 0.41 | +46.6 |
| logistic|h1|all | 420 | 7 | 420 | 0.569 | 0.52-0.62 | 0.598 | 0.494 | +0.0026 | 0.107 | 0.04 | -116.6 |
| logistic|h1|on_time | 360 | 6 | 360 | 0.533 | 0.48-0.58 | 0.589 | 0.490 | -0.0067 | 0.103 | 0.04 | -135.6 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 240 | 4 | 240 | 0.471 | 0.41-0.53 | 0.525 | 0.510 | -0.0224 | 0.058 | 0.15 | -47.5 |
| logistic|h4|on_time | 240 | 4 | 240 | 0.471 | 0.41-0.53 | 0.525 | 0.510 | -0.0224 | 0.058 | 0.15 | -47.5 |
| momentum_24|h1|all | 420 | 7 | 420 | 0.595 | 0.55-0.64 | 0.598 | 0.502 | +0.0069 | 0.095 | 0.00 | - |
| momentum_24|h1|on_time | 360 | 6 | 360 | 0.578 | 0.53-0.63 | 0.589 | 0.502 | +0.0057 | 0.086 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 240 | 4 | 240 | 0.525 | 0.46-0.59 | 0.525 | 0.503 | +0.0001 | 0.022 | 0.00 | - |
| momentum_24|h4|on_time | 240 | 4 | 240 | 0.525 | 0.46-0.59 | 0.525 | 0.503 | +0.0001 | 0.022 | 0.00 | - |
| orthosys|h1|all | 420 | 7 | 13 | 0.462 | 0.23-0.71 | 0.598 | 0.500 | +0.0014 | 0.098 | 0.00 | - |
| orthosys|h1|on_time | 360 | 6 | 12 | 0.417 | 0.19-0.68 | 0.589 | 0.500 | +0.0009 | 0.089 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 240 | 4 | 5 | 0.400 | 0.12-0.77 | 0.525 | 0.500 | -0.0002 | 0.025 | 0.00 | - |
| orthosys|h4|on_time | 240 | 4 | 5 | 0.400 | 0.12-0.77 | 0.525 | 0.500 | -0.0002 | 0.025 | 0.00 | - |
| recent_base_rate_7d|h1|all | 360 | 6 | 360 | 0.411 | 0.36-0.46 | 0.589 | 0.468 | -0.0242 | 0.121 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 360 | 6 | 360 | 0.411 | 0.36-0.46 | 0.589 | 0.468 | -0.0242 | 0.121 | 0.00 | - |
| recent_base_rate_7d|h4|all | 180 | 3 | 180 | 0.400 | 0.33-0.47 | 0.600 | 0.429 | -0.0777 | 0.171 | 1.00 | -36.3 |
| recent_base_rate_7d|h4|on_time | 180 | 3 | 180 | 0.400 | 0.33-0.47 | 0.600 | 0.429 | -0.0777 | 0.171 | 1.00 | -36.3 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 992.53 | -0.75% | 52 | 9 | 2 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 7 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 4 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 2 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 2 |
| lgbm_calibrated|h1 | 968.57 | -3.14% | 61 | 13 | 7 |
| lgbm_calibrated|h4 | 1001.68 | +0.17% | 99 | 70 | 4 |
| logistic|h1 | 925.33 | -7.47% | 18 | 6 | 7 |
| logistic|h4 | 1000.63 | +0.06% | 35 | 13 | 4 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 7 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 4 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 7 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 4 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 6 |
| recent_base_rate_7d|h4 | 997.28 | -0.27% | 180 | 76 | 3 |
| benchmark_long_all_coins|h1 | 988.29 | -1.17% | 420 | 132 | 7 |
| benchmark_long_all_coins|h4 | 999.87 | -0.01% | 240 | 93 | 4 |

## Unverified (pending, not scored)

- analog_k100|h1: 60
- analog_k100|h4: 180
- base_rate|h1: 60
- base_rate|h4: 240
- council|h1: 60
- council|h4: 180
- derivatives|h1: 60
- derivatives|h4: 180
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
