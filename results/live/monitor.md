# Live monitor (2026-10-20T10:19:31.041770+00:00)

## Alerts

- none

## Health

- **venue**: okx
- **symbols**: 60
- **universe_size**: 60
- **fetched_only_for_scoring**: []
- **last_closed_bar**: 2026-10-20 09:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 17.8
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 100.9 instruments 60/60']
- **feature_nan_share_latest_bar**: 0.026
- **note**: bar already predicted; only resolving
- **predictions_written**: 0
- **resolved_this_cycle**: 0
- **ledger_chain_valid**: True
- **ledger_rows**: 18600

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 780 | 13 | 780 | 0.523 | 0.49-0.56 | 0.482 | 0.484 | +0.0025 | 0.025 | 0.43 | -7.1 |
| analog_k100|h1|on_time | 780 | 13 | 780 | 0.523 | 0.49-0.56 | 0.482 | 0.484 | +0.0025 | 0.025 | 0.43 | -7.1 |
| analog_k100|h4|all | 600 | 10 | 600 | 0.545 | 0.50-0.58 | 0.445 | 0.461 | +0.0024 | 0.031 | 0.57 | -0.1 |
| analog_k100|h4|on_time | 600 | 10 | 600 | 0.545 | 0.50-0.58 | 0.445 | 0.461 | +0.0024 | 0.031 | 0.57 | -0.1 |
| base_rate|h1|all | 1080 | 18 | 1080 | 0.511 | 0.48-0.54 | 0.489 | 0.498 | +0.0000 | 0.009 | 0.00 | - |
| base_rate|h1|on_time | 1020 | 17 | 1020 | 0.521 | 0.49-0.55 | 0.479 | 0.498 | +0.0000 | 0.019 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 900 | 15 | 900 | 0.493 | 0.46-0.53 | 0.493 | 0.503 | +0.0000 | 0.010 | 0.00 | - |
| base_rate|h4|on_time | 900 | 15 | 900 | 0.493 | 0.46-0.53 | 0.493 | 0.503 | +0.0000 | 0.010 | 0.00 | - |
| council|h1|all | 780 | 13 | 89 | 0.562 | 0.46-0.66 | 0.482 | 0.497 | +0.0009 | 0.015 | 0.00 | - |
| council|h1|on_time | 780 | 13 | 89 | 0.562 | 0.46-0.66 | 0.482 | 0.497 | +0.0009 | 0.015 | 0.00 | - |
| council|h4|all | 600 | 10 | 12 | 0.750 | 0.47-0.91 | 0.445 | 0.500 | +0.0028 | 0.055 | 0.00 | - |
| council|h4|on_time | 600 | 10 | 12 | 0.750 | 0.47-0.91 | 0.445 | 0.500 | +0.0028 | 0.055 | 0.00 | - |
| derivatives|h1|all | 780 | 13 | 780 | 0.512 | 0.48-0.55 | 0.482 | 0.498 | -0.0001 | 0.016 | 0.00 | - |
| derivatives|h1|on_time | 780 | 13 | 780 | 0.512 | 0.48-0.55 | 0.482 | 0.498 | -0.0001 | 0.016 | 0.00 | - |
| derivatives|h4|all | 600 | 10 | 600 | 0.465 | 0.43-0.51 | 0.445 | 0.503 | +0.0006 | 0.058 | 0.00 | -325.5 |
| derivatives|h4|on_time | 600 | 10 | 600 | 0.465 | 0.43-0.51 | 0.445 | 0.503 | +0.0006 | 0.058 | 0.00 | -325.5 |
| lgbm_calibrated|h1|all | 1080 | 18 | 1080 | 0.556 | 0.53-0.58 | 0.489 | 0.478 | +0.0047 | 0.033 | 0.08 | -33.2 |
| lgbm_calibrated|h1|on_time | 1020 | 17 | 1020 | 0.568 | 0.54-0.60 | 0.479 | 0.479 | +0.0072 | 0.045 | 0.08 | -33.2 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 900 | 15 | 900 | 0.504 | 0.47-0.54 | 0.493 | 0.461 | -0.0024 | 0.034 | 0.21 | -0.9 |
| lgbm_calibrated|h4|on_time | 900 | 15 | 900 | 0.504 | 0.47-0.54 | 0.493 | 0.461 | -0.0024 | 0.034 | 0.21 | -0.9 |
| logistic|h1|all | 1080 | 18 | 1080 | 0.535 | 0.51-0.56 | 0.489 | 0.491 | +0.0023 | 0.019 | 0.06 | -29.0 |
| logistic|h1|on_time | 1020 | 17 | 1020 | 0.521 | 0.49-0.55 | 0.479 | 0.489 | -0.0010 | 0.013 | 0.06 | -29.4 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 900 | 15 | 900 | 0.520 | 0.49-0.55 | 0.493 | 0.490 | +0.0004 | 0.009 | 0.14 | +4.1 |
| logistic|h4|on_time | 900 | 15 | 900 | 0.520 | 0.49-0.55 | 0.493 | 0.490 | +0.0004 | 0.009 | 0.14 | +4.1 |
| momentum_24|h1|all | 1080 | 18 | 1080 | 0.563 | 0.53-0.59 | 0.489 | 0.500 | +0.0044 | 0.053 | 0.00 | - |
| momentum_24|h1|on_time | 1020 | 17 | 1020 | 0.555 | 0.52-0.59 | 0.479 | 0.500 | +0.0039 | 0.045 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 900 | 15 | 900 | 0.493 | 0.46-0.53 | 0.493 | 0.503 | +0.0001 | 0.010 | 0.00 | - |
| momentum_24|h4|on_time | 900 | 15 | 900 | 0.493 | 0.46-0.53 | 0.493 | 0.503 | +0.0001 | 0.010 | 0.00 | - |
| orthosys|h1|all | 1080 | 18 | 45 | 0.533 | 0.39-0.67 | 0.489 | 0.499 | +0.0003 | 0.010 | 0.00 | - |
| orthosys|h1|on_time | 1020 | 17 | 44 | 0.523 | 0.38-0.66 | 0.479 | 0.499 | +0.0001 | 0.020 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 900 | 15 | 32 | 0.562 | 0.39-0.72 | 0.493 | 0.500 | +0.0009 | 0.006 | 0.00 | - |
| orthosys|h4|on_time | 900 | 15 | 32 | 0.562 | 0.39-0.72 | 0.493 | 0.500 | +0.0009 | 0.006 | 0.00 | - |
| recent_base_rate_7d|h1|all | 1020 | 17 | 1020 | 0.521 | 0.49-0.55 | 0.479 | 0.471 | +0.0017 | 0.008 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 1020 | 17 | 1020 | 0.521 | 0.49-0.55 | 0.479 | 0.471 | +0.0017 | 0.008 | 0.00 | - |
| recent_base_rate_7d|h4|all | 840 | 14 | 840 | 0.493 | 0.46-0.53 | 0.507 | 0.438 | -0.0276 | 0.070 | 1.00 | -21.8 |
| recent_base_rate_7d|h4|on_time | 840 | 14 | 840 | 0.493 | 0.46-0.53 | 0.507 | 0.438 | -0.0276 | 0.070 | 1.00 | -21.8 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 990.99 | -0.90% | 338 | 135 | 13 |
| analog_k100|h4 | 1000.30 | +0.03% | 342 | 174 | 10 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 18 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 15 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 13 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 10 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 13 |
| derivatives|h4 | 991.86 | -0.81% | 1 | 0 | 10 |
| lgbm_calibrated|h1 | 944.33 | -5.57% | 84 | 27 | 18 |
| lgbm_calibrated|h4 | 993.15 | -0.68% | 192 | 108 | 15 |
| logistic|h1 | 952.85 | -4.71% | 63 | 29 | 18 |
| logistic|h4 | 1006.85 | +0.68% | 129 | 58 | 15 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 18 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 15 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 18 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 15 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 17 |
| recent_base_rate_7d|h4 | 992.37 | -0.76% | 840 | 381 | 14 |
| benchmark_long_all_coins|h1 | 989.82 | -1.02% | 1080 | 456 | 18 |
| benchmark_long_all_coins|h4 | 999.29 | -0.07% | 900 | 395 | 15 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 13 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 10 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 15 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 13 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 10 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 13 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 10 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 15 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 15 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 15 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 15 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 17 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 14 |

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
