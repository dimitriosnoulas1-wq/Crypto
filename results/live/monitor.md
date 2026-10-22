# Live monitor (2026-10-22T01:06:04.808908+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h4|all says 0.44 on average, reality 0.55 (ECE 0.119)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.479
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.56 (ECE 0.096)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.460
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.487
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.45 on average, reality 0.56 (ECE 0.113)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.455

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['HBAR', 'OP']
- **last_closed_bar**: 2026-10-22 00:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.0
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 108.8 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.035
- **council_weights_h1**: {'base_rate': 0.144, 'recent_base_rate_7d': 0.099, 'momentum_24': 0.164, 'logistic': 0.148, 'lgbm_calibrated': 0.131, 'analog_k100': 0.019, 'derivatives': 0.15, 'orthosys': 0.146}
- **council_member_logloss_h1**: {'base_rate': 0.6932, 'recent_base_rate_7d': 0.6955, 'momentum_24': 0.6924, 'logistic': 0.693, 'lgbm_calibrated': 0.6938, 'analog_k100': 0.7065, 'derivatives': 0.6931, 'orthosys': 0.6932}
- **council_calls_h1**: 2
- **council_abstain_h1**: {'no_edge': 50, 'extreme_volatility': 7, 'spoke': 2, 'missing_inputs': 1}
- **council_weights_h4**: {'base_rate': 0.222, 'recent_base_rate_7d': 0.004, 'momentum_24': 0.22, 'logistic': 0.091, 'lgbm_calibrated': 0.032, 'analog_k100': 0.001, 'derivatives': 0.237, 'orthosys': 0.191}
- **council_member_logloss_h4**: {'base_rate': 0.6925, 'recent_base_rate_7d': 0.7179, 'momentum_24': 0.6926, 'logistic': 0.6981, 'lgbm_calibrated': 0.7047, 'analog_k100': 0.7319, 'derivatives': 0.6919, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 51, 'extreme_volatility': 7, 'missing_inputs': 1, 'members_disagree': 1}
- **prediction_latency_min**: 6.0
- **price_snapshot_age_s**: 1.1
- **train_rows_h1**: 91025
- **orthosys_hist_hit_h1**: 0.53
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0086
- **p_spread_logistic_h1**: 0.0452
- **p_spread_lgbm_calibrated_h1**: 0.0144
- **p_spread_analog_k100_h1**: 0.0591
- **p_spread_derivatives_h1**: 0.0316
- **p_spread_orthosys_h1**: 0.0084
- **p_spread_council_h1**: 0.0041
- **train_rows_h4**: 90839
- **orthosys_hist_hit_h4**: 0.5099
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0008
- **p_spread_logistic_h4**: 0.0675
- **p_spread_lgbm_calibrated_h4**: 0.015
- **p_spread_analog_k100_h4**: 0.1038
- **p_spread_derivatives_h4**: 0.0585
- **p_spread_orthosys_h4**: 0.0028
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 60720

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 3120 | 52 | 3120 | 0.493 | 0.48-0.51 | 0.508 | 0.466 | -0.0261 | 0.063 | 0.51 | -14.5 |
| analog_k100|h1|on_time | 3120 | 52 | 3120 | 0.493 | 0.48-0.51 | 0.508 | 0.466 | -0.0261 | 0.063 | 0.51 | -14.5 |
| analog_k100|h4|all | 2940 | 49 | 2940 | 0.461 | 0.44-0.48 | 0.554 | 0.445 | -0.0689 | 0.119 | 0.65 | -23.4 |
| analog_k100|h4|on_time | 2940 | 49 | 2940 | 0.461 | 0.44-0.48 | 0.554 | 0.445 | -0.0689 | 0.119 | 0.65 | -23.4 |
| base_rate|h1|all | 3420 | 57 | 3420 | 0.492 | 0.48-0.51 | 0.508 | 0.498 | +0.0000 | 0.010 | 0.00 | - |
| base_rate|h1|on_time | 3360 | 56 | 3360 | 0.495 | 0.48-0.51 | 0.505 | 0.498 | +0.0000 | 0.007 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 3240 | 54 | 3240 | 0.557 | 0.54-0.57 | 0.557 | 0.504 | +0.0000 | 0.053 | 0.00 | - |
| base_rate|h4|on_time | 3240 | 54 | 3240 | 0.557 | 0.54-0.57 | 0.557 | 0.504 | +0.0000 | 0.053 | 0.00 | - |
| council|h1|all | 3120 | 52 | 487 | 0.511 | 0.47-0.56 | 0.508 | 0.496 | +0.0005 | 0.012 | 0.00 | +18.3 |
| council|h1|on_time | 3120 | 52 | 487 | 0.511 | 0.47-0.56 | 0.508 | 0.496 | +0.0005 | 0.012 | 0.00 | +18.3 |
| council|h4|all | 2940 | 49 | 25 | 0.600 | 0.41-0.77 | 0.554 | 0.500 | -0.0007 | 0.054 | 0.00 | - |
| council|h4|on_time | 2940 | 49 | 25 | 0.600 | 0.41-0.77 | 0.554 | 0.500 | -0.0007 | 0.054 | 0.00 | - |
| derivatives|h1|all | 3120 | 52 | 3120 | 0.492 | 0.47-0.51 | 0.508 | 0.497 | +0.0004 | 0.011 | 0.01 | -59.0 |
| derivatives|h1|on_time | 3120 | 52 | 3120 | 0.492 | 0.47-0.51 | 0.508 | 0.497 | +0.0004 | 0.011 | 0.01 | -59.0 |
| derivatives|h4|all | 2940 | 49 | 2940 | 0.562 | 0.54-0.58 | 0.554 | 0.501 | +0.0016 | 0.057 | 0.01 | +482.3 |
| derivatives|h4|on_time | 2940 | 49 | 2940 | 0.562 | 0.54-0.58 | 0.554 | 0.501 | +0.0016 | 0.057 | 0.01 | +482.3 |
| lgbm_calibrated|h1|all | 3420 | 57 | 3419 | 0.538 | 0.52-0.56 | 0.508 | 0.474 | -0.0009 | 0.034 | 0.15 | -2.6 |
| lgbm_calibrated|h1|on_time | 3360 | 56 | 3359 | 0.542 | 0.52-0.56 | 0.505 | 0.474 | -0.0002 | 0.031 | 0.16 | -2.6 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 3240 | 54 | 3240 | 0.443 | 0.43-0.46 | 0.557 | 0.463 | -0.0222 | 0.096 | 0.16 | -48.0 |
| lgbm_calibrated|h4|on_time | 3240 | 54 | 3240 | 0.443 | 0.43-0.46 | 0.557 | 0.463 | -0.0222 | 0.096 | 0.16 | -48.0 |
| logistic|h1|all | 3420 | 57 | 3420 | 0.522 | 0.51-0.54 | 0.508 | 0.491 | +0.0013 | 0.019 | 0.11 | -24.8 |
| logistic|h1|on_time | 3360 | 56 | 3360 | 0.518 | 0.50-0.53 | 0.505 | 0.490 | +0.0003 | 0.017 | 0.11 | -24.8 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 3240 | 54 | 3240 | 0.510 | 0.49-0.53 | 0.557 | 0.493 | -0.0105 | 0.071 | 0.23 | -19.1 |
| logistic|h4|on_time | 3240 | 54 | 3240 | 0.510 | 0.49-0.53 | 0.557 | 0.493 | -0.0105 | 0.071 | 0.23 | -19.1 |
| momentum_24|h1|all | 3420 | 57 | 3420 | 0.525 | 0.51-0.54 | 0.508 | 0.496 | +0.0015 | 0.015 | 0.00 | - |
| momentum_24|h1|on_time | 3360 | 56 | 3360 | 0.522 | 0.50-0.54 | 0.505 | 0.495 | +0.0013 | 0.012 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 3240 | 54 | 3240 | 0.557 | 0.54-0.57 | 0.557 | 0.504 | -0.0001 | 0.053 | 0.00 | - |
| momentum_24|h4|on_time | 3240 | 54 | 3240 | 0.557 | 0.54-0.57 | 0.557 | 0.504 | -0.0001 | 0.053 | 0.00 | - |
| orthosys|h1|all | 3420 | 57 | 245 | 0.518 | 0.46-0.58 | 0.508 | 0.499 | +0.0002 | 0.012 | 0.00 | - |
| orthosys|h1|on_time | 3360 | 56 | 244 | 0.516 | 0.45-0.58 | 0.505 | 0.499 | +0.0001 | 0.009 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 3240 | 54 | 232 | 0.422 | 0.36-0.49 | 0.557 | 0.499 | -0.0016 | 0.058 | 0.00 | - |
| orthosys|h4|on_time | 3240 | 54 | 232 | 0.422 | 0.36-0.49 | 0.557 | 0.499 | -0.0016 | 0.058 | 0.00 | - |
| recent_base_rate_7d|h1|all | 3360 | 56 | 3360 | 0.495 | 0.48-0.51 | 0.505 | 0.476 | -0.0048 | 0.029 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 3360 | 56 | 3360 | 0.495 | 0.48-0.51 | 0.505 | 0.476 | -0.0048 | 0.029 | 0.00 | - |
| recent_base_rate_7d|h4|all | 3180 | 53 | 3180 | 0.438 | 0.42-0.46 | 0.562 | 0.449 | -0.0485 | 0.113 | 0.66 | -68.7 |
| recent_base_rate_7d|h4|on_time | 3180 | 53 | 3180 | 0.438 | 0.42-0.46 | 0.562 | 0.449 | -0.0485 | 0.113 | 0.66 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 931.65 | -6.83% | 1578 | 631 | 52 |
| analog_k100|h4 | 976.90 | -2.31% | 1897 | 786 | 49 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 57 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 54 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 52 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 49 |
| derivatives|h1 | 1049.24 | +4.92% | 22 | 8 | 52 |
| derivatives|h4 | 1153.37 | +15.34% | 43 | 24 | 49 |
| lgbm_calibrated|h1 | 907.27 | -9.27% | 528 | 246 | 57 |
| lgbm_calibrated|h4 | 916.34 | -8.37% | 523 | 218 | 54 |
| logistic|h1 | 830.63 | -16.94% | 370 | 178 | 57 |
| logistic|h4 | 995.75 | -0.43% | 754 | 353 | 54 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 57 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 54 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 57 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 54 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 56 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 53 |
| benchmark_long_all_coins|h1 | 995.90 | -0.41% | 3420 | 1567 | 57 |
| benchmark_long_all_coins|h4 | 1036.70 | +3.67% | 3240 | 1720 | 54 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 57 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 57 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 57 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 57 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 57 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 54 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 53 |

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
