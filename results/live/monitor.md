# Live monitor (2026-10-20T11:06:54.956313+00:00)

## Alerts

- none

## Health

- **venue**: okx
- **symbols**: 60
- **universe_size**: 60
- **fetched_only_for_scoring**: []
- **last_closed_bar**: 2026-10-20 10:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.8
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 104.6 instruments 60/60']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.118, 'recent_base_rate_7d': 0.124, 'momentum_24': 0.133, 'logistic': 0.125, 'lgbm_calibrated': 0.134, 'analog_k100': 0.127, 'derivatives': 0.121, 'orthosys': 0.119}
- **council_member_logloss_h1**: {'base_rate': 0.6932, 'recent_base_rate_7d': 0.6923, 'momentum_24': 0.691, 'logistic': 0.6921, 'lgbm_calibrated': 0.6908, 'analog_k100': 0.6919, 'derivatives': 0.6932, 'orthosys': 0.693}
- **council_calls_h1**: 7
- **council_abstain_h1**: {'no_edge': 48, 'spoke': 7, 'extreme_volatility': 5}
- **council_weights_h4**: {'base_rate': 0.133, 'recent_base_rate_7d': 0.074, 'momentum_24': 0.133, 'logistic': 0.134, 'lgbm_calibrated': 0.126, 'analog_k100': 0.133, 'derivatives': 0.13, 'orthosys': 0.136}
- **council_member_logloss_h4**: {'base_rate': 0.6935, 'recent_base_rate_7d': 0.7072, 'momentum_24': 0.6934, 'logistic': 0.6934, 'lgbm_calibrated': 0.6947, 'analog_k100': 0.6931, 'derivatives': 0.6938, 'orthosys': 0.693}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 39, 'members_disagree': 16, 'extreme_volatility': 5}
- **prediction_latency_min**: 6.8
- **price_snapshot_age_s**: 1.0
- **train_rows_h1**: 87379
- **orthosys_hist_hit_h1**: 0.528
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.011
- **p_spread_logistic_h1**: 0.0221
- **p_spread_lgbm_calibrated_h1**: 0.0033
- **p_spread_analog_k100_h1**: 0.061
- **p_spread_derivatives_h1**: 0.0013
- **p_spread_orthosys_h1**: 0.0062
- **p_spread_council_h1**: 0.0074
- **train_rows_h4**: 87199
- **orthosys_hist_hit_h4**: 0.5189
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0008
- **p_spread_logistic_h4**: 0.0291
- **p_spread_lgbm_calibrated_h4**: 0.0034
- **p_spread_analog_k100_h4**: 0.0782
- **p_spread_derivatives_h4**: 0.0084
- **p_spread_orthosys_h4**: 0.0042
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 19680

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 840 | 14 | 840 | 0.517 | 0.48-0.55 | 0.489 | 0.482 | -0.0032 | 0.032 | 0.44 | -10.0 |
| analog_k100|h1|on_time | 840 | 14 | 840 | 0.517 | 0.48-0.55 | 0.489 | 0.482 | -0.0032 | 0.032 | 0.44 | -10.0 |
| analog_k100|h4|all | 660 | 11 | 660 | 0.547 | 0.51-0.58 | 0.424 | 0.460 | +0.0115 | 0.042 | 0.57 | -1.1 |
| analog_k100|h4|on_time | 660 | 11 | 660 | 0.547 | 0.51-0.58 | 0.424 | 0.460 | +0.0115 | 0.042 | 0.57 | -1.1 |
| base_rate|h1|all | 1140 | 19 | 1140 | 0.506 | 0.48-0.54 | 0.494 | 0.498 | +0.0000 | 0.004 | 0.00 | - |
| base_rate|h1|on_time | 1080 | 18 | 1080 | 0.515 | 0.49-0.54 | 0.485 | 0.498 | +0.0000 | 0.013 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 960 | 16 | 960 | 0.476 | 0.44-0.51 | 0.476 | 0.503 | +0.0000 | 0.027 | 0.00 | - |
| base_rate|h4|on_time | 960 | 16 | 960 | 0.476 | 0.44-0.51 | 0.476 | 0.503 | +0.0000 | 0.027 | 0.00 | - |
| council|h1|all | 840 | 14 | 96 | 0.552 | 0.45-0.65 | 0.489 | 0.497 | +0.0008 | 0.008 | 0.00 | - |
| council|h1|on_time | 840 | 14 | 96 | 0.552 | 0.45-0.65 | 0.489 | 0.497 | +0.0008 | 0.008 | 0.00 | - |
| council|h4|all | 660 | 11 | 12 | 0.750 | 0.47-0.91 | 0.424 | 0.500 | +0.0031 | 0.075 | 0.00 | - |
| council|h4|on_time | 660 | 11 | 12 | 0.750 | 0.47-0.91 | 0.424 | 0.500 | +0.0031 | 0.075 | 0.00 | - |
| derivatives|h1|all | 840 | 14 | 840 | 0.505 | 0.47-0.54 | 0.489 | 0.498 | -0.0002 | 0.009 | 0.00 | - |
| derivatives|h1|on_time | 840 | 14 | 840 | 0.505 | 0.47-0.54 | 0.489 | 0.498 | -0.0002 | 0.009 | 0.00 | - |
| derivatives|h4|all | 660 | 11 | 660 | 0.445 | 0.41-0.48 | 0.424 | 0.503 | +0.0002 | 0.078 | 0.00 | -162.9 |
| derivatives|h4|on_time | 660 | 11 | 660 | 0.445 | 0.41-0.48 | 0.424 | 0.503 | +0.0002 | 0.078 | 0.00 | -162.9 |
| lgbm_calibrated|h1|all | 1140 | 19 | 1140 | 0.548 | 0.52-0.58 | 0.494 | 0.479 | +0.0040 | 0.026 | 0.07 | -33.2 |
| lgbm_calibrated|h1|on_time | 1080 | 18 | 1080 | 0.559 | 0.53-0.59 | 0.485 | 0.479 | +0.0063 | 0.038 | 0.08 | -33.2 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 960 | 16 | 960 | 0.522 | 0.49-0.55 | 0.476 | 0.461 | +0.0028 | 0.017 | 0.20 | -0.9 |
| lgbm_calibrated|h4|on_time | 960 | 16 | 960 | 0.522 | 0.49-0.55 | 0.476 | 0.461 | +0.0028 | 0.017 | 0.20 | -0.9 |
| logistic|h1|all | 1140 | 19 | 1140 | 0.537 | 0.51-0.57 | 0.494 | 0.492 | +0.0026 | 0.020 | 0.06 | -28.2 |
| logistic|h1|on_time | 1080 | 18 | 1080 | 0.523 | 0.49-0.55 | 0.485 | 0.490 | -0.0005 | 0.008 | 0.06 | -28.5 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 960 | 16 | 960 | 0.505 | 0.47-0.54 | 0.476 | 0.491 | -0.0014 | 0.023 | 0.14 | +8.3 |
| logistic|h4|on_time | 960 | 16 | 960 | 0.505 | 0.47-0.54 | 0.476 | 0.491 | -0.0014 | 0.023 | 0.14 | +8.3 |
| momentum_24|h1|all | 1140 | 19 | 1140 | 0.555 | 0.53-0.58 | 0.494 | 0.500 | +0.0038 | 0.046 | 0.00 | - |
| momentum_24|h1|on_time | 1080 | 18 | 1080 | 0.547 | 0.52-0.58 | 0.485 | 0.500 | +0.0032 | 0.038 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 960 | 16 | 960 | 0.476 | 0.44-0.51 | 0.476 | 0.503 | +0.0001 | 0.027 | 0.00 | - |
| momentum_24|h4|on_time | 960 | 16 | 960 | 0.476 | 0.44-0.51 | 0.476 | 0.503 | +0.0001 | 0.027 | 0.00 | - |
| orthosys|h1|all | 1140 | 19 | 48 | 0.500 | 0.36-0.64 | 0.494 | 0.499 | +0.0001 | 0.006 | 0.00 | - |
| orthosys|h1|on_time | 1080 | 18 | 47 | 0.489 | 0.35-0.63 | 0.485 | 0.499 | -0.0002 | 0.016 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 960 | 16 | 38 | 0.605 | 0.45-0.74 | 0.476 | 0.500 | +0.0015 | 0.024 | 0.00 | - |
| orthosys|h4|on_time | 960 | 16 | 38 | 0.605 | 0.45-0.74 | 0.476 | 0.500 | +0.0015 | 0.024 | 0.00 | - |
| recent_base_rate_7d|h1|all | 1080 | 18 | 1080 | 0.515 | 0.49-0.54 | 0.485 | 0.471 | +0.0002 | 0.014 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 1080 | 18 | 1080 | 0.515 | 0.49-0.54 | 0.485 | 0.471 | +0.0002 | 0.014 | 0.00 | - |
| recent_base_rate_7d|h4|all | 900 | 15 | 900 | 0.512 | 0.48-0.54 | 0.488 | 0.438 | -0.0171 | 0.050 | 1.00 | -17.6 |
| recent_base_rate_7d|h4|on_time | 900 | 15 | 900 | 0.512 | 0.48-0.54 | 0.488 | 0.438 | -0.0171 | 0.050 | 1.00 | -17.6 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 986.98 | -1.30% | 370 | 141 | 14 |
| analog_k100|h4 | 1000.00 | -0.00% | 374 | 196 | 11 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 19 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 16 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 14 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 11 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 14 |
| derivatives|h4 | 991.86 | -0.81% | 2 | 0 | 11 |
| lgbm_calibrated|h1 | 944.33 | -5.57% | 84 | 27 | 19 |
| lgbm_calibrated|h4 | 993.15 | -0.68% | 192 | 108 | 16 |
| logistic|h1 | 955.17 | -4.48% | 64 | 30 | 19 |
| logistic|h4 | 1010.46 | +1.05% | 133 | 60 | 16 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 19 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 16 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 19 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 16 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 18 |
| recent_base_rate_7d|h4 | 993.42 | -0.66% | 900 | 424 | 15 |
| benchmark_long_all_coins|h1 | 990.62 | -0.94% | 1140 | 489 | 19 |
| benchmark_long_all_coins|h4 | 997.73 | -0.23% | 960 | 405 | 16 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 14 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 11 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 19 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 16 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 14 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 11 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 14 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 11 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 19 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 16 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 19 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 16 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 19 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 16 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 19 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 16 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 15 |

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
