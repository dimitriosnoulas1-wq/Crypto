# Live monitor (2026-10-22T04:06:40.779264+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h4|all says 0.44 on average, reality 0.52 (ECE 0.104)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.495
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.486
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.475
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.45 on average, reality 0.53 (ECE 0.084)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.482

## Health

- **venue**: okx
- **symbols**: 61
- **universe_size**: 60
- **fetched_only_for_scoring**: ['DASH']
- **last_closed_bar**: 2026-10-22 03:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.7
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 100.5 instruments 61/61']
- **feature_nan_share_latest_bar**: 0.034
- **council_weights_h1**: {'base_rate': 0.152, 'recent_base_rate_7d': 0.115, 'momentum_24': 0.17, 'logistic': 0.112, 'lgbm_calibrated': 0.129, 'analog_k100': 0.017, 'derivatives': 0.159, 'orthosys': 0.146}
- **council_member_logloss_h1**: {'base_rate': 0.6931, 'recent_base_rate_7d': 0.6947, 'momentum_24': 0.6924, 'logistic': 0.6948, 'lgbm_calibrated': 0.694, 'analog_k100': 0.7068, 'derivatives': 0.693, 'orthosys': 0.6933}
- **council_calls_h1**: 0
- **council_abstain_h1**: {'no_edge': 52, 'extreme_volatility': 7, 'missing_inputs': 1}
- **council_weights_h4**: {'base_rate': 0.209, 'recent_base_rate_7d': 0.006, 'momentum_24': 0.207, 'logistic': 0.076, 'lgbm_calibrated': 0.051, 'analog_k100': 0.003, 'derivatives': 0.255, 'orthosys': 0.193}
- **council_member_logloss_h4**: {'base_rate': 0.693, 'recent_base_rate_7d': 0.7149, 'momentum_24': 0.6931, 'logistic': 0.699, 'lgbm_calibrated': 0.7014, 'analog_k100': 0.7209, 'derivatives': 0.6916, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 52, 'extreme_volatility': 7, 'missing_inputs': 1}
- **prediction_latency_min**: 6.6
- **price_snapshot_age_s**: 0.8
- **train_rows_h1**: 89653
- **orthosys_hist_hit_h1**: 0.5294
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0065
- **p_spread_logistic_h1**: 0.0482
- **p_spread_lgbm_calibrated_h1**: 0.0062
- **p_spread_analog_k100_h1**: 0.0643
- **p_spread_derivatives_h1**: 0.0312
- **p_spread_orthosys_h1**: 0.0131
- **p_spread_council_h1**: 0.0
- **train_rows_h4**: 89470
- **orthosys_hist_hit_h4**: 0.5095
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0003
- **p_spread_logistic_h4**: 0.0934
- **p_spread_lgbm_calibrated_h4**: 0.0087
- **p_spread_analog_k100_h4**: 0.1205
- **p_spread_derivatives_h4**: 0.0545
- **p_spread_orthosys_h4**: 0.0042
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 63960

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 3300 | 55 | 3300 | 0.492 | 0.48-0.51 | 0.489 | 0.468 | -0.0279 | 0.065 | 0.51 | -13.7 |
| analog_k100|h1|on_time | 3300 | 55 | 3300 | 0.492 | 0.48-0.51 | 0.489 | 0.468 | -0.0279 | 0.065 | 0.51 | -13.7 |
| analog_k100|h4|all | 3120 | 52 | 3120 | 0.478 | 0.46-0.50 | 0.525 | 0.443 | -0.0481 | 0.104 | 0.65 | -12.7 |
| analog_k100|h4|on_time | 3120 | 52 | 3120 | 0.478 | 0.46-0.50 | 0.525 | 0.443 | -0.0481 | 0.104 | 0.65 | -12.7 |
| base_rate|h1|all | 3600 | 60 | 3600 | 0.510 | 0.49-0.53 | 0.490 | 0.498 | +0.0000 | 0.008 | 0.00 | - |
| base_rate|h1|on_time | 3540 | 59 | 3540 | 0.512 | 0.50-0.53 | 0.488 | 0.498 | +0.0000 | 0.010 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 3420 | 57 | 3420 | 0.530 | 0.51-0.55 | 0.530 | 0.504 | +0.0000 | 0.027 | 0.00 | - |
| base_rate|h4|on_time | 3420 | 57 | 3420 | 0.530 | 0.51-0.55 | 0.530 | 0.504 | +0.0000 | 0.027 | 0.00 | - |
| council|h1|all | 3300 | 55 | 492 | 0.510 | 0.47-0.55 | 0.489 | 0.496 | -0.0001 | 0.011 | 0.00 | +18.3 |
| council|h1|on_time | 3300 | 55 | 492 | 0.510 | 0.47-0.55 | 0.489 | 0.496 | -0.0001 | 0.011 | 0.00 | +18.3 |
| council|h4|all | 3120 | 52 | 25 | 0.600 | 0.41-0.77 | 0.525 | 0.500 | +0.0002 | 0.025 | 0.00 | - |
| council|h4|on_time | 3120 | 52 | 25 | 0.600 | 0.41-0.77 | 0.525 | 0.500 | +0.0002 | 0.025 | 0.00 | - |
| derivatives|h1|all | 3300 | 55 | 3300 | 0.511 | 0.49-0.53 | 0.489 | 0.497 | +0.0004 | 0.008 | 0.01 | -35.7 |
| derivatives|h1|on_time | 3300 | 55 | 3300 | 0.511 | 0.49-0.53 | 0.489 | 0.497 | +0.0004 | 0.008 | 0.01 | -35.7 |
| derivatives|h4|all | 3120 | 52 | 3120 | 0.537 | 0.52-0.55 | 0.525 | 0.500 | +0.0032 | 0.031 | 0.02 | +532.1 |
| derivatives|h4|on_time | 3120 | 52 | 3120 | 0.537 | 0.52-0.55 | 0.525 | 0.500 | +0.0032 | 0.031 | 0.02 | +532.1 |
| lgbm_calibrated|h1|all | 3600 | 60 | 3599 | 0.535 | 0.52-0.55 | 0.490 | 0.476 | -0.0028 | 0.014 | 0.15 | -2.5 |
| lgbm_calibrated|h1|on_time | 3540 | 59 | 3539 | 0.539 | 0.52-0.55 | 0.488 | 0.476 | -0.0022 | 0.012 | 0.15 | -2.5 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 3420 | 57 | 3420 | 0.469 | 0.45-0.49 | 0.530 | 0.463 | -0.0150 | 0.069 | 0.15 | -48.0 |
| lgbm_calibrated|h4|on_time | 3420 | 57 | 3420 | 0.469 | 0.45-0.49 | 0.530 | 0.463 | -0.0150 | 0.069 | 0.15 | -48.0 |
| logistic|h1|all | 3600 | 60 | 3600 | 0.512 | 0.50-0.53 | 0.490 | 0.492 | -0.0043 | 0.013 | 0.12 | -32.1 |
| logistic|h1|on_time | 3540 | 59 | 3540 | 0.508 | 0.49-0.52 | 0.488 | 0.492 | -0.0054 | 0.017 | 0.13 | -32.1 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 3420 | 57 | 3420 | 0.501 | 0.48-0.52 | 0.530 | 0.494 | -0.0118 | 0.045 | 0.24 | -20.9 |
| logistic|h4|on_time | 3420 | 57 | 3420 | 0.501 | 0.48-0.52 | 0.530 | 0.494 | -0.0118 | 0.045 | 0.24 | -20.9 |
| momentum_24|h1|all | 3600 | 60 | 3600 | 0.520 | 0.50-0.54 | 0.490 | 0.496 | +0.0012 | 0.010 | 0.00 | - |
| momentum_24|h1|on_time | 3540 | 59 | 3540 | 0.517 | 0.50-0.53 | 0.488 | 0.496 | +0.0009 | 0.008 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 3420 | 57 | 3420 | 0.530 | 0.51-0.55 | 0.530 | 0.504 | -0.0002 | 0.027 | 0.00 | - |
| momentum_24|h4|on_time | 3420 | 57 | 3420 | 0.530 | 0.51-0.55 | 0.530 | 0.504 | -0.0002 | 0.027 | 0.00 | - |
| orthosys|h1|all | 3600 | 60 | 268 | 0.496 | 0.44-0.56 | 0.490 | 0.499 | -0.0007 | 0.009 | 0.00 | - |
| orthosys|h1|on_time | 3540 | 59 | 267 | 0.494 | 0.43-0.55 | 0.488 | 0.499 | -0.0008 | 0.012 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 3420 | 57 | 245 | 0.412 | 0.35-0.47 | 0.530 | 0.499 | -0.0008 | 0.031 | 0.00 | - |
| orthosys|h4|on_time | 3420 | 57 | 245 | 0.412 | 0.35-0.47 | 0.530 | 0.499 | -0.0008 | 0.031 | 0.00 | - |
| recent_base_rate_7d|h1|all | 3540 | 59 | 3540 | 0.512 | 0.50-0.53 | 0.488 | 0.477 | -0.0027 | 0.011 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 3540 | 59 | 3540 | 0.512 | 0.50-0.53 | 0.488 | 0.477 | -0.0027 | 0.011 | 0.00 | - |
| recent_base_rate_7d|h4|all | 3360 | 56 | 3360 | 0.465 | 0.45-0.48 | 0.535 | 0.450 | -0.0412 | 0.084 | 0.62 | -68.7 |
| recent_base_rate_7d|h4|on_time | 3360 | 56 | 3360 | 0.465 | 0.45-0.48 | 0.535 | 0.450 | -0.0412 | 0.084 | 0.62 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 930.86 | -6.91% | 1687 | 678 | 55 |
| analog_k100|h4 | 987.69 | -1.23% | 2023 | 895 | 52 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 60 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 57 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 55 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 52 |
| derivatives|h1 | 1091.84 | +9.18% | 25 | 10 | 55 |
| derivatives|h4 | 1209.52 | +20.95% | 52 | 33 | 52 |
| lgbm_calibrated|h1 | 907.89 | -9.21% | 530 | 247 | 60 |
| lgbm_calibrated|h4 | 916.34 | -8.37% | 523 | 218 | 57 |
| logistic|h1 | 808.60 | -19.14% | 449 | 189 | 60 |
| logistic|h4 | 993.25 | -0.67% | 817 | 377 | 57 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 60 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 57 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 60 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 57 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 59 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 56 |
| benchmark_long_all_coins|h1 | 972.46 | -2.75% | 3600 | 1588 | 60 |
| benchmark_long_all_coins|h4 | 1017.20 | +1.72% | 3420 | 1728 | 57 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 60 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 57 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 60 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 57 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 60 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 57 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 60 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 57 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 60 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 57 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 59 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 56 |

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
