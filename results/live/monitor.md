# Live monitor (2026-10-19T21:07:05.688438+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- LATENCY SLIPPAGE: base_rate|h1|all live price differs from bar close by +19.0 bps on average
- LATENCY SLIPPAGE: base_rate|h4|all live price differs from bar close by +16.6 bps on average
- LATENCY SLIPPAGE: lgbm_calibrated|h1|all live price differs from bar close by +19.0 bps on average
- LATENCY SLIPPAGE: lgbm_calibrated|h4|all live price differs from bar close by +16.6 bps on average
- MISCALIBRATED: logistic|h1|all says 0.50 on average, reality 0.51 (ECE 0.193)
- LATENCY SLIPPAGE: logistic|h1|all live price differs from bar close by +19.0 bps on average
- LATENCY SLIPPAGE: logistic|h4|all live price differs from bar close by +16.6 bps on average
- LATENCY SLIPPAGE: momentum_24|h1|all live price differs from bar close by +19.0 bps on average
- LATENCY SLIPPAGE: momentum_24|h4|all live price differs from bar close by +16.6 bps on average
- LATENCY SLIPPAGE: orthosys|h1|all live price differs from bar close by +19.0 bps on average
- LATENCY SLIPPAGE: orthosys|h4|all live price differs from bar close by +16.6 bps on average
- LATENCY SLIPPAGE: recent_base_rate_7d|h1|all live price differs from bar close by +16.6 bps on average

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['AERO', 'SHIB']
- **last_closed_bar**: 2026-10-19 20:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.2
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 101.2 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.123, 'recent_base_rate_7d': 0.135, 'momentum_24': 0.123, 'logistic': 0.141, 'lgbm_calibrated': 0.146, 'analog_k100': 0.105, 'derivatives': 0.105, 'orthosys': 0.122}
- **council_member_logloss_h1**: {'base_rate': 0.6925, 'recent_base_rate_7d': 0.685, 'momentum_24': 0.6926, 'logistic': 0.6814, 'lgbm_calibrated': 0.6786, 'analog_k100': 0.7061, 'derivatives': 0.7061, 'orthosys': 0.6934}
- **council_calls_h1**: 22
- **council_abstain_h1**: {'no_edge': 35, 'spoke': 22, 'extreme_volatility': 3}
- **council_weights_h4**: {'base_rate': 0.127, 'recent_base_rate_7d': 0.117, 'momentum_24': 0.127, 'logistic': 0.117, 'lgbm_calibrated': 0.149, 'analog_k100': 0.117, 'derivatives': 0.117, 'orthosys': 0.128}
- **council_member_logloss_h4**: {'base_rate': 0.6963, 'recent_base_rate_7d': 0.7228, 'momentum_24': 0.6961, 'logistic': 0.7228, 'lgbm_calibrated': 0.6438, 'analog_k100': 0.7228, 'derivatives': 0.7228, 'orthosys': 0.6939}
- **council_calls_h4**: 5
- **council_abstain_h4**: {'members_disagree': 35, 'no_edge': 17, 'spoke': 5, 'extreme_volatility': 3}
- **prediction_latency_min**: 7.0
- **price_snapshot_age_s**: 0.8
- **train_rows_h1**: 89590
- **orthosys_hist_hit_h1**: 0.5271
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0085
- **p_spread_logistic_h1**: 0.0208
- **p_spread_lgbm_calibrated_h1**: 0.0052
- **p_spread_analog_k100_h1**: 0.0574
- **p_spread_derivatives_h1**: 0.0012
- **p_spread_orthosys_h1**: 0.0061
- **p_spread_council_h1**: 0.0133
- **train_rows_h4**: 89404
- **orthosys_hist_hit_h4**: 0.517
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0005
- **p_spread_logistic_h4**: 0.0353
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0683
- **p_spread_derivatives_h4**: 0.0042
- **p_spread_orthosys_h4**: 0.0038
- **p_spread_council_h4**: 0.0063
- **predictions_written**: 1080
- **resolved_this_cycle**: 720
- **ledger_chain_valid**: True
- **ledger_rows**: 4560

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| base_rate|h1|all | 300 | 5 | 300 | 0.493 | 0.44-0.55 | 0.507 | 0.498 | +0.0000 | 0.009 | 0.00 | - |
| base_rate|h1|on_time | 240 | 4 | 240 | 0.529 | 0.47-0.59 | 0.471 | 0.497 | +0.0000 | 0.027 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 120 | 2 | 120 | 0.317 | 0.24-0.40 | 0.317 | 0.504 | +0.0000 | 0.187 | 0.00 | - |
| base_rate|h4|on_time | 120 | 2 | 120 | 0.317 | 0.24-0.40 | 0.317 | 0.504 | +0.0000 | 0.187 | 0.00 | - |
| lgbm_calibrated|h1|all | 300 | 5 | 300 | 0.580 | 0.52-0.63 | 0.507 | 0.477 | +0.0079 | 0.055 | 0.00 | -285.5 |
| lgbm_calibrated|h1|on_time | 240 | 4 | 240 | 0.637 | 0.57-0.70 | 0.471 | 0.479 | +0.0192 | 0.114 | 0.00 | -285.5 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 120 | 2 | 120 | 0.683 | 0.60-0.76 | 0.317 | 0.444 | +0.0892 | 0.127 | 0.78 | +51.0 |
| lgbm_calibrated|h4|on_time | 120 | 2 | 120 | 0.683 | 0.60-0.76 | 0.317 | 0.444 | +0.0892 | 0.127 | 0.78 | +51.0 |
| logistic|h1|all | 300 | 5 | 300 | 0.703 | 0.65-0.75 | 0.507 | 0.500 | +0.0243 | 0.193 | 0.03 | -114.2 |
| logistic|h1|on_time | 240 | 4 | 240 | 0.683 | 0.62-0.74 | 0.471 | 0.495 | +0.0158 | 0.177 | 0.03 | -154.0 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 120 | 2 | 120 | 0.392 | 0.31-0.48 | 0.317 | 0.518 | -0.0414 | 0.224 | 0.21 | -115.4 |
| logistic|h4|on_time | 120 | 2 | 120 | 0.392 | 0.31-0.48 | 0.317 | 0.518 | -0.0414 | 0.224 | 0.21 | -115.4 |
| momentum_24|h1|all | 300 | 5 | 300 | 0.553 | 0.50-0.61 | 0.507 | 0.502 | +0.0036 | 0.045 | 0.00 | - |
| momentum_24|h1|on_time | 240 | 4 | 240 | 0.517 | 0.45-0.58 | 0.471 | 0.502 | +0.0009 | 0.032 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 120 | 2 | 120 | 0.317 | 0.24-0.40 | 0.317 | 0.503 | +0.0004 | 0.187 | 0.00 | - |
| momentum_24|h4|on_time | 120 | 2 | 120 | 0.317 | 0.24-0.40 | 0.317 | 0.503 | +0.0004 | 0.187 | 0.00 | - |
| orthosys|h1|all | 300 | 5 | 7 | 0.429 | 0.16-0.75 | 0.507 | 0.500 | -0.0001 | 0.007 | 0.00 | - |
| orthosys|h1|on_time | 240 | 4 | 6 | 0.333 | 0.10-0.70 | 0.471 | 0.500 | -0.0013 | 0.038 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 120 | 2 | 2 | 0.000 | 0.00-0.66 | 0.317 | 0.500 | +0.0043 | 0.192 | 0.00 | - |
| orthosys|h4|on_time | 120 | 2 | 2 | 0.000 | 0.00-0.66 | 0.317 | 0.500 | +0.0043 | 0.192 | 0.00 | - |
| recent_base_rate_7d|h1|all | 240 | 4 | 240 | 0.529 | 0.47-0.59 | 0.471 | 0.468 | +0.0038 | 0.003 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 240 | 4 | 240 | 0.529 | 0.47-0.59 | 0.471 | 0.468 | +0.0038 | 0.003 | 0.00 | - |
| recent_base_rate_7d|h4|all | 60 | 1 | 60 | 0.667 | 0.54-0.77 | 0.333 | 0.428 | +0.0797 | 0.095 | 1.00 | -2.1 |
| recent_base_rate_7d|h4|on_time | 60 | 1 | 60 | 0.667 | 0.54-0.77 | 0.333 | 0.428 | +0.0797 | 0.095 | 1.00 | -2.1 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 5 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 2 |
| lgbm_calibrated|h1 | 971.45 | -2.86% | 1 | 0 | 5 |
| lgbm_calibrated|h4 | 1002.57 | +0.26% | 94 | 69 | 2 |
| logistic|h1 | 953.83 | -4.62% | 10 | 4 | 5 |
| logistic|h4 | 994.97 | -0.50% | 25 | 6 | 2 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 5 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 2 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 5 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 2 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 4 |
| recent_base_rate_7d|h4 | 999.95 | -0.01% | 60 | 36 | 1 |
| benchmark_long_all_coins|h1 | 986.34 | -1.37% | 300 | 62 | 5 |
| benchmark_long_all_coins|h4 | 998.21 | -0.18% | 120 | 22 | 2 |

## Unverified (pending, not scored)

- analog_k100|h1: 60
- analog_k100|h4: 60
- base_rate|h1: 60
- base_rate|h4: 240
- council|h1: 60
- council|h4: 60
- derivatives|h1: 60
- derivatives|h4: 60
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
