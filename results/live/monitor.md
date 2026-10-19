# Live monitor (2026-10-19T18:06:30.020861+00:00)

## Alerts

- LATENCY SLIPPAGE: base_rate|h1|all live price differs from bar close by +16.6 bps on average
- LATENCY SLIPPAGE: lgbm_calibrated|h1|all live price differs from bar close by +16.6 bps on average
- LATENCY SLIPPAGE: logistic|h1|all live price differs from bar close by +16.6 bps on average
- LATENCY SLIPPAGE: momentum_24|h1|all live price differs from bar close by +16.6 bps on average
- LATENCY SLIPPAGE: orthosys|h1|all live price differs from bar close by +16.6 bps on average

## Health

- **venue**: okx
- **symbols**: 63
- **universe_size**: 60
- **fetched_only_for_scoring**: ['AEON', 'DASH', 'PYTH']
- **last_closed_bar**: 2026-10-19 17:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.5
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 106.6 instruments 63/63']
- **feature_nan_share_latest_bar**: 0.026
- **prediction_latency_min**: 6.4
- **price_snapshot_age_s**: 0.7
- **train_rows_h1**: 90908
- **orthosys_hist_hit_h1**: 0.5272
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0072
- **p_spread_logistic_h1**: 0.0283
- **p_spread_lgbm_calibrated_h1**: 0.0099
- **p_spread_orthosys_h1**: 0.0035
- **train_rows_h4**: 90719
- **orthosys_hist_hit_h4**: 0.52
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0001
- **p_spread_logistic_h4**: 0.0412
- **p_spread_lgbm_calibrated_h4**: 0.0023
- **p_spread_orthosys_h4**: 0.0026
- **predictions_written**: 720
- **resolved_this_cycle**: 360
- **ledger_chain_valid**: True
- **ledger_rows**: 2040

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| base_rate|h1|all | 120 | 2 | 120 | 0.592 | 0.50-0.68 | 0.408 | 0.498 | +0.0000 | 0.089 | 0.00 | - |
| base_rate|h1|on_time | 60 | 1 | 60 | 0.833 | 0.72-0.91 | 0.167 | 0.498 | +0.0000 | 0.331 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| lgbm_calibrated|h1|all | 120 | 2 | 120 | 0.608 | 0.52-0.69 | 0.408 | 0.460 | +0.0425 | 0.068 | 0.00 | - |
| lgbm_calibrated|h1|on_time | 60 | 1 | 60 | 0.867 | 0.76-0.93 | 0.167 | 0.453 | +0.1228 | 0.319 | 0.00 | - |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| logistic|h1|all | 120 | 2 | 120 | 0.717 | 0.63-0.79 | 0.408 | 0.505 | +0.0304 | 0.207 | 0.04 | -241.0 |
| logistic|h1|on_time | 60 | 1 | 60 | 0.650 | 0.52-0.76 | 0.167 | 0.492 | +0.0026 | 0.346 | 0.03 | -570.2 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| momentum_24|h1|all | 120 | 2 | 120 | 0.492 | 0.40-0.58 | 0.408 | 0.503 | -0.0015 | 0.094 | 0.00 | - |
| momentum_24|h1|on_time | 60 | 1 | 60 | 0.283 | 0.19-0.41 | 0.167 | 0.503 | -0.0174 | 0.336 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| orthosys|h1|all | 120 | 2 | 2 | 0.500 | 0.09-0.91 | 0.408 | 0.500 | -0.0017 | 0.092 | 0.00 | - |
| orthosys|h1|on_time | 60 | 1 | 1 | 0.000 | 0.00-0.79 | 0.167 | 0.500 | -0.0080 | 0.334 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| recent_base_rate_7d|h1|all | 60 | 1 | 60 | 0.833 | 0.72-0.91 | 0.167 | 0.467 | +0.0770 | 0.301 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 60 | 1 | 60 | 0.833 | 0.72-0.91 | 0.167 | 0.467 | +0.0770 | 0.301 | 0.00 | - |

## Unverified (pending, not scored)

- base_rate|h1: 60
- base_rate|h4: 180
- lgbm_calibrated|h1: 60
- lgbm_calibrated|h4: 180
- logistic|h1: 60
- logistic|h4: 180
- momentum_24|h1: 60
- momentum_24|h4: 180
- orthosys|h1: 60
- orthosys|h4: 180
- recent_base_rate_7d|h1: 60
- recent_base_rate_7d|h4: 120
