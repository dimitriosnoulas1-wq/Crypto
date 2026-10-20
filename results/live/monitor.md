# Live monitor (2026-10-20T00:06:11.147277+00:00)

## Alerts

- LATENCY SLIPPAGE: base_rate|h1|all live price differs from bar close by +17.4 bps on average
- LATENCY SLIPPAGE: base_rate|h4|all live price differs from bar close by +19.0 bps on average
- LATENCY SLIPPAGE: lgbm_calibrated|h1|all live price differs from bar close by +17.4 bps on average
- LATENCY SLIPPAGE: lgbm_calibrated|h4|all live price differs from bar close by +19.0 bps on average
- LATENCY SLIPPAGE: logistic|h1|all live price differs from bar close by +17.4 bps on average
- LATENCY SLIPPAGE: logistic|h4|all live price differs from bar close by +19.0 bps on average
- LATENCY SLIPPAGE: momentum_24|h1|all live price differs from bar close by +17.4 bps on average
- LATENCY SLIPPAGE: momentum_24|h4|all live price differs from bar close by +19.0 bps on average
- LATENCY SLIPPAGE: orthosys|h1|all live price differs from bar close by +17.4 bps on average
- LATENCY SLIPPAGE: orthosys|h4|all live price differs from bar close by +19.0 bps on average
- LATENCY SLIPPAGE: recent_base_rate_7d|h1|all live price differs from bar close by +15.8 bps on average
- LATENCY SLIPPAGE: recent_base_rate_7d|h4|all live price differs from bar close by +16.6 bps on average

## Health

