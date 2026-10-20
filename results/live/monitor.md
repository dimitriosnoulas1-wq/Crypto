# Live monitor (2026-10-20T17:08:19.434293+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.491
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.497

## Health

- **venue**: okx
- **symbols**: 65
- **universe_size**: 60
- **fetched_only_for_scoring**: ['ASTER', 'MUBARAK', 'PYTH', 'S', 'WLFI']
- **last_closed_bar**: 2026-10-20 16:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 6.2
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 115.5 instruments 65/65']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.123, 'recent_base_rate_7d': 0.099, 'momentum_24': 0.147, 'logistic': 0.145, 'lgbm_calibrated': 0.156, 'analog_k100': 0.075, 'derivatives': 0.126, 'orthosys': 0.129}
- **council_member_logloss_h1**: {'base_rate': 0.6935, 'recent_base_rate_7d': 0.6967, 'momentum_24': 0.691, 'logistic': 0.6912, 'lgbm_calibrated': 0.6901, 'analog_k100': 0.7027, 'derivatives': 0.6936, 'orthosys': 0.6928}
- **council_calls_h1**: 29
- **council_abstain_h1**: {'no_edge': 30, 'spoke': 29, 'extreme_volatility': 1}
- **council_weights_h4**: {'base_rate': 0.152, 'recent_base_rate_7d': 0.032, 'momentum_24': 0.153, 'logistic': 0.246, 'lgbm_calibrated': 0.089, 'analog_k100': 0.027, 'derivatives': 0.147, 'orthosys': 0.153}
- **council_member_logloss_h4**: {'base_rate': 0.6931, 'recent_base_rate_7d': 0.7188, 'momentum_24': 0.693, 'logistic': 0.6854, 'lgbm_calibrated': 0.7015, 'analog_k100': 0.7286, 'derivatives': 0.6934, 'orthosys': 0.6929}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'members_disagree': 38, 'no_edge': 21, 'extreme_volatility': 1}
- **prediction_latency_min**: 8.2
- **price_snapshot_age_s**: 1.0
- **train_rows_h1**: 95261
- **orthosys_hist_hit_h1**: 0.5268
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0075
- **p_spread_logistic_h1**: 0.0316
- **p_spread_lgbm_calibrated_h1**: 0.0117
- **p_spread_analog_k100_h1**: 0.0561
- **p_spread_derivatives_h1**: 0.0009
- **p_spread_orthosys_h1**: 0.0143
- **p_spread_council_h1**: 0.0141
- **train_rows_h4**: 95066
- **orthosys_hist_hit_h4**: 0.516
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0014
- **p_spread_logistic_h4**: 0.0617
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0791
- **p_spread_derivatives_h4**: 0.0067
- **p_spread_orthosys_h4**: 0.0086
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 26160

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1200 | 20 | 1200 | 0.493 | 0.47-0.52 | 0.541 | 0.473 | -0.0222 | 0.072 | 0.48 | -11.0 |
| analog_k100|h1|on_time | 1200 | 20 | 1200 | 0.493 | 0.47-0.52 | 0.541 | 0.473 | -0.0222 | 0.072 | 0.48 | -11.0 |
| analog_k100|h4|all | 1020 | 17 | 1020 | 0.452 | 0.42-0.48 | 0.545 | 0.446 | -0.0821 | 0.127 | 0.62 | -74.6 |
| analog_k100|h4|on_time | 1020 | 17 | 1020 | 0.452 | 0.42-0.48 | 0.545 | 0.446 | -0.0821 | 0.127 | 0.62 | -74.6 |
| base_rate|h1|all | 1500 | 25 | 1500 | 0.466 | 0.44-0.49 | 0.534 | 0.498 | +0.0000 | 0.036 | 0.00 | - |
| base_rate|h1|on_time | 1440 | 24 | 1440 | 0.471 | 0.45-0.50 | 0.529 | 0.498 | +0.0000 | 0.031 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 1320 | 22 | 1320 | 0.555 | 0.53-0.58 | 0.555 | 0.503 | +0.0000 | 0.052 | 0.00 | - |
| base_rate|h4|on_time | 1320 | 22 | 1320 | 0.555 | 0.53-0.58 | 0.555 | 0.503 | +0.0000 | 0.052 | 0.00 | - |
| council|h1|all | 1200 | 20 | 201 | 0.547 | 0.48-0.61 | 0.541 | 0.495 | +0.0033 | 0.053 | 0.00 | +64.4 |
| council|h1|on_time | 1200 | 20 | 201 | 0.547 | 0.48-0.61 | 0.541 | 0.495 | +0.0033 | 0.053 | 0.00 | +64.4 |
| council|h4|all | 1020 | 17 | 15 | 0.667 | 0.42-0.85 | 0.545 | 0.500 | +0.0004 | 0.050 | 0.00 | - |
| council|h4|on_time | 1020 | 17 | 15 | 0.667 | 0.42-0.85 | 0.545 | 0.500 | +0.0004 | 0.050 | 0.00 | - |
| derivatives|h1|all | 1200 | 20 | 1200 | 0.457 | 0.43-0.48 | 0.541 | 0.498 | -0.0001 | 0.045 | 0.00 | - |
| derivatives|h1|on_time | 1200 | 20 | 1200 | 0.457 | 0.43-0.48 | 0.541 | 0.498 | -0.0001 | 0.045 | 0.00 | - |
| derivatives|h4|all | 1020 | 17 | 1020 | 0.543 | 0.51-0.57 | 0.545 | 0.502 | -0.0005 | 0.043 | 0.00 | -117.6 |
| derivatives|h4|on_time | 1020 | 17 | 1020 | 0.543 | 0.51-0.57 | 0.545 | 0.502 | -0.0005 | 0.043 | 0.00 | -117.6 |
| lgbm_calibrated|h1|all | 1500 | 25 | 1500 | 0.565 | 0.54-0.59 | 0.534 | 0.479 | +0.0075 | 0.061 | 0.10 | +37.4 |
| lgbm_calibrated|h1|on_time | 1440 | 24 | 1440 | 0.574 | 0.55-0.60 | 0.529 | 0.480 | +0.0094 | 0.056 | 0.10 | +37.4 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 1320 | 22 | 1320 | 0.444 | 0.42-0.47 | 0.555 | 0.462 | -0.0217 | 0.094 | 0.15 | -17.9 |
| lgbm_calibrated|h4|on_time | 1320 | 22 | 1320 | 0.444 | 0.42-0.47 | 0.555 | 0.462 | -0.0217 | 0.094 | 0.15 | -17.9 |
| logistic|h1|all | 1500 | 25 | 1500 | 0.533 | 0.51-0.56 | 0.534 | 0.490 | +0.0083 | 0.049 | 0.12 | -3.8 |
| logistic|h1|on_time | 1440 | 24 | 1440 | 0.522 | 0.50-0.55 | 0.529 | 0.489 | +0.0062 | 0.046 | 0.12 | -3.5 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 1320 | 22 | 1320 | 0.559 | 0.53-0.59 | 0.555 | 0.499 | +0.0141 | 0.056 | 0.14 | +83.9 |
| logistic|h4|on_time | 1320 | 22 | 1320 | 0.559 | 0.53-0.59 | 0.555 | 0.499 | +0.0141 | 0.056 | 0.14 | +83.9 |
| momentum_24|h1|all | 1500 | 25 | 1500 | 0.555 | 0.53-0.58 | 0.534 | 0.499 | +0.0040 | 0.045 | 0.00 | - |
| momentum_24|h1|on_time | 1440 | 24 | 1440 | 0.549 | 0.52-0.57 | 0.529 | 0.499 | +0.0035 | 0.039 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 1320 | 22 | 1320 | 0.555 | 0.53-0.58 | 0.555 | 0.503 | +0.0003 | 0.052 | 0.00 | - |
| momentum_24|h4|on_time | 1320 | 22 | 1320 | 0.555 | 0.53-0.58 | 0.555 | 0.503 | +0.0003 | 0.052 | 0.00 | - |
| orthosys|h1|all | 1500 | 25 | 105 | 0.514 | 0.42-0.61 | 0.534 | 0.499 | +0.0008 | 0.035 | 0.00 | - |
| orthosys|h1|on_time | 1440 | 24 | 104 | 0.510 | 0.41-0.60 | 0.529 | 0.499 | +0.0006 | 0.031 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 1320 | 22 | 57 | 0.579 | 0.45-0.70 | 0.555 | 0.500 | -0.0000 | 0.063 | 0.00 | - |
| orthosys|h4|on_time | 1320 | 22 | 57 | 0.579 | 0.45-0.70 | 0.555 | 0.500 | -0.0000 | 0.063 | 0.00 | - |
| recent_base_rate_7d|h1|all | 1440 | 24 | 1440 | 0.471 | 0.45-0.50 | 0.529 | 0.472 | -0.0085 | 0.057 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 1440 | 24 | 1440 | 0.471 | 0.45-0.50 | 0.529 | 0.472 | -0.0085 | 0.057 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1260 | 21 | 1260 | 0.433 | 0.41-0.46 | 0.567 | 0.436 | -0.0592 | 0.131 | 1.00 | -71.3 |
| recent_base_rate_7d|h4|on_time | 1260 | 21 | 1260 | 0.433 | 0.41-0.46 | 0.567 | 0.436 | -0.0592 | 0.131 | 1.00 | -71.3 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 974.47 | -2.55% | 579 | 217 | 20 |
| analog_k100|h4 | 972.03 | -2.80% | 636 | 243 | 17 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 25 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 22 |
| council|h1 | 1006.44 | +0.64% | 3 | 2 | 20 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 17 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 20 |
| derivatives|h4 | 985.33 | -1.47% | 5 | 1 | 17 |
| lgbm_calibrated|h1 | 957.21 | -4.28% | 144 | 80 | 25 |
| lgbm_calibrated|h4 | 923.28 | -7.67% | 197 | 108 | 22 |
| logistic|h1 | 962.79 | -3.72% | 183 | 95 | 25 |
| logistic|h4 | 1048.85 | +4.88% | 182 | 100 | 22 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 25 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 22 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 25 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 22 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 24 |
| recent_base_rate_7d|h4 | 963.11 | -3.69% | 1260 | 481 | 21 |
| benchmark_long_all_coins|h1 | 1005.77 | +0.58% | 1500 | 707 | 25 |
| benchmark_long_all_coins|h4 | 1025.82 | +2.58% | 1320 | 694 | 22 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 20 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 17 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 20 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 17 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 20 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 17 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 21 |

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
