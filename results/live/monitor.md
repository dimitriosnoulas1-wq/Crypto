# Live monitor (2026-10-21T16:07:38.118771+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.58 (ECE 0.139)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.462
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.487
- MISCALIBRATED: base_rate|h4|all says 0.50 on average, reality 0.58 (ECE 0.081)
- MISCALIBRATED: council|h4|all says 0.50 on average, reality 0.58 (ECE 0.084)
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.485
- MISCALIBRATED: derivatives|h4|all says 0.50 on average, reality 0.58 (ECE 0.082)
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.58 (ECE 0.124)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.434
- MISCALIBRATED: logistic|h4|all says 0.50 on average, reality 0.58 (ECE 0.089)
- MISCALIBRATED: momentum_24|h4|all says 0.50 on average, reality 0.58 (ECE 0.081)
- MISCALIBRATED: orthosys|h4|all says 0.50 on average, reality 0.58 (ECE 0.085)
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.493
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.490
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.59 (ECE 0.147)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.428

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['AERO', 'HBAR']
- **last_closed_bar**: 2026-10-21 15:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.5
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 112.5 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.137, 'recent_base_rate_7d': 0.085, 'momentum_24': 0.15, 'logistic': 0.191, 'lgbm_calibrated': 0.122, 'analog_k100': 0.026, 'derivatives': 0.143, 'orthosys': 0.144}
- **council_member_logloss_h1**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.6969, 'momentum_24': 0.6928, 'logistic': 0.6911, 'lgbm_calibrated': 0.6943, 'analog_k100': 0.7068, 'derivatives': 0.6933, 'orthosys': 0.6931}
- **council_calls_h1**: 2
- **council_abstain_h1**: {'no_edge': 52, 'extreme_volatility': 5, 'spoke': 2, 'members_disagree': 1}
- **council_weights_h4**: {'base_rate': 0.211, 'recent_base_rate_7d': 0.005, 'momentum_24': 0.211, 'logistic': 0.161, 'lgbm_calibrated': 0.033, 'analog_k100': 0.002, 'derivatives': 0.196, 'orthosys': 0.181}
- **council_member_logloss_h4**: {'base_rate': 0.6923, 'recent_base_rate_7d': 0.7211, 'momentum_24': 0.6923, 'logistic': 0.6944, 'lgbm_calibrated': 0.7065, 'analog_k100': 0.7336, 'derivatives': 0.6927, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 51, 'extreme_volatility': 5, 'members_disagree': 4}
- **prediction_latency_min**: 7.5
- **price_snapshot_age_s**: 0.2
- **train_rows_h1**: 92040
- **orthosys_hist_hit_h1**: 0.5305
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0067
- **p_spread_logistic_h1**: 0.0341
- **p_spread_lgbm_calibrated_h1**: 0.0063
- **p_spread_analog_k100_h1**: 0.0449
- **p_spread_derivatives_h1**: 0.0149
- **p_spread_orthosys_h1**: 0.0105
- **p_spread_council_h1**: 0.0038
- **train_rows_h4**: 91854
- **orthosys_hist_hit_h4**: 0.5116
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0007
- **p_spread_logistic_h4**: 0.0788
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0849
- **p_spread_derivatives_h4**: 0.0244
- **p_spread_orthosys_h4**: 0.004
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 51000

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 2580 | 43 | 2580 | 0.496 | 0.48-0.52 | 0.534 | 0.465 | -0.0295 | 0.074 | 0.52 | -13.6 |
| analog_k100|h1|on_time | 2580 | 43 | 2580 | 0.496 | 0.48-0.52 | 0.534 | 0.465 | -0.0295 | 0.074 | 0.52 | -13.6 |
| analog_k100|h4|all | 2400 | 40 | 2400 | 0.443 | 0.42-0.46 | 0.583 | 0.451 | -0.0842 | 0.139 | 0.63 | -30.1 |
| analog_k100|h4|on_time | 2400 | 40 | 2400 | 0.443 | 0.42-0.46 | 0.583 | 0.451 | -0.0842 | 0.139 | 0.63 | -30.1 |
| base_rate|h1|all | 2880 | 48 | 2880 | 0.469 | 0.45-0.49 | 0.531 | 0.498 | +0.0000 | 0.033 | 0.00 | - |
| base_rate|h1|on_time | 2820 | 47 | 2820 | 0.471 | 0.45-0.49 | 0.529 | 0.498 | +0.0000 | 0.031 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 2700 | 45 | 2700 | 0.584 | 0.57-0.60 | 0.584 | 0.503 | +0.0000 | 0.081 | 0.00 | - |
| base_rate|h4|on_time | 2700 | 45 | 2700 | 0.584 | 0.57-0.60 | 0.584 | 0.503 | +0.0000 | 0.081 | 0.00 | - |
| council|h1|all | 2580 | 43 | 469 | 0.505 | 0.46-0.55 | 0.534 | 0.495 | +0.0008 | 0.039 | 0.00 | +18.3 |
| council|h1|on_time | 2580 | 43 | 469 | 0.505 | 0.46-0.55 | 0.534 | 0.495 | +0.0008 | 0.039 | 0.00 | +18.3 |
| council|h4|all | 2400 | 40 | 21 | 0.571 | 0.37-0.76 | 0.583 | 0.500 | -0.0018 | 0.084 | 0.00 | - |
| council|h4|on_time | 2400 | 40 | 21 | 0.571 | 0.37-0.76 | 0.583 | 0.500 | -0.0018 | 0.084 | 0.00 | - |
| derivatives|h1|all | 2580 | 43 | 2580 | 0.466 | 0.45-0.49 | 0.534 | 0.498 | +0.0003 | 0.037 | 0.00 | -11.5 |
| derivatives|h1|on_time | 2580 | 43 | 2580 | 0.466 | 0.45-0.49 | 0.534 | 0.498 | +0.0003 | 0.037 | 0.00 | -11.5 |
| derivatives|h4|all | 2400 | 40 | 2400 | 0.584 | 0.56-0.60 | 0.583 | 0.502 | -0.0004 | 0.082 | 0.01 | -171.1 |
| derivatives|h4|on_time | 2400 | 40 | 2400 | 0.584 | 0.56-0.60 | 0.583 | 0.502 | -0.0004 | 0.082 | 0.01 | -171.1 |
| lgbm_calibrated|h1|all | 2880 | 48 | 2880 | 0.524 | 0.51-0.54 | 0.531 | 0.473 | -0.0045 | 0.059 | 0.16 | -3.0 |
| lgbm_calibrated|h1|on_time | 2820 | 47 | 2820 | 0.528 | 0.51-0.55 | 0.529 | 0.473 | -0.0038 | 0.056 | 0.17 | -3.0 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 2700 | 45 | 2700 | 0.416 | 0.40-0.43 | 0.584 | 0.462 | -0.0296 | 0.124 | 0.18 | -50.2 |
| lgbm_calibrated|h4|on_time | 2700 | 45 | 2700 | 0.416 | 0.40-0.43 | 0.584 | 0.462 | -0.0296 | 0.124 | 0.18 | -50.2 |
| logistic|h1|all | 2880 | 48 | 2880 | 0.523 | 0.51-0.54 | 0.531 | 0.489 | +0.0024 | 0.043 | 0.10 | -31.5 |
| logistic|h1|on_time | 2820 | 47 | 2820 | 0.518 | 0.50-0.54 | 0.529 | 0.489 | +0.0012 | 0.041 | 0.10 | -31.6 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 2700 | 45 | 2700 | 0.520 | 0.50-0.54 | 0.584 | 0.496 | -0.0053 | 0.089 | 0.20 | -46.3 |
| logistic|h4|on_time | 2700 | 45 | 2700 | 0.520 | 0.50-0.54 | 0.584 | 0.496 | -0.0053 | 0.089 | 0.20 | -46.3 |
| momentum_24|h1|all | 2880 | 48 | 2880 | 0.516 | 0.50-0.53 | 0.531 | 0.496 | +0.0010 | 0.035 | 0.00 | - |
| momentum_24|h1|on_time | 2820 | 47 | 2820 | 0.512 | 0.49-0.53 | 0.529 | 0.496 | +0.0007 | 0.033 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 2700 | 45 | 2700 | 0.584 | 0.57-0.60 | 0.584 | 0.503 | -0.0000 | 0.081 | 0.00 | - |
| momentum_24|h4|on_time | 2700 | 45 | 2700 | 0.584 | 0.57-0.60 | 0.584 | 0.503 | -0.0000 | 0.081 | 0.00 | - |
| orthosys|h1|all | 2880 | 48 | 206 | 0.529 | 0.46-0.60 | 0.531 | 0.499 | +0.0008 | 0.033 | 0.00 | - |
| orthosys|h1|on_time | 2820 | 47 | 205 | 0.527 | 0.46-0.59 | 0.529 | 0.499 | +0.0007 | 0.031 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 2700 | 45 | 196 | 0.423 | 0.36-0.49 | 0.584 | 0.499 | -0.0026 | 0.085 | 0.00 | - |
| orthosys|h4|on_time | 2700 | 45 | 196 | 0.423 | 0.36-0.49 | 0.584 | 0.499 | -0.0026 | 0.085 | 0.00 | - |
| recent_base_rate_7d|h1|all | 2820 | 47 | 2820 | 0.471 | 0.45-0.49 | 0.529 | 0.474 | -0.0075 | 0.054 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 2820 | 47 | 2820 | 0.471 | 0.45-0.49 | 0.529 | 0.474 | -0.0075 | 0.054 | 0.00 | - |
| recent_base_rate_7d|h4|all | 2640 | 44 | 2640 | 0.409 | 0.39-0.43 | 0.591 | 0.443 | -0.0592 | 0.147 | 0.80 | -68.7 |
| recent_base_rate_7d|h4|on_time | 2640 | 44 | 2640 | 0.409 | 0.39-0.43 | 0.591 | 0.443 | -0.0592 | 0.147 | 0.80 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 948.40 | -5.16% | 1341 | 524 | 43 |
| analog_k100|h4 | 976.31 | -2.37% | 1513 | 584 | 40 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 48 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 45 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 43 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 40 |
| derivatives|h1 | 975.90 | -2.41% | 6 | 3 | 43 |
| derivatives|h4 | 972.57 | -2.74% | 14 | 5 | 40 |
| lgbm_calibrated|h1 | 932.99 | -6.70% | 470 | 209 | 48 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 45 |
| logistic|h1 | 828.85 | -17.12% | 289 | 144 | 48 |
| logistic|h4 | 977.86 | -2.21% | 544 | 260 | 45 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 48 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 45 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 48 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 45 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 47 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 44 |
| benchmark_long_all_coins|h1 | 1019.82 | +1.98% | 2880 | 1370 | 48 |
| benchmark_long_all_coins|h4 | 1054.17 | +5.42% | 2700 | 1501 | 45 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 47 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 44 |

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
