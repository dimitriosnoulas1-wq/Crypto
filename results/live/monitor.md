# Live monitor (2026-10-22T08:06:32.807453+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.49 (ECE 0.112)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.489
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.434

## Health

- **venue**: okx
- **symbols**: 63
- **universe_size**: 60
- **fetched_only_for_scoring**: ['APR', 'CHIP', 'SHIB']
- **last_closed_bar**: 2026-10-22 07:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.4
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 106.0 instruments 63/63']
- **feature_nan_share_latest_bar**: 0.033
- **council_weights_h1**: {'base_rate': 0.157, 'recent_base_rate_7d': 0.138, 'momentum_24': 0.164, 'logistic': 0.085, 'lgbm_calibrated': 0.137, 'analog_k100': 0.012, 'derivatives': 0.176, 'orthosys': 0.132}
- **council_member_logloss_h1**: {'base_rate': 0.6928, 'recent_base_rate_7d': 0.6935, 'momentum_24': 0.6926, 'logistic': 0.6961, 'lgbm_calibrated': 0.6936, 'analog_k100': 0.7079, 'derivatives': 0.6923, 'orthosys': 0.6937}
- **council_calls_h1**: 1
- **council_abstain_h1**: {'no_edge': 51, 'extreme_volatility': 7, 'missing_inputs': 1, 'spoke': 1}
- **council_weights_h4**: {'base_rate': 0.194, 'recent_base_rate_7d': 0.009, 'momentum_24': 0.191, 'logistic': 0.046, 'lgbm_calibrated': 0.097, 'analog_k100': 0.002, 'derivatives': 0.274, 'orthosys': 0.186}
- **council_member_logloss_h4**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.7104, 'momentum_24': 0.6934, 'logistic': 0.7013, 'lgbm_calibrated': 0.6972, 'analog_k100': 0.7214, 'derivatives': 0.6912, 'orthosys': 0.6936}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 51, 'extreme_volatility': 7, 'missing_inputs': 1, 'members_disagree': 1}
- **prediction_latency_min**: 6.4
- **price_snapshot_age_s**: 0.9
- **train_rows_h1**: 92957
- **orthosys_hist_hit_h1**: 0.5264
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0051
- **p_spread_logistic_h1**: 0.034
- **p_spread_lgbm_calibrated_h1**: 0.0059
- **p_spread_analog_k100_h1**: 0.0885
- **p_spread_derivatives_h1**: 0.0192
- **p_spread_orthosys_h1**: 0.0124
- **p_spread_council_h1**: 0.0026
- **train_rows_h4**: 92768
- **orthosys_hist_hit_h4**: 0.5077
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0001
- **p_spread_logistic_h4**: 0.0578
- **p_spread_lgbm_calibrated_h4**: 0.0573
- **p_spread_analog_k100_h4**: 0.0769
- **p_spread_derivatives_h4**: 0.0329
- **p_spread_orthosys_h4**: 0.0036
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 68280

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 3540 | 59 | 3540 | 0.493 | 0.48-0.51 | 0.475 | 0.470 | -0.0280 | 0.065 | 0.51 | -14.7 |
| analog_k100|h1|on_time | 3540 | 59 | 3540 | 0.493 | 0.48-0.51 | 0.475 | 0.470 | -0.0280 | 0.065 | 0.51 | -14.7 |
| analog_k100|h4|all | 3360 | 56 | 3360 | 0.472 | 0.46-0.49 | 0.494 | 0.449 | -0.0603 | 0.112 | 0.66 | -15.1 |
| analog_k100|h4|on_time | 3360 | 56 | 3360 | 0.472 | 0.46-0.49 | 0.494 | 0.449 | -0.0603 | 0.112 | 0.66 | -15.1 |
| base_rate|h1|all | 3840 | 64 | 3840 | 0.523 | 0.51-0.54 | 0.477 | 0.498 | +0.0000 | 0.020 | 0.00 | - |
| base_rate|h1|on_time | 3780 | 63 | 3780 | 0.525 | 0.51-0.54 | 0.475 | 0.498 | +0.0000 | 0.023 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 3660 | 61 | 3660 | 0.502 | 0.49-0.52 | 0.502 | 0.504 | +0.0000 | 0.002 | 0.00 | - |
| base_rate|h4|on_time | 3660 | 61 | 3660 | 0.502 | 0.49-0.52 | 0.502 | 0.504 | +0.0000 | 0.002 | 0.00 | - |
| council|h1|all | 3540 | 59 | 495 | 0.513 | 0.47-0.56 | 0.475 | 0.496 | -0.0005 | 0.025 | 0.00 | +18.3 |
| council|h1|on_time | 3540 | 59 | 495 | 0.513 | 0.47-0.56 | 0.475 | 0.496 | -0.0005 | 0.025 | 0.00 | +18.3 |
| council|h4|all | 3360 | 56 | 25 | 0.600 | 0.41-0.77 | 0.494 | 0.500 | +0.0009 | 0.006 | 0.00 | - |
| council|h4|on_time | 3360 | 56 | 25 | 0.600 | 0.41-0.77 | 0.494 | 0.500 | +0.0009 | 0.006 | 0.00 | - |
| derivatives|h1|all | 3540 | 59 | 3540 | 0.525 | 0.51-0.54 | 0.475 | 0.496 | +0.0013 | 0.022 | 0.01 | -10.1 |
| derivatives|h1|on_time | 3540 | 59 | 3540 | 0.525 | 0.51-0.54 | 0.475 | 0.496 | +0.0013 | 0.022 | 0.01 | -10.1 |
| derivatives|h4|all | 3360 | 56 | 3360 | 0.511 | 0.49-0.53 | 0.494 | 0.500 | +0.0045 | 0.007 | 0.02 | +448.9 |
| derivatives|h4|on_time | 3360 | 56 | 3360 | 0.511 | 0.49-0.53 | 0.494 | 0.500 | +0.0045 | 0.007 | 0.02 | +448.9 |
| lgbm_calibrated|h1|all | 3840 | 64 | 3839 | 0.547 | 0.53-0.56 | 0.477 | 0.476 | -0.0012 | 0.019 | 0.14 | -1.4 |
| lgbm_calibrated|h1|on_time | 3780 | 63 | 3779 | 0.550 | 0.53-0.57 | 0.475 | 0.476 | -0.0007 | 0.022 | 0.14 | -1.4 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 3660 | 61 | 3660 | 0.498 | 0.48-0.51 | 0.502 | 0.463 | -0.0058 | 0.040 | 0.15 | -40.7 |
| lgbm_calibrated|h4|on_time | 3660 | 61 | 3660 | 0.498 | 0.48-0.51 | 0.502 | 0.463 | -0.0058 | 0.040 | 0.15 | -40.7 |
| logistic|h1|all | 3840 | 64 | 3840 | 0.503 | 0.49-0.52 | 0.477 | 0.493 | -0.0067 | 0.023 | 0.13 | -25.0 |
| logistic|h1|on_time | 3780 | 63 | 3780 | 0.498 | 0.48-0.51 | 0.475 | 0.493 | -0.0078 | 0.027 | 0.13 | -25.0 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 3660 | 61 | 3660 | 0.485 | 0.47-0.50 | 0.502 | 0.495 | -0.0176 | 0.055 | 0.26 | -26.9 |
| logistic|h4|on_time | 3660 | 61 | 3660 | 0.485 | 0.47-0.50 | 0.502 | 0.495 | -0.0176 | 0.055 | 0.26 | -26.9 |
| momentum_24|h1|all | 3840 | 64 | 3840 | 0.507 | 0.49-0.52 | 0.477 | 0.496 | +0.0003 | 0.019 | 0.00 | - |
| momentum_24|h1|on_time | 3780 | 63 | 3780 | 0.504 | 0.49-0.52 | 0.475 | 0.496 | +0.0001 | 0.021 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 3660 | 61 | 3660 | 0.502 | 0.49-0.52 | 0.502 | 0.504 | -0.0001 | 0.002 | 0.00 | - |
| momentum_24|h4|on_time | 3660 | 61 | 3660 | 0.502 | 0.49-0.52 | 0.502 | 0.504 | -0.0001 | 0.002 | 0.00 | - |
| orthosys|h1|all | 3840 | 64 | 358 | 0.458 | 0.41-0.51 | 0.477 | 0.500 | -0.0020 | 0.023 | 0.00 | - |
| orthosys|h1|on_time | 3780 | 63 | 357 | 0.457 | 0.41-0.51 | 0.475 | 0.500 | -0.0021 | 0.025 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 3660 | 61 | 284 | 0.377 | 0.32-0.43 | 0.502 | 0.500 | -0.0004 | 0.004 | 0.00 | - |
| orthosys|h4|on_time | 3660 | 61 | 284 | 0.377 | 0.32-0.43 | 0.502 | 0.500 | -0.0004 | 0.004 | 0.00 | - |
| recent_base_rate_7d|h1|all | 3780 | 63 | 3780 | 0.525 | 0.51-0.54 | 0.475 | 0.477 | -0.0013 | 0.003 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 3780 | 63 | 3780 | 0.525 | 0.51-0.54 | 0.475 | 0.477 | -0.0013 | 0.003 | 0.00 | - |
| recent_base_rate_7d|h4|all | 3600 | 60 | 3600 | 0.495 | 0.48-0.51 | 0.505 | 0.452 | -0.0317 | 0.053 | 0.58 | -68.7 |
| recent_base_rate_7d|h4|on_time | 3600 | 60 | 3600 | 0.495 | 0.48-0.51 | 0.505 | 0.452 | -0.0317 | 0.053 | 0.58 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 922.54 | -7.75% | 1813 | 722 | 59 |
| analog_k100|h4 | 983.62 | -1.64% | 2208 | 960 | 56 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 64 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 61 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 59 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 56 |
| derivatives|h1 | 1137.30 | +13.73% | 33 | 16 | 59 |
| derivatives|h4 | 1226.44 | +22.64% | 65 | 43 | 56 |
| lgbm_calibrated|h1 | 914.91 | -8.51% | 537 | 250 | 64 |
| lgbm_calibrated|h4 | 922.72 | -7.73% | 535 | 229 | 61 |
| logistic|h1 | 830.64 | -16.94% | 486 | 210 | 64 |
| logistic|h4 | 987.01 | -1.30% | 944 | 404 | 61 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 64 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 61 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 64 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 61 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 63 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 60 |
| benchmark_long_all_coins|h1 | 957.71 | -4.23% | 3840 | 1648 | 64 |
| benchmark_long_all_coins|h4 | 995.91 | -0.41% | 3660 | 1748 | 61 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 59 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 64 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 61 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 59 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 59 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 64 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 61 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 64 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 61 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 64 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 61 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 64 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 61 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 63 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 60 |

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
