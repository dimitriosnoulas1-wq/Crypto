# Live monitor (2026-10-20T20:06:09.133304+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.495
- MISCALIBRATED: lgbm_calibrated|h4|all says 0.46 on average, reality 0.56 (ECE 0.102)
- WORSE THAN COIN FLIP: lgbm_calibrated|h4|all hit-rate CI upper bound 0.468
- MISCALIBRATED: recent_base_rate_7d|h4|all says 0.44 on average, reality 0.57 (ECE 0.130)
- WORSE THAN COIN FLIP: recent_base_rate_7d|h4|all hit-rate CI upper bound 0.458

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['A', 'WLFI']
- **last_closed_bar**: 2026-10-20 19:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.1
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 107.8 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.122, 'recent_base_rate_7d': 0.093, 'momentum_24': 0.145, 'logistic': 0.163, 'lgbm_calibrated': 0.157, 'analog_k100': 0.067, 'derivatives': 0.125, 'orthosys': 0.129}
- **council_member_logloss_h1**: {'base_rate': 0.6935, 'recent_base_rate_7d': 0.697, 'momentum_24': 0.6914, 'logistic': 0.6899, 'lgbm_calibrated': 0.6904, 'analog_k100': 0.703, 'derivatives': 0.6936, 'orthosys': 0.6928}
- **council_calls_h1**: 9
- **council_abstain_h1**: {'no_edge': 48, 'spoke': 9, 'extreme_volatility': 3}
- **council_weights_h4**: {'base_rate': 0.156, 'recent_base_rate_7d': 0.022, 'momentum_24': 0.158, 'logistic': 0.251, 'lgbm_calibrated': 0.088, 'analog_k100': 0.016, 'derivatives': 0.151, 'orthosys': 0.158}
- **council_member_logloss_h4**: {'base_rate': 0.6929, 'recent_base_rate_7d': 0.7214, 'momentum_24': 0.6928, 'logistic': 0.6863, 'lgbm_calibrated': 0.7009, 'analog_k100': 0.7321, 'derivatives': 0.6932, 'orthosys': 0.6928}
- **council_calls_h4**: 1
- **council_abstain_h4**: {'no_edge': 47, 'members_disagree': 9, 'extreme_volatility': 3, 'spoke': 1}
- **prediction_latency_min**: 6.1
- **price_snapshot_age_s**: 0.3
- **train_rows_h1**: 90902
- **orthosys_hist_hit_h1**: 0.5251
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0057
- **p_spread_logistic_h1**: 0.0222
- **p_spread_lgbm_calibrated_h1**: 0.0196
- **p_spread_analog_k100_h1**: 0.056
- **p_spread_derivatives_h1**: 0.001
- **p_spread_orthosys_h1**: 0.0
- **p_spread_council_h1**: 0.0089
- **train_rows_h4**: 90716
- **orthosys_hist_hit_h4**: 0.5146
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0004
- **p_spread_logistic_h4**: 0.0516
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0717
- **p_spread_derivatives_h4**: 0.0034
- **p_spread_orthosys_h4**: 0.0
- **p_spread_council_h4**: 0.0029
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 29400

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1380 | 23 | 1380 | 0.503 | 0.48-0.53 | 0.533 | 0.471 | -0.0183 | 0.067 | 0.50 | -10.8 |
| analog_k100|h1|on_time | 1380 | 23 | 1380 | 0.503 | 0.48-0.53 | 0.533 | 0.471 | -0.0183 | 0.067 | 0.50 | -10.8 |
| analog_k100|h4|all | 1200 | 20 | 1200 | 0.458 | 0.43-0.49 | 0.548 | 0.446 | -0.0748 | 0.121 | 0.63 | -56.4 |
| analog_k100|h4|on_time | 1200 | 20 | 1200 | 0.458 | 0.43-0.49 | 0.548 | 0.446 | -0.0748 | 0.121 | 0.63 | -56.4 |
| base_rate|h1|all | 1680 | 28 | 1680 | 0.471 | 0.45-0.50 | 0.529 | 0.498 | +0.0000 | 0.030 | 0.00 | - |
| base_rate|h1|on_time | 1620 | 27 | 1620 | 0.476 | 0.45-0.50 | 0.524 | 0.498 | +0.0000 | 0.026 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 1500 | 25 | 1500 | 0.557 | 0.53-0.58 | 0.557 | 0.503 | +0.0000 | 0.054 | 0.00 | - |
| base_rate|h4|on_time | 1500 | 25 | 1500 | 0.557 | 0.53-0.58 | 0.557 | 0.503 | +0.0000 | 0.054 | 0.00 | - |
| council|h1|all | 1380 | 23 | 245 | 0.539 | 0.48-0.60 | 0.533 | 0.495 | +0.0026 | 0.043 | 0.00 | +64.4 |
| council|h1|on_time | 1380 | 23 | 245 | 0.539 | 0.48-0.60 | 0.533 | 0.495 | +0.0026 | 0.043 | 0.00 | +64.4 |
| council|h4|all | 1200 | 20 | 18 | 0.556 | 0.34-0.75 | 0.548 | 0.500 | -0.0001 | 0.050 | 0.00 | - |
| council|h4|on_time | 1200 | 20 | 18 | 0.556 | 0.34-0.75 | 0.548 | 0.500 | -0.0001 | 0.050 | 0.00 | - |
| derivatives|h1|all | 1380 | 23 | 1380 | 0.464 | 0.44-0.49 | 0.533 | 0.498 | -0.0001 | 0.038 | 0.00 | - |
| derivatives|h1|on_time | 1380 | 23 | 1380 | 0.464 | 0.44-0.49 | 0.533 | 0.498 | -0.0001 | 0.038 | 0.00 | - |
| derivatives|h4|all | 1200 | 20 | 1200 | 0.547 | 0.52-0.57 | 0.548 | 0.502 | -0.0001 | 0.046 | 0.00 | -117.6 |
| derivatives|h4|on_time | 1200 | 20 | 1200 | 0.547 | 0.52-0.57 | 0.548 | 0.502 | -0.0001 | 0.046 | 0.00 | -117.6 |
| lgbm_calibrated|h1|all | 1680 | 28 | 1680 | 0.560 | 0.54-0.58 | 0.529 | 0.478 | +0.0055 | 0.055 | 0.09 | +33.6 |
| lgbm_calibrated|h1|on_time | 1620 | 27 | 1620 | 0.568 | 0.54-0.59 | 0.524 | 0.478 | +0.0071 | 0.051 | 0.09 | +33.6 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 1500 | 25 | 1500 | 0.443 | 0.42-0.47 | 0.557 | 0.458 | -0.0185 | 0.102 | 0.18 | -9.1 |
| lgbm_calibrated|h4|on_time | 1500 | 25 | 1500 | 0.443 | 0.42-0.47 | 0.557 | 0.458 | -0.0185 | 0.102 | 0.18 | -9.1 |
| logistic|h1|all | 1680 | 28 | 1680 | 0.535 | 0.51-0.56 | 0.529 | 0.491 | +0.0070 | 0.042 | 0.12 | -9.5 |
| logistic|h1|on_time | 1620 | 27 | 1620 | 0.526 | 0.50-0.55 | 0.524 | 0.490 | +0.0051 | 0.039 | 0.12 | -9.3 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 1500 | 25 | 1500 | 0.543 | 0.52-0.57 | 0.557 | 0.494 | +0.0101 | 0.063 | 0.18 | +32.8 |
| logistic|h4|on_time | 1500 | 25 | 1500 | 0.543 | 0.52-0.57 | 0.557 | 0.494 | +0.0101 | 0.063 | 0.18 | +32.8 |
| momentum_24|h1|all | 1680 | 28 | 1680 | 0.554 | 0.53-0.58 | 0.529 | 0.498 | +0.0039 | 0.043 | 0.00 | - |
| momentum_24|h1|on_time | 1620 | 27 | 1620 | 0.548 | 0.52-0.57 | 0.524 | 0.498 | +0.0035 | 0.038 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 1500 | 25 | 1500 | 0.557 | 0.53-0.58 | 0.557 | 0.503 | +0.0002 | 0.054 | 0.00 | - |
| momentum_24|h4|on_time | 1500 | 25 | 1500 | 0.557 | 0.53-0.58 | 0.557 | 0.503 | +0.0002 | 0.054 | 0.00 | - |
| orthosys|h1|all | 1680 | 28 | 173 | 0.543 | 0.47-0.62 | 0.529 | 0.498 | +0.0012 | 0.033 | 0.00 | - |
| orthosys|h1|on_time | 1620 | 27 | 172 | 0.541 | 0.47-0.61 | 0.524 | 0.498 | +0.0011 | 0.028 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 1500 | 25 | 105 | 0.543 | 0.45-0.63 | 0.557 | 0.499 | -0.0002 | 0.061 | 0.00 | - |
| orthosys|h4|on_time | 1500 | 25 | 105 | 0.543 | 0.45-0.63 | 0.557 | 0.499 | -0.0002 | 0.061 | 0.00 | - |
| recent_base_rate_7d|h1|all | 1620 | 27 | 1620 | 0.476 | 0.45-0.50 | 0.524 | 0.473 | -0.0074 | 0.052 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 1620 | 27 | 1620 | 0.476 | 0.45-0.50 | 0.524 | 0.473 | -0.0074 | 0.052 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1440 | 24 | 1440 | 0.433 | 0.41-0.46 | 0.567 | 0.438 | -0.0574 | 0.130 | 1.00 | -67.9 |
| recent_base_rate_7d|h4|on_time | 1440 | 24 | 1440 | 0.433 | 0.41-0.46 | 0.567 | 0.438 | -0.0574 | 0.130 | 1.00 | -67.9 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 971.43 | -2.86% | 688 | 271 | 23 |
| analog_k100|h4 | 974.55 | -2.55% | 756 | 311 | 20 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 28 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 25 |
| council|h1 | 1006.44 | +0.64% | 3 | 2 | 23 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 20 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 23 |
| derivatives|h4 | 985.33 | -1.47% | 5 | 1 | 20 |
| lgbm_calibrated|h1 | 951.51 | -4.85% | 150 | 81 | 28 |
| lgbm_calibrated|h4 | 925.72 | -7.43% | 277 | 155 | 25 |
| logistic|h1 | 940.54 | -5.95% | 200 | 102 | 28 |
| logistic|h4 | 1037.06 | +3.71% | 265 | 149 | 25 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 28 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 25 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 28 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 25 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 27 |
| recent_base_rate_7d|h4 | 959.92 | -4.01% | 1440 | 577 | 24 |
| benchmark_long_all_coins|h1 | 1005.23 | +0.52% | 1680 | 793 | 28 |
| benchmark_long_all_coins|h4 | 1027.67 | +2.77% | 1500 | 770 | 25 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 20 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 20 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 20 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 28 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 27 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 24 |

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
