# Live monitor (2026-10-20T18:07:46.721254+00:00)

## Alerts

- WORSE THAN COIN FLIP: base_rate|h1|all hit-rate CI upper bound 0.486
- WORSE THAN COIN FLIP: recent_base_rate_7d|h1|all hit-rate CI upper bound 0.491

## Health

- **venue**: okx
- **symbols**: 64
- **universe_size**: 60
- **fetched_only_for_scoring**: ['MUBARAK', 'PYTH', 'S', 'WLFI']
- **last_closed_bar**: 2026-10-20 17:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.6
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 112.9 instruments 64/64']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.122, 'recent_base_rate_7d': 0.091, 'momentum_24': 0.142, 'logistic': 0.167, 'lgbm_calibrated': 0.163, 'analog_k100': 0.063, 'derivatives': 0.125, 'orthosys': 0.126}
- **council_member_logloss_h1**: {'base_rate': 0.6935, 'recent_base_rate_7d': 0.6978, 'momentum_24': 0.6916, 'logistic': 0.6894, 'lgbm_calibrated': 0.6897, 'analog_k100': 0.705, 'derivatives': 0.6937, 'orthosys': 0.6932}
- **council_calls_h1**: 13
- **council_abstain_h1**: {'no_edge': 45, 'spoke': 13, 'extreme_volatility': 2}
- **council_weights_h4**: {'base_rate': 0.159, 'recent_base_rate_7d': 0.024, 'momentum_24': 0.16, 'logistic': 0.252, 'lgbm_calibrated': 0.077, 'analog_k100': 0.017, 'derivatives': 0.152, 'orthosys': 0.158}
- **council_member_logloss_h4**: {'base_rate': 0.6929, 'recent_base_rate_7d': 0.7226, 'momentum_24': 0.6928, 'logistic': 0.686, 'lgbm_calibrated': 0.7038, 'analog_k100': 0.7361, 'derivatives': 0.6933, 'orthosys': 0.693}
- **council_calls_h4**: 1
- **council_abstain_h4**: {'no_edge': 37, 'members_disagree': 20, 'extreme_volatility': 2, 'spoke': 1}
- **prediction_latency_min**: 7.7
- **price_snapshot_age_s**: 0.4
- **train_rows_h1**: 93802
- **orthosys_hist_hit_h1**: 0.5252
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0079
- **p_spread_logistic_h1**: 0.029
- **p_spread_lgbm_calibrated_h1**: 0.0084
- **p_spread_analog_k100_h1**: 0.0521
- **p_spread_derivatives_h1**: 0.0012
- **p_spread_orthosys_h1**: 0.0135
- **p_spread_council_h1**: 0.0103
- **train_rows_h4**: 93610
- **orthosys_hist_hit_h4**: 0.5143
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0011
- **p_spread_logistic_h4**: 0.0559
- **p_spread_lgbm_calibrated_h4**: 0.0052
- **p_spread_analog_k100_h4**: 0.0702
- **p_spread_derivatives_h4**: 0.0045
- **p_spread_orthosys_h4**: 0.0076
- **p_spread_council_h4**: 0.0029
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 27240

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 1260 | 21 | 1260 | 0.489 | 0.46-0.52 | 0.546 | 0.472 | -0.0245 | 0.078 | 0.49 | -12.5 |
| analog_k100|h1|on_time | 1260 | 21 | 1260 | 0.489 | 0.46-0.52 | 0.546 | 0.472 | -0.0245 | 0.078 | 0.49 | -12.5 |
| analog_k100|h4|all | 1080 | 18 | 1080 | 0.445 | 0.42-0.48 | 0.563 | 0.447 | -0.0858 | 0.133 | 0.62 | -73.0 |
| analog_k100|h4|on_time | 1080 | 18 | 1080 | 0.445 | 0.42-0.48 | 0.563 | 0.447 | -0.0858 | 0.133 | 0.62 | -73.0 |
| base_rate|h1|all | 1560 | 26 | 1560 | 0.462 | 0.44-0.49 | 0.538 | 0.498 | +0.0000 | 0.040 | 0.00 | - |
| base_rate|h1|on_time | 1500 | 25 | 1500 | 0.466 | 0.44-0.49 | 0.534 | 0.498 | +0.0000 | 0.036 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 1380 | 23 | 1380 | 0.569 | 0.54-0.59 | 0.569 | 0.503 | +0.0000 | 0.066 | 0.00 | - |
| base_rate|h4|on_time | 1380 | 23 | 1380 | 0.569 | 0.54-0.59 | 0.569 | 0.503 | +0.0000 | 0.066 | 0.00 | - |
| council|h1|all | 1260 | 21 | 230 | 0.517 | 0.45-0.58 | 0.546 | 0.495 | +0.0022 | 0.051 | 0.00 | +64.4 |
| council|h1|on_time | 1260 | 21 | 230 | 0.517 | 0.45-0.58 | 0.546 | 0.495 | +0.0022 | 0.051 | 0.00 | +64.4 |
| council|h4|all | 1080 | 18 | 18 | 0.556 | 0.34-0.75 | 0.563 | 0.500 | -0.0003 | 0.064 | 0.00 | - |
| council|h4|on_time | 1080 | 18 | 18 | 0.556 | 0.34-0.75 | 0.563 | 0.500 | -0.0003 | 0.064 | 0.00 | - |
| derivatives|h1|all | 1260 | 21 | 1260 | 0.451 | 0.42-0.48 | 0.546 | 0.498 | -0.0001 | 0.051 | 0.00 | - |
| derivatives|h1|on_time | 1260 | 21 | 1260 | 0.451 | 0.42-0.48 | 0.546 | 0.498 | -0.0001 | 0.051 | 0.00 | - |
| derivatives|h4|all | 1080 | 18 | 1080 | 0.559 | 0.53-0.59 | 0.563 | 0.502 | -0.0004 | 0.061 | 0.00 | -117.6 |
| derivatives|h4|on_time | 1080 | 18 | 1080 | 0.559 | 0.53-0.59 | 0.563 | 0.502 | -0.0004 | 0.061 | 0.00 | -117.6 |
| lgbm_calibrated|h1|all | 1560 | 26 | 1560 | 0.557 | 0.53-0.58 | 0.538 | 0.478 | +0.0042 | 0.066 | 0.10 | +33.6 |
| lgbm_calibrated|h1|on_time | 1500 | 25 | 1500 | 0.565 | 0.54-0.59 | 0.534 | 0.478 | +0.0059 | 0.061 | 0.10 | +33.6 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 1380 | 23 | 1380 | 0.430 | 0.40-0.46 | 0.569 | 0.462 | -0.0265 | 0.108 | 0.14 | -17.9 |
| lgbm_calibrated|h4|on_time | 1380 | 23 | 1380 | 0.430 | 0.40-0.46 | 0.569 | 0.462 | -0.0265 | 0.108 | 0.14 | -17.9 |
| logistic|h1|all | 1560 | 26 | 1560 | 0.525 | 0.50-0.55 | 0.538 | 0.490 | +0.0064 | 0.053 | 0.12 | -6.3 |
| logistic|h1|on_time | 1500 | 25 | 1500 | 0.515 | 0.49-0.54 | 0.534 | 0.489 | +0.0043 | 0.050 | 0.12 | -6.0 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 1380 | 23 | 1380 | 0.543 | 0.52-0.57 | 0.569 | 0.498 | +0.0085 | 0.071 | 0.14 | +48.8 |
| logistic|h4|on_time | 1380 | 23 | 1380 | 0.543 | 0.52-0.57 | 0.569 | 0.498 | +0.0085 | 0.071 | 0.14 | +48.8 |
| momentum_24|h1|all | 1560 | 26 | 1560 | 0.547 | 0.52-0.57 | 0.538 | 0.498 | +0.0034 | 0.040 | 0.00 | - |
| momentum_24|h1|on_time | 1500 | 25 | 1500 | 0.541 | 0.52-0.57 | 0.534 | 0.498 | +0.0029 | 0.036 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 1380 | 23 | 1380 | 0.569 | 0.54-0.59 | 0.569 | 0.503 | +0.0002 | 0.066 | 0.00 | - |
| momentum_24|h4|on_time | 1380 | 23 | 1380 | 0.569 | 0.54-0.59 | 0.569 | 0.503 | +0.0002 | 0.066 | 0.00 | - |
| orthosys|h1|all | 1560 | 26 | 134 | 0.470 | 0.39-0.55 | 0.538 | 0.498 | +0.0000 | 0.040 | 0.00 | - |
| orthosys|h1|on_time | 1500 | 25 | 133 | 0.466 | 0.38-0.55 | 0.534 | 0.498 | -0.0002 | 0.036 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 1380 | 23 | 64 | 0.547 | 0.43-0.66 | 0.569 | 0.499 | -0.0005 | 0.073 | 0.00 | - |
| orthosys|h4|on_time | 1380 | 23 | 64 | 0.547 | 0.43-0.66 | 0.569 | 0.499 | -0.0005 | 0.073 | 0.00 | - |
| recent_base_rate_7d|h1|all | 1500 | 25 | 1500 | 0.466 | 0.44-0.49 | 0.534 | 0.472 | -0.0092 | 0.062 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 1500 | 25 | 1500 | 0.466 | 0.44-0.49 | 0.534 | 0.472 | -0.0092 | 0.062 | 0.00 | - |
| recent_base_rate_7d|h4|all | 1320 | 22 | 1320 | 0.419 | 0.39-0.45 | 0.581 | 0.437 | -0.0652 | 0.144 | 1.00 | -74.0 |
| recent_base_rate_7d|h4|on_time | 1320 | 22 | 1320 | 0.419 | 0.39-0.45 | 0.581 | 0.437 | -0.0652 | 0.144 | 1.00 | -74.0 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 970.99 | -2.90% | 618 | 232 | 21 |
| analog_k100|h4 | 970.91 | -2.91% | 672 | 257 | 18 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 26 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 23 |
| council|h1 | 1006.44 | +0.64% | 3 | 2 | 21 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 18 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 21 |
| derivatives|h4 | 985.33 | -1.47% | 5 | 1 | 18 |
| lgbm_calibrated|h1 | 951.51 | -4.85% | 150 | 81 | 26 |
| lgbm_calibrated|h4 | 923.28 | -7.67% | 197 | 108 | 23 |
| logistic|h1 | 955.94 | -4.41% | 190 | 97 | 26 |
| logistic|h4 | 1038.97 | +3.90% | 197 | 107 | 23 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 26 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 23 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 26 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 23 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 25 |
| recent_base_rate_7d|h4 | 960.01 | -4.00% | 1320 | 502 | 22 |
| benchmark_long_all_coins|h1 | 1007.54 | +0.75% | 1560 | 739 | 26 |
| benchmark_long_all_coins|h4 | 1028.61 | +2.86% | 1380 | 728 | 23 |
| PRO_analog_k100|h1 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_analog_k100|h4 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_council|h1 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_council|h4 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 21 |
| PRO_derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 18 |
| PRO_lgbm_calibrated|h1 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_lgbm_calibrated|h4 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_logistic|h1 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_logistic|h4 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 26 |
| PRO_orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 23 |
| PRO_recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 25 |
| PRO_recent_base_rate_7d|h4 | 1000.00 | +0.00% | 0 | 0 | 22 |

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
