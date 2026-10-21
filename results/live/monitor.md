# Live monitor (2026-10-21T21:07:40.046675+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.58 (ECE 0.143)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.463
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.496
- MISCALIBRATED: base_rate|h4|all says 0.50 on average, reality 0.58 (ECE 0.081)
- MISCALIBRATED: council|h4|all says 0.50 on average, reality 0.58 (ECE 0.085)
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.495
- MISCALIBRATED: derivatives|h4|all says 0.50 on average, reality 0.58 (ECE 0.083)
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.58 (ECE 0.124)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.433
- MISCALIBRATED: logistic|h4|all says 0.49 on average, reality 0.58 (ECE 0.095)
- MISCALIBRATED: momentum_24|h4|all says 0.50 on average, reality 0.58 (ECE 0.081)
- MISCALIBRATED: orthosys|h4|all says 0.50 on average, reality 0.58 (ECE 0.085)
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.493
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.498
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.45 on average, reality 0.59 (ECE 0.145)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.427

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['COMP', 'RAY']
- **last_closed_bar**: 2026-10-21 20:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.6
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 105.2 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.147, 'recent_base_rate_7d': 0.09, 'momentum_24': 0.158, 'logistic': 0.169, 'lgbm_calibrated': 0.117, 'analog_k100': 0.016, 'derivatives': 0.149, 'orthosys': 0.155}
- **council_member_logloss_h1**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.6967, 'momentum_24': 0.6929, 'logistic': 0.6925, 'lgbm_calibrated': 0.6949, 'analog_k100': 0.7095, 'derivatives': 0.6935, 'orthosys': 0.6931}
- **council_calls_h1**: 2
- **council_abstain_h1**: {'no_edge': 53, 'extreme_volatility': 5, 'spoke': 2}
- **council_weights_h4**: {'base_rate': 0.229, 'recent_base_rate_7d': 0.004, 'momentum_24': 0.228, 'logistic': 0.098, 'lgbm_calibrated': 0.024, 'analog_k100': 0.001, 'derivatives': 0.228, 'orthosys': 0.188}
- **council_member_logloss_h4**: {'base_rate': 0.6921, 'recent_base_rate_7d': 0.721, 'momentum_24': 0.6921, 'logistic': 0.6979, 'lgbm_calibrated': 0.7074, 'analog_k100': 0.7374, 'derivatives': 0.6919, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 54, 'extreme_volatility': 5, 'members_disagree': 1}
- **prediction_latency_min**: 7.6
- **price_snapshot_age_s**: 0.8
- **train_rows_h1**: 92352
- **orthosys_hist_hit_h1**: 0.5309
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0073
- **p_spread_logistic_h1**: 0.0301
- **p_spread_lgbm_calibrated_h1**: 0.0147
- **p_spread_analog_k100_h1**: 0.0485
- **p_spread_derivatives_h1**: 0.0128
- **p_spread_orthosys_h1**: 0.0056
- **p_spread_council_h1**: 0.0044
- **train_rows_h4**: 92166
- **orthosys_hist_hit_h4**: 0.5118
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0005
- **p_spread_logistic_h4**: 0.0686
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0715
- **p_spread_derivatives_h4**: 0.0512
- **p_spread_orthosys_h4**: 0.0021
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 56400

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 2880 | 48 | 2880 | 0.491 | 0.47-0.51 | 0.523 | 0.466 | -0.0306 | 0.065 | 0.51 | -16.2 |
| analog_k100|h1|on_time | 2880 | 48 | 2880 | 0.491 | 0.47-0.51 | 0.523 | 0.466 | -0.0306 | 0.065 | 0.51 | -16.2 |
| analog_k100|h4|all | 2700 | 45 | 2700 | 0.444 | 0.43-0.46 | 0.584 | 0.447 | -0.0856 | 0.143 | 0.64 | -33.6 |
| analog_k100|h4|on_time | 2700 | 45 | 2700 | 0.444 | 0.43-0.46 | 0.584 | 0.447 | -0.0856 | 0.143 | 0.64 | -33.6 |
| base_rate|h1|all | 3180 | 53 | 3180 | 0.478 | 0.46-0.50 | 0.522 | 0.498 | +0.0000 | 0.024 | 0.00 | - |
| base_rate|h1|on_time | 3120 | 52 | 3120 | 0.481 | 0.46-0.50 | 0.519 | 0.498 | +0.0000 | 0.021 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 3000 | 50 | 3000 | 0.585 | 0.57-0.60 | 0.585 | 0.504 | +0.0000 | 0.081 | 0.00 | - |
| base_rate|h4|on_time | 3000 | 50 | 3000 | 0.585 | 0.57-0.60 | 0.585 | 0.504 | +0.0000 | 0.081 | 0.00 | - |
| council|h1|all | 2880 | 48 | 481 | 0.509 | 0.46-0.55 | 0.523 | 0.496 | +0.0008 | 0.028 | 0.00 | +18.3 |
| council|h1|on_time | 2880 | 48 | 481 | 0.509 | 0.46-0.55 | 0.523 | 0.496 | +0.0008 | 0.028 | 0.00 | +18.3 |
| council|h4|all | 2700 | 45 | 25 | 0.600 | 0.41-0.77 | 0.584 | 0.500 | -0.0019 | 0.085 | 0.00 | - |
| council|h4|on_time | 2700 | 45 | 25 | 0.600 | 0.41-0.77 | 0.584 | 0.500 | -0.0019 | 0.085 | 0.00 | - |
| derivatives|h1|all | 2880 | 48 | 2880 | 0.477 | 0.46-0.49 | 0.523 | 0.497 | -0.0002 | 0.026 | 0.01 | -287.7 |
| derivatives|h1|on_time | 2880 | 48 | 2880 | 0.477 | 0.46-0.49 | 0.523 | 0.497 | -0.0002 | 0.026 | 0.01 | -287.7 |
| derivatives|h4|all | 2700 | 45 | 2700 | 0.588 | 0.57-0.61 | 0.584 | 0.501 | +0.0006 | 0.083 | 0.01 | +386.7 |
| derivatives|h4|on_time | 2700 | 45 | 2700 | 0.588 | 0.57-0.61 | 0.584 | 0.501 | +0.0006 | 0.083 | 0.01 | +386.7 |
| lgbm_calibrated|h1|all | 3180 | 53 | 3179 | 0.527 | 0.51-0.54 | 0.522 | 0.473 | -0.0027 | 0.048 | 0.16 | +1.0 |
| lgbm_calibrated|h1|on_time | 3120 | 52 | 3119 | 0.531 | 0.51-0.55 | 0.519 | 0.474 | -0.0020 | 0.046 | 0.16 | +1.0 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 3000 | 50 | 3000 | 0.415 | 0.40-0.43 | 0.585 | 0.462 | -0.0302 | 0.124 | 0.17 | -48.0 |
| lgbm_calibrated|h4|on_time | 3000 | 50 | 3000 | 0.415 | 0.40-0.43 | 0.585 | 0.462 | -0.0302 | 0.124 | 0.17 | -48.0 |
| logistic|h1|all | 3180 | 53 | 3180 | 0.525 | 0.51-0.54 | 0.522 | 0.490 | +0.0019 | 0.033 | 0.10 | -35.6 |
| logistic|h1|on_time | 3120 | 52 | 3120 | 0.520 | 0.50-0.54 | 0.519 | 0.489 | +0.0008 | 0.031 | 0.10 | -35.7 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 3000 | 50 | 3000 | 0.511 | 0.49-0.53 | 0.585 | 0.494 | -0.0113 | 0.095 | 0.22 | -37.1 |
| logistic|h4|on_time | 3000 | 50 | 3000 | 0.511 | 0.49-0.53 | 0.585 | 0.494 | -0.0113 | 0.095 | 0.22 | -37.1 |
| momentum_24|h1|all | 3180 | 53 | 3180 | 0.518 | 0.50-0.54 | 0.522 | 0.496 | +0.0011 | 0.026 | 0.00 | - |
| momentum_24|h1|on_time | 3120 | 52 | 3120 | 0.514 | 0.50-0.53 | 0.519 | 0.495 | +0.0009 | 0.024 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 3000 | 50 | 3000 | 0.585 | 0.57-0.60 | 0.585 | 0.504 | -0.0000 | 0.081 | 0.00 | - |
| momentum_24|h4|on_time | 3000 | 50 | 3000 | 0.585 | 0.57-0.60 | 0.585 | 0.504 | -0.0000 | 0.081 | 0.00 | - |
| orthosys|h1|all | 3180 | 53 | 230 | 0.526 | 0.46-0.59 | 0.522 | 0.499 | +0.0006 | 0.026 | 0.00 | - |
| orthosys|h1|on_time | 3120 | 52 | 229 | 0.524 | 0.46-0.59 | 0.519 | 0.499 | +0.0005 | 0.023 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 3000 | 50 | 216 | 0.426 | 0.36-0.49 | 0.585 | 0.499 | -0.0027 | 0.085 | 0.00 | - |
| orthosys|h4|on_time | 3000 | 50 | 216 | 0.426 | 0.36-0.49 | 0.585 | 0.499 | -0.0027 | 0.085 | 0.00 | - |
| recent_base_rate_7d|h1|all | 3120 | 52 | 3120 | 0.481 | 0.46-0.50 | 0.519 | 0.476 | -0.0062 | 0.044 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 3120 | 52 | 3120 | 0.481 | 0.46-0.50 | 0.519 | 0.476 | -0.0062 | 0.044 | 0.00 | - |
| recent_base_rate_7d|h4|all | 2940 | 49 | 2940 | 0.410 | 0.39-0.43 | 0.590 | 0.446 | -0.0567 | 0.145 | 0.71 | -68.7 |
| recent_base_rate_7d|h4|on_time | 2940 | 49 | 2940 | 0.410 | 0.39-0.43 | 0.590 | 0.446 | -0.0567 | 0.145 | 0.71 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 928.03 | -7.20% | 1456 | 564 | 48 |
| analog_k100|h4 | 968.78 | -3.12% | 1723 | 663 | 45 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 53 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 50 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 48 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 45 |
| derivatives|h1 | 816.44 | -18.36% | 15 | 4 | 48 |
| derivatives|h4 | 1083.35 | +8.34% | 29 | 14 | 45 |
| lgbm_calibrated|h1 | 929.90 | -7.01% | 511 | 242 | 53 |
| lgbm_calibrated|h4 | 916.34 | -8.37% | 523 | 218 | 50 |
| logistic|h1 | 808.66 | -19.13% | 325 | 162 | 53 |
| logistic|h4 | 980.25 | -1.97% | 674 | 310 | 50 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 53 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 50 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 53 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 50 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 52 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 49 |
| benchmark_long_all_coins|h1 | 1017.32 | +1.73% | 3180 | 1509 | 53 |
| benchmark_long_all_coins|h4 | 1053.64 | +5.36% | 3000 | 1675 | 50 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 49 |

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
