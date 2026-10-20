# Live monitor (2026-10-20T03:06:54.142278+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- LATENCY SLIPPAGE: base_rate|h4|all live price differs from bar close by +17.4 bps on average
- LATENCY SLIPPAGE: lgbm_calibrated|h4|all live price differs from bar close by +17.4 bps on average
- LATENCY SLIPPAGE: logistic|h4|all live price differs from bar close by +17.4 bps on average
- LATENCY SLIPPAGE: momentum_24|h4|all live price differs from bar close by +17.4 bps on average
- LATENCY SLIPPAGE: orthosys|h4|all live price differs from bar close by +17.4 bps on average
- LATENCY SLIPPAGE: recent_base_rate_7d|h4|all live price differs from bar close by +15.8 bps on average

## Health

- **venue**: okx
- **symbols**: 63
- **universe_size**: 60
- **fetched_only_for_scoring**: ['CHIP', 'TRX', 'W']
- **last_closed_bar**: 2026-10-20 02:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.8
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 109.1 instruments 63/63']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.129, 'recent_base_rate_7d': 0.112, 'momentum_24': 0.14, 'logistic': 0.136, 'lgbm_calibrated': 0.12, 'analog_k100': 0.1, 'derivatives': 0.132, 'orthosys': 0.131}
- **council_member_logloss_h1**: {'base_rate': 0.6936, 'recent_base_rate_7d': 0.6991, 'momentum_24': 0.6909, 'logistic': 0.6919, 'lgbm_calibrated': 0.696, 'analog_k100': 0.7128, 'derivatives': 0.6941, 'orthosys': 0.6932}
- **council_calls_h1**: 2
- **council_abstain_h1**: {'no_edge': 55, 'extreme_volatility': 3, 'spoke': 2}
- **council_weights_h4**: {'base_rate': 0.151, 'recent_base_rate_7d': 0.058, 'momentum_24': 0.151, 'logistic': 0.12, 'lgbm_calibrated': 0.106, 'analog_k100': 0.119, 'derivatives': 0.147, 'orthosys': 0.147}
- **council_member_logloss_h4**: {'base_rate': 0.6921, 'recent_base_rate_7d': 0.7448, 'momentum_24': 0.6921, 'logistic': 0.703, 'lgbm_calibrated': 0.7093, 'analog_k100': 0.7264, 'derivatives': 0.6915, 'orthosys': 0.6934}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 49, 'members_disagree': 8, 'extreme_volatility': 3}
- **prediction_latency_min**: 6.8
- **price_snapshot_age_s**: 0.7
- **train_rows_h1**: 91447
- **orthosys_hist_hit_h1**: 0.5269
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.01
- **p_spread_logistic_h1**: 0.0184
- **p_spread_lgbm_calibrated_h1**: 0.0024
- **p_spread_analog_k100_h1**: 0.0594
- **p_spread_derivatives_h1**: 0.0018
- **p_spread_orthosys_h1**: 0.0049
- **p_spread_council_h1**: 0.0054
- **train_rows_h4**: 91258
- **orthosys_hist_hit_h4**: 0.5152
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0005
- **p_spread_logistic_h4**: 0.0265
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0822
- **p_spread_derivatives_h4**: 0.0058
- **p_spread_orthosys_h4**: 0.0028
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 11040

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 360 | 6 | 360 | 0.497 | 0.45-0.55 | 0.608 | 0.490 | -0.0261 | 0.130 | 0.42 | -8.9 |
| analog_k100|h1|on_time | 360 | 6 | 360 | 0.497 | 0.45-0.55 | 0.608 | 0.490 | -0.0261 | 0.130 | 0.42 | -8.9 |
| analog_k100|h4|all | 180 | 3 | 180 | 0.494 | 0.42-0.57 | 0.578 | 0.438 | -0.0429 | 0.142 | 0.67 | -16.9 |
| analog_k100|h4|on_time | 180 | 3 | 180 | 0.494 | 0.42-0.57 | 0.578 | 0.438 | -0.0429 | 0.142 | 0.67 | -16.9 |
| base_rate|h1|all | 660 | 11 | 660 | 0.438 | 0.40-0.48 | 0.562 | 0.498 | +0.0000 | 0.064 | 0.00 | - |
| base_rate|h1|on_time | 600 | 10 | 600 | 0.447 | 0.41-0.49 | 0.553 | 0.498 | +0.0000 | 0.055 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 480 | 8 | 480 | 0.585 | 0.54-0.63 | 0.585 | 0.503 | +0.0000 | 0.082 | 0.00 | - |
| base_rate|h4|on_time | 480 | 8 | 480 | 0.585 | 0.54-0.63 | 0.585 | 0.503 | +0.0000 | 0.082 | 0.00 | - |
| council|h1|all | 360 | 6 | 41 | 0.317 | 0.20-0.47 | 0.608 | 0.497 | -0.0026 | 0.111 | 0.00 | - |
| council|h1|on_time | 360 | 6 | 41 | 0.317 | 0.20-0.47 | 0.608 | 0.497 | -0.0026 | 0.111 | 0.00 | - |
| council|h4|all | 180 | 3 | 10 | 0.900 | 0.60-0.98 | 0.578 | 0.499 | +0.0025 | 0.115 | 0.00 | - |
| council|h4|on_time | 180 | 3 | 10 | 0.900 | 0.60-0.98 | 0.578 | 0.499 | +0.0025 | 0.115 | 0.00 | - |
| derivatives|h1|all | 360 | 6 | 360 | 0.378 | 0.33-0.43 | 0.608 | 0.498 | -0.0003 | 0.124 | 0.00 | - |
| derivatives|h1|on_time | 360 | 6 | 360 | 0.378 | 0.33-0.43 | 0.608 | 0.498 | -0.0003 | 0.124 | 0.00 | - |
| derivatives|h4|all | 180 | 3 | 180 | 0.578 | 0.50-0.65 | 0.578 | 0.503 | -0.0007 | 0.075 | 0.00 | - |
| derivatives|h4|on_time | 180 | 3 | 180 | 0.578 | 0.50-0.65 | 0.578 | 0.503 | -0.0007 | 0.075 | 0.00 | - |
| lgbm_calibrated|h1|all | 660 | 11 | 660 | 0.482 | 0.44-0.52 | 0.562 | 0.474 | -0.0073 | 0.088 | 0.09 | -33.8 |
| lgbm_calibrated|h1|on_time | 600 | 10 | 600 | 0.495 | 0.46-0.53 | 0.553 | 0.475 | -0.0043 | 0.078 | 0.10 | -33.8 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 480 | 8 | 480 | 0.415 | 0.37-0.46 | 0.585 | 0.457 | -0.0295 | 0.129 | 0.33 | -9.6 |
| lgbm_calibrated|h4|on_time | 480 | 8 | 480 | 0.415 | 0.37-0.46 | 0.585 | 0.457 | -0.0295 | 0.129 | 0.33 | -9.6 |
| logistic|h1|all | 660 | 11 | 660 | 0.538 | 0.50-0.58 | 0.562 | 0.490 | -0.0001 | 0.074 | 0.04 | -69.9 |
| logistic|h1|on_time | 600 | 10 | 600 | 0.513 | 0.47-0.55 | 0.553 | 0.487 | -0.0059 | 0.069 | 0.04 | -75.5 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 480 | 8 | 480 | 0.490 | 0.45-0.53 | 0.585 | 0.496 | -0.0182 | 0.090 | 0.15 | -58.3 |
| logistic|h4|on_time | 480 | 8 | 480 | 0.490 | 0.45-0.53 | 0.585 | 0.496 | -0.0182 | 0.090 | 0.15 | -58.3 |
| momentum_24|h1|all | 660 | 11 | 660 | 0.562 | 0.52-0.60 | 0.562 | 0.501 | +0.0044 | 0.061 | 0.00 | - |
| momentum_24|h1|on_time | 600 | 10 | 600 | 0.548 | 0.51-0.59 | 0.553 | 0.501 | +0.0034 | 0.052 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 480 | 8 | 480 | 0.585 | 0.54-0.63 | 0.585 | 0.503 | -0.0000 | 0.082 | 0.00 | - |
| momentum_24|h4|on_time | 480 | 8 | 480 | 0.585 | 0.54-0.63 | 0.585 | 0.503 | -0.0000 | 0.082 | 0.00 | - |
| orthosys|h1|all | 660 | 11 | 19 | 0.474 | 0.27-0.68 | 0.562 | 0.500 | +0.0009 | 0.062 | 0.00 | - |
| orthosys|h1|on_time | 600 | 10 | 18 | 0.444 | 0.25-0.66 | 0.553 | 0.500 | +0.0005 | 0.054 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 480 | 8 | 15 | 0.400 | 0.20-0.64 | 0.585 | 0.500 | -0.0023 | 0.085 | 0.00 | - |
| orthosys|h4|on_time | 480 | 8 | 15 | 0.400 | 0.20-0.64 | 0.585 | 0.500 | -0.0023 | 0.085 | 0.00 | - |
| recent_base_rate_7d|h1|all | 600 | 10 | 600 | 0.447 | 0.41-0.49 | 0.553 | 0.471 | -0.0149 | 0.082 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 600 | 10 | 600 | 0.447 | 0.41-0.49 | 0.553 | 0.471 | -0.0149 | 0.082 | 0.00 | - |
| recent_base_rate_7d|h4|all | 420 | 7 | 420 | 0.374 | 0.33-0.42 | 0.626 | 0.431 | -0.0910 | 0.195 | 1.00 | -40.9 |
| recent_base_rate_7d|h4|on_time | 420 | 7 | 420 | 0.374 | 0.33-0.42 | 0.626 | 0.431 | -0.0910 | 0.195 | 1.00 | -40.9 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 994.62 | -0.54% | 153 | 62 | 6 |
| analog_k100|h4 | 998.76 | -0.12% | 121 | 52 | 3 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 11 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 8 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 6 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 3 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 6 |
| derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 3 |
| lgbm_calibrated|h1 | 968.57 | -3.14% | 61 | 13 | 11 |
| lgbm_calibrated|h4 | 992.62 | -0.74% | 157 | 80 | 8 |
| logistic|h1 | 946.10 | -5.39% | 29 | 12 | 11 |
| logistic|h4 | 991.18 | -0.88% | 70 | 24 | 8 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 11 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 8 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 11 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 8 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 10 |
| recent_base_rate_7d|h4 | 992.87 | -0.71% | 420 | 160 | 7 |
| benchmark_long_all_coins|h1 | 994.01 | -0.60% | 660 | 264 | 11 |
| benchmark_long_all_coins|h4 | 1002.30 | +0.23% | 480 | 224 | 8 |

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
