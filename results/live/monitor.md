# Live monitor (2026-10-19T22:07:09.472219+00:00)

## Alerts

- LATENCY SLIPPAGE: base_rate|h1|all live price differs from bar close by +16.1 bps on average
- LATENCY SLIPPAGE: base_rate|h4|all live price differs from bar close by +26.7 bps on average
- LATENCY SLIPPAGE: lgbm_calibrated|h1|all live price differs from bar close by +16.1 bps on average
- LATENCY SLIPPAGE: lgbm_calibrated|h4|all live price differs from bar close by +26.7 bps on average
- MISCALIBRATED: logistic|h1|all says 0.50 on average, reality 0.54 (ECE 0.126)
- LATENCY SLIPPAGE: logistic|h1|all live price differs from bar close by +16.1 bps on average
- LATENCY SLIPPAGE: logistic|h4|all live price differs from bar close by +26.7 bps on average
- LATENCY SLIPPAGE: momentum_24|h1|all live price differs from bar close by +16.1 bps on average
- LATENCY SLIPPAGE: momentum_24|h4|all live price differs from bar close by +26.7 bps on average
- LATENCY SLIPPAGE: orthosys|h1|all live price differs from bar close by +16.1 bps on average
- LATENCY SLIPPAGE: orthosys|h4|all live price differs from bar close by +26.7 bps on average
- LATENCY SLIPPAGE: recent_base_rate_7d|h4|all live price differs from bar close by +25.7 bps on average

## Health

