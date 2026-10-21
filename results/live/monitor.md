# Live monitor (2026-10-21T17:07:24.236344+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.59 (ECE 0.144)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.459
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.494
- MISCALIBRATED: base_rate|h4|all says 0.50 on average, reality 0.59 (ECE 0.085)
- MISCALIBRATED: council|h4|all says 0.50 on average, reality 0.59 (ECE 0.089)
- WORSE THAN COIN FLIP: derivatives|h1|all hit-rate CI upper bound 0.493
- MISCALIBRATED: derivatives|h4|all says 0.50 on average, reality 0.59 (ECE 0.086)
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.59 (ECE 0.128)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.430
- MISCALIBRATED: logistic|h4|all says 0.50 on average, reality 0.59 (ECE 0.094)
- MISCALIBRATED: momentum_24|h4|all says 0.50 on average, reality 0.59 (ECE 0.085)
- MISCALIBRATED: orthosys|h4|all says 0.50 on average, reality 0.59 (ECE 0.089)
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.489
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.497
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.59 (ECE 0.151)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.424

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['AERO', 'CHIP']
- **last_closed_bar**: 2026-10-21 16:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.4
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 102.5 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.146, 'recent_base_rate_7d': 0.087, 'momentum_24': 0.157, 'logistic': 0.173, 'lgbm_calibrated': 0.106, 'analog_k100': 0.021, 'derivatives': 0.154, 'orthosys': 0.155}
- **council_member_logloss_h1**: {'base_rate': 0.6935, 'recent_base_rate_7d': 0.6972, 'momentum_24': 0.693, 'logistic': 0.6923, 'lgbm_calibrated': 0.6957, 'analog_k100': 0.7087, 'derivatives': 0.6933, 'orthosys': 0.6931}
- **council_calls_h1**: 1
- **council_abstain_h1**: {'no_edge': 54, 'extreme_volatility': 5, 'spoke': 1}
- **council_weights_h4**: {'base_rate': 0.216, 'recent_base_rate_7d': 0.004, 'momentum_24': 0.216, 'logistic': 0.147, 'lgbm_calibrated': 0.03, 'analog_k100': 0.001, 'derivatives': 0.204, 'orthosys': 0.182}
- **council_member_logloss_h4**: {'base_rate': 0.6922, 'recent_base_rate_7d': 0.7218, 'momentum_24': 0.6922, 'logistic': 0.6951, 'lgbm_calibrated': 0.7069, 'analog_k100': 0.7358, 'derivatives': 0.6924, 'orthosys': 0.6935}
- **council_calls_h4**: 1
- **council_abstain_h4**: {'no_edge': 52, 'extreme_volatility': 5, 'members_disagree': 2, 'spoke': 1}
- **prediction_latency_min**: 7.3
- **price_snapshot_age_s**: 0.7
- **train_rows_h1**: 92102
- **orthosys_hist_hit_h1**: 0.5306
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0068
- **p_spread_logistic_h1**: 0.033
- **p_spread_lgbm_calibrated_h1**: 0.015
- **p_spread_analog_k100_h1**: 0.0502
- **p_spread_derivatives_h1**: 0.0112
- **p_spread_orthosys_h1**: 0.0067
- **p_spread_council_h1**: 0.0033
- **train_rows_h4**: 91916
- **orthosys_hist_hit_h4**: 0.5115
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0008
- **p_spread_logistic_h4**: 0.0736
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0927
- **p_spread_derivatives_h4**: 0.0456
- **p_spread_orthosys_h4**: 0.0025
- **p_spread_council_h4**: 0.0027
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 52080

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 2640 | 44 | 2640 | 0.499 | 0.48-0.52 | 0.526 | 0.466 | -0.0280 | 0.066 | 0.51 | -12.9 |
| analog_k100|h1|on_time | 2640 | 44 | 2640 | 0.499 | 0.48-0.52 | 0.526 | 0.466 | -0.0280 | 0.066 | 0.51 | -12.9 |
| analog_k100|h4|all | 2460 | 41 | 2460 | 0.439 | 0.42-0.46 | 0.588 | 0.450 | -0.0878 | 0.144 | 0.63 | -30.0 |
| analog_k100|h4|on_time | 2460 | 41 | 2460 | 0.439 | 0.42-0.46 | 0.588 | 0.450 | -0.0878 | 0.144 | 0.63 | -30.0 |
| base_rate|h1|all | 2940 | 49 | 2940 | 0.476 | 0.46-0.49 | 0.524 | 0.498 | +0.0000 | 0.026 | 0.00 | - |
| base_rate|h1|on_time | 2880 | 48 | 2880 | 0.478 | 0.46-0.50 | 0.522 | 0.498 | +0.0000 | 0.024 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 2760 | 46 | 2760 | 0.588 | 0.57-0.61 | 0.588 | 0.503 | +0.0000 | 0.085 | 0.00 | - |
| base_rate|h4|on_time | 2760 | 46 | 2760 | 0.588 | 0.57-0.61 | 0.588 | 0.503 | +0.0000 | 0.085 | 0.00 | - |
| council|h1|all | 2640 | 44 | 471 | 0.507 | 0.46-0.55 | 0.526 | 0.495 | +0.0008 | 0.031 | 0.00 | +18.3 |
| council|h1|on_time | 2640 | 44 | 471 | 0.507 | 0.46-0.55 | 0.526 | 0.495 | +0.0008 | 0.031 | 0.00 | +18.3 |
| council|h4|all | 2460 | 41 | 21 | 0.571 | 0.37-0.76 | 0.588 | 0.500 | -0.0020 | 0.089 | 0.00 | - |
| council|h4|on_time | 2460 | 41 | 21 | 0.571 | 0.37-0.76 | 0.588 | 0.500 | -0.0020 | 0.089 | 0.00 | - |
| derivatives|h1|all | 2640 | 44 | 2640 | 0.474 | 0.45-0.49 | 0.526 | 0.498 | +0.0004 | 0.029 | 0.00 | -139.9 |
| derivatives|h1|on_time | 2640 | 44 | 2640 | 0.474 | 0.45-0.49 | 0.526 | 0.498 | +0.0004 | 0.029 | 0.00 | -139.9 |
| derivatives|h4|all | 2460 | 41 | 2460 | 0.589 | 0.57-0.61 | 0.588 | 0.502 | -0.0002 | 0.086 | 0.01 | +161.5 |
| derivatives|h4|on_time | 2460 | 41 | 2460 | 0.589 | 0.57-0.61 | 0.588 | 0.502 | -0.0002 | 0.086 | 0.01 | +161.5 |
| lgbm_calibrated|h1|all | 2940 | 49 | 2940 | 0.530 | 0.51-0.55 | 0.524 | 0.473 | -0.0039 | 0.051 | 0.16 | -3.0 |
| lgbm_calibrated|h1|on_time | 2880 | 48 | 2880 | 0.533 | 0.52-0.55 | 0.522 | 0.473 | -0.0032 | 0.049 | 0.16 | -3.0 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 2760 | 46 | 2760 | 0.411 | 0.39-0.43 | 0.588 | 0.462 | -0.0305 | 0.128 | 0.18 | -50.2 |
| lgbm_calibrated|h4|on_time | 2760 | 46 | 2760 | 0.411 | 0.39-0.43 | 0.588 | 0.462 | -0.0305 | 0.128 | 0.18 | -50.2 |
| logistic|h1|all | 2940 | 49 | 2940 | 0.525 | 0.51-0.54 | 0.524 | 0.489 | +0.0024 | 0.036 | 0.10 | -31.9 |
| logistic|h1|on_time | 2880 | 48 | 2880 | 0.519 | 0.50-0.54 | 0.522 | 0.489 | +0.0013 | 0.034 | 0.10 | -32.0 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 2760 | 46 | 2760 | 0.517 | 0.50-0.54 | 0.588 | 0.496 | -0.0070 | 0.094 | 0.20 | -39.3 |
| logistic|h4|on_time | 2760 | 46 | 2760 | 0.517 | 0.50-0.54 | 0.588 | 0.496 | -0.0070 | 0.094 | 0.20 | -39.3 |
| momentum_24|h1|all | 2940 | 49 | 2940 | 0.519 | 0.50-0.54 | 0.524 | 0.496 | +0.0012 | 0.028 | 0.00 | - |
| momentum_24|h1|on_time | 2880 | 48 | 2880 | 0.516 | 0.50-0.53 | 0.522 | 0.496 | +0.0010 | 0.026 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 2760 | 46 | 2760 | 0.588 | 0.57-0.61 | 0.588 | 0.503 | -0.0000 | 0.085 | 0.00 | - |
| momentum_24|h4|on_time | 2760 | 46 | 2760 | 0.588 | 0.57-0.61 | 0.588 | 0.503 | -0.0000 | 0.085 | 0.00 | - |
| orthosys|h1|all | 2940 | 49 | 213 | 0.531 | 0.46-0.60 | 0.524 | 0.499 | +0.0007 | 0.028 | 0.00 | - |
| orthosys|h1|on_time | 2880 | 48 | 212 | 0.528 | 0.46-0.59 | 0.522 | 0.499 | +0.0006 | 0.025 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 2760 | 46 | 200 | 0.420 | 0.35-0.49 | 0.588 | 0.499 | -0.0028 | 0.089 | 0.00 | - |
| orthosys|h4|on_time | 2760 | 46 | 200 | 0.420 | 0.35-0.49 | 0.588 | 0.499 | -0.0028 | 0.089 | 0.00 | - |
| recent_base_rate_7d|h1|all | 2880 | 48 | 2880 | 0.478 | 0.46-0.50 | 0.522 | 0.475 | -0.0067 | 0.047 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 2880 | 48 | 2880 | 0.478 | 0.46-0.50 | 0.522 | 0.475 | -0.0067 | 0.047 | 0.00 | - |
| recent_base_rate_7d|h4|all | 2700 | 45 | 2700 | 0.405 | 0.39-0.42 | 0.595 | 0.444 | -0.0601 | 0.151 | 0.78 | -68.7 |
| recent_base_rate_7d|h4|on_time | 2700 | 45 | 2700 | 0.405 | 0.39-0.42 | 0.595 | 0.444 | -0.0601 | 0.151 | 0.78 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 952.42 | -4.76% | 1358 | 535 | 44 |
| analog_k100|h4 | 975.66 | -2.43% | 1551 | 594 | 41 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 49 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 46 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 44 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 41 |
| derivatives|h1 | 924.64 | -7.54% | 8 | 4 | 44 |
| derivatives|h4 | 1014.24 | +1.42% | 17 | 7 | 41 |
| lgbm_calibrated|h1 | 932.99 | -6.70% | 470 | 209 | 49 |
| lgbm_calibrated|h4 | 916.65 | -8.33% | 492 | 204 | 46 |
| logistic|h1 | 824.93 | -17.51% | 296 | 149 | 49 |
| logistic|h4 | 983.08 | -1.69% | 559 | 265 | 46 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 49 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 46 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 49 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 46 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 48 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 45 |
| benchmark_long_all_coins|h1 | 1014.32 | +1.43% | 2940 | 1380 | 49 |
| benchmark_long_all_coins|h4 | 1052.49 | +5.25% | 2760 | 1545 | 46 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 44 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 41 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 49 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 46 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 45 |

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
