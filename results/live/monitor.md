# Live monitor (2026-10-21T12:06:57.147579+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.57 (ECE 0.126)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.472
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.494
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.492
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.57 (ECE 0.112)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.449
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.498
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.58 (ECE 0.136)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.442

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['CASHCAT', 'GRASS']
- **last_closed_bar**: 2026-10-21 11:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.8
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 106.7 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.13, 'recent_base_rate_7d': 0.085, 'momentum_24': 0.146, 'logistic': 0.204, 'lgbm_calibrated': 0.131, 'analog_k100': 0.032, 'derivatives': 0.135, 'orthosys': 0.137}
- **council_member_logloss_h1**: {'base_rate': 0.6934, 'recent_base_rate_7d': 0.6968, 'momentum_24': 0.6925, 'logistic': 0.6899, 'lgbm_calibrated': 0.6933, 'analog_k100': 0.7061, 'derivatives': 0.6933, 'orthosys': 0.693}
- **council_calls_h1**: 6
- **council_abstain_h1**: {'no_edge': 50, 'spoke': 6, 'extreme_volatility': 4}
- **council_weights_h4**: {'base_rate': 0.198, 'recent_base_rate_7d': 0.006, 'momentum_24': 0.198, 'logistic': 0.184, 'lgbm_calibrated': 0.035, 'analog_k100': 0.003, 'derivatives': 0.201, 'orthosys': 0.175}
- **council_member_logloss_h4**: {'base_rate': 0.6924, 'recent_base_rate_7d': 0.7216, 'momentum_24': 0.6924, 'logistic': 0.693, 'lgbm_calibrated': 0.7068, 'analog_k100': 0.733, 'derivatives': 0.692, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 54, 'extreme_volatility': 4, 'members_disagree': 2}
- **prediction_latency_min**: 6.8
- **price_snapshot_age_s**: 0.5
- **train_rows_h1**: 91457
- **orthosys_hist_hit_h1**: 0.5292
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0079
- **p_spread_logistic_h1**: 0.0371
- **p_spread_lgbm_calibrated_h1**: 0.0233
- **p_spread_analog_k100_h1**: 0.0578
- **p_spread_derivatives_h1**: 0.011
- **p_spread_orthosys_h1**: 0.0066
- **p_spread_council_h1**: 0.0078
- **train_rows_h4**: 91271
- **orthosys_hist_hit_h4**: 0.512
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0002
- **p_spread_logistic_h4**: 0.0686
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0725
- **p_spread_derivatives_h4**: 0.0224
- **p_spread_orthosys_h4**: 0.0027
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 46680

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 2340 | 39 | 2340 | 0.502 | 0.48-0.52 | 0.527 | 0.465 | -0.0235 | 0.067 | 0.52 | -11.5 |
| analog_k100|h1|on_time | 2340 | 39 | 2340 | 0.502 | 0.48-0.52 | 0.527 | 0.465 | -0.0235 | 0.067 | 0.52 | -11.5 |
| analog_k100|h4|all | 2160 | 36 | 2160 | 0.451 | 0.43-0.47 | 0.568 | 0.451 | -0.0756 | 0.126 | 0.64 | -35.9 |
| analog_k100|h4|on_time | 2160 | 36 | 2160 | 0.451 | 0.43-0.47 | 0.568 | 0.451 | -0.0756 | 0.126 | 0.64 | -35.9 |
| base_rate|h1|all | 2640 | 44 | 2640 | 0.475 | 0.46-0.49 | 0.525 | 0.498 | +0.0000 | 0.027 | 0.00 | - |
| base_rate|h1|on_time | 2580 | 43 | 2580 | 0.478 | 0.46-0.50 | 0.522 | 0.498 | +0.0000 | 0.024 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 2460 | 41 | 2460 | 0.571 | 0.55-0.59 | 0.571 | 0.503 | +0.0000 | 0.067 | 0.00 | - |
| base_rate|h4|on_time | 2460 | 41 | 2460 | 0.571 | 0.55-0.59 | 0.571 | 0.503 | +0.0000 | 0.067 | 0.00 | - |
| council|h1|all | 2340 | 39 | 412 | 0.546 | 0.50-0.59 | 0.527 | 0.495 | +0.0022 | 0.039 | 0.00 | +18.3 |
| council|h1|on_time | 2340 | 39 | 412 | 0.546 | 0.50-0.59 | 0.527 | 0.495 | +0.0022 | 0.039 | 0.00 | +18.3 |
| council|h4|all | 2160 | 36 | 21 | 0.571 | 0.37-0.76 | 0.568 | 0.500 | -0.0012 | 0.069 | 0.00 | - |
| council|h4|on_time | 2160 | 36 | 21 | 0.571 | 0.37-0.76 | 0.568 | 0.500 | -0.0012 | 0.069 | 0.00 | - |
| derivatives|h1|all | 2340 | 39 | 2340 | 0.472 | 0.45-0.49 | 0.527 | 0.498 | +0.0000 | 0.031 | 0.00 | -9.9 |
| derivatives|h1|on_time | 2340 | 39 | 2340 | 0.472 | 0.45-0.49 | 0.527 | 0.498 | +0.0000 | 0.031 | 0.00 | -9.9 |
| derivatives|h4|all | 2160 | 36 | 2160 | 0.568 | 0.55-0.59 | 0.568 | 0.502 | +0.0010 | 0.067 | 0.00 | +59.9 |
| derivatives|h4|on_time | 2160 | 36 | 2160 | 0.568 | 0.55-0.59 | 0.568 | 0.502 | +0.0010 | 0.067 | 0.00 | +59.9 |
| lgbm_calibrated|h1|all | 2640 | 44 | 2640 | 0.535 | 0.52-0.55 | 0.525 | 0.473 | +0.0002 | 0.052 | 0.15 | +3.3 |
| lgbm_calibrated|h1|on_time | 2580 | 43 | 2580 | 0.540 | 0.52-0.56 | 0.522 | 0.473 | +0.0011 | 0.049 | 0.15 | +3.3 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 2460 | 41 | 2460 | 0.429 | 0.41-0.45 | 0.571 | 0.460 | -0.0276 | 0.112 | 0.20 | -50.2 |
| lgbm_calibrated|h4|on_time | 2460 | 41 | 2460 | 0.429 | 0.41-0.45 | 0.571 | 0.460 | -0.0276 | 0.112 | 0.20 | -50.2 |
| logistic|h1|all | 2640 | 44 | 2640 | 0.534 | 0.52-0.55 | 0.525 | 0.490 | +0.0065 | 0.036 | 0.09 | -10.9 |
| logistic|h1|on_time | 2580 | 43 | 2580 | 0.528 | 0.51-0.55 | 0.522 | 0.489 | +0.0053 | 0.034 | 0.09 | -10.7 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 2460 | 41 | 2460 | 0.524 | 0.50-0.54 | 0.571 | 0.496 | -0.0007 | 0.074 | 0.19 | -9.3 |
| logistic|h4|on_time | 2460 | 41 | 2460 | 0.524 | 0.50-0.54 | 0.571 | 0.496 | -0.0007 | 0.074 | 0.19 | -9.3 |
| momentum_24|h1|all | 2640 | 44 | 2640 | 0.523 | 0.50-0.54 | 0.525 | 0.496 | +0.0015 | 0.029 | 0.00 | - |
| momentum_24|h1|on_time | 2580 | 43 | 2580 | 0.519 | 0.50-0.54 | 0.522 | 0.496 | +0.0012 | 0.026 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 2460 | 41 | 2460 | 0.571 | 0.55-0.59 | 0.571 | 0.503 | -0.0000 | 0.067 | 0.00 | - |
| momentum_24|h4|on_time | 2460 | 41 | 2460 | 0.571 | 0.55-0.59 | 0.571 | 0.503 | -0.0000 | 0.067 | 0.00 | - |
| orthosys|h1|all | 2640 | 44 | 193 | 0.534 | 0.46-0.60 | 0.525 | 0.499 | +0.0008 | 0.028 | 0.00 | - |
| orthosys|h1|on_time | 2580 | 43 | 192 | 0.531 | 0.46-0.60 | 0.522 | 0.499 | +0.0007 | 0.024 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 2460 | 41 | 188 | 0.436 | 0.37-0.51 | 0.571 | 0.499 | -0.0020 | 0.072 | 0.00 | - |
| orthosys|h4|on_time | 2460 | 41 | 188 | 0.436 | 0.37-0.51 | 0.571 | 0.499 | -0.0020 | 0.072 | 0.00 | - |
| recent_base_rate_7d|h1|all | 2580 | 43 | 2580 | 0.478 | 0.46-0.50 | 0.522 | 0.474 | -0.0069 | 0.048 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 2580 | 43 | 2580 | 0.478 | 0.46-0.50 | 0.522 | 0.474 | -0.0069 | 0.048 | 0.00 | - |
| recent_base_rate_7d|h4|all | 2400 | 40 | 2400 | 0.422 | 0.40-0.44 | 0.578 | 0.442 | -0.0558 | 0.136 | 0.88 | -68.7 |
| recent_base_rate_7d|h4|on_time | 2400 | 40 | 2400 | 0.422 | 0.40-0.44 | 0.578 | 0.442 | -0.0558 | 0.136 | 0.88 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 955.17 | -4.48% | 1224 | 483 | 39 |
| analog_k100|h4 | 971.93 | -2.81% | 1377 | 550 | 36 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 44 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 41 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 39 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 36 |
| derivatives|h1 | 996.81 | -0.32% | 3 | 2 | 39 |
| derivatives|h4 | 1013.33 | +1.33% | 9 | 4 | 36 |
| lgbm_calibrated|h1 | 949.71 | -5.03% | 392 | 187 | 44 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 41 |
| logistic|h1 | 908.64 | -9.14% | 245 | 133 | 44 |
| logistic|h4 | 1011.97 | +1.20% | 479 | 235 | 41 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 44 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 41 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 44 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 41 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 43 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 40 |
| benchmark_long_all_coins|h1 | 1016.38 | +1.64% | 2640 | 1243 | 44 |
| benchmark_long_all_coins|h4 | 1044.87 | +4.49% | 2460 | 1327 | 41 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 39 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 36 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 40 |

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
