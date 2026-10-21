# Live monitor (2026-10-21T20:07:15.328263+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.59 (ECE 0.144)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.461
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.493
- MISCALIBRATED: base_rate|h4|all says 0.50 on average, reality 0.59 (ECE 0.083)
- MISCALIBRATED: council|h4|all says 0.50 on average, reality 0.59 (ECE 0.086)
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.492
- MISCALIBRATED: derivatives|h4|all says 0.50 on average, reality 0.59 (ECE 0.085)
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.59 (ECE 0.126)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.432
- MISCALIBRATED: logistic|h4|all says 0.49 on average, reality 0.59 (ECE 0.096)
- MISCALIBRATED: momentum_24|h4|all says 0.50 on average, reality 0.59 (ECE 0.083)
- MISCALIBRATED: orthosys|h4|all says 0.50 on average, reality 0.59 (ECE 0.087)
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.499
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.495
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.45 on average, reality 0.59 (ECE 0.147)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.426

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['HBAR', 'RAY']
- **last_closed_bar**: 2026-10-21 19:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.2
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 107.9 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.145, 'recent_base_rate_7d': 0.089, 'momentum_24': 0.158, 'logistic': 0.174, 'lgbm_calibrated': 0.117, 'analog_k100': 0.017, 'derivatives': 0.147, 'orthosys': 0.153}
- **council_member_logloss_h1**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.6967, 'momentum_24': 0.6928, 'logistic': 0.6922, 'lgbm_calibrated': 0.6948, 'analog_k100': 0.7091, 'derivatives': 0.6935, 'orthosys': 0.6931}
- **council_calls_h1**: 1
- **council_abstain_h1**: {'no_edge': 54, 'extreme_volatility': 5, 'spoke': 1}
- **council_weights_h4**: {'base_rate': 0.229, 'recent_base_rate_7d': 0.003, 'momentum_24': 0.229, 'logistic': 0.102, 'lgbm_calibrated': 0.023, 'analog_k100': 0.0, 'derivatives': 0.228, 'orthosys': 0.186}
- **council_member_logloss_h4**: {'base_rate': 0.692, 'recent_base_rate_7d': 0.722, 'momentum_24': 0.692, 'logistic': 0.6977, 'lgbm_calibrated': 0.708, 'analog_k100': 0.7395, 'derivatives': 0.6918, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 54, 'extreme_volatility': 5, 'members_disagree': 1}
- **prediction_latency_min**: 7.2
- **price_snapshot_age_s**: 0.3
- **train_rows_h1**: 92290
- **orthosys_hist_hit_h1**: 0.531
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0065
- **p_spread_logistic_h1**: 0.033
- **p_spread_lgbm_calibrated_h1**: 0.0067
- **p_spread_analog_k100_h1**: 0.0542
- **p_spread_derivatives_h1**: 0.0104
- **p_spread_orthosys_h1**: 0.007
- **p_spread_council_h1**: 0.0026
- **train_rows_h4**: 92104
- **orthosys_hist_hit_h4**: 0.512
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0005
- **p_spread_logistic_h4**: 0.0661
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0804
- **p_spread_derivatives_h4**: 0.0439
- **p_spread_orthosys_h4**: 0.0027
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 55320

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 2820 | 47 | 2820 | 0.491 | 0.47-0.51 | 0.527 | 0.466 | -0.0312 | 0.067 | 0.51 | -16.1 |
| analog_k100|h1|on_time | 2820 | 47 | 2820 | 0.491 | 0.47-0.51 | 0.527 | 0.466 | -0.0312 | 0.067 | 0.51 | -16.1 |
| analog_k100|h4|all | 2640 | 44 | 2640 | 0.442 | 0.42-0.46 | 0.586 | 0.448 | -0.0872 | 0.144 | 0.63 | -33.8 |
| analog_k100|h4|on_time | 2640 | 44 | 2640 | 0.442 | 0.42-0.46 | 0.586 | 0.448 | -0.0872 | 0.144 | 0.63 | -33.8 |
| base_rate|h1|all | 3120 | 52 | 3120 | 0.475 | 0.46-0.49 | 0.525 | 0.498 | +0.0000 | 0.027 | 0.00 | - |
| base_rate|h1|on_time | 3060 | 51 | 3060 | 0.478 | 0.46-0.50 | 0.522 | 0.498 | +0.0000 | 0.024 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 2940 | 49 | 2940 | 0.586 | 0.57-0.60 | 0.586 | 0.504 | +0.0000 | 0.083 | 0.00 | - |
| base_rate|h4|on_time | 2940 | 49 | 2940 | 0.586 | 0.57-0.60 | 0.586 | 0.504 | +0.0000 | 0.083 | 0.00 | - |
| council|h1|all | 2820 | 47 | 480 | 0.510 | 0.47-0.55 | 0.527 | 0.496 | +0.0009 | 0.031 | 0.00 | +18.3 |
| council|h1|on_time | 2820 | 47 | 480 | 0.510 | 0.47-0.55 | 0.527 | 0.496 | +0.0009 | 0.031 | 0.00 | +18.3 |
| council|h4|all | 2640 | 44 | 24 | 0.583 | 0.39-0.76 | 0.586 | 0.500 | -0.0020 | 0.086 | 0.00 | - |
| council|h4|on_time | 2640 | 44 | 24 | 0.583 | 0.39-0.76 | 0.586 | 0.500 | -0.0020 | 0.086 | 0.00 | - |
| derivatives|h1|all | 2820 | 47 | 2820 | 0.473 | 0.46-0.49 | 0.527 | 0.497 | -0.0002 | 0.029 | 0.00 | -301.9 |
| derivatives|h1|on_time | 2820 | 47 | 2820 | 0.473 | 0.46-0.49 | 0.527 | 0.497 | -0.0002 | 0.029 | 0.00 | -301.9 |
| derivatives|h4|all | 2640 | 44 | 2640 | 0.590 | 0.57-0.61 | 0.586 | 0.502 | +0.0005 | 0.085 | 0.01 | +479.4 |
| derivatives|h4|on_time | 2640 | 44 | 2640 | 0.590 | 0.57-0.61 | 0.586 | 0.502 | +0.0005 | 0.085 | 0.01 | +479.4 |
| lgbm_calibrated|h1|all | 3120 | 52 | 3119 | 0.525 | 0.51-0.54 | 0.525 | 0.473 | -0.0029 | 0.052 | 0.16 | +1.0 |
| lgbm_calibrated|h1|on_time | 3060 | 51 | 3059 | 0.529 | 0.51-0.55 | 0.522 | 0.473 | -0.0023 | 0.049 | 0.17 | +1.0 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 2940 | 49 | 2940 | 0.414 | 0.40-0.43 | 0.586 | 0.462 | -0.0307 | 0.126 | 0.18 | -48.0 |
| lgbm_calibrated|h4|on_time | 2940 | 49 | 2940 | 0.414 | 0.40-0.43 | 0.586 | 0.462 | -0.0307 | 0.126 | 0.18 | -48.0 |
| logistic|h1|all | 3120 | 52 | 3120 | 0.524 | 0.51-0.54 | 0.525 | 0.490 | +0.0018 | 0.036 | 0.10 | -35.1 |
| logistic|h1|on_time | 3060 | 51 | 3060 | 0.519 | 0.50-0.54 | 0.522 | 0.489 | +0.0007 | 0.034 | 0.10 | -35.2 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 2940 | 49 | 2940 | 0.512 | 0.49-0.53 | 0.586 | 0.494 | -0.0108 | 0.096 | 0.22 | -31.5 |
| logistic|h4|on_time | 2940 | 49 | 2940 | 0.512 | 0.49-0.53 | 0.586 | 0.494 | -0.0108 | 0.096 | 0.22 | -31.5 |
| momentum_24|h1|all | 3120 | 52 | 3120 | 0.516 | 0.50-0.53 | 0.525 | 0.496 | +0.0010 | 0.029 | 0.00 | - |
| momentum_24|h1|on_time | 3060 | 51 | 3060 | 0.512 | 0.49-0.53 | 0.522 | 0.496 | +0.0007 | 0.027 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 2940 | 49 | 2940 | 0.586 | 0.57-0.60 | 0.586 | 0.503 | -0.0000 | 0.083 | 0.00 | - |
| momentum_24|h4|on_time | 2940 | 49 | 2940 | 0.586 | 0.57-0.60 | 0.586 | 0.503 | -0.0000 | 0.083 | 0.00 | - |
| orthosys|h1|all | 3120 | 52 | 227 | 0.529 | 0.46-0.59 | 0.525 | 0.499 | +0.0007 | 0.028 | 0.00 | - |
| orthosys|h1|on_time | 3060 | 51 | 226 | 0.527 | 0.46-0.59 | 0.522 | 0.499 | +0.0006 | 0.026 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 2940 | 49 | 213 | 0.432 | 0.37-0.50 | 0.586 | 0.499 | -0.0027 | 0.087 | 0.00 | - |
| orthosys|h4|on_time | 2940 | 49 | 213 | 0.432 | 0.37-0.50 | 0.586 | 0.499 | -0.0027 | 0.087 | 0.00 | - |
| recent_base_rate_7d|h1|all | 3060 | 51 | 3060 | 0.478 | 0.46-0.50 | 0.522 | 0.475 | -0.0065 | 0.047 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 3060 | 51 | 3060 | 0.478 | 0.46-0.50 | 0.522 | 0.475 | -0.0065 | 0.047 | 0.00 | - |
| recent_base_rate_7d|h4|all | 2880 | 48 | 2880 | 0.408 | 0.39-0.43 | 0.592 | 0.445 | -0.0578 | 0.147 | 0.73 | -68.7 |
| recent_base_rate_7d|h4|on_time | 2880 | 48 | 2880 | 0.408 | 0.39-0.43 | 0.592 | 0.445 | -0.0578 | 0.147 | 0.73 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 930.44 | -6.96% | 1434 | 553 | 47 |
| analog_k100|h4 | 969.44 | -3.06% | 1676 | 645 | 44 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 52 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 49 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 47 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 44 |
| derivatives|h1 | 823.75 | -17.62% | 14 | 4 | 47 |
| derivatives|h4 | 1088.60 | +8.86% | 25 | 13 | 44 |
| lgbm_calibrated|h1 | 929.90 | -7.01% | 511 | 242 | 52 |
| lgbm_calibrated|h4 | 916.34 | -8.37% | 523 | 218 | 49 |
| logistic|h1 | 816.02 | -18.40% | 322 | 160 | 52 |
| logistic|h4 | 984.97 | -1.50% | 650 | 302 | 49 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 52 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 49 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 52 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 49 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 51 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 48 |
| benchmark_long_all_coins|h1 | 1017.45 | +1.74% | 3120 | 1474 | 52 |
| benchmark_long_all_coins|h4 | 1052.69 | +5.27% | 2940 | 1644 | 49 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 52 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 48 |

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
