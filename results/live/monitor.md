# Live monitor (2026-10-22T00:07:35.708629+00:00)

## Alerts

- MISCALIBRATED: analog_k100|h4|all says 0.45 on average, reality 0.56 (ECE 0.126)
- WORSE THAN COIN FLIP: analog_k100|h4|all hit-rate CI upper bound 0.472
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.57 (ECE 0.104)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.452
- WORSE THAN COIN FLIP: orthosys|h4|all hit-rate CI upper bound 0.491
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.45 on average, reality 0.57 (ECE 0.122)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.447

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['COMP', 'HBAR']
- **last_closed_bar**: 2026-10-21 23:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.7
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 101.5 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.14, 'recent_base_rate_7d': 0.091, 'momentum_24': 0.158, 'logistic': 0.173, 'lgbm_calibrated': 0.133, 'analog_k100': 0.015, 'derivatives': 0.143, 'orthosys': 0.145}
- **council_member_logloss_h1**: {'base_rate': 0.6933, 'recent_base_rate_7d': 0.696, 'momentum_24': 0.6926, 'logistic': 0.692, 'lgbm_calibrated': 0.6936, 'analog_k100': 0.7082, 'derivatives': 0.6934, 'orthosys': 0.6931}
- **council_calls_h1**: 1
- **council_abstain_h1**: {'no_edge': 52, 'extreme_volatility': 7, 'spoke': 1}
- **council_weights_h4**: {'base_rate': 0.229, 'recent_base_rate_7d': 0.004, 'momentum_24': 0.227, 'logistic': 0.087, 'lgbm_calibrated': 0.028, 'analog_k100': 0.001, 'derivatives': 0.232, 'orthosys': 0.192}
- **council_member_logloss_h4**: {'base_rate': 0.6923, 'recent_base_rate_7d': 0.719, 'momentum_24': 0.6924, 'logistic': 0.6985, 'lgbm_calibrated': 0.7058, 'analog_k100': 0.7336, 'derivatives': 0.692, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 53, 'extreme_volatility': 7}
- **prediction_latency_min**: 7.5
- **price_snapshot_age_s**: 0.6
- **train_rows_h1**: 92483
- **orthosys_hist_hit_h1**: 0.5305
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0088
- **p_spread_logistic_h1**: 0.0462
- **p_spread_lgbm_calibrated_h1**: 0.0166
- **p_spread_analog_k100_h1**: 0.0604
- **p_spread_derivatives_h1**: 0.0246
- **p_spread_orthosys_h1**: 0.0092
- **p_spread_council_h1**: 0.0036
- **train_rows_h4**: 92297
- **orthosys_hist_hit_h4**: 0.5111
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0003
- **p_spread_logistic_h4**: 0.0749
- **p_spread_lgbm_calibrated_h4**: 0.0104
- **p_spread_analog_k100_h4**: 0.0989
- **p_spread_derivatives_h4**: 0.0538
- **p_spread_orthosys_h4**: 0.0034
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 59640

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 3060 | 51 | 3060 | 0.494 | 0.48-0.51 | 0.506 | 0.466 | -0.0258 | 0.062 | 0.51 | -15.0 |
| analog_k100|h1|on_time | 3060 | 51 | 3060 | 0.494 | 0.48-0.51 | 0.506 | 0.466 | -0.0258 | 0.062 | 0.51 | -15.0 |
| analog_k100|h4|all | 2880 | 48 | 2880 | 0.454 | 0.44-0.47 | 0.562 | 0.446 | -0.0754 | 0.126 | 0.64 | -25.4 |
| analog_k100|h4|on_time | 2880 | 48 | 2880 | 0.454 | 0.44-0.47 | 0.562 | 0.446 | -0.0754 | 0.126 | 0.64 | -25.4 |
| base_rate|h1|all | 3360 | 56 | 3360 | 0.494 | 0.48-0.51 | 0.506 | 0.498 | +0.0000 | 0.008 | 0.00 | - |
| base_rate|h1|on_time | 3300 | 55 | 3300 | 0.497 | 0.48-0.51 | 0.503 | 0.498 | +0.0000 | 0.005 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 3180 | 53 | 3180 | 0.565 | 0.55-0.58 | 0.565 | 0.504 | +0.0000 | 0.061 | 0.00 | - |
| base_rate|h4|on_time | 3180 | 53 | 3180 | 0.565 | 0.55-0.58 | 0.565 | 0.504 | +0.0000 | 0.061 | 0.00 | - |
| council|h1|all | 3060 | 51 | 486 | 0.510 | 0.47-0.55 | 0.506 | 0.496 | +0.0004 | 0.010 | 0.00 | +18.3 |
| council|h1|on_time | 3060 | 51 | 486 | 0.510 | 0.47-0.55 | 0.506 | 0.496 | +0.0004 | 0.010 | 0.00 | +18.3 |
| council|h4|all | 2880 | 48 | 25 | 0.600 | 0.41-0.77 | 0.562 | 0.500 | -0.0011 | 0.063 | 0.00 | - |
| council|h4|on_time | 2880 | 48 | 25 | 0.600 | 0.41-0.77 | 0.562 | 0.500 | -0.0011 | 0.063 | 0.00 | - |
| derivatives|h1|all | 3060 | 51 | 3060 | 0.494 | 0.48-0.51 | 0.506 | 0.497 | +0.0002 | 0.009 | 0.01 | -62.4 |
| derivatives|h1|on_time | 3060 | 51 | 3060 | 0.494 | 0.48-0.51 | 0.506 | 0.497 | +0.0002 | 0.009 | 0.01 | -62.4 |
| derivatives|h4|all | 2880 | 48 | 2880 | 0.570 | 0.55-0.59 | 0.562 | 0.501 | +0.0013 | 0.064 | 0.01 | +430.9 |
| derivatives|h4|on_time | 2880 | 48 | 2880 | 0.570 | 0.55-0.59 | 0.562 | 0.501 | +0.0013 | 0.064 | 0.01 | +430.9 |
| lgbm_calibrated|h1|all | 3360 | 56 | 3359 | 0.539 | 0.52-0.56 | 0.506 | 0.474 | -0.0011 | 0.032 | 0.16 | -2.6 |
| lgbm_calibrated|h1|on_time | 3300 | 55 | 3299 | 0.542 | 0.52-0.56 | 0.503 | 0.474 | -0.0005 | 0.030 | 0.16 | -2.6 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 3180 | 53 | 3180 | 0.435 | 0.42-0.45 | 0.565 | 0.462 | -0.0244 | 0.104 | 0.16 | -48.0 |
| lgbm_calibrated|h4|on_time | 3180 | 53 | 3180 | 0.435 | 0.42-0.45 | 0.565 | 0.462 | -0.0244 | 0.104 | 0.16 | -48.0 |
| logistic|h1|all | 3360 | 56 | 3360 | 0.520 | 0.50-0.54 | 0.506 | 0.490 | +0.0004 | 0.017 | 0.11 | -23.2 |
| logistic|h1|on_time | 3300 | 55 | 3300 | 0.515 | 0.50-0.53 | 0.503 | 0.490 | -0.0006 | 0.015 | 0.11 | -23.2 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 3180 | 53 | 3180 | 0.512 | 0.49-0.53 | 0.565 | 0.493 | -0.0105 | 0.079 | 0.23 | -22.1 |
| logistic|h4|on_time | 3180 | 53 | 3180 | 0.512 | 0.49-0.53 | 0.565 | 0.493 | -0.0105 | 0.079 | 0.23 | -22.1 |
| momentum_24|h1|all | 3360 | 56 | 3360 | 0.525 | 0.51-0.54 | 0.506 | 0.496 | +0.0016 | 0.015 | 0.00 | - |
| momentum_24|h1|on_time | 3300 | 55 | 3300 | 0.522 | 0.51-0.54 | 0.503 | 0.495 | +0.0013 | 0.012 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 3180 | 53 | 3180 | 0.565 | 0.55-0.58 | 0.565 | 0.504 | -0.0001 | 0.061 | 0.00 | - |
| momentum_24|h4|on_time | 3180 | 53 | 3180 | 0.565 | 0.55-0.58 | 0.565 | 0.504 | -0.0001 | 0.061 | 0.00 | - |
| orthosys|h1|all | 3360 | 56 | 239 | 0.519 | 0.46-0.58 | 0.506 | 0.499 | +0.0002 | 0.010 | 0.00 | - |
| orthosys|h1|on_time | 3300 | 55 | 238 | 0.517 | 0.45-0.58 | 0.503 | 0.499 | +0.0001 | 0.007 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 3180 | 53 | 230 | 0.426 | 0.36-0.49 | 0.565 | 0.499 | -0.0019 | 0.066 | 0.00 | - |
| orthosys|h4|on_time | 3180 | 53 | 230 | 0.426 | 0.36-0.49 | 0.565 | 0.499 | -0.0019 | 0.066 | 0.00 | - |
| recent_base_rate_7d|h1|all | 3300 | 55 | 3300 | 0.497 | 0.48-0.51 | 0.503 | 0.476 | -0.0046 | 0.027 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 3300 | 55 | 3300 | 0.497 | 0.48-0.51 | 0.503 | 0.476 | -0.0046 | 0.027 | 0.00 | - |
| recent_base_rate_7d|h4|all | 3120 | 52 | 3120 | 0.430 | 0.41-0.45 | 0.570 | 0.448 | -0.0507 | 0.122 | 0.67 | -68.7 |
| recent_base_rate_7d|h4|on_time | 3120 | 52 | 3120 | 0.430 | 0.41-0.45 | 0.570 | 0.448 | -0.0507 | 0.122 | 0.67 | -68.7 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 930.20 | -6.98% | 1549 | 613 | 51 |
| analog_k100|h4 | 975.50 | -2.45% | 1850 | 748 | 48 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 56 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 53 |
| council|h1 | 1001.32 | +0.13% | 5 | 2 | 51 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 48 |
| derivatives|h1 | 1048.09 | +4.81% | 21 | 7 | 51 |
| derivatives|h4 | 1125.71 | +12.57% | 39 | 21 | 48 |
| lgbm_calibrated|h1 | 907.27 | -9.27% | 528 | 246 | 56 |
| lgbm_calibrated|h4 | 916.34 | -8.37% | 523 | 218 | 53 |
| logistic|h1 | 837.88 | -16.21% | 361 | 175 | 56 |
| logistic|h4 | 991.95 | -0.80% | 741 | 348 | 53 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 56 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 53 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 56 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 53 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 55 |
| recent_base_rate_7d|h4 | 941.49 | -5.85% | 2100 | 789 | 52 |
| benchmark_long_all_coins|h1 | 996.59 | -0.34% | 3360 | 1550 | 56 |
| benchmark_long_all_coins|h4 | 1041.92 | +4.19% | 3180 | 1711 | 53 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 51 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 48 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 56 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 53 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 55 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 52 |

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
