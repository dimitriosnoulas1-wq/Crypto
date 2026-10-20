# Live monitor (2026-10-20T02:06:17.958342+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- LATENCY SLIPPAGE: analog_k100|h4|all live price differs from bar close by +25.6 bps on average
- LATENCY SLIPPAGE: base_rate|h4|all live price differs from bar close by +20.9 bps on average
- LATENCY SLIPPAGE: council|h4|all live price differs from bar close by +25.6 bps on average
- LATENCY SLIPPAGE: derivatives|h4|all live price differs from bar close by +25.6 bps on average
- LATENCY SLIPPAGE: lgbm_calibrated|h4|all live price differs from bar close by +20.9 bps on average
- LATENCY SLIPPAGE: logistic|h4|all live price differs from bar close by +20.9 bps on average
- LATENCY SLIPPAGE: momentum_24|h4|all live price differs from bar close by +20.9 bps on average
- LATENCY SLIPPAGE: orthosys|h4|all live price differs from bar close by +20.9 bps on average
- LATENCY SLIPPAGE: recent_base_rate_7d|h4|all live price differs from bar close by +19.6 bps on average

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['CHIP', 'TRX']
- **last_closed_bar**: 2026-10-20 01:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.2
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 106.4 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.13, 'recent_base_rate_7d': 0.112, 'momentum_24': 0.14, 'logistic': 0.136, 'lgbm_calibrated': 0.121, 'analog_k100': 0.097, 'derivatives': 0.133, 'orthosys': 0.131}
- **council_member_logloss_h1**: {'base_rate': 0.6937, 'recent_base_rate_7d': 0.7001, 'momentum_24': 0.6909, 'logistic': 0.6919, 'lgbm_calibrated': 0.6964, 'analog_k100': 0.7209, 'derivatives': 0.6943, 'orthosys': 0.6934}
- **council_calls_h1**: 0
- **council_abstain_h1**: {'no_edge': 57, 'extreme_volatility': 3}
- **council_weights_h4**: {'base_rate': 0.147, 'recent_base_rate_7d': 0.062, 'momentum_24': 0.147, 'logistic': 0.124, 'lgbm_calibrated': 0.108, 'analog_k100': 0.125, 'derivatives': 0.143, 'orthosys': 0.143}
- **council_member_logloss_h4**: {'base_rate': 0.6921, 'recent_base_rate_7d': 0.7494, 'momentum_24': 0.6921, 'logistic': 0.7016, 'lgbm_calibrated': 0.7095, 'analog_k100': 0.7355, 'derivatives': 0.6906, 'orthosys': 0.6936}
- **council_calls_h4**: 1
- **council_abstain_h4**: {'no_edge': 48, 'members_disagree': 8, 'extreme_volatility': 3, 'spoke': 1}
- **prediction_latency_min**: 6.2
- **price_snapshot_age_s**: 0.5
- **train_rows_h1**: 89887
- **orthosys_hist_hit_h1**: 0.5282
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.01
- **p_spread_logistic_h1**: 0.0195
- **p_spread_lgbm_calibrated_h1**: 0.0147
- **p_spread_analog_k100_h1**: 0.0545
- **p_spread_derivatives_h1**: 0.0003
- **p_spread_orthosys_h1**: 0.0036
- **p_spread_council_h1**: 0.0
- **train_rows_h4**: 89701
- **orthosys_hist_hit_h4**: 0.5163
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0005
- **p_spread_logistic_h4**: 0.0282
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0696
- **p_spread_derivatives_h4**: 0.0026
- **p_spread_orthosys_h4**: 0.0021
- **p_spread_council_h4**: 0.0027
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 9960

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 300 | 5 | 300 | 0.483 | 0.43-0.54 | 0.570 | 0.487 | -0.0371 | 0.095 | 0.41 | -13.7 |
| analog_k100|h1|on_time | 300 | 5 | 300 | 0.483 | 0.43-0.54 | 0.570 | 0.487 | -0.0371 | 0.095 | 0.41 | -13.7 |
| analog_k100|h4|all | 120 | 2 | 120 | 0.458 | 0.37-0.55 | 0.633 | 0.439 | -0.0694 | 0.199 | 0.68 | -23.0 |
| analog_k100|h4|on_time | 120 | 2 | 120 | 0.458 | 0.37-0.55 | 0.633 | 0.439 | -0.0694 | 0.199 | 0.68 | -23.0 |
| base_rate|h1|all | 600 | 10 | 600 | 0.462 | 0.42-0.50 | 0.538 | 0.498 | +0.0000 | 0.041 | 0.00 | - |
| base_rate|h1|on_time | 540 | 9 | 540 | 0.474 | 0.43-0.52 | 0.526 | 0.498 | +0.0000 | 0.028 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 420 | 7 | 420 | 0.602 | 0.55-0.65 | 0.602 | 0.503 | +0.0000 | 0.099 | 0.00 | - |
| base_rate|h4|on_time | 420 | 7 | 420 | 0.602 | 0.55-0.65 | 0.602 | 0.503 | +0.0000 | 0.099 | 0.00 | - |
| council|h1|all | 300 | 5 | 41 | 0.317 | 0.20-0.47 | 0.570 | 0.496 | -0.0038 | 0.074 | 0.00 | - |
| council|h1|on_time | 300 | 5 | 41 | 0.317 | 0.20-0.47 | 0.570 | 0.496 | -0.0038 | 0.074 | 0.00 | - |
| council|h4|all | 120 | 2 | 8 | 0.875 | 0.53-0.98 | 0.633 | 0.499 | +0.0014 | 0.173 | 0.00 | - |
| council|h4|on_time | 120 | 2 | 8 | 0.875 | 0.53-0.98 | 0.633 | 0.499 | +0.0014 | 0.173 | 0.00 | - |
| derivatives|h1|all | 300 | 5 | 300 | 0.413 | 0.36-0.47 | 0.570 | 0.498 | -0.0004 | 0.089 | 0.00 | - |
| derivatives|h1|on_time | 300 | 5 | 300 | 0.413 | 0.36-0.47 | 0.570 | 0.498 | -0.0004 | 0.089 | 0.00 | - |
| derivatives|h4|all | 120 | 2 | 120 | 0.633 | 0.54-0.71 | 0.633 | 0.503 | -0.0002 | 0.131 | 0.00 | - |
| derivatives|h4|on_time | 120 | 2 | 120 | 0.633 | 0.54-0.71 | 0.633 | 0.503 | -0.0002 | 0.131 | 0.00 | - |
| lgbm_calibrated|h1|all | 600 | 10 | 600 | 0.510 | 0.47-0.55 | 0.538 | 0.473 | -0.0048 | 0.065 | 0.10 | -33.8 |
| lgbm_calibrated|h1|on_time | 540 | 9 | 540 | 0.528 | 0.49-0.57 | 0.526 | 0.474 | -0.0012 | 0.052 | 0.11 | -33.8 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 420 | 7 | 420 | 0.398 | 0.35-0.45 | 0.602 | 0.456 | -0.0344 | 0.146 | 0.37 | -8.1 |
| lgbm_calibrated|h4|on_time | 420 | 7 | 420 | 0.398 | 0.35-0.45 | 0.602 | 0.456 | -0.0344 | 0.146 | 0.37 | -8.1 |
| logistic|h1|all | 600 | 10 | 600 | 0.565 | 0.53-0.60 | 0.538 | 0.491 | +0.0035 | 0.052 | 0.04 | -71.2 |
| logistic|h1|on_time | 540 | 9 | 540 | 0.541 | 0.50-0.58 | 0.526 | 0.488 | -0.0026 | 0.041 | 0.04 | -77.7 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 420 | 7 | 420 | 0.481 | 0.43-0.53 | 0.602 | 0.501 | -0.0211 | 0.102 | 0.12 | -71.6 |
| logistic|h4|on_time | 420 | 7 | 420 | 0.481 | 0.43-0.53 | 0.602 | 0.501 | -0.0211 | 0.102 | 0.12 | -71.6 |
| momentum_24|h1|all | 600 | 10 | 600 | 0.577 | 0.54-0.62 | 0.538 | 0.502 | +0.0055 | 0.068 | 0.00 | - |
| momentum_24|h1|on_time | 540 | 9 | 540 | 0.563 | 0.52-0.60 | 0.526 | 0.502 | +0.0045 | 0.054 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 420 | 7 | 420 | 0.602 | 0.55-0.65 | 0.602 | 0.503 | -0.0000 | 0.099 | 0.00 | - |
| momentum_24|h4|on_time | 420 | 7 | 420 | 0.602 | 0.55-0.65 | 0.602 | 0.503 | -0.0000 | 0.099 | 0.00 | - |
| orthosys|h1|all | 600 | 10 | 18 | 0.500 | 0.29-0.71 | 0.538 | 0.500 | +0.0008 | 0.039 | 0.00 | - |
| orthosys|h1|on_time | 540 | 9 | 17 | 0.471 | 0.26-0.69 | 0.526 | 0.500 | +0.0004 | 0.026 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 420 | 7 | 13 | 0.385 | 0.18-0.64 | 0.602 | 0.500 | -0.0027 | 0.102 | 0.00 | - |
| orthosys|h4|on_time | 420 | 7 | 13 | 0.385 | 0.18-0.64 | 0.602 | 0.500 | -0.0027 | 0.102 | 0.00 | - |
| recent_base_rate_7d|h1|all | 540 | 9 | 540 | 0.474 | 0.43-0.52 | 0.526 | 0.470 | -0.0112 | 0.056 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 540 | 9 | 540 | 0.474 | 0.43-0.52 | 0.526 | 0.470 | -0.0112 | 0.056 | 0.00 | - |
| recent_base_rate_7d|h4|all | 360 | 6 | 360 | 0.347 | 0.30-0.40 | 0.653 | 0.431 | -0.1064 | 0.222 | 1.00 | -44.0 |
| recent_base_rate_7d|h4|on_time | 360 | 6 | 360 | 0.347 | 0.30-0.40 | 0.653 | 0.431 | -0.1064 | 0.222 | 1.00 | -44.0 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 993.51 | -0.65% | 124 | 45 | 5 |
| analog_k100|h4 | 998.88 | -0.11% | 81 | 34 | 2 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 10 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 7 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 5 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 2 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 5 |
| derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 2 |
| lgbm_calibrated|h1 | 968.57 | -3.14% | 61 | 13 | 10 |
| lgbm_calibrated|h4 | 998.94 | -0.11% | 156 | 80 | 7 |
| logistic|h1 | 951.73 | -4.83% | 26 | 11 | 10 |
| logistic|h4 | 991.74 | -0.83% | 51 | 17 | 7 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 10 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 7 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 10 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 7 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 9 |
| recent_base_rate_7d|h4 | 993.42 | -0.66% | 360 | 136 | 6 |
| benchmark_long_all_coins|h1 | 987.33 | -1.27% | 600 | 213 | 10 |
| benchmark_long_all_coins|h4 | 1002.25 | +0.22% | 420 | 197 | 7 |

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
