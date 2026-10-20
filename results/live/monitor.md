# Live monitor (2026-10-20T01:07:52.328314+00:00)

## Alerts

- MODEL COLLAPSED: p_spread_lgbm_calibrated_h4 = 0.0 (same probability for every coin)
- LATENCY SLIPPAGE: base_rate|h4|all live price differs from bar close by +16.1 bps on average
- LATENCY SLIPPAGE: lgbm_calibrated|h4|all live price differs from bar close by +16.1 bps on average
- LATENCY SLIPPAGE: logistic|h4|all live price differs from bar close by +16.1 bps on average
- LATENCY SLIPPAGE: momentum_24|h4|all live price differs from bar close by +16.1 bps on average
- LATENCY SLIPPAGE: orthosys|h4|all live price differs from bar close by +16.1 bps on average

## Health

- **venue**: okx
- **symbols**: 62
- **universe_size**: 60
- **fetched_only_for_scoring**: ['TRX', 'XLM']
- **last_closed_bar**: 2026-10-20 00:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.7
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 109.9 instruments 62/62']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.133, 'recent_base_rate_7d': 0.106, 'momentum_24': 0.144, 'logistic': 0.133, 'lgbm_calibrated': 0.112, 'analog_k100': 0.101, 'derivatives': 0.136, 'orthosys': 0.135}
- **council_member_logloss_h1**: {'base_rate': 0.694, 'recent_base_rate_7d': 0.7052, 'momentum_24': 0.6906, 'logistic': 0.6938, 'lgbm_calibrated': 0.7011, 'analog_k100': 0.7292, 'derivatives': 0.6953, 'orthosys': 0.6933}
- **council_calls_h1**: 2
- **council_abstain_h1**: {'no_edge': 55, 'extreme_volatility': 3, 'spoke': 2}
- **council_weights_h4**: {'base_rate': 0.139, 'recent_base_rate_7d': 0.071, 'momentum_24': 0.139, 'logistic': 0.132, 'lgbm_calibrated': 0.112, 'analog_k100': 0.135, 'derivatives': 0.135, 'orthosys': 0.137}
- **council_member_logloss_h4**: {'base_rate': 0.6924, 'recent_base_rate_7d': 0.7477, 'momentum_24': 0.6923, 'logistic': 0.696, 'lgbm_calibrated': 0.7067, 'orthosys': 0.6935}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 49, 'members_disagree': 8, 'extreme_volatility': 3}
- **prediction_latency_min**: 7.8
- **price_snapshot_age_s**: 1.1
- **train_rows_h1**: 89825
- **orthosys_hist_hit_h1**: 0.5279
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0097
- **p_spread_logistic_h1**: 0.0149
- **p_spread_lgbm_calibrated_h1**: 0.011
- **p_spread_analog_k100_h1**: 0.0556
- **p_spread_derivatives_h1**: 0.0017
- **p_spread_orthosys_h1**: 0.005
- **p_spread_council_h1**: 0.0041
- **train_rows_h4**: 89639
- **orthosys_hist_hit_h4**: 0.5144
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0001
- **p_spread_logistic_h4**: 0.0221
- **p_spread_lgbm_calibrated_h4**: 0.0
- **p_spread_analog_k100_h4**: 0.0677
- **p_spread_derivatives_h4**: 0.0044
- **p_spread_orthosys_h4**: 0.0026
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 8880

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 240 | 4 | 240 | 0.463 | 0.40-0.53 | 0.596 | 0.482 | -0.0525 | 0.130 | 0.41 | -21.5 |
| analog_k100|h1|on_time | 240 | 4 | 240 | 0.463 | 0.40-0.53 | 0.596 | 0.482 | -0.0525 | 0.130 | 0.41 | -21.5 |
| analog_k100|h4|all | 60 | 1 | 60 | 0.400 | 0.29-0.53 | 0.700 | 0.437 | -0.0894 | 0.263 | 0.72 | -31.7 |
| analog_k100|h4|on_time | 60 | 1 | 60 | 0.400 | 0.29-0.53 | 0.700 | 0.437 | -0.0894 | 0.263 | 0.72 | -31.7 |
| base_rate|h1|all | 540 | 9 | 540 | 0.454 | 0.41-0.50 | 0.546 | 0.498 | +0.0000 | 0.049 | 0.00 | - |
| base_rate|h1|on_time | 480 | 8 | 480 | 0.467 | 0.42-0.51 | 0.533 | 0.498 | +0.0000 | 0.036 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 360 | 6 | 360 | 0.608 | 0.56-0.66 | 0.608 | 0.503 | +0.0000 | 0.105 | 0.00 | - |
| base_rate|h4|on_time | 360 | 6 | 360 | 0.608 | 0.56-0.66 | 0.608 | 0.503 | +0.0000 | 0.105 | 0.00 | - |
| council|h1|all | 240 | 4 | 39 | 0.282 | 0.17-0.44 | 0.596 | 0.496 | -0.0054 | 0.100 | 0.00 | - |
| council|h1|on_time | 240 | 4 | 39 | 0.282 | 0.17-0.44 | 0.596 | 0.496 | -0.0054 | 0.100 | 0.00 | - |
| council|h4|all | 60 | 1 | 5 | 0.800 | 0.38-0.96 | 0.700 | 0.499 | -0.0008 | 0.231 | 0.00 | - |
| council|h4|on_time | 60 | 1 | 5 | 0.800 | 0.38-0.96 | 0.700 | 0.499 | -0.0008 | 0.231 | 0.00 | - |
| derivatives|h1|all | 240 | 4 | 240 | 0.388 | 0.33-0.45 | 0.596 | 0.498 | -0.0004 | 0.114 | 0.00 | - |
| derivatives|h1|on_time | 240 | 4 | 240 | 0.388 | 0.33-0.45 | 0.596 | 0.498 | -0.0004 | 0.114 | 0.00 | - |
| derivatives|h4|all | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.700 | 0.502 | -0.0002 | 0.198 | 0.00 | - |
| derivatives|h4|on_time | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.700 | 0.502 | -0.0002 | 0.198 | 0.00 | - |
| lgbm_calibrated|h1|all | 540 | 9 | 540 | 0.507 | 0.47-0.55 | 0.546 | 0.473 | -0.0054 | 0.073 | 0.11 | -33.8 |
| lgbm_calibrated|h1|on_time | 480 | 8 | 480 | 0.527 | 0.48-0.57 | 0.533 | 0.474 | -0.0015 | 0.059 | 0.13 | -33.8 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 360 | 6 | 360 | 0.392 | 0.34-0.44 | 0.608 | 0.455 | -0.0350 | 0.153 | 0.42 | -8.7 |
| lgbm_calibrated|h4|on_time | 360 | 6 | 360 | 0.392 | 0.34-0.44 | 0.608 | 0.455 | -0.0350 | 0.153 | 0.42 | -8.7 |
| logistic|h1|all | 540 | 9 | 540 | 0.572 | 0.53-0.61 | 0.546 | 0.491 | +0.0036 | 0.060 | 0.04 | -76.6 |
| logistic|h1|on_time | 480 | 8 | 480 | 0.546 | 0.50-0.59 | 0.533 | 0.487 | -0.0032 | 0.049 | 0.04 | -84.4 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 360 | 6 | 360 | 0.500 | 0.45-0.55 | 0.608 | 0.504 | -0.0183 | 0.104 | 0.13 | -66.7 |
| logistic|h4|on_time | 360 | 6 | 360 | 0.500 | 0.45-0.55 | 0.608 | 0.504 | -0.0183 | 0.104 | 0.13 | -66.7 |
| momentum_24|h1|all | 540 | 9 | 540 | 0.578 | 0.54-0.62 | 0.546 | 0.502 | +0.0055 | 0.069 | 0.00 | - |
| momentum_24|h1|on_time | 480 | 8 | 480 | 0.562 | 0.52-0.61 | 0.533 | 0.502 | +0.0044 | 0.054 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 360 | 6 | 360 | 0.608 | 0.56-0.66 | 0.608 | 0.503 | +0.0000 | 0.105 | 0.00 | - |
| momentum_24|h4|on_time | 360 | 6 | 360 | 0.608 | 0.56-0.66 | 0.608 | 0.503 | +0.0000 | 0.105 | 0.00 | - |
| orthosys|h1|all | 540 | 9 | 16 | 0.438 | 0.23-0.67 | 0.546 | 0.500 | +0.0005 | 0.046 | 0.00 | - |
| orthosys|h1|on_time | 480 | 8 | 15 | 0.400 | 0.20-0.64 | 0.533 | 0.500 | +0.0000 | 0.033 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 360 | 6 | 10 | 0.300 | 0.11-0.60 | 0.608 | 0.500 | -0.0030 | 0.108 | 0.00 | - |
| orthosys|h4|on_time | 360 | 6 | 10 | 0.300 | 0.11-0.60 | 0.608 | 0.500 | -0.0030 | 0.108 | 0.00 | - |
| recent_base_rate_7d|h1|all | 480 | 8 | 480 | 0.467 | 0.42-0.51 | 0.533 | 0.470 | -0.0130 | 0.064 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 480 | 8 | 480 | 0.467 | 0.42-0.51 | 0.533 | 0.470 | -0.0130 | 0.064 | 0.00 | - |
| recent_base_rate_7d|h4|all | 300 | 5 | 300 | 0.330 | 0.28-0.39 | 0.670 | 0.431 | -0.1161 | 0.239 | 1.00 | -55.1 |
| recent_base_rate_7d|h4|on_time | 300 | 5 | 300 | 0.330 | 0.28-0.39 | 0.670 | 0.431 | -0.1161 | 0.239 | 1.00 | -55.1 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 991.93 | -0.81% | 98 | 26 | 4 |
| analog_k100|h4 | 999.21 | -0.08% | 43 | 12 | 1 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 9 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 6 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 4 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 1 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 4 |
| derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 1 |
| lgbm_calibrated|h1 | 968.57 | -3.14% | 61 | 13 | 9 |
| lgbm_calibrated|h4 | 998.78 | -0.12% | 150 | 76 | 6 |
| logistic|h1 | 952.33 | -4.77% | 24 | 10 | 9 |
| logistic|h4 | 994.65 | -0.53% | 46 | 15 | 6 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 9 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 6 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 9 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 6 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 8 |
| recent_base_rate_7d|h4 | 993.12 | -0.69% | 300 | 99 | 5 |
| benchmark_long_all_coins|h1 | 984.71 | -1.53% | 540 | 172 | 9 |
| benchmark_long_all_coins|h4 | 1003.04 | +0.30% | 360 | 179 | 6 |

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
