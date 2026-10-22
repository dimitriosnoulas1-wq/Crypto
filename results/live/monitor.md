# Live monitor (2026-10-22T03:07:19.089133+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.44 on average, reality 0.53 (ECE 0.106)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.493
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.478
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.482
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.45 on average, reality 0.54 (ECE 0.093)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.474

## Health

- **venue**: okx
- **symbols**: 61
- **universe_size**: 60
- **fetched_only_for_scoring**: ['DASH']
- **last_closed_bar**: 2026-10-22 02:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.1
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 106.5 instruments 61/61']
- **feature_nan_share_latest_bar**: 0.034
- **council_weights_h1**: {'base_rate': 0.141, 'recent_base_rate_7d': 0.101, 'momentum_24': 0.162, 'logistic': 0.15, 'lgbm_calibrated': 0.137, 'analog_k100': 0.023, 'derivatives': 0.145, 'orthosys': 0.14}
- **council_member_logloss_h1**: {'base_rate': 0.6932, 'recent_base_rate_7d': 0.6951, 'momentum_24': 0.6924, 'logistic': 0.6928, 'lgbm_calibrated': 0.6933, 'analog_k100': 0.7049, 'derivatives': 0.6932, 'orthosys': 0.6932}
- **council_calls_h1**: 0
- **council_abstain_h1**: {'no_edge': 51, 'extreme_volatility': 7, 'missing_inputs': 1, 'members_disagree': 1}
- **council_weights_h4**: {'base_rate': 0.213, 'recent_base_rate_7d': 0.005, 'momentum_24': 0.21, 'logistic': 0.087, 'lgbm_calibrated': 0.045, 'analog_k100': 0.002, 'derivatives': 0.246, 'orthosys': 0.193}
- **council_member_logloss_h4**: {'base_rate': 0.6929, 'recent_base_rate_7d': 0.716, 'momentum_24': 0.6929, 'logistic': 0.6983, 'lgbm_calibrated': 0.7023, 'analog_k100': 0.7247, 'derivatives': 0.6918, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 51, 'extreme_volatility': 7, 'missing_inputs': 1, 'members_disagree': 1}
- **prediction_latency_min**: 7.2
- **price_snapshot_age_s**: 0.2
- **train_rows_h1**: 89592
- **orthosys_hist_hit_h1**: 0.5296
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0072
- **p_spread_logistic_h1**: 0.0489
- **p_spread_lgbm_calibrated_h1**: 0.014
- **p_spread_analog_k100_h1**: 0.06
- **p_spread_derivatives_h1**: 0.0285
- **p_spread_orthosys_h1**: 0.0111
- **p_spread_council_h1**: 0.0
- **train_rows_h4**: 89409
- **orthosys_hist_hit_h4**: 0.5098
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0004
- **p_spread_logistic_h4**: 0.0887
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.1142
- **p_spread_derivatives_h4**: 0.058
- **p_spread_orthosys_h4**: 0.0037
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 62880

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 3240 | 54 | 3240 | 0.494 | 0.48-0.51 | 0.493 | 0.467 | -0.0266 | 0.063 | 0.51 | -13.6 |
| analog_k100|h1|on_time | 3240 | 54 | 3240 | 0.494 | 0.48-0.51 | 0.493 | 0.467 | -0.0266 | 0.063 | 0.51 | -13.6 |
| analog_k100|h4|all | 3060 | 51 | 3060 | 0.475 | 0.46-0.49 | 0.533 | 0.443 | -0.0531 | 0.106 | 0.65 | -15.1 |
| analog_k100|h4|on_time | 3060 | 51 | 3060 | 0.475 | 0.46-0.49 | 0.533 | 0.443 | -0.0531 | 0.106 | 0.65 | -15.1 |
| base_rate|h1|all | 3540 | 59 | 3540 | 0.506 | 0.49-0.52 | 0.494 | 0.498 | +0.0000 | 0.004 | 0.00 | - |
| base_rate|h1|on_time | 3480 | 58 | 3480 | 0.508 | 0.49-0.52 | 0.492 | 0.498 | +0.0000 | 0.006 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 3360 | 56 | 3360 | 0.538 | 0.52-0.56 | 0.538 | 0.504 | +0.0000 | 0.035 | 0.00 | - |
| base_rate|h4|on_time | 3360 | 56 | 3360 | 0.538 | 0.52-0.56 | 0.538 | 0.504 | +0.0000 | 0.035 | 0.00 | - |
| council|h1|all | 3240 | 54 | 492 | 0.510 | 0.47-0.55 | 0.493 | 0.496 | +0.0001 | 0.007 | 0.00 | +18.3 |
| council|h1|on_time | 3240 | 54 | 492 | 0.510 | 0.47-0.55 | 0.493 | 0.496 | +0.0001 | 0.007 | 0.00 | +18.3 |
| council|h4|all | 3060 | 51 | 25 | 0.600 | 0.41-0.77 | 0.533 | 0.500 | +0.0000 | 0.034 | 0.00 | - |
| council|h4|on_time | 3060 | 51 | 25 | 0.600 | 0.41-0.77 | 0.533 | 0.500 | +0.0000 | 0.034 | 0.00 | - |
| derivatives|h1|all | 3240 | 54 | 3240 | 0.506 | 0.49-0.52 | 0.493 | 0.497 | +0.0002 | 0.004 | 0.01 | -41.0 |
| derivatives|h1|on_time | 3240 | 54 | 3240 | 0.506 | 0.49-0.52 | 0.493 | 0.497 | +0.0002 | 0.004 | 0.01 | -41.0 |
| derivatives|h4|all | 3060 | 51 | 3060 | 0.545 | 0.53-0.56 | 0.533 | 0.501 | +0.0028 | 0.039 | 0.02 | +537.6 |
| derivatives|h4|on_time | 3060 | 51 | 3060 | 0.545 | 0.53-0.56 | 0.533 | 0.501 | +0.0028 | 0.039 | 0.02 | +537.6 |
| lgbm_calibrated|h1|all | 3540 | 59 | 3539 | 0.539 | 0.52-0.55 | 0.494 | 0.475 | -0.0019 | 0.019 | 0.15 | -2.5 |
| lgbm_calibrated|h1|on_time | 3480 | 58 | 3479 | 0.542 | 0.53-0.56 | 0.492 | 0.475 | -0.0013 | 0.016 | 0.15 | -2.5 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 3360 | 56 | 3360 | 0.461 | 0.44-0.48 | 0.538 | 0.463 | -0.0168 | 0.077 | 0.16 | -48.0 |
| lgbm_calibrated|h4|on_time | 3360 | 56 | 3360 | 0.461 | 0.44-0.48 | 0.538 | 0.463 | -0.0168 | 0.077 | 0.16 | -48.0 |
| logistic|h1|all | 3540 | 59 | 3540 | 0.515 | 0.50-0.53 | 0.494 | 0.492 | -0.0034 | 0.010 | 0.12 | -32.1 |
| logistic|h1|on_time | 3480 | 58 | 3480 | 0.510 | 0.49-0.53 | 0.492 | 0.491 | -0.0044 | 0.014 | 0.12 | -32.2 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 3360 | 56 | 3360 | 0.506 | 0.49-0.52 | 0.538 | 0.493 | -0.0114 | 0.053 | 0.24 | -19.0 |
| logistic|h4|on_time | 3360 | 56 | 3360 | 0.506 | 0.49-0.52 | 0.538 | 0.493 | -0.0114 | 0.053 | 0.24 | -19.0 |
| momentum_24|h1|all | 3540 | 59 | 3540 | 0.521 | 0.50-0.54 | 0.494 | 0.496 | +0.0013 | 0.012 | 0.00 | - |
| momentum_24|h1|on_time | 3480 | 58 | 3480 | 0.518 | 0.50-0.53 | 0.492 | 0.496 | +0.0011 | 0.009 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 3360 | 56 | 3360 | 0.538 | 0.52-0.56 | 0.538 | 0.504 | -0.0002 | 0.035 | 0.00 | - |
| momentum_24|h4|on_time | 3360 | 56 | 3360 | 0.538 | 0.52-0.56 | 0.538 | 0.504 | -0.0002 | 0.035 | 0.00 | - |
| orthosys|h1|all | 3540 | 59 | 258 | 0.500 | 0.44-0.56 | 0.494 | 0.499 | -0.0005 | 0.005 | 0.00 | - |
| orthosys|h1|on_time | 3480 | 58 | 257 | 0.498 | 0.44-0.56 | 0.492 | 0.499 | -0.0006 | 0.008 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 3360 | 56 | 239 | 0.418 | 0.36-0.48 | 0.538 | 0.499 | -0.0010 | 0.039 | 0.00 | - |
| orthosys|h4|on_time | 3360 | 56 | 239 | 0.418 | 0.36-0.48 | 0.538 | 0.499 | -0.0010 | 0.039 | 0.00 | - |
| recent_base_rate_7d|h1|all | 3480 | 58 | 3480 | 0.508 | 0.49-0.52 | 0.492 | 0.477 | -0.0032 | 0.015 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 3480 | 58 | 3480 | 0.508 | 0.49-0.52 | 0.492 | 0.477 | -0.0032 | 0.015 | 0.00 | - |
| recent_base_rate_7d|h4|all | 3300 | 55 | 3300 | 0.457 | 0.44-0.47 | 0.543 | 0.450 | -0.0436 | 0.093 | 0.64 | -68.7 |
| recent_base_rate_7d|h4|on_time | 3300 | 55 | 3300 | 0.457 | 0.44-0.47 | 0.543 | 0.450 | -0.0436 | 0.093 | 0.64 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 932.69 | -6.73% | 1651 | 670 | 54 |
| analog_k100|h4 | 984.87 | -1.51% | 1986 | 864 | 51 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 59 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 56 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 54 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 51 |
| derivatives|h1 | 1081.86 | +8.19% | 24 | 9 | 54 |
| derivatives|h4 | 1201.93 | +20.19% | 51 | 32 | 51 |
| lgbm_calibrated|h1 | 907.89 | -9.21% | 530 | 247 | 59 |
| lgbm_calibrated|h4 | 916.34 | -8.37% | 523 | 218 | 56 |
| logistic|h1 | 811.14 | -18.89% | 414 | 184 | 59 |
| logistic|h4 | 995.48 | -0.45% | 795 | 368 | 56 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 59 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 56 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 59 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 56 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 58 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 55 |
| benchmark_long_all_coins|h1 | 977.44 | -2.26% | 3540 | 1580 | 59 |
| benchmark_long_all_coins|h4 | 1024.01 | +2.40% | 3360 | 1727 | 56 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 59 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 59 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 59 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 59 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 59 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 58 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 55 |

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
