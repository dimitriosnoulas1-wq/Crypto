# Live monitor (2026-10-20T16:06:38.770870+00:00)

## Alerts

- none

## Health

- **venue**: okx
- **symbols**: 64
- **universe_size**: 60
- **fetched_only_for_scoring**: ['ASTER', 'MUBARAK', 'PYTH', 'S']
- **last_closed_bar**: 2026-10-20 15:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.5
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 112.0 instruments 64/64']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.143, 'recent_base_rate_7d': 0.104, 'momentum_24': 0.162, 'logistic': 0.113, 'lgbm_calibrated': 0.127, 'analog_k100': 0.06, 'derivatives': 0.146, 'orthosys': 0.145}
- **council_member_logloss_h1**: {'base_rate': 0.6936, 'recent_base_rate_7d': 0.6984, 'momentum_24': 0.6918, 'logistic': 0.697, 'lgbm_calibrated': 0.6953, 'analog_k100': 0.7101, 'derivatives': 0.6938, 'orthosys': 0.6934}
- **council_calls_h1**: 1
- **council_abstain_h1**: {'no_edge': 57, 'extreme_volatility': 2, 'spoke': 1}
- **council_weights_h4**: {'base_rate': 0.148, 'recent_base_rate_7d': 0.044, 'momentum_24': 0.149, 'logistic': 0.214, 'lgbm_calibrated': 0.105, 'analog_k100': 0.047, 'derivatives': 0.144, 'orthosys': 0.15}
- **council_member_logloss_h4**: {'base_rate': 0.6932, 'recent_base_rate_7d': 0.7143, 'momentum_24': 0.6931, 'logistic': 0.6871, 'lgbm_calibrated': 0.699, 'analog_k100': 0.7185, 'derivatives': 0.6935, 'orthosys': 0.6929}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 36, 'members_disagree': 22, 'extreme_volatility': 2}
- **prediction_latency_min**: 6.5
- **price_snapshot_age_s**: 0.4
- **train_rows_h1**: 93699
- **orthosys_hist_hit_h1**: 0.5272
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0079
- **p_spread_logistic_h1**: 0.0252
- **p_spread_lgbm_calibrated_h1**: 0.0112
- **p_spread_analog_k100_h1**: 0.0641
- **p_spread_derivatives_h1**: 0.001
- **p_spread_orthosys_h1**: 0.0136
- **p_spread_council_h1**: 0.0028
- **train_rows_h4**: 93507
- **orthosys_hist_hit_h4**: 0.5152
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.001
- **p_spread_logistic_h4**: 0.0488
- **p_spread_lgbm_calibrated_h4**: 0.0036
- **p_spread_analog_k100_h4**: 0.0655
- **p_spread_derivatives_h4**: 0.0041
- **p_spread_orthosys_h4**: 0.0076
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 25080

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1140 | 19 | 1140 | 0.502 | 0.47-0.53 | 0.528 | 0.473 | -0.0178 | 0.060 | 0.48 | -7.4 |
| analog_k100|h1|on_time | 1140 | 19 | 1140 | 0.502 | 0.47-0.53 | 0.528 | 0.473 | -0.0178 | 0.060 | 0.48 | -7.4 |
| analog_k100|h4|all | 960 | 16 | 960 | 0.466 | 0.43-0.50 | 0.524 | 0.447 | -0.0672 | 0.113 | 0.62 | -62.8 |
| analog_k100|h4|on_time | 960 | 16 | 960 | 0.466 | 0.43-0.50 | 0.524 | 0.447 | -0.0672 | 0.113 | 0.62 | -62.8 |
| base_rate|h1|all | 1440 | 24 | 1440 | 0.476 | 0.45-0.50 | 0.524 | 0.498 | +0.0000 | 0.025 | 0.00 | - |
| base_rate|h1|on_time | 1380 | 23 | 1380 | 0.482 | 0.46-0.51 | 0.518 | 0.498 | +0.0000 | 0.020 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 1260 | 21 | 1260 | 0.540 | 0.51-0.57 | 0.540 | 0.503 | +0.0000 | 0.037 | 0.00 | - |
| base_rate|h4|on_time | 1260 | 21 | 1260 | 0.540 | 0.51-0.57 | 0.540 | 0.503 | +0.0000 | 0.037 | 0.00 | - |
| council|h1|all | 1140 | 19 | 200 | 0.550 | 0.48-0.62 | 0.528 | 0.495 | +0.0033 | 0.041 | 0.00 | +64.4 |
| council|h1|on_time | 1140 | 19 | 200 | 0.550 | 0.48-0.62 | 0.528 | 0.495 | +0.0033 | 0.041 | 0.00 | +64.4 |
| council|h4|all | 960 | 16 | 13 | 0.692 | 0.42-0.87 | 0.524 | 0.500 | +0.0008 | 0.029 | 0.00 | - |
| council|h4|on_time | 960 | 16 | 13 | 0.692 | 0.42-0.87 | 0.524 | 0.500 | +0.0008 | 0.029 | 0.00 | - |
| derivatives|h1|all | 1140 | 19 | 1140 | 0.469 | 0.44-0.50 | 0.528 | 0.498 | -0.0001 | 0.033 | 0.00 | - |
| derivatives|h1|on_time | 1140 | 19 | 1140 | 0.469 | 0.44-0.50 | 0.528 | 0.498 | -0.0001 | 0.033 | 0.00 | - |
| derivatives|h4|all | 960 | 16 | 960 | 0.527 | 0.50-0.56 | 0.524 | 0.502 | -0.0002 | 0.023 | 0.00 | -92.4 |
| derivatives|h4|on_time | 960 | 16 | 960 | 0.527 | 0.50-0.56 | 0.524 | 0.502 | -0.0002 | 0.023 | 0.00 | -92.4 |
| lgbm_calibrated|h1|all | 1440 | 24 | 1440 | 0.556 | 0.53-0.58 | 0.524 | 0.478 | +0.0065 | 0.052 | 0.10 | +37.4 |
| lgbm_calibrated|h1|on_time | 1380 | 23 | 1380 | 0.564 | 0.54-0.59 | 0.518 | 0.478 | +0.0084 | 0.047 | 0.10 | +37.4 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 1260 | 21 | 1260 | 0.460 | 0.43-0.49 | 0.540 | 0.462 | -0.0169 | 0.079 | 0.15 | -13.3 |
| lgbm_calibrated|h4|on_time | 1260 | 21 | 1260 | 0.460 | 0.43-0.49 | 0.540 | 0.462 | -0.0169 | 0.079 | 0.15 | -13.3 |
| logistic|h1|all | 1440 | 24 | 1440 | 0.524 | 0.50-0.55 | 0.524 | 0.488 | +0.0045 | 0.041 | 0.11 | -5.3 |
| logistic|h1|on_time | 1380 | 23 | 1380 | 0.512 | 0.49-0.54 | 0.518 | 0.486 | +0.0022 | 0.037 | 0.11 | -5.0 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 1260 | 21 | 1260 | 0.563 | 0.54-0.59 | 0.540 | 0.499 | +0.0153 | 0.041 | 0.14 | +87.4 |
| logistic|h4|on_time | 1260 | 21 | 1260 | 0.563 | 0.54-0.59 | 0.540 | 0.499 | +0.0153 | 0.041 | 0.14 | +87.4 |
| momentum_24|h1|all | 1440 | 24 | 1440 | 0.566 | 0.54-0.59 | 0.524 | 0.499 | +0.0049 | 0.056 | 0.00 | - |
| momentum_24|h1|on_time | 1380 | 23 | 1380 | 0.560 | 0.53-0.59 | 0.518 | 0.499 | +0.0045 | 0.050 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 1260 | 21 | 1260 | 0.540 | 0.51-0.57 | 0.540 | 0.503 | +0.0002 | 0.037 | 0.00 | - |
| momentum_24|h4|on_time | 1260 | 21 | 1260 | 0.540 | 0.51-0.57 | 0.540 | 0.503 | +0.0002 | 0.037 | 0.00 | - |
| orthosys|h1|all | 1440 | 24 | 87 | 0.575 | 0.47-0.67 | 0.524 | 0.499 | +0.0014 | 0.030 | 0.00 | - |
| orthosys|h1|on_time | 1380 | 23 | 86 | 0.570 | 0.46-0.67 | 0.518 | 0.499 | +0.0013 | 0.024 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 1260 | 21 | 53 | 0.585 | 0.45-0.71 | 0.540 | 0.500 | +0.0002 | 0.048 | 0.00 | - |
| orthosys|h4|on_time | 1260 | 21 | 53 | 0.585 | 0.45-0.71 | 0.540 | 0.500 | +0.0002 | 0.048 | 0.00 | - |
| recent_base_rate_7d|h1|all | 1380 | 23 | 1380 | 0.482 | 0.46-0.51 | 0.518 | 0.472 | -0.0066 | 0.046 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 1380 | 23 | 1380 | 0.482 | 0.46-0.51 | 0.518 | 0.472 | -0.0066 | 0.046 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1200 | 20 | 1200 | 0.448 | 0.42-0.48 | 0.552 | 0.436 | -0.0514 | 0.115 | 1.00 | -60.9 |
| recent_base_rate_7d|h4|on_time | 1200 | 20 | 1200 | 0.448 | 0.42-0.48 | 0.552 | 0.436 | -0.0514 | 0.115 | 1.00 | -60.9 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 981.56 | -1.84% | 547 | 207 | 19 |
| analog_k100|h4 | 978.38 | -2.16% | 598 | 239 | 16 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 24 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 21 |
| council|h1 | 1006.44 | +0.64% | 3 | 2 | 19 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 16 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 19 |
| derivatives|h4 | 990.74 | -0.93% | 4 | 1 | 16 |
| lgbm_calibrated|h1 | 957.21 | -4.28% | 144 | 80 | 24 |
| lgbm_calibrated|h4 | 934.18 | -6.58% | 195 | 108 | 21 |
| logistic|h1 | 962.30 | -3.77% | 157 | 80 | 24 |
| logistic|h4 | 1049.95 | +4.99% | 177 | 97 | 21 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 24 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 21 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 24 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 21 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 23 |
| recent_base_rate_7d|h4 | 969.91 | -3.01% | 1200 | 476 | 20 |
| benchmark_long_all_coins|h1 | 1004.41 | +0.44% | 1440 | 672 | 24 |
| benchmark_long_all_coins|h4 | 1019.18 | +1.92% | 1260 | 640 | 21 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 19 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 16 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 19 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 16 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 19 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 16 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 24 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 20 |

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
