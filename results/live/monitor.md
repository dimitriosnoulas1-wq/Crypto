# Live monitor (2026-10-19T20:06:13.838478+00:00)

## Alerts

- LATENCY SLIPPAGE: base_rate|h1|all live price differs from bar close by +18.1 bps on average
- LATENCY SLIPPAGE: lgbm_calibrated|h1|all live price differs from bar close by +18.1 bps on average
- LATENCY SLIPPAGE: logistic|h1|all live price differs from bar close by +18.1 bps on average
- LATENCY SLIPPAGE: momentum_24|h1|all live price differs from bar close by +18.1 bps on average
- LATENCY SLIPPAGE: orthosys|h1|all live price differs from bar close by +18.1 bps on average

## Health

- **venue**: okx
- **symbols**: 64
- **universe_size**: 60
- **fetched_only_for_scoring**: ['AEON', 'AERO', 'PYTH', 'SHIB']
- **last_closed_bar**: 2026-10-19 19:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.0
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 120.3 instruments 64/64']
- **feature_nan_share_latest_bar**: 0.026
- **prediction_latency_min**: 6.2
- **price_snapshot_age_s**: 1.1
- **train_rows_h1**: 92532
- **orthosys_hist_hit_h1**: 0.5283
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0082
- **p_spread_logistic_h1**: 0.0202
- **p_spread_lgbm_calibrated_h1**: 0.0132
- **p_spread_orthosys_h1**: 0.0052
- **train_rows_h4**: 92340
- **orthosys_hist_hit_h4**: 0.5195
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0
- **p_spread_logistic_h4**: 0.033
- **p_spread_lgbm_calibrated_h4**: 0.007
- **p_spread_orthosys_h4**: 0.0036
- **predictions_written**: 720
- **resolved_this_cycle**: 660
- **ledger_chain_valid**: True
- **ledger_rows**: 3480

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| base_rate|h1|all | 240 | 4 | 240 | 0.575 | 0.51-0.64 | 0.425 | 0.498 | +0.0000 | 0.073 | 0.00 | - |
| base_rate|h1|on_time | 180 | 3 | 180 | 0.650 | 0.58-0.72 | 0.350 | 0.497 | +0.0000 | 0.147 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 60 | 1 | 60 | 0.300 | 0.20-0.43 | 0.300 | 0.504 | +0.0000 | 0.204 | 0.00 | - |
| base_rate|h4|on_time | 60 | 1 | 60 | 0.300 | 0.20-0.43 | 0.300 | 0.504 | +0.0000 | 0.204 | 0.00 | - |
| lgbm_calibrated|h1|all | 240 | 4 | 240 | 0.671 | 0.61-0.73 | 0.425 | 0.478 | +0.0276 | 0.147 | 0.00 | -285.5 |
| lgbm_calibrated|h1|on_time | 180 | 3 | 180 | 0.778 | 0.71-0.83 | 0.350 | 0.482 | +0.0493 | 0.257 | 0.01 | -285.5 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.300 | 0.441 | +0.1037 | 0.141 | 0.75 | +62.2 |
| lgbm_calibrated|h4|on_time | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.300 | 0.441 | +0.1037 | 0.141 | 0.75 | +62.2 |
| logistic|h1|all | 240 | 4 | 240 | 0.713 | 0.65-0.77 | 0.425 | 0.499 | +0.0222 | 0.206 | 0.04 | -151.1 |
| logistic|h1|on_time | 180 | 3 | 180 | 0.689 | 0.62-0.75 | 0.350 | 0.493 | +0.0102 | 0.189 | 0.03 | -215.9 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 60 | 1 | 60 | 0.367 | 0.26-0.49 | 0.300 | 0.528 | -0.0523 | 0.249 | 0.30 | -134.1 |
| logistic|h4|on_time | 60 | 1 | 60 | 0.367 | 0.26-0.49 | 0.300 | 0.528 | -0.0523 | 0.249 | 0.30 | -134.1 |
| momentum_24|h1|all | 240 | 4 | 240 | 0.504 | 0.44-0.57 | 0.425 | 0.502 | -0.0003 | 0.077 | 0.00 | - |
| momentum_24|h1|on_time | 180 | 3 | 180 | 0.439 | 0.37-0.51 | 0.350 | 0.502 | -0.0053 | 0.152 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 60 | 1 | 60 | 0.300 | 0.20-0.43 | 0.300 | 0.503 | +0.0005 | 0.203 | 0.00 | - |
| momentum_24|h4|on_time | 60 | 1 | 60 | 0.300 | 0.20-0.43 | 0.300 | 0.503 | +0.0005 | 0.203 | 0.00 | - |
| orthosys|h1|all | 240 | 4 | 5 | 0.400 | 0.12-0.77 | 0.425 | 0.500 | -0.0019 | 0.076 | 0.00 | - |
| orthosys|h1|on_time | 180 | 3 | 4 | 0.250 | 0.05-0.70 | 0.350 | 0.500 | -0.0040 | 0.156 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 60 | 1 | 1 | 0.000 | 0.00-0.79 | 0.300 | 0.500 | +0.0049 | 0.217 | 0.00 | - |
| orthosys|h4|on_time | 60 | 1 | 1 | 0.000 | 0.00-0.79 | 0.300 | 0.500 | +0.0049 | 0.217 | 0.00 | - |
| recent_base_rate_7d|h1|all | 180 | 3 | 180 | 0.650 | 0.58-0.72 | 0.350 | 0.467 | +0.0324 | 0.117 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 180 | 3 | 180 | 0.650 | 0.58-0.72 | 0.350 | 0.467 | +0.0324 | 0.117 | 0.00 | - |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 4 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 1 |
| lgbm_calibrated|h1 | 971.45 | -2.86% | 1 | 0 | 4 |
| lgbm_calibrated|h4 | 1001.55 | +0.16% | 45 | 37 | 1 |
| logistic|h1 | 933.56 | -6.64% | 9 | 3 | 4 |
| logistic|h4 | 996.65 | -0.34% | 18 | 4 | 1 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 4 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 1 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 4 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 1 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 3 |
| benchmark_long_all_coins|h1 | 986.83 | -1.32% | 240 | 39 | 4 |
| benchmark_long_all_coins|h4 | 998.65 | -0.13% | 60 | 9 | 1 |

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
- recent_base_rate_7d|h4: 240
