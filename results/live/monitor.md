# Live monitor (2026-10-20T15:08:29.649116+00:00)

## Alerts

- none

## Health

- **venue**: okx
- **symbols**: 64
- **universe_size**: 60
- **fetched_only_for_scoring**: ['ASTER', 'MUBARAK', 'PYTH', 'RAY']
- **last_closed_bar**: 2026-10-20 14:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 6.3
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 113.6 instruments 64/64']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.13, 'recent_base_rate_7d': 0.108, 'momentum_24': 0.151, 'logistic': 0.136, 'lgbm_calibrated': 0.146, 'analog_k100': 0.065, 'derivatives': 0.133, 'orthosys': 0.132}
- **council_member_logloss_h1**: {'base_rate': 0.6935, 'recent_base_rate_7d': 0.6965, 'momentum_24': 0.6912, 'logistic': 0.6927, 'lgbm_calibrated': 0.6917, 'analog_k100': 0.7075, 'derivatives': 0.6936, 'orthosys': 0.6932}
- **council_calls_h1**: 53
- **council_abstain_h1**: {'spoke': 53, 'extreme_volatility': 4, 'no_edge': 3}
- **council_weights_h4**: {'base_rate': 0.142, 'recent_base_rate_7d': 0.063, 'momentum_24': 0.143, 'logistic': 0.169, 'lgbm_calibrated': 0.123, 'analog_k100': 0.075, 'derivatives': 0.139, 'orthosys': 0.146}
- **council_member_logloss_h4**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.7082, 'momentum_24': 0.6933, 'logistic': 0.6904, 'lgbm_calibrated': 0.696, 'analog_k100': 0.7082, 'derivatives': 0.6936, 'orthosys': 0.6929}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'members_disagree': 39, 'no_edge': 17, 'extreme_volatility': 4}
- **prediction_latency_min**: 8.4
- **price_snapshot_age_s**: 1.2
- **train_rows_h1**: 93659
- **orthosys_hist_hit_h1**: 0.5264
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0053
- **p_spread_logistic_h1**: 0.0339
- **p_spread_lgbm_calibrated_h1**: 0.0478
- **p_spread_analog_k100_h1**: 0.0608
- **p_spread_derivatives_h1**: 0.0014
- **p_spread_orthosys_h1**: 0.0142
- **p_spread_council_h1**: 0.0143
- **train_rows_h4**: 93467
- **orthosys_hist_hit_h4**: 0.5168
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0006
- **p_spread_logistic_h4**: 0.0783
- **p_spread_lgbm_calibrated_h4**: 0.0939
- **p_spread_analog_k100_h4**: 0.0848
- **p_spread_derivatives_h4**: 0.0057
- **p_spread_orthosys_h4**: 0.009
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 24000

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1080 | 18 | 1080 | 0.481 | 0.45-0.51 | 0.554 | 0.475 | -0.0319 | 0.083 | 0.47 | -24.0 |
| analog_k100|h1|on_time | 1080 | 18 | 1080 | 0.481 | 0.45-0.51 | 0.554 | 0.475 | -0.0319 | 0.083 | 0.47 | -24.0 |
| analog_k100|h4|all | 900 | 15 | 900 | 0.487 | 0.45-0.52 | 0.500 | 0.449 | -0.0475 | 0.090 | 0.62 | -51.1 |
| analog_k100|h4|on_time | 900 | 15 | 900 | 0.487 | 0.45-0.52 | 0.500 | 0.449 | -0.0475 | 0.090 | 0.62 | -51.1 |
| base_rate|h1|all | 1380 | 23 | 1380 | 0.457 | 0.43-0.48 | 0.543 | 0.498 | +0.0000 | 0.045 | 0.00 | - |
| base_rate|h1|on_time | 1320 | 22 | 1320 | 0.461 | 0.43-0.49 | 0.539 | 0.498 | +0.0000 | 0.040 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 1200 | 20 | 1200 | 0.522 | 0.49-0.55 | 0.522 | 0.503 | +0.0000 | 0.019 | 0.00 | - |
| base_rate|h4|on_time | 1200 | 20 | 1200 | 0.522 | 0.49-0.55 | 0.522 | 0.503 | +0.0000 | 0.019 | 0.00 | - |
| council|h1|all | 1080 | 18 | 147 | 0.401 | 0.33-0.48 | 0.554 | 0.497 | -0.0022 | 0.057 | 0.00 | - |
| council|h1|on_time | 1080 | 18 | 147 | 0.401 | 0.33-0.48 | 0.554 | 0.497 | -0.0022 | 0.057 | 0.00 | - |
| council|h4|all | 900 | 15 | 12 | 0.750 | 0.47-0.91 | 0.500 | 0.500 | +0.0013 | 0.006 | 0.00 | - |
| council|h4|on_time | 900 | 15 | 12 | 0.750 | 0.47-0.91 | 0.500 | 0.500 | +0.0013 | 0.006 | 0.00 | - |
| derivatives|h1|all | 1080 | 18 | 1080 | 0.443 | 0.41-0.47 | 0.554 | 0.498 | -0.0002 | 0.059 | 0.00 | - |
| derivatives|h1|on_time | 1080 | 18 | 1080 | 0.443 | 0.41-0.47 | 0.554 | 0.498 | -0.0002 | 0.059 | 0.00 | - |
| derivatives|h4|all | 900 | 15 | 900 | 0.510 | 0.48-0.54 | 0.500 | 0.502 | -0.0000 | 0.006 | 0.00 | -92.4 |
| derivatives|h4|on_time | 900 | 15 | 900 | 0.510 | 0.48-0.54 | 0.500 | 0.502 | -0.0000 | 0.006 | 0.00 | -92.4 |
| lgbm_calibrated|h1|all | 1380 | 23 | 1380 | 0.539 | 0.51-0.57 | 0.543 | 0.480 | -0.0034 | 0.063 | 0.06 | -33.2 |
| lgbm_calibrated|h1|on_time | 1320 | 22 | 1320 | 0.548 | 0.52-0.57 | 0.539 | 0.481 | -0.0018 | 0.058 | 0.06 | -33.2 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 1200 | 20 | 1200 | 0.477 | 0.45-0.50 | 0.522 | 0.462 | -0.0116 | 0.061 | 0.16 | -11.1 |
| lgbm_calibrated|h4|on_time | 1200 | 20 | 1200 | 0.477 | 0.45-0.50 | 0.522 | 0.462 | -0.0116 | 0.061 | 0.16 | -11.1 |
| logistic|h1|all | 1380 | 23 | 1380 | 0.505 | 0.48-0.53 | 0.543 | 0.491 | -0.0066 | 0.053 | 0.08 | -73.4 |
| logistic|h1|on_time | 1320 | 22 | 1320 | 0.492 | 0.47-0.52 | 0.539 | 0.490 | -0.0096 | 0.050 | 0.08 | -74.9 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 1200 | 20 | 1200 | 0.548 | 0.52-0.58 | 0.522 | 0.498 | +0.0123 | 0.025 | 0.14 | +83.9 |
| logistic|h4|on_time | 1200 | 20 | 1200 | 0.548 | 0.52-0.58 | 0.522 | 0.498 | +0.0123 | 0.025 | 0.14 | +83.9 |
| momentum_24|h1|all | 1380 | 23 | 1380 | 0.551 | 0.53-0.58 | 0.543 | 0.500 | +0.0037 | 0.044 | 0.00 | - |
| momentum_24|h1|on_time | 1320 | 22 | 1320 | 0.545 | 0.52-0.57 | 0.539 | 0.499 | +0.0032 | 0.039 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 1200 | 20 | 1200 | 0.522 | 0.49-0.55 | 0.522 | 0.503 | +0.0001 | 0.019 | 0.00 | - |
| momentum_24|h4|on_time | 1200 | 20 | 1200 | 0.522 | 0.49-0.55 | 0.522 | 0.503 | +0.0001 | 0.019 | 0.00 | - |
| orthosys|h1|all | 1380 | 23 | 64 | 0.469 | 0.35-0.59 | 0.543 | 0.499 | +0.0005 | 0.044 | 0.00 | - |
| orthosys|h1|on_time | 1320 | 22 | 63 | 0.460 | 0.34-0.58 | 0.539 | 0.499 | +0.0003 | 0.039 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 1200 | 20 | 51 | 0.588 | 0.45-0.71 | 0.522 | 0.500 | +0.0005 | 0.032 | 0.00 | - |
| orthosys|h4|on_time | 1200 | 20 | 51 | 0.588 | 0.45-0.71 | 0.522 | 0.500 | +0.0005 | 0.032 | 0.00 | - |
| recent_base_rate_7d|h1|all | 1320 | 22 | 1320 | 0.461 | 0.43-0.49 | 0.539 | 0.471 | -0.0096 | 0.067 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 1320 | 22 | 1320 | 0.461 | 0.43-0.49 | 0.539 | 0.471 | -0.0096 | 0.067 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1140 | 19 | 1140 | 0.466 | 0.44-0.49 | 0.534 | 0.437 | -0.0422 | 0.098 | 1.00 | -52.1 |
| recent_base_rate_7d|h4|on_time | 1140 | 19 | 1140 | 0.466 | 0.44-0.49 | 0.534 | 0.437 | -0.0422 | 0.098 | 1.00 | -52.1 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 962.00 | -3.80% | 507 | 169 | 18 |
| analog_k100|h4 | 983.75 | -1.62% | 556 | 233 | 15 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 23 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 20 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 18 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 15 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 18 |
| derivatives|h4 | 990.74 | -0.93% | 4 | 1 | 15 |
| lgbm_calibrated|h1 | 944.33 | -5.57% | 84 | 27 | 23 |
| lgbm_calibrated|h4 | 944.84 | -5.52% | 194 | 108 | 20 |
| logistic|h1 | 948.56 | -5.14% | 108 | 35 | 23 |
| logistic|h4 | 1045.42 | +4.54% | 170 | 92 | 20 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 23 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 20 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 23 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 20 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 22 |
| recent_base_rate_7d|h4 | 975.48 | -2.45% | 1140 | 470 | 19 |
| benchmark_long_all_coins|h1 | 1020.36 | +2.04% | 1380 | 668 | 23 |
| benchmark_long_all_coins|h4 | 1013.90 | +1.39% | 1200 | 588 | 20 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 15 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 20 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 15 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 15 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 20 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 20 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 20 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 20 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 22 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 19 |

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