- **venue**: okx
- **symbols**: 61
- **universe_size**: 60
- **fetched_only_for_scoring**: ['XLM']
- **last_closed_bar**: 2026-10-19 23:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.3
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 100.7 instruments 61/61']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.132, 'recent_base_rate_7d': 0.107, 'momentum_24': 0.142, 'logistic': 0.136, 'lgbm_calibrated': 0.114, 'analog_k100': 0.098, 'derivatives': 0.136, 'orthosys': 0.134}
- **council_member_logloss_h1**: {'base_rate': 0.694, 'recent_base_rate_7d': 0.7061, 'momentum_24': 0.6906, 'logistic': 0.6928, 'lgbm_calibrated': 0.701, 'analog_k100': 0.7514, 'derivatives': 0.6962, 'orthosys': 0.6933}
- **council_calls_h1**: 2
- **council_abstain_h1**: {'no_edge': 55, 'extreme_volatility': 3, 'spoke': 2}
- **council_weights_h4**: {'base_rate': 0.132, 'recent_base_rate_7d': 0.093, 'momentum_24': 0.132, 'logistic': 0.114, 'lgbm_calibrated': 0.139, 'analog_k100': 0.129, 'derivatives': 0.129, 'orthosys': 0.132}
- **council_member_logloss_h4**: {'base_rate': 0.6932, 'recent_base_rate_7d': 0.7312, 'momentum_24': 0.6931, 'logistic': 0.705, 'lgbm_calibrated': 0.6887, 'orthosys': 0.6933}
- **council_calls_h4**: 1
- **council_abstain_h4**: {'no_edge': 39, 'members_disagree': 17, 'extreme_volatility': 3, 'spoke': 1}
- **prediction_latency_min**: 6.1
- **price_snapshot_age_s**: 1.0
- **train_rows_h1**: 88266
- **orthosys_hist_hit_h1**: 0.5288
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0096
- **p_spread_logistic_h1**: 0.0169
- **p_spread_lgbm_calibrated_h1**: 0.0123
- **p_spread_analog_k100_h1**: 0.0523
- **p_spread_derivatives_h1**: 0.0002
- **p_spread_orthosys_h1**: 0.0037
- **p_spread_council_h1**: 0.0043
- **train_rows_h4**: 88083
- **orthosys_hist_hit_h4**: 0.5156
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0001
- **p_spread_logistic_h4**: 0.0357
- **p_spread_lgbm_calibrated_h4**: 0.0089
- **p_spread_analog_k100_h4**: 0.0727
- **p_spread_derivatives_h4**: 0.0016
- **p_spread_orthosys_h4**: 0.002
- **p_spread_council_h4**: 0.0042
- **predictions_written**: 1080
- **resolved_this_cycle**: 900
- **ledger_chain_valid**: True
- **ledger_rows**: 7800

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 180 | 3 | 180 | 0.433 | 0.36-0.51 | 0.733 | 0.475 | -0.0669 | 0.266 | 0.43 | -27.7 |
| analog_k100|h1|on_time | 180 | 3 | 180 | 0.433 | 0.36-0.51 | 0.733 | 0.475 | -0.0669 | 0.266 | 0.43 | -27.7 |
| base_rate|h1|all | 480 | 8 | 480 | 0.408 | 0.37-0.45 | 0.592 | 0.498 | +0.0000 | 0.094 | 0.00 | - |
| base_rate|h1|on_time | 420 | 7 | 420 | 0.417 | 0.37-0.46 | 0.583 | 0.498 | +0.0000 | 0.086 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 300 | 5 | 300 | 0.590 | 0.53-0.64 | 0.590 | 0.503 | +0.0000 | 0.087 | 0.00 | - |
| base_rate|h4|on_time | 300 | 5 | 300 | 0.590 | 0.53-0.64 | 0.590 | 0.503 | +0.0000 | 0.087 | 0.00 | - |
| council|h1|all | 180 | 3 | 37 | 0.270 | 0.15-0.43 | 0.733 | 0.495 | -0.0060 | 0.239 | 0.00 | - |
| council|h1|on_time | 180 | 3 | 37 | 0.270 | 0.15-0.43 | 0.733 | 0.495 | -0.0060 | 0.239 | 0.00 | - |
| derivatives|h1|all | 180 | 3 | 180 | 0.244 | 0.19-0.31 | 0.733 | 0.498 | -0.0005 | 0.258 | 0.00 | - |
| derivatives|h1|on_time | 180 | 3 | 180 | 0.244 | 0.19-0.31 | 0.733 | 0.498 | -0.0005 | 0.258 | 0.00 | - |
| lgbm_calibrated|h1|all | 480 | 8 | 480 | 0.469 | 0.42-0.51 | 0.592 | 0.473 | -0.0141 | 0.118 | 0.13 | -33.8 |
| lgbm_calibrated|h1|on_time | 420 | 7 | 420 | 0.486 | 0.44-0.53 | 0.583 | 0.474 | -0.0108 | 0.109 | 0.15 | -33.8 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 300 | 5 | 300 | 0.410 | 0.36-0.47 | 0.590 | 0.453 | -0.0287 | 0.137 | 0.50 | -8.7 |
| lgbm_calibrated|h4|on_time | 300 | 5 | 300 | 0.410 | 0.36-0.47 | 0.590 | 0.453 | -0.0287 | 0.137 | 0.50 | -8.7 |
| logistic|h1|all | 480 | 8 | 480 | 0.544 | 0.50-0.59 | 0.592 | 0.491 | +0.0004 | 0.103 | 0.05 | -92.9 |
| logistic|h1|on_time | 420 | 7 | 420 | 0.510 | 0.46-0.56 | 0.583 | 0.487 | -0.0078 | 0.099 | 0.05 | -103.7 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 300 | 5 | 300 | 0.537 | 0.48-0.59 | 0.590 | 0.510 | -0.0065 | 0.080 | 0.12 | -49.2 |
| logistic|h4|on_time | 300 | 5 | 300 | 0.537 | 0.48-0.59 | 0.590 | 0.510 | -0.0065 | 0.080 | 0.12 | -49.2 |
| momentum_24|h1|all | 480 | 8 | 480 | 0.592 | 0.55-0.63 | 0.592 | 0.502 | +0.0067 | 0.090 | 0.00 | - |
| momentum_24|h1|on_time | 420 | 7 | 420 | 0.576 | 0.53-0.62 | 0.583 | 0.502 | +0.0056 | 0.081 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 300 | 5 | 300 | 0.590 | 0.53-0.64 | 0.590 | 0.503 | +0.0001 | 0.087 | 0.00 | - |
| momentum_24|h4|on_time | 300 | 5 | 300 | 0.590 | 0.53-0.64 | 0.590 | 0.503 | +0.0001 | 0.087 | 0.00 | - |
| orthosys|h1|all | 480 | 8 | 15 | 0.467 | 0.25-0.70 | 0.592 | 0.500 | +0.0013 | 0.092 | 0.00 | - |
| orthosys|h1|on_time | 420 | 7 | 14 | 0.429 | 0.21-0.67 | 0.583 | 0.500 | +0.0008 | 0.083 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 300 | 5 | 7 | 0.286 | 0.08-0.64 | 0.590 | 0.500 | -0.0023 | 0.090 | 0.00 | - |
| orthosys|h4|on_time | 300 | 5 | 7 | 0.286 | 0.08-0.64 | 0.590 | 0.500 | -0.0023 | 0.090 | 0.00 | - |
| recent_base_rate_7d|h1|all | 420 | 7 | 420 | 0.417 | 0.37-0.46 | 0.583 | 0.469 | -0.0225 | 0.115 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 420 | 7 | 420 | 0.417 | 0.37-0.46 | 0.583 | 0.469 | -0.0225 | 0.115 | 0.00 | - |
| recent_base_rate_7d|h4|all | 240 | 4 | 240 | 0.338 | 0.28-0.40 | 0.662 | 0.430 | -0.1123 | 0.233 | 1.00 | -53.8 |
| recent_base_rate_7d|h4|on_time | 240 | 4 | 240 | 0.338 | 0.28-0.40 | 0.662 | 0.430 | -0.1123 | 0.233 | 1.00 | -53.8 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 991.80 | -0.82% | 77 | 17 | 3 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 8 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 5 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 3 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 3 |
| lgbm_calibrated|h1 | 968.57 | -3.14% | 61 | 13 | 8 |
| lgbm_calibrated|h4 | 998.78 | -0.12% | 150 | 76 | 5 |
| logistic|h1 | 924.60 | -7.54% | 23 | 9 | 8 |
| logistic|h4 | 997.88 | -0.21% | 36 | 13 | 5 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 8 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 5 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 8 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 5 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 7 |
| recent_base_rate_7d|h4 | 994.63 | -0.54% | 240 | 87 | 4 |
| benchmark_long_all_coins|h1 | 987.98 | -1.20% | 480 | 160 | 8 |
| benchmark_long_all_coins|h4 | 1002.03 | +0.20% | 300 | 140 | 5 |

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
