# Live monitor (2026-10-22T07:12:48.282881+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.50 (ECE 0.109)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.492
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.451

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['APR', 'CHIP']
- **last_closed_bar**: 2026-10-22 06:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 10.8
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 104.1 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.033
- **council_weights_h1**: {'base_rate': 0.156, 'recent_base_rate_7d': 0.131, 'momentum_24': 0.167, 'logistic': 0.092, 'lgbm_calibrated': 0.13, 'analog_k100': 0.011, 'derivatives': 0.172, 'orthosys': 0.14}
- **council_member_logloss_h1**: {'base_rate': 0.6929, 'recent_base_rate_7d': 0.6939, 'momentum_24': 0.6925, 'logistic': 0.6957, 'lgbm_calibrated': 0.6939, 'analog_k100': 0.7085, 'derivatives': 0.6925, 'orthosys': 0.6935}
- **council_calls_h1**: 1
- **council_abstain_h1**: {'no_edge': 51, 'extreme_volatility': 7, 'missing_inputs': 1, 'spoke': 1}
- **council_weights_h4**: {'base_rate': 0.198, 'recent_base_rate_7d': 0.008, 'momentum_24': 0.195, 'logistic': 0.055, 'lgbm_calibrated': 0.08, 'analog_k100': 0.004, 'derivatives': 0.27, 'orthosys': 0.189}
- **council_member_logloss_h4**: {'base_rate': 0.6933, 'recent_base_rate_7d': 0.7115, 'momentum_24': 0.6934, 'logistic': 0.7005, 'lgbm_calibrated': 0.6984, 'analog_k100': 0.7174, 'derivatives': 0.6913, 'orthosys': 0.6936}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 50, 'extreme_volatility': 7, 'members_disagree': 2, 'missing_inputs': 1}
- **prediction_latency_min**: 12.7
- **price_snapshot_age_s**: 1.0
- **train_rows_h1**: 91397
- **orthosys_hist_hit_h1**: 0.5269
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0042
- **p_spread_logistic_h1**: 0.035
- **p_spread_lgbm_calibrated_h1**: 0.0107
- **p_spread_analog_k100_h1**: 0.0825
- **p_spread_derivatives_h1**: 0.0246
- **p_spread_orthosys_h1**: 0.0136
- **p_spread_council_h1**: 0.0027
- **train_rows_h4**: 91211
- **orthosys_hist_hit_h4**: 0.5076
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0003
- **p_spread_logistic_h4**: 0.0626
- **p_spread_lgbm_calibrated_h4**: 0.0043
- **p_spread_analog_k100_h4**: 0.0884
- **p_spread_derivatives_h4**: 0.0435
- **p_spread_orthosys_h4**: 0.0038
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 67200

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 3480 | 58 | 3480 | 0.491 | 0.47-0.51 | 0.477 | 0.470 | -0.0294 | 0.066 | 0.51 | -14.1 |
| analog_k100|h1|on_time | 3480 | 58 | 3480 | 0.491 | 0.47-0.51 | 0.477 | 0.470 | -0.0294 | 0.066 | 0.51 | -14.1 |
| analog_k100|h4|all | 3300 | 55 | 3300 | 0.475 | 0.46-0.49 | 0.501 | 0.447 | -0.0532 | 0.109 | 0.65 | -14.2 |
| analog_k100|h4|on_time | 3300 | 55 | 3300 | 0.475 | 0.46-0.49 | 0.501 | 0.447 | -0.0532 | 0.109 | 0.65 | -14.2 |
| base_rate|h1|all | 3780 | 63 | 3780 | 0.521 | 0.50-0.54 | 0.479 | 0.498 | +0.0000 | 0.019 | 0.00 | - |
| base_rate|h1|on_time | 3720 | 62 | 3720 | 0.524 | 0.51-0.54 | 0.476 | 0.498 | +0.0000 | 0.021 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 3600 | 60 | 3600 | 0.508 | 0.49-0.52 | 0.508 | 0.504 | +0.0000 | 0.005 | 0.00 | - |
| base_rate|h4|on_time | 3600 | 60 | 3600 | 0.508 | 0.49-0.52 | 0.508 | 0.504 | +0.0000 | 0.005 | 0.00 | - |
| council|h1|all | 3480 | 58 | 494 | 0.512 | 0.47-0.56 | 0.477 | 0.496 | -0.0004 | 0.023 | 0.00 | +18.3 |
| council|h1|on_time | 3480 | 58 | 494 | 0.512 | 0.47-0.56 | 0.477 | 0.496 | -0.0004 | 0.023 | 0.00 | +18.3 |
| council|h4|all | 3300 | 55 | 25 | 0.600 | 0.41-0.77 | 0.501 | 0.500 | +0.0007 | 0.001 | 0.00 | - |
| council|h4|on_time | 3300 | 55 | 25 | 0.600 | 0.41-0.77 | 0.501 | 0.500 | +0.0007 | 0.001 | 0.00 | - |
| derivatives|h1|all | 3480 | 58 | 3480 | 0.523 | 0.51-0.54 | 0.477 | 0.497 | +0.0010 | 0.020 | 0.01 | -15.0 |
| derivatives|h1|on_time | 3480 | 58 | 3480 | 0.523 | 0.51-0.54 | 0.477 | 0.497 | +0.0010 | 0.020 | 0.01 | -15.0 |
| derivatives|h4|all | 3300 | 55 | 3300 | 0.517 | 0.50-0.53 | 0.501 | 0.500 | +0.0041 | 0.011 | 0.02 | +454.7 |
| derivatives|h4|on_time | 3300 | 55 | 3300 | 0.517 | 0.50-0.53 | 0.501 | 0.500 | +0.0041 | 0.011 | 0.02 | +454.7 |
| lgbm_calibrated|h1|all | 3780 | 63 | 3779 | 0.545 | 0.53-0.56 | 0.479 | 0.476 | -0.0015 | 0.018 | 0.14 | -1.0 |
| lgbm_calibrated|h1|on_time | 3720 | 62 | 3719 | 0.549 | 0.53-0.56 | 0.476 | 0.476 | -0.0009 | 0.021 | 0.14 | -1.0 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 3600 | 60 | 3600 | 0.491 | 0.47-0.51 | 0.508 | 0.463 | -0.0077 | 0.047 | 0.15 | -48.0 |
| lgbm_calibrated|h4|on_time | 3600 | 60 | 3600 | 0.491 | 0.47-0.51 | 0.508 | 0.463 | -0.0077 | 0.047 | 0.15 | -48.0 |
| logistic|h1|all | 3780 | 63 | 3780 | 0.504 | 0.49-0.52 | 0.479 | 0.493 | -0.0065 | 0.021 | 0.13 | -28.9 |
| logistic|h1|on_time | 3720 | 62 | 3720 | 0.500 | 0.48-0.52 | 0.476 | 0.493 | -0.0075 | 0.025 | 0.13 | -28.9 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 3600 | 60 | 3600 | 0.490 | 0.47-0.51 | 0.508 | 0.494 | -0.0154 | 0.050 | 0.25 | -23.4 |
| logistic|h4|on_time | 3600 | 60 | 3600 | 0.490 | 0.47-0.51 | 0.508 | 0.494 | -0.0154 | 0.050 | 0.25 | -23.4 |
| momentum_24|h1|all | 3780 | 63 | 3780 | 0.510 | 0.49-0.53 | 0.479 | 0.496 | +0.0005 | 0.017 | 0.00 | - |
| momentum_24|h1|on_time | 3720 | 62 | 3720 | 0.506 | 0.49-0.52 | 0.476 | 0.496 | +0.0002 | 0.020 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 3600 | 60 | 3600 | 0.508 | 0.49-0.52 | 0.508 | 0.504 | -0.0001 | 0.005 | 0.00 | - |
| momentum_24|h4|on_time | 3600 | 60 | 3600 | 0.508 | 0.49-0.52 | 0.508 | 0.504 | -0.0001 | 0.005 | 0.00 | - |
| orthosys|h1|all | 3780 | 63 | 330 | 0.461 | 0.41-0.51 | 0.479 | 0.500 | -0.0018 | 0.021 | 0.00 | - |
| orthosys|h1|on_time | 3720 | 62 | 329 | 0.459 | 0.41-0.51 | 0.476 | 0.500 | -0.0019 | 0.024 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 3600 | 60 | 268 | 0.392 | 0.34-0.45 | 0.508 | 0.500 | -0.0004 | 0.009 | 0.00 | - |
| orthosys|h4|on_time | 3600 | 60 | 268 | 0.392 | 0.34-0.45 | 0.508 | 0.500 | -0.0004 | 0.009 | 0.00 | - |
| recent_base_rate_7d|h1|all | 3720 | 62 | 3720 | 0.524 | 0.51-0.54 | 0.476 | 0.477 | -0.0015 | 0.001 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 3720 | 62 | 3720 | 0.524 | 0.51-0.54 | 0.476 | 0.477 | -0.0015 | 0.001 | 0.00 | - |
| recent_base_rate_7d|h4|all | 3540 | 59 | 3540 | 0.488 | 0.47-0.50 | 0.512 | 0.451 | -0.0340 | 0.060 | 0.59 | -68.7 |
| recent_base_rate_7d|h4|on_time | 3540 | 59 | 3540 | 0.488 | 0.47-0.50 | 0.512 | 0.451 | -0.0340 | 0.060 | 0.59 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 926.83 | -7.32% | 1774 | 711 | 58 |
| analog_k100|h4 | 984.99 | -1.50% | 2160 | 950 | 55 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 63 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 60 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 58 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 55 |
| derivatives|h1 | 1132.87 | +13.29% | 30 | 14 | 58 |
| derivatives|h4 | 1218.34 | +21.83% | 63 | 41 | 55 |
| lgbm_calibrated|h1 | 924.79 | -7.52% | 535 | 249 | 63 |
| lgbm_calibrated|h4 | 916.34 | -8.37% | 523 | 218 | 60 |
| logistic|h1 | 815.86 | -18.41% | 477 | 203 | 63 |
| logistic|h4 | 989.57 | -1.04% | 902 | 398 | 60 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 63 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 60 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 63 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 60 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 62 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 59 |
| benchmark_long_all_coins|h1 | 954.96 | -4.50% | 3780 | 1619 | 63 |
| benchmark_long_all_coins|h4 | 999.82 | -0.02% | 3600 | 1742 | 60 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 58 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 63 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 60 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 58 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 58 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 63 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 60 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 63 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 60 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 63 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 60 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 63 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 60 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 62 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 59 |

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
