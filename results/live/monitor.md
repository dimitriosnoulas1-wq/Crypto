# Live monitor (2026-10-19T19:06:50.232992+00:00)

## Alerts

- LATENCY SLIPPAGE: base_rate|h1|all live price differs from bar close by +26.7 bps on average
- LATENCY SLIPPAGE: lgbm_calibrated|h1|all live price differs from bar close by +26.7 bps on average
- LATENCY SLIPPAGE: logistic|h1|all live price differs from bar close by +26.7 bps on average
- LATENCY SLIPPAGE: momentum_24|h1|all live price differs from bar close by +26.7 bps on average
- LATENCY SLIPPAGE: orthosys|h1|all live price differs from bar close by +26.7 bps on average
- LATENCY SLIPPAGE: recent_base_rate_7d|h1|all live price differs from bar close by +25.7 bps on average

## Health

- **venue**: okx
- **symbols**: 63
- **universe_size**: 60
- **fetched_only_for_scoring**: ['AEON', 'AERO', 'PYTH']
- **last_closed_bar**: 2026-10-19 18:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.2
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 144.2 instruments 63/63']
- **feature_nan_share_latest_bar**: 0.026
- **prediction_latency_min**: 6.8
- **price_snapshot_age_s**: 1.3
- **train_rows_h1**: 90971
- **orthosys_hist_hit_h1**: 0.5271
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0083
- **p_spread_logistic_h1**: 0.0223
- **p_spread_lgbm_calibrated_h1**: 0.0041
- **p_spread_orthosys_h1**: 0.005
- **train_rows_h4**: 90782
- **orthosys_hist_hit_h4**: 0.5199
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0001
- **p_spread_logistic_h4**: 0.0345
- **p_spread_lgbm_calibrated_h4**: 0.0086
- **p_spread_orthosys_h4**: 0.0037
- **predictions_written**: 720
- **resolved_this_cycle**: 360
- **ledger_chain_valid**: True
- **ledger_rows**: 2760

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| base_rate|h1|all | 180 | 3 | 180 | 0.506 | 0.43-0.58 | 0.494 | 0.498 | +0.0000 | 0.003 | 0.00 | - |
| base_rate|h1|on_time | 120 | 2 | 120 | 0.583 | 0.49-0.67 | 0.417 | 0.497 | +0.0000 | 0.081 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| lgbm_calibrated|h1|all | 180 | 3 | 180 | 0.628 | 0.56-0.70 | 0.494 | 0.474 | +0.0308 | 0.099 | 0.01 | -285.5 |
| lgbm_calibrated|h1|on_time | 120 | 2 | 120 | 0.767 | 0.68-0.83 | 0.417 | 0.478 | +0.0649 | 0.240 | 0.01 | -285.5 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| logistic|h1|all | 180 | 3 | 180 | 0.683 | 0.61-0.75 | 0.494 | 0.504 | +0.0174 | 0.186 | 0.04 | -216.2 |
| logistic|h1|on_time | 120 | 2 | 120 | 0.633 | 0.54-0.71 | 0.417 | 0.497 | -0.0031 | 0.149 | 0.03 | -362.2 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| momentum_24|h1|all | 180 | 3 | 180 | 0.550 | 0.48-0.62 | 0.494 | 0.503 | +0.0031 | 0.042 | 0.00 | - |
| momentum_24|h1|on_time | 120 | 2 | 120 | 0.475 | 0.39-0.56 | 0.417 | 0.503 | -0.0026 | 0.086 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| orthosys|h1|all | 180 | 3 | 3 | 0.333 | 0.06-0.79 | 0.494 | 0.500 | -0.0005 | 0.006 | 0.00 | - |
| orthosys|h1|on_time | 120 | 2 | 2 | 0.000 | 0.00-0.66 | 0.417 | 0.500 | -0.0031 | 0.084 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| recent_base_rate_7d|h1|all | 120 | 2 | 120 | 0.583 | 0.49-0.67 | 0.417 | 0.468 | +0.0165 | 0.051 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 120 | 2 | 120 | 0.583 | 0.49-0.67 | 0.417 | 0.468 | +0.0165 | 0.051 | 0.00 | - |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 3 |
| lgbm_calibrated|h1 | 971.45 | -2.86% | 1 | 0 | 3 |
| logistic|h1 | 926.44 | -7.36% | 7 | 1 | 3 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 3 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 3 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 2 |
| benchmark_long_all_coins|h1 | 990.70 | -0.93% | 180 | 28 | 3 |

## Unverified (pending, not scored)

- base_rate|h1: 60
- base_rate|h4: 240
- lgbm_calibrated|h1: 60
- lgbm_calibrated|h4: 240
- logistic|h1: 60
- logistic|h4: 240
- momentum_24|h1: 60
- momentum_24|h4: 240
- orthosys|h1: 60
- orthosys|h4: 240
- recent_base_rate_7d|h1: 60
- recent_base_rate_7d|h4: 180