- **venue**: okx
- **symbols**: 63
- **universe_size**: 60
- **fetched_only_for_scoring**: ['AERO', 'SHIB', 'XLM']
- **last_closed_bar**: 2026-10-19 21:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.0
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 111.9 instruments 63/63']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.119, 'recent_base_rate_7d': 0.123, 'momentum_24': 0.123, 'logistic': 0.143, 'lgbm_calibrated': 0.127, 'analog_k100': 0.123, 'derivatives': 0.123, 'orthosys': 0.119}
- **council_member_logloss_h1**: {'base_rate': 0.6933, 'recent_base_rate_7d': 0.6911, 'momentum_24': 0.6915, 'logistic': 0.6812, 'lgbm_calibrated': 0.6893, 'orthosys': 0.6934}
- **council_calls_h1**: 11
- **council_abstain_h1**: {'no_edge': 46, 'spoke': 11, 'extreme_volatility': 3}
- **council_weights_h4**: {'base_rate': 0.12, 'recent_base_rate_7d': 0.135, 'momentum_24': 0.12, 'logistic': 0.105, 'lgbm_calibrated': 0.157, 'analog_k100': 0.12, 'derivatives': 0.12, 'orthosys': 0.121}
- **council_member_logloss_h4**: {'base_rate': 0.696, 'recent_base_rate_7d': 0.6553, 'momentum_24': 0.6958, 'logistic': 0.7173, 'lgbm_calibrated': 0.6509, 'orthosys': 0.6938}
- **council_calls_h4**: 3
- **council_abstain_h4**: {'members_disagree': 35, 'no_edge': 19, 'extreme_volatility': 3, 'spoke': 3}
- **prediction_latency_min**: 7.1
- **price_snapshot_age_s**: 0.6
- **train_rows_h1**: 91150
- **orthosys_hist_hit_h1**: 0.5277
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0083
- **p_spread_logistic_h1**: 0.0223
- **p_spread_lgbm_calibrated_h1**: 0.0196
- **p_spread_analog_k100_h1**: 0.0504
- **p_spread_derivatives_h1**: 0.0004
- **p_spread_orthosys_h1**: 0.0062
- **p_spread_council_h1**: 0.0101
- **train_rows_h4**: 90961
- **orthosys_hist_hit_h4**: 0.5151
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0003
- **p_spread_logistic_h4**: 0.0354
- **p_spread_lgbm_calibrated_h4**: 0.0089
- **p_spread_analog_k100_h4**: 0.0684
- **p_spread_derivatives_h4**: 0.0027
- **p_spread_orthosys_h4**: 0.0034
- **p_spread_council_h4**: 0.0062
- **predictions_written**: 1080
- **resolved_this_cycle**: 900
- **ledger_chain_valid**: True
- **ledger_rows**: 5640

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 60 | 1 | 60 | 0.333 | 0.23-0.46 | 0.717 | 0.464 | -0.1250 | 0.275 | 0.45 | -40.0 |
| analog_k100|h1|on_time | 60 | 1 | 60 | 0.333 | 0.23-0.46 | 0.717 | 0.464 | -0.1250 | 0.275 | 0.45 | -40.0 |
| base_rate|h1|all | 360 | 6 | 360 | 0.458 | 0.41-0.51 | 0.542 | 0.498 | +0.0000 | 0.044 | 0.00 | - |
| base_rate|h1|on_time | 300 | 5 | 300 | 0.480 | 0.42-0.54 | 0.520 | 0.498 | +0.0000 | 0.022 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 180 | 3 | 180 | 0.422 | 0.35-0.50 | 0.422 | 0.504 | +0.0000 | 0.081 | 0.00 | - |
| base_rate|h4|on_time | 180 | 3 | 180 | 0.422 | 0.35-0.50 | 0.422 | 0.504 | +0.0000 | 0.081 | 0.00 | - |
| council|h1|all | 60 | 1 | 22 | 0.182 | 0.07-0.39 | 0.717 | 0.490 | -0.0204 | 0.226 | 0.00 | - |
| council|h1|on_time | 60 | 1 | 22 | 0.182 | 0.07-0.39 | 0.717 | 0.490 | -0.0204 | 0.226 | 0.00 | - |
| derivatives|h1|all | 60 | 1 | 60 | 0.233 | 0.14-0.35 | 0.717 | 0.498 | -0.0012 | 0.269 | 0.00 | - |
| derivatives|h1|on_time | 60 | 1 | 60 | 0.233 | 0.14-0.35 | 0.717 | 0.498 | -0.0012 | 0.269 | 0.00 | - |
| lgbm_calibrated|h1|all | 360 | 6 | 360 | 0.531 | 0.48-0.58 | 0.542 | 0.472 | -0.0092 | 0.070 | 0.17 | -33.8 |
| lgbm_calibrated|h1|on_time | 300 | 5 | 300 | 0.567 | 0.51-0.62 | 0.520 | 0.473 | -0.0036 | 0.047 | 0.20 | -33.8 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 180 | 3 | 180 | 0.578 | 0.50-0.65 | 0.422 | 0.452 | +0.0458 | 0.030 | 0.52 | +51.0 |
| lgbm_calibrated|h4|on_time | 180 | 3 | 180 | 0.578 | 0.50-0.65 | 0.422 | 0.452 | +0.0458 | 0.030 | 0.52 | +51.0 |
| logistic|h1|all | 360 | 6 | 360 | 0.636 | 0.59-0.68 | 0.542 | 0.496 | +0.0127 | 0.126 | 0.04 | -104.6 |
| logistic|h1|on_time | 300 | 5 | 300 | 0.607 | 0.55-0.66 | 0.520 | 0.491 | +0.0036 | 0.100 | 0.04 | -123.8 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 180 | 3 | 180 | 0.494 | 0.42-0.57 | 0.422 | 0.516 | -0.0221 | 0.117 | 0.16 | -89.9 |
| logistic|h4|on_time | 180 | 3 | 180 | 0.494 | 0.42-0.57 | 0.422 | 0.516 | -0.0221 | 0.117 | 0.16 | -89.9 |
| momentum_24|h1|all | 360 | 6 | 360 | 0.572 | 0.52-0.62 | 0.542 | 0.502 | +0.0051 | 0.064 | 0.00 | - |
| momentum_24|h1|on_time | 300 | 5 | 300 | 0.547 | 0.49-0.60 | 0.520 | 0.502 | +0.0032 | 0.039 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 180 | 3 | 180 | 0.422 | 0.35-0.50 | 0.422 | 0.503 | +0.0002 | 0.081 | 0.00 | - |
| momentum_24|h4|on_time | 180 | 3 | 180 | 0.422 | 0.35-0.50 | 0.422 | 0.503 | +0.0002 | 0.081 | 0.00 | - |
| orthosys|h1|all | 360 | 6 | 10 | 0.500 | 0.24-0.76 | 0.542 | 0.500 | +0.0008 | 0.042 | 0.00 | - |
| orthosys|h1|on_time | 300 | 5 | 9 | 0.444 | 0.19-0.73 | 0.520 | 0.500 | +0.0001 | 0.020 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 180 | 3 | 3 | 0.333 | 0.06-0.79 | 0.422 | 0.500 | +0.0023 | 0.084 | 0.00 | - |
| orthosys|h4|on_time | 180 | 3 | 3 | 0.333 | 0.06-0.79 | 0.422 | 0.500 | +0.0023 | 0.084 | 0.00 | - |
| recent_base_rate_7d|h1|all | 300 | 5 | 300 | 0.480 | 0.42-0.54 | 0.520 | 0.468 | -0.0081 | 0.052 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 300 | 5 | 300 | 0.480 | 0.42-0.54 | 0.520 | 0.468 | -0.0081 | 0.052 | 0.00 | - |
| recent_base_rate_7d|h4|all | 120 | 2 | 120 | 0.517 | 0.43-0.60 | 0.483 | 0.429 | -0.0093 | 0.055 | 1.00 | -6.5 |
| recent_base_rate_7d|h4|on_time | 120 | 2 | 120 | 0.517 | 0.43-0.60 | 0.483 | 0.429 | -0.0093 | 0.055 | 1.00 | -6.5 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 996.00 | -0.40% | 27 | 4 | 1 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 6 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 3 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 1 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 1 |
| lgbm_calibrated|h1 | 968.57 | -3.14% | 61 | 13 | 6 |
| lgbm_calibrated|h4 | 1002.57 | +0.26% | 94 | 69 | 3 |
| logistic|h1 | 945.39 | -5.46% | 16 | 6 | 6 |
| logistic|h4 | 996.71 | -0.33% | 29 | 9 | 3 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 6 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 3 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 6 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 3 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 5 |
| recent_base_rate_7d|h4 | 999.68 | -0.03% | 120 | 68 | 2 |
| benchmark_long_all_coins|h1 | 987.29 | -1.27% | 360 | 99 | 6 |
| benchmark_long_all_coins|h4 | 997.98 | -0.20% | 180 | 44 | 3 |

## Unverified (pending, not scored)

- analog_k100|h1: 60
- analog_k100|h4: 120
- base_rate|h1: 60
- base_rate|h4: 240
- council|h1: 60
- council|h4: 120
- derivatives|h1: 60
- derivatives|h4: 120
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
