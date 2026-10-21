# Live monitor (2026-10-21T03:06:14.002246+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0004 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.59 (ECE 0.149)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.459
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.490
- MISCALIBRATED: base_rate|h4|all says 0.50 on average, reality 0.59 (ECE 0.084)
- MISCALIBRATED: council|h4|all says 0.50 on average, reality 0.59 (ECE 0.087)
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.485
- MISCALIBRATED: derivatives|h4|all says 0.50 on average, reality 0.59 (ECE 0.084)
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.59 (ECE 0.133)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.435
- MISCALIBRATED: logistic|h4|all says 0.49 on average, reality 0.59 (ECE 0.095)
- MISCALIBRATED: momentum_24|h4|all says 0.50 on average, reality 0.59 (ECE 0.084)
- MISCALIBRATED: orthosys|h4|all says 0.50 on average, reality 0.59 (ECE 0.088)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.494
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.60 (ECE 0.156)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.426

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['DASH', 'ENSO']
- **last_closed_bar**: 2026-10-21 02:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.3
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 103.6 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.131, 'recent_base_rate_7d': 0.084, 'momentum_24': 0.147, 'logistic': 0.192, 'lgbm_calibrated': 0.138, 'analog_k100': 0.034, 'derivatives': 0.135, 'orthosys': 0.14}
- **council_member_logloss_h1**: {'base_rate': 0.6936, 'recent_base_rate_7d': 0.6982, 'momentum_24': 0.6925, 'logistic': 0.6899, 'lgbm_calibrated': 0.6931, 'analog_k100': 0.7093, 'derivatives': 0.6937, 'orthosys': 0.6929}
- **council_calls_h1**: 2
- **council_abstain_h1**: {'no_edge': 55, 'extreme_volatility': 3, 'spoke': 2}
- **council_weights_h4**: {'base_rate': 0.203, 'recent_base_rate_7d': 0.009, 'momentum_24': 0.204, 'logistic': 0.163, 'lgbm_calibrated': 0.039, 'analog_k100': 0.004, 'derivatives': 0.197, 'orthosys': 0.18}
- **council_member_logloss_h4**: {'base_rate': 0.6923, 'recent_base_rate_7d': 0.7264, 'momentum_24': 0.6923, 'logistic': 0.6946, 'lgbm_calibrated': 0.7101, 'analog_k100': 0.7408, 'derivatives': 0.6923, 'orthosys': 0.6936}
- **council_calls_h4**: 1
- **council_abstain_h4**: {'no_edge': 56, 'extreme_volatility': 3, 'spoke': 1}
- **prediction_latency_min**: 6.1
- **price_snapshot_age_s**: 0.4
- **train_rows_h1**: 90930
- **orthosys_hist_hit_h1**: 0.5275
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0042
- **p_spread_logistic_h1**: 0.0212
- **p_spread_lgbm_calibrated_h1**: 0.0141
- **p_spread_analog_k100_h1**: 0.0673
- **p_spread_derivatives_h1**: 0.001
- **p_spread_orthosys_h1**: 0.0035
- **p_spread_council_h1**: 0.0038
- **train_rows_h4**: 90744
- **orthosys_hist_hit_h4**: 0.5134
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0003
- **p_spread_logistic_h4**: 0.0328
- **p_spread_lgbm_calibrated_h4**: 0.0004
- **p_spread_analog_k100_h4**: 0.0839
- **p_spread_derivatives_h4**: 0.0035
- **p_spread_orthosys_h4**: 0.0017
- **p_spread_council_h4**: 0.0027
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 36960

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1800 | 30 | 1800 | 0.497 | 0.47-0.52 | 0.536 | 0.466 | -0.0271 | 0.075 | 0.52 | -15.3 |
| analog_k100|h1|on_time | 1800 | 30 | 1800 | 0.497 | 0.47-0.52 | 0.536 | 0.466 | -0.0271 | 0.075 | 0.52 | -15.3 |
| analog_k100|h4|all | 1620 | 27 | 1620 | 0.435 | 0.41-0.46 | 0.586 | 0.446 | -0.0916 | 0.149 | 0.65 | -53.1 |
| analog_k100|h4|on_time | 1620 | 27 | 1620 | 0.435 | 0.41-0.46 | 0.586 | 0.446 | -0.0916 | 0.149 | 0.65 | -53.1 |
| base_rate|h1|all | 2100 | 35 | 2100 | 0.469 | 0.45-0.49 | 0.531 | 0.498 | +0.0000 | 0.033 | 0.00 | - |
| base_rate|h1|on_time | 2040 | 34 | 2040 | 0.472 | 0.45-0.49 | 0.528 | 0.498 | +0.0000 | 0.030 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 1920 | 32 | 1920 | 0.587 | 0.56-0.61 | 0.587 | 0.503 | +0.0000 | 0.084 | 0.00 | - |
| base_rate|h4|on_time | 1920 | 32 | 1920 | 0.587 | 0.56-0.61 | 0.587 | 0.503 | +0.0000 | 0.084 | 0.00 | - |
| council|h1|all | 1800 | 30 | 336 | 0.548 | 0.49-0.60 | 0.536 | 0.495 | +0.0026 | 0.049 | 0.00 | +18.3 |
| council|h1|on_time | 1800 | 30 | 336 | 0.548 | 0.49-0.60 | 0.536 | 0.495 | +0.0026 | 0.049 | 0.00 | +18.3 |
| council|h4|all | 1620 | 27 | 20 | 0.600 | 0.39-0.78 | 0.586 | 0.500 | -0.0015 | 0.087 | 0.00 | - |
| council|h4|on_time | 1620 | 27 | 20 | 0.600 | 0.39-0.78 | 0.586 | 0.500 | -0.0015 | 0.087 | 0.00 | - |
| derivatives|h1|all | 1800 | 30 | 1800 | 0.462 | 0.44-0.49 | 0.536 | 0.498 | -0.0001 | 0.040 | 0.00 | - |
| derivatives|h1|on_time | 1800 | 30 | 1800 | 0.462 | 0.44-0.49 | 0.536 | 0.498 | -0.0001 | 0.040 | 0.00 | - |
| derivatives|h4|all | 1620 | 27 | 1620 | 0.583 | 0.56-0.61 | 0.586 | 0.502 | -0.0002 | 0.084 | 0.00 | -117.6 |
| derivatives|h4|on_time | 1620 | 27 | 1620 | 0.583 | 0.56-0.61 | 0.586 | 0.502 | -0.0002 | 0.084 | 0.00 | -117.6 |
| lgbm_calibrated|h1|all | 2100 | 35 | 2100 | 0.540 | 0.52-0.56 | 0.531 | 0.474 | +0.0025 | 0.058 | 0.13 | +6.3 |
| lgbm_calibrated|h1|on_time | 2040 | 34 | 2040 | 0.545 | 0.52-0.57 | 0.528 | 0.474 | +0.0037 | 0.054 | 0.13 | +6.3 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 1920 | 32 | 1920 | 0.412 | 0.39-0.43 | 0.587 | 0.457 | -0.0349 | 0.133 | 0.26 | -50.2 |
| lgbm_calibrated|h4|on_time | 1920 | 32 | 1920 | 0.412 | 0.39-0.43 | 0.587 | 0.457 | -0.0349 | 0.133 | 0.26 | -50.2 |
| logistic|h1|all | 2100 | 35 | 2100 | 0.536 | 0.51-0.56 | 0.531 | 0.490 | +0.0078 | 0.044 | 0.10 | -7.3 |
| logistic|h1|on_time | 2040 | 34 | 2040 | 0.528 | 0.51-0.55 | 0.528 | 0.489 | +0.0064 | 0.042 | 0.10 | -7.1 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 1920 | 32 | 1920 | 0.514 | 0.49-0.54 | 0.587 | 0.492 | -0.0047 | 0.095 | 0.21 | +1.1 |
| logistic|h4|on_time | 1920 | 32 | 1920 | 0.514 | 0.49-0.54 | 0.587 | 0.492 | -0.0047 | 0.095 | 0.21 | +1.1 |
| momentum_24|h1|all | 2100 | 35 | 2100 | 0.537 | 0.52-0.56 | 0.531 | 0.497 | +0.0025 | 0.035 | 0.00 | - |
| momentum_24|h1|on_time | 2040 | 34 | 2040 | 0.532 | 0.51-0.55 | 0.528 | 0.496 | +0.0022 | 0.032 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 1920 | 32 | 1920 | 0.587 | 0.56-0.61 | 0.587 | 0.503 | +0.0000 | 0.084 | 0.00 | - |
| momentum_24|h4|on_time | 1920 | 32 | 1920 | 0.587 | 0.56-0.61 | 0.587 | 0.503 | +0.0000 | 0.084 | 0.00 | - |
| orthosys|h1|all | 2100 | 35 | 182 | 0.544 | 0.47-0.61 | 0.531 | 0.498 | +0.0012 | 0.036 | 0.00 | - |
| orthosys|h1|on_time | 2040 | 34 | 181 | 0.541 | 0.47-0.61 | 0.528 | 0.498 | +0.0011 | 0.032 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 1920 | 32 | 177 | 0.435 | 0.36-0.51 | 0.587 | 0.499 | -0.0025 | 0.088 | 0.00 | - |
| orthosys|h4|on_time | 1920 | 32 | 177 | 0.435 | 0.36-0.51 | 0.587 | 0.499 | -0.0025 | 0.088 | 0.00 | - |
| recent_base_rate_7d|h1|all | 2040 | 34 | 2040 | 0.472 | 0.45-0.49 | 0.528 | 0.474 | -0.0080 | 0.054 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 2040 | 34 | 2040 | 0.472 | 0.45-0.49 | 0.528 | 0.474 | -0.0080 | 0.054 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1860 | 31 | 1860 | 0.404 | 0.38-0.43 | 0.596 | 0.440 | -0.0663 | 0.156 | 0.94 | -70.7 |
| recent_base_rate_7d|h4|on_time | 1860 | 31 | 1860 | 0.404 | 0.38-0.43 | 0.596 | 0.440 | -0.0663 | 0.156 | 0.94 | -70.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 953.86 | -4.61% | 941 | 363 | 30 |
| analog_k100|h4 | 967.40 | -3.26% | 1054 | 402 | 27 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 35 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 32 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 30 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 27 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 30 |
| derivatives|h4 | 985.33 | -1.47% | 5 | 1 | 27 |
| lgbm_calibrated|h1 | 934.27 | -6.57% | 263 | 129 | 35 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 32 |
| logistic|h1 | 952.64 | -4.74% | 215 | 113 | 35 |
| logistic|h4 | 1029.32 | +2.93% | 400 | 194 | 32 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 35 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 32 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 35 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 32 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 34 |
| recent_base_rate_7d|h4 | 949.92 | -5.01% | 1740 | 667 | 31 |
| benchmark_long_all_coins|h1 | 1017.79 | +1.78% | 2100 | 1016 | 35 |
| benchmark_long_all_coins|h4 | 1040.00 | +4.00% | 1920 | 1050 | 32 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 30 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 35 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 32 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 34 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 31 |

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
