# Live monitor (2026-10-21T13:09:45.330530+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.57 (ECE 0.127)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.471
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.494
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.492
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.57 (ECE 0.115)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.446
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.497
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.58 (ECE 0.138)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.440

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['CASHCAT', 'HBAR']
- **last_closed_bar**: 2026-10-21 12:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 7.7
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 106.1 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.131, 'recent_base_rate_7d': 0.084, 'momentum_24': 0.144, 'logistic': 0.201, 'lgbm_calibrated': 0.133, 'analog_k100': 0.033, 'derivatives': 0.135, 'orthosys': 0.138}
- **council_member_logloss_h1**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.6969, 'momentum_24': 0.6927, 'logistic': 0.6902, 'lgbm_calibrated': 0.6933, 'analog_k100': 0.7056, 'derivatives': 0.6934, 'orthosys': 0.693}
- **council_calls_h1**: 7
- **council_abstain_h1**: {'no_edge': 49, 'spoke': 7, 'extreme_volatility': 4}
- **council_weights_h4**: {'base_rate': 0.197, 'recent_base_rate_7d': 0.007, 'momentum_24': 0.196, 'logistic': 0.185, 'lgbm_calibrated': 0.036, 'analog_k100': 0.003, 'derivatives': 0.202, 'orthosys': 0.174}
- **council_member_logloss_h4**: {'base_rate': 0.6925, 'recent_base_rate_7d': 0.7204, 'momentum_24': 0.6925, 'logistic': 0.6929, 'lgbm_calibrated': 0.7062, 'analog_k100': 0.7317, 'derivatives': 0.692, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 54, 'extreme_volatility': 4, 'members_disagree': 2}
- **prediction_latency_min**: 9.6
- **price_snapshot_age_s**: 0.5
- **train_rows_h1**: 91518
- **orthosys_hist_hit_h1**: 0.5298
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0071
- **p_spread_logistic_h1**: 0.0293
- **p_spread_lgbm_calibrated_h1**: 0.0247
- **p_spread_analog_k100_h1**: 0.0588
- **p_spread_derivatives_h1**: 0.0096
- **p_spread_orthosys_h1**: 0.0078
- **p_spread_council_h1**: 0.0076
- **train_rows_h4**: 91332
- **orthosys_hist_hit_h4**: 0.5117
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0002
- **p_spread_logistic_h4**: 0.0759
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0792
- **p_spread_derivatives_h4**: 0.0384
- **p_spread_orthosys_h4**: 0.003
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 47760

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 2400 | 40 | 2400 | 0.501 | 0.48-0.52 | 0.527 | 0.465 | -0.0240 | 0.066 | 0.52 | -9.7 |
| analog_k100|h1|on_time | 2400 | 40 | 2400 | 0.501 | 0.48-0.52 | 0.527 | 0.465 | -0.0240 | 0.066 | 0.52 | -9.7 |
| analog_k100|h4|all | 2220 | 37 | 2220 | 0.450 | 0.43-0.47 | 0.571 | 0.451 | -0.0763 | 0.127 | 0.63 | -32.0 |
| analog_k100|h4|on_time | 2220 | 37 | 2220 | 0.450 | 0.43-0.47 | 0.571 | 0.451 | -0.0763 | 0.127 | 0.63 | -32.0 |
| base_rate|h1|all | 2700 | 45 | 2700 | 0.475 | 0.46-0.49 | 0.525 | 0.498 | +0.0000 | 0.027 | 0.00 | - |
| base_rate|h1|on_time | 2640 | 44 | 2640 | 0.478 | 0.46-0.50 | 0.522 | 0.498 | +0.0000 | 0.024 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 2520 | 42 | 2520 | 0.573 | 0.55-0.59 | 0.573 | 0.503 | +0.0000 | 0.070 | 0.00 | - |
| base_rate|h4|on_time | 2520 | 42 | 2520 | 0.573 | 0.55-0.59 | 0.573 | 0.503 | +0.0000 | 0.070 | 0.00 | - |
| council|h1|all | 2400 | 40 | 418 | 0.545 | 0.50-0.59 | 0.527 | 0.495 | +0.0021 | 0.039 | 0.00 | +18.3 |
| council|h1|on_time | 2400 | 40 | 418 | 0.545 | 0.50-0.59 | 0.527 | 0.495 | +0.0021 | 0.039 | 0.00 | +18.3 |
| council|h4|all | 2220 | 37 | 21 | 0.571 | 0.37-0.76 | 0.571 | 0.500 | -0.0013 | 0.072 | 0.00 | - |
| council|h4|on_time | 2220 | 37 | 21 | 0.571 | 0.37-0.76 | 0.571 | 0.500 | -0.0013 | 0.072 | 0.00 | - |
| derivatives|h1|all | 2400 | 40 | 2400 | 0.472 | 0.45-0.49 | 0.527 | 0.498 | -0.0001 | 0.031 | 0.00 | -99.5 |
| derivatives|h1|on_time | 2400 | 40 | 2400 | 0.472 | 0.45-0.49 | 0.527 | 0.498 | -0.0001 | 0.031 | 0.00 | -99.5 |
| derivatives|h4|all | 2220 | 37 | 2220 | 0.571 | 0.55-0.59 | 0.571 | 0.502 | +0.0004 | 0.070 | 0.00 | -190.6 |
| derivatives|h4|on_time | 2220 | 37 | 2220 | 0.571 | 0.55-0.59 | 0.571 | 0.502 | +0.0004 | 0.070 | 0.00 | -190.6 |
| lgbm_calibrated|h1|all | 2700 | 45 | 2700 | 0.534 | 0.52-0.55 | 0.525 | 0.474 | +0.0000 | 0.051 | 0.15 | +3.0 |
| lgbm_calibrated|h1|on_time | 2640 | 44 | 2640 | 0.538 | 0.52-0.56 | 0.522 | 0.474 | +0.0008 | 0.048 | 0.15 | +3.0 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 2520 | 42 | 2520 | 0.426 | 0.41-0.45 | 0.573 | 0.461 | -0.0280 | 0.115 | 0.20 | -50.2 |
| lgbm_calibrated|h4|on_time | 2520 | 42 | 2520 | 0.426 | 0.41-0.45 | 0.573 | 0.461 | -0.0280 | 0.115 | 0.20 | -50.2 |
| logistic|h1|all | 2700 | 45 | 2700 | 0.533 | 0.51-0.55 | 0.525 | 0.490 | +0.0059 | 0.036 | 0.09 | -27.5 |
| logistic|h1|on_time | 2640 | 44 | 2640 | 0.528 | 0.51-0.55 | 0.522 | 0.489 | +0.0047 | 0.034 | 0.09 | -27.6 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 2520 | 42 | 2520 | 0.525 | 0.51-0.54 | 0.573 | 0.496 | -0.0015 | 0.077 | 0.20 | -26.0 |
| logistic|h4|on_time | 2520 | 42 | 2520 | 0.525 | 0.51-0.54 | 0.573 | 0.496 | -0.0015 | 0.077 | 0.20 | -26.0 |
| momentum_24|h1|all | 2700 | 45 | 2700 | 0.520 | 0.50-0.54 | 0.525 | 0.496 | +0.0013 | 0.029 | 0.00 | - |
| momentum_24|h1|on_time | 2640 | 44 | 2640 | 0.516 | 0.50-0.53 | 0.522 | 0.496 | +0.0010 | 0.026 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 2520 | 42 | 2520 | 0.573 | 0.55-0.59 | 0.573 | 0.503 | -0.0000 | 0.070 | 0.00 | - |
| momentum_24|h4|on_time | 2520 | 42 | 2520 | 0.573 | 0.55-0.59 | 0.573 | 0.503 | -0.0000 | 0.070 | 0.00 | - |
| orthosys|h1|all | 2700 | 45 | 196 | 0.536 | 0.47-0.60 | 0.525 | 0.499 | +0.0008 | 0.028 | 0.00 | - |
| orthosys|h1|on_time | 2640 | 44 | 195 | 0.533 | 0.46-0.60 | 0.522 | 0.499 | +0.0007 | 0.025 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 2520 | 42 | 189 | 0.434 | 0.37-0.51 | 0.573 | 0.499 | -0.0021 | 0.074 | 0.00 | - |
| orthosys|h4|on_time | 2520 | 42 | 189 | 0.434 | 0.37-0.51 | 0.573 | 0.499 | -0.0021 | 0.074 | 0.00 | - |
| recent_base_rate_7d|h1|all | 2640 | 44 | 2640 | 0.478 | 0.46-0.50 | 0.522 | 0.474 | -0.0069 | 0.048 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 2640 | 44 | 2640 | 0.478 | 0.46-0.50 | 0.522 | 0.474 | -0.0069 | 0.048 | 0.00 | - |
| recent_base_rate_7d|h4|all | 2460 | 41 | 2460 | 0.420 | 0.40-0.44 | 0.580 | 0.442 | -0.0566 | 0.138 | 0.85 | -68.7 |
| recent_base_rate_7d|h4|on_time | 2460 | 41 | 2460 | 0.420 | 0.40-0.44 | 0.580 | 0.442 | -0.0566 | 0.138 | 0.85 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 963.02 | -3.70% | 1248 | 494 | 40 |
| analog_k100|h4 | 975.90 | -2.41% | 1405 | 560 | 37 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 45 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 42 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 40 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 37 |
| derivatives|h1 | 960.09 | -3.99% | 4 | 2 | 40 |
| derivatives|h4 | 979.95 | -2.01% | 11 | 4 | 37 |
| lgbm_calibrated|h1 | 947.46 | -5.25% | 396 | 188 | 45 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 42 |
| logistic|h1 | 844.49 | -15.55% | 251 | 135 | 45 |
| logistic|h4 | 996.80 | -0.32% | 493 | 240 | 42 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 45 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 42 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 45 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 42 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 44 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 41 |
| benchmark_long_all_coins|h1 | 1021.53 | +2.15% | 2700 | 1267 | 45 |
| benchmark_long_all_coins|h4 | 1048.24 | +4.82% | 2520 | 1368 | 42 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 40 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 37 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 45 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 42 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 41 |

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
