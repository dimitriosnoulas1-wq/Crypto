# Live monitor (2026-10-21T19:07:38.238657+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.59 (ECE 0.149)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.456
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.494
- MISCALIBRATED: base_rate|h4|all says 0.50 on average, reality 0.59 (ECE 0.088)
- MISCALIBRATED: council|h4|all says 0.50 on average, reality 0.59 (ECE 0.093)
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.493
- MISCALIBRATED: derivatives|h4|all says 0.50 on average, reality 0.59 (ECE 0.091)
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.59 (ECE 0.132)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.426
- MISCALIBRATED: logistic|h4|all says 0.49 on average, reality 0.59 (ECE 0.100)
- MISCALIBRATED: momentum_24|h4|all says 0.50 on average, reality 0.59 (ECE 0.089)
- MISCALIBRATED: orthosys|h4|all says 0.50 on average, reality 0.59 (ECE 0.093)
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.495
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.496
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.60 (ECE 0.154)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.420

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['AERO', 'HBAR']
- **last_closed_bar**: 2026-10-21 18:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.6
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 106.3 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.146, 'recent_base_rate_7d': 0.087, 'momentum_24': 0.156, 'logistic': 0.18, 'lgbm_calibrated': 0.105, 'analog_k100': 0.017, 'derivatives': 0.153, 'orthosys': 0.155}
- **council_member_logloss_h1**: {'base_rate': 0.6935, 'recent_base_rate_7d': 0.697, 'momentum_24': 0.693, 'logistic': 0.6921, 'lgbm_calibrated': 0.6957, 'analog_k100': 0.7095, 'derivatives': 0.6933, 'orthosys': 0.693}
- **council_calls_h1**: 2
- **council_abstain_h1**: {'no_edge': 53, 'extreme_volatility': 5, 'spoke': 2}
- **council_weights_h4**: {'base_rate': 0.225, 'recent_base_rate_7d': 0.003, 'momentum_24': 0.225, 'logistic': 0.118, 'lgbm_calibrated': 0.025, 'analog_k100': 0.001, 'derivatives': 0.222, 'orthosys': 0.182}
- **council_member_logloss_h4**: {'base_rate': 0.692, 'recent_base_rate_7d': 0.7225, 'momentum_24': 0.692, 'logistic': 0.6966, 'lgbm_calibrated': 0.7076, 'analog_k100': 0.7385, 'derivatives': 0.6918, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 54, 'extreme_volatility': 5, 'members_disagree': 1}
- **prediction_latency_min**: 7.5
- **price_snapshot_age_s**: 0.8
- **train_rows_h1**: 92226
- **orthosys_hist_hit_h1**: 0.5305
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0061
- **p_spread_logistic_h1**: 0.0369
- **p_spread_lgbm_calibrated_h1**: 0.0107
- **p_spread_analog_k100_h1**: 0.0419
- **p_spread_derivatives_h1**: 0.0128
- **p_spread_orthosys_h1**: 0.0097
- **p_spread_council_h1**: 0.0038
- **train_rows_h4**: 92040
- **orthosys_hist_hit_h4**: 0.5116
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0008
- **p_spread_logistic_h4**: 0.0729
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0837
- **p_spread_derivatives_h4**: 0.049
- **p_spread_orthosys_h4**: 0.0037
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 54240

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 2760 | 46 | 2760 | 0.493 | 0.47-0.51 | 0.526 | 0.466 | -0.0304 | 0.066 | 0.51 | -15.4 |
| analog_k100|h1|on_time | 2760 | 46 | 2760 | 0.493 | 0.47-0.51 | 0.526 | 0.466 | -0.0304 | 0.066 | 0.51 | -15.4 |
| analog_k100|h4|all | 2580 | 43 | 2580 | 0.436 | 0.42-0.46 | 0.592 | 0.449 | -0.0916 | 0.149 | 0.63 | -34.3 |
| analog_k100|h4|on_time | 2580 | 43 | 2580 | 0.436 | 0.42-0.46 | 0.592 | 0.449 | -0.0916 | 0.149 | 0.63 | -34.3 |
| base_rate|h1|all | 3060 | 51 | 3060 | 0.476 | 0.46-0.49 | 0.524 | 0.498 | +0.0000 | 0.026 | 0.00 | - |
| base_rate|h1|on_time | 3000 | 50 | 3000 | 0.478 | 0.46-0.50 | 0.522 | 0.498 | +0.0000 | 0.024 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 2880 | 48 | 2880 | 0.592 | 0.57-0.61 | 0.592 | 0.504 | +0.0000 | 0.088 | 0.00 | - |
| base_rate|h4|on_time | 2880 | 48 | 2880 | 0.592 | 0.57-0.61 | 0.592 | 0.504 | +0.0000 | 0.088 | 0.00 | - |
| council|h1|all | 2760 | 46 | 478 | 0.510 | 0.47-0.56 | 0.526 | 0.495 | +0.0009 | 0.031 | 0.00 | +18.3 |
| council|h1|on_time | 2760 | 46 | 478 | 0.510 | 0.47-0.56 | 0.526 | 0.495 | +0.0009 | 0.031 | 0.00 | +18.3 |
| council|h4|all | 2580 | 43 | 24 | 0.583 | 0.39-0.76 | 0.592 | 0.500 | -0.0022 | 0.093 | 0.00 | - |
| council|h4|on_time | 2580 | 43 | 24 | 0.583 | 0.39-0.76 | 0.592 | 0.500 | -0.0022 | 0.093 | 0.00 | - |
| derivatives|h1|all | 2760 | 46 | 2760 | 0.474 | 0.46-0.49 | 0.526 | 0.497 | -0.0002 | 0.029 | 0.00 | -328.3 |
| derivatives|h1|on_time | 2760 | 46 | 2760 | 0.474 | 0.46-0.49 | 0.526 | 0.497 | -0.0002 | 0.029 | 0.00 | -328.3 |
| derivatives|h4|all | 2580 | 43 | 2580 | 0.596 | 0.58-0.61 | 0.592 | 0.502 | +0.0004 | 0.091 | 0.01 | +565.2 |
| derivatives|h4|on_time | 2580 | 43 | 2580 | 0.596 | 0.58-0.61 | 0.592 | 0.502 | +0.0004 | 0.091 | 0.01 | +565.2 |
| lgbm_calibrated|h1|all | 3060 | 51 | 3060 | 0.527 | 0.51-0.55 | 0.524 | 0.473 | -0.0028 | 0.051 | 0.17 | +1.0 |
| lgbm_calibrated|h1|on_time | 3000 | 50 | 3000 | 0.531 | 0.51-0.55 | 0.522 | 0.473 | -0.0021 | 0.049 | 0.17 | +1.0 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 2880 | 48 | 2880 | 0.408 | 0.39-0.43 | 0.592 | 0.462 | -0.0322 | 0.132 | 0.18 | -48.0 |
| lgbm_calibrated|h4|on_time | 2880 | 48 | 2880 | 0.408 | 0.39-0.43 | 0.592 | 0.462 | -0.0322 | 0.132 | 0.18 | -48.0 |
| logistic|h1|all | 3060 | 51 | 3060 | 0.525 | 0.51-0.54 | 0.524 | 0.489 | +0.0024 | 0.036 | 0.10 | -33.2 |
| logistic|h1|on_time | 3000 | 50 | 3000 | 0.520 | 0.50-0.54 | 0.522 | 0.489 | +0.0013 | 0.034 | 0.10 | -33.3 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 2880 | 48 | 2880 | 0.511 | 0.49-0.53 | 0.592 | 0.495 | -0.0107 | 0.100 | 0.21 | -29.5 |
| logistic|h4|on_time | 2880 | 48 | 2880 | 0.511 | 0.49-0.53 | 0.592 | 0.495 | -0.0107 | 0.100 | 0.21 | -29.5 |
| momentum_24|h1|all | 3060 | 51 | 3060 | 0.518 | 0.50-0.54 | 0.524 | 0.496 | +0.0011 | 0.028 | 0.00 | - |
| momentum_24|h1|on_time | 3000 | 50 | 3000 | 0.515 | 0.50-0.53 | 0.522 | 0.496 | +0.0009 | 0.026 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 2880 | 48 | 2880 | 0.592 | 0.57-0.61 | 0.592 | 0.503 | -0.0000 | 0.089 | 0.00 | - |
| momentum_24|h4|on_time | 2880 | 48 | 2880 | 0.592 | 0.57-0.61 | 0.592 | 0.503 | -0.0000 | 0.089 | 0.00 | - |
| orthosys|h1|all | 3060 | 51 | 221 | 0.529 | 0.46-0.59 | 0.524 | 0.499 | +0.0007 | 0.028 | 0.00 | - |
| orthosys|h1|on_time | 3000 | 50 | 220 | 0.527 | 0.46-0.59 | 0.522 | 0.499 | +0.0006 | 0.025 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 2880 | 48 | 206 | 0.427 | 0.36-0.50 | 0.592 | 0.499 | -0.0029 | 0.093 | 0.00 | - |
| orthosys|h4|on_time | 2880 | 48 | 206 | 0.427 | 0.36-0.50 | 0.592 | 0.499 | -0.0029 | 0.093 | 0.00 | - |
| recent_base_rate_7d|h1|all | 3000 | 50 | 3000 | 0.478 | 0.46-0.50 | 0.522 | 0.475 | -0.0065 | 0.046 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 3000 | 50 | 3000 | 0.478 | 0.46-0.50 | 0.522 | 0.475 | -0.0065 | 0.046 | 0.00 | - |
| recent_base_rate_7d|h4|all | 2820 | 47 | 2820 | 0.402 | 0.38-0.42 | 0.598 | 0.445 | -0.0600 | 0.154 | 0.74 | -68.7 |
| recent_base_rate_7d|h4|on_time | 2820 | 47 | 2820 | 0.402 | 0.38-0.42 | 0.598 | 0.445 | -0.0600 | 0.154 | 0.74 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 937.56 | -6.24% | 1418 | 552 | 46 |
| analog_k100|h4 | 969.79 | -3.02% | 1635 | 622 | 43 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 51 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 48 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 46 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 43 |
| derivatives|h1 | 835.78 | -16.42% | 12 | 4 | 46 |
| derivatives|h4 | 1102.61 | +10.26% | 23 | 12 | 43 |
| lgbm_calibrated|h1 | 929.90 | -7.01% | 511 | 242 | 51 |
| lgbm_calibrated|h4 | 916.34 | -8.37% | 523 | 218 | 48 |
| logistic|h1 | 824.31 | -17.57% | 313 | 157 | 51 |
| logistic|h4 | 986.58 | -1.34% | 614 | 285 | 48 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 51 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 48 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 51 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 48 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 50 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 47 |
| benchmark_long_all_coins|h1 | 1015.06 | +1.51% | 3060 | 1437 | 51 |
| benchmark_long_all_coins|h4 | 1052.85 | +5.29% | 2880 | 1623 | 48 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 43 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 50 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 47 |

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
