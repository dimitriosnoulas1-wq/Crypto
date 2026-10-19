# Live monitor (2026-10-19T17:06:37.425435+00:00)

## Alerts

- none

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['AEON', 'PYTH']
- **last_closed_bar**: 2026-10-19 16:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.8
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 108.2 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **note**: bar already predicted; only resolving
- **predictions_written**: 0
- **resolved_this_cycle**: 10
- **ledger_chain_valid**: True
- **ledger_rows**: 1320

## Realized results (resolved predictions only)

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| base_rate|h1|all | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| lgbm_calibrated|h1|all | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| logistic|h1|all | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| momentum_24|h1|all | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| orthosys|h1|all | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |

## Unverified (pending, not scored)

- base_rate|h1: 60
- base_rate|h4: 120
- lgbm_calibrated|h1: 60
- lgbm_calibrated|h4: 120
- logistic|h1: 60
- logistic|h4: 120
- momentum_24|h1: 60
- momentum_24|h4: 120
- orthosys|h1: 60
- orthosys|h4: 120
- recent_base_rate_7d|h1: 60
- recent_base_rate_7d|h4: 60
