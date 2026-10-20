# Live monitor (2026-10-20T23:06:42.777982+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.001 (same probability for every coin)
- MISCALIBRATED: analog_k100|h1|all says 0.47 on average, reality 0.54 (ECE 0.081)
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.484
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.477
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.58 (ECE 0.124)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.446
- MISCALIBRATED: logistic|h4|all says 0.49 on average, reality 0.58 (ECE 0.086)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.488
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.59 (ECE 0.149)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.436

## Health

- **venue**: okx
- **symbols**: 61
- **universe_size**: 60
- **fetched_only_for_scoring**: ['GRASS']
- **last_closed_bar**: 2026-10-20 22:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.8
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 103.1 instruments 61/61']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.13, 'recent_base_rate_7d': 0.086, 'momentum_24': 0.147, 'logistic': 0.178, 'lgbm_calibrated': 0.133, 'analog_k100': 0.055, 'derivatives': 0.133, 'orthosys': 0.138}
- **council_member_logloss_h1**: {'base_rate': 0.6936, 'recent_base_rate_7d': 0.6984, 'momentum_24': 0.6922, 'logistic': 0.6901, 'lgbm_calibrated': 0.6933, 'analog_k100': 0.7054, 'derivatives': 0.6937, 'orthosys': 0.6929}
- **council_calls_h1**: 27
- **council_abstain_h1**: {'no_edge': 31, 'spoke': 27, 'extreme_volatility': 2}
- **council_weights_h4**: {'base_rate': 0.188, 'recent_base_rate_7d': 0.016, 'momentum_24': 0.189, 'logistic': 0.179, 'lgbm_calibrated': 0.062, 'analog_k100': 0.009, 'derivatives': 0.183, 'orthosys': 0.174}
- **council_member_logloss_h4**: {'base_rate': 0.6926, 'recent_base_rate_7d': 0.7239, 'momentum_24': 0.6926, 'logistic': 0.6933, 'lgbm_calibrated': 0.7063, 'analog_k100': 0.7391, 'derivatives': 0.6927, 'orthosys': 0.6936}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 58, 'extreme_volatility': 2}
- **prediction_latency_min**: 6.6
- **price_snapshot_age_s**: 0.8
- **train_rows_h1**: 89570
- **orthosys_hist_hit_h1**: 0.5285
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0053
- **p_spread_logistic_h1**: 0.018
- **p_spread_lgbm_calibrated_h1**: 0.0073
- **p_spread_analog_k100_h1**: 0.0685
- **p_spread_derivatives_h1**: 0.0012
- **p_spread_orthosys_h1**: 0.0037
- **p_spread_council_h1**: 0.0121
- **train_rows_h4**: 89387
- **orthosys_hist_hit_h4**: 0.5141
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0003
- **p_spread_logistic_h4**: 0.0306
- **p_spread_lgbm_calibrated_h4**: 0.001
- **p_spread_analog_k100_h4**: 0.0723
- **p_spread_derivatives_h4**: 0.0042
- **p_spread_orthosys_h4**: 0.0018
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 32640

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1560 | 26 | 1560 | 0.498 | 0.47-0.52 | 0.545 | 0.469 | -0.0241 | 0.081 | 0.51 | -15.2 |
| analog_k100|h1|on_time | 1560 | 26 | 1560 | 0.498 | 0.47-0.52 | 0.545 | 0.469 | -0.0241 | 0.081 | 0.51 | -15.2 |
| analog_k100|h4|all | 1380 | 23 | 1380 | 0.435 | 0.41-0.46 | 0.575 | 0.444 | -0.0959 | 0.146 | 0.64 | -58.8 |
| analog_k100|h4|on_time | 1380 | 23 | 1380 | 0.435 | 0.41-0.46 | 0.575 | 0.444 | -0.0959 | 0.146 | 0.64 | -58.8 |
| base_rate|h1|all | 1860 | 31 | 1860 | 0.461 | 0.44-0.48 | 0.539 | 0.498 | +0.0000 | 0.041 | 0.00 | - |
| base_rate|h1|on_time | 1800 | 30 | 1800 | 0.465 | 0.44-0.49 | 0.535 | 0.498 | +0.0000 | 0.037 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 1680 | 28 | 1680 | 0.577 | 0.55-0.60 | 0.577 | 0.503 | +0.0000 | 0.074 | 0.00 | - |
| base_rate|h4|on_time | 1680 | 28 | 1680 | 0.577 | 0.55-0.60 | 0.577 | 0.503 | +0.0000 | 0.074 | 0.00 | - |
| council|h1|all | 1560 | 26 | 289 | 0.536 | 0.48-0.59 | 0.545 | 0.495 | +0.0025 | 0.054 | 0.00 | +18.3 |
| council|h1|on_time | 1560 | 26 | 289 | 0.536 | 0.48-0.59 | 0.545 | 0.495 | +0.0025 | 0.054 | 0.00 | +18.3 |
| council|h4|all | 1380 | 23 | 19 | 0.579 | 0.36-0.77 | 0.575 | 0.500 | -0.0010 | 0.076 | 0.00 | - |
| council|h4|on_time | 1380 | 23 | 19 | 0.579 | 0.36-0.77 | 0.575 | 0.500 | -0.0010 | 0.076 | 0.00 | - |
| derivatives|h1|all | 1560 | 26 | 1560 | 0.453 | 0.43-0.48 | 0.545 | 0.498 | -0.0001 | 0.049 | 0.00 | - |
| derivatives|h1|on_time | 1560 | 26 | 1560 | 0.453 | 0.43-0.48 | 0.545 | 0.498 | -0.0001 | 0.049 | 0.00 | - |
| derivatives|h4|all | 1380 | 23 | 1380 | 0.572 | 0.55-0.60 | 0.575 | 0.502 | +0.0001 | 0.072 | 0.00 | -117.6 |
| derivatives|h4|on_time | 1380 | 23 | 1380 | 0.572 | 0.55-0.60 | 0.575 | 0.502 | +0.0001 | 0.072 | 0.00 | -117.6 |
| lgbm_calibrated|h1|all | 1860 | 31 | 1860 | 0.541 | 0.52-0.56 | 0.539 | 0.476 | +0.0012 | 0.063 | 0.11 | +9.8 |
| lgbm_calibrated|h1|on_time | 1800 | 30 | 1800 | 0.548 | 0.52-0.57 | 0.535 | 0.476 | +0.0025 | 0.059 | 0.12 | +9.8 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 1680 | 28 | 1680 | 0.422 | 0.40-0.45 | 0.577 | 0.456 | -0.0315 | 0.124 | 0.27 | -50.8 |
| lgbm_calibrated|h4|on_time | 1680 | 28 | 1680 | 0.422 | 0.40-0.45 | 0.577 | 0.456 | -0.0315 | 0.124 | 0.27 | -50.8 |
| logistic|h1|all | 1860 | 31 | 1860 | 0.532 | 0.51-0.55 | 0.539 | 0.491 | +0.0071 | 0.052 | 0.11 | -9.7 |
| logistic|h1|on_time | 1800 | 30 | 1800 | 0.524 | 0.50-0.55 | 0.535 | 0.490 | +0.0054 | 0.049 | 0.12 | -9.6 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 1680 | 28 | 1680 | 0.518 | 0.49-0.54 | 0.577 | 0.491 | -0.0036 | 0.086 | 0.21 | -0.2 |
| logistic|h4|on_time | 1680 | 28 | 1680 | 0.518 | 0.49-0.54 | 0.577 | 0.491 | -0.0036 | 0.086 | 0.21 | -0.2 |
| momentum_24|h1|all | 1860 | 31 | 1860 | 0.538 | 0.52-0.56 | 0.539 | 0.497 | +0.0027 | 0.041 | 0.00 | - |
| momentum_24|h1|on_time | 1800 | 30 | 1800 | 0.533 | 0.51-0.56 | 0.535 | 0.497 | +0.0023 | 0.038 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 1680 | 28 | 1680 | 0.577 | 0.55-0.60 | 0.577 | 0.503 | +0.0001 | 0.075 | 0.00 | - |
| momentum_24|h4|on_time | 1680 | 28 | 1680 | 0.577 | 0.55-0.60 | 0.577 | 0.503 | +0.0001 | 0.075 | 0.00 | - |
| orthosys|h1|all | 1860 | 31 | 176 | 0.545 | 0.47-0.62 | 0.539 | 0.498 | +0.0014 | 0.043 | 0.00 | - |
| orthosys|h1|on_time | 1800 | 30 | 175 | 0.543 | 0.47-0.61 | 0.535 | 0.498 | +0.0013 | 0.039 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 1680 | 28 | 173 | 0.428 | 0.36-0.50 | 0.577 | 0.499 | -0.0022 | 0.079 | 0.00 | - |
| orthosys|h4|on_time | 1680 | 28 | 173 | 0.428 | 0.36-0.50 | 0.577 | 0.499 | -0.0022 | 0.079 | 0.00 | - |
| recent_base_rate_7d|h1|all | 1800 | 30 | 1800 | 0.465 | 0.44-0.49 | 0.535 | 0.473 | -0.0094 | 0.062 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 1800 | 30 | 1800 | 0.465 | 0.44-0.49 | 0.535 | 0.473 | -0.0094 | 0.062 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1620 | 27 | 1620 | 0.412 | 0.39-0.44 | 0.588 | 0.439 | -0.0642 | 0.149 | 0.93 | -71.0 |
| recent_base_rate_7d|h4|on_time | 1620 | 27 | 1620 | 0.412 | 0.39-0.44 | 0.588 | 0.439 | -0.0642 | 0.149 | 0.93 | -71.0 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 959.43 | -4.06% | 797 | 310 | 26 |
| analog_k100|h4 | 969.18 | -3.08% | 887 | 338 | 23 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 31 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 28 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 26 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 23 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 26 |
| derivatives|h4 | 985.33 | -1.47% | 5 | 1 | 23 |
| lgbm_calibrated|h1 | 934.89 | -6.51% | 207 | 102 | 31 |
| lgbm_calibrated|h4 | 917.65 | -8.24% | 453 | 189 | 28 |
| logistic|h1 | 923.83 | -7.62% | 210 | 109 | 31 |
| logistic|h4 | 1028.90 | +2.89% | 349 | 172 | 28 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 31 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 28 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 31 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 28 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 30 |
| recent_base_rate_7d|h4 | 956.48 | -4.35% | 1500 | 589 | 27 |
| benchmark_long_all_coins|h1 | 1013.16 | +1.32% | 1860 | 895 | 31 |
| benchmark_long_all_coins|h4 | 1034.95 | +3.49% | 1680 | 902 | 28 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 31 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 27 |

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
