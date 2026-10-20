# Live monitor (2026-10-20T05:07:17.809359+00:00)

## Alerts

- none

## Health

- **venue**: okx
- **symbols**: 63
- **universe_size**: 60
- **fetched_only_for_scoring**: ['CHIP', 'USELESS', 'W']
- **last_closed_bar**: 2026-10-20 04:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 5.3
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 104.3 instruments 63/63']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.133, 'recent_base_rate_7d': 0.098, 'momentum_24': 0.145, 'logistic': 0.12, 'lgbm_calibrated': 0.114, 'analog_k100': 0.117, 'derivatives': 0.137, 'orthosys': 0.135}
- **council_member_logloss_h1**: {'base_rate': 0.6938, 'recent_base_rate_7d': 0.7032, 'momentum_24': 0.6914, 'logistic': 0.6967, 'lgbm_calibrated': 0.6981, 'analog_k100': 0.7016, 'derivatives': 0.6943, 'orthosys': 0.6934}
- **council_calls_h1**: 5
- **council_abstain_h1**: {'no_edge': 52, 'spoke': 5, 'extreme_volatility': 3}
- **council_weights_h4**: {'base_rate': 0.158, 'recent_base_rate_7d': 0.049, 'momentum_24': 0.158, 'logistic': 0.117, 'lgbm_calibrated': 0.096, 'analog_k100': 0.116, 'derivatives': 0.153, 'orthosys': 0.152}
- **council_member_logloss_h4**: {'base_rate': 0.692, 'recent_base_rate_7d': 0.74, 'momentum_24': 0.692, 'logistic': 0.703, 'lgbm_calibrated': 0.7104, 'analog_k100': 0.7149, 'derivatives': 0.6919, 'orthosys': 0.6934}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 52, 'members_disagree': 5, 'extreme_volatility': 3}
- **prediction_latency_min**: 7.2
- **price_snapshot_age_s**: 1.0
- **train_rows_h1**: 91561
- **orthosys_hist_hit_h1**: 0.5292
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0104
- **p_spread_logistic_h1**: 0.0228
- **p_spread_lgbm_calibrated_h1**: 0.0197
- **p_spread_analog_k100_h1**: 0.0499
- **p_spread_derivatives_h1**: 0.0019
- **p_spread_orthosys_h1**: 0.0075
- **p_spread_council_h1**: 0.0081
- **train_rows_h4**: 91372
- **orthosys_hist_hit_h4**: 0.5162
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0005
- **p_spread_logistic_h4**: 0.0273
- **p_spread_lgbm_calibrated_h4**: 0.0066
- **p_spread_analog_k100_h4**: 0.0651
- **p_spread_derivatives_h4**: 0.008
- **p_spread_orthosys_h4**: 0.0042
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 13200

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 480 | 8 | 480 | 0.521 | 0.48-0.57 | 0.579 | 0.493 | -0.0077 | 0.096 | 0.43 | -1.2 |
| analog_k100|h1|on_time | 480 | 8 | 480 | 0.521 | 0.48-0.57 | 0.579 | 0.493 | -0.0077 | 0.096 | 0.43 | -1.2 |
| analog_k100|h4|all | 300 | 5 | 300 | 0.500 | 0.44-0.56 | 0.633 | 0.453 | -0.0318 | 0.183 | 0.62 | -11.1 |
| analog_k100|h4|on_time | 300 | 5 | 300 | 0.500 | 0.44-0.56 | 0.633 | 0.453 | -0.0318 | 0.183 | 0.62 | -11.1 |
| base_rate|h1|all | 780 | 13 | 780 | 0.449 | 0.41-0.48 | 0.551 | 0.498 | +0.0000 | 0.053 | 0.00 | - |
| base_rate|h1|on_time | 720 | 12 | 720 | 0.457 | 0.42-0.49 | 0.543 | 0.498 | +0.0000 | 0.045 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 600 | 10 | 600 | 0.612 | 0.57-0.65 | 0.612 | 0.503 | +0.0000 | 0.108 | 0.00 | - |
| base_rate|h4|on_time | 600 | 10 | 600 | 0.612 | 0.57-0.65 | 0.612 | 0.503 | +0.0000 | 0.108 | 0.00 | - |
| council|h1|all | 480 | 8 | 62 | 0.500 | 0.38-0.62 | 0.579 | 0.497 | +0.0010 | 0.082 | 0.00 | - |
| council|h1|on_time | 480 | 8 | 62 | 0.500 | 0.38-0.62 | 0.579 | 0.497 | +0.0010 | 0.082 | 0.00 | - |
| council|h4|all | 300 | 5 | 11 | 0.818 | 0.52-0.95 | 0.633 | 0.499 | -0.0012 | 0.152 | 0.00 | - |
| council|h4|on_time | 300 | 5 | 11 | 0.818 | 0.52-0.95 | 0.633 | 0.499 | -0.0012 | 0.152 | 0.00 | - |
| derivatives|h1|all | 480 | 8 | 480 | 0.408 | 0.37-0.45 | 0.579 | 0.498 | -0.0002 | 0.093 | 0.00 | - |
| derivatives|h1|on_time | 480 | 8 | 480 | 0.408 | 0.37-0.45 | 0.579 | 0.498 | -0.0002 | 0.093 | 0.00 | - |
| derivatives|h4|all | 300 | 5 | 300 | 0.637 | 0.58-0.69 | 0.633 | 0.503 | +0.0003 | 0.133 | 0.00 | - |
| derivatives|h4|on_time | 300 | 5 | 300 | 0.637 | 0.58-0.69 | 0.633 | 0.503 | +0.0003 | 0.133 | 0.00 | - |
| lgbm_calibrated|h1|all | 780 | 13 | 780 | 0.488 | 0.45-0.52 | 0.551 | 0.474 | +0.0015 | 0.077 | 0.08 | -33.8 |
| lgbm_calibrated|h1|on_time | 720 | 12 | 720 | 0.500 | 0.46-0.54 | 0.543 | 0.474 | +0.0047 | 0.069 | 0.08 | -33.8 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 600 | 10 | 600 | 0.385 | 0.35-0.42 | 0.612 | 0.458 | -0.0387 | 0.157 | 0.27 | -10.0 |
| lgbm_calibrated|h4|on_time | 600 | 10 | 600 | 0.385 | 0.35-0.42 | 0.612 | 0.458 | -0.0387 | 0.157 | 0.27 | -10.0 |
| logistic|h1|all | 780 | 13 | 780 | 0.537 | 0.50-0.57 | 0.551 | 0.486 | +0.0027 | 0.067 | 0.06 | -37.3 |
| logistic|h1|on_time | 720 | 12 | 720 | 0.517 | 0.48-0.55 | 0.543 | 0.484 | -0.0020 | 0.061 | 0.06 | -38.3 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 600 | 10 | 600 | 0.457 | 0.42-0.50 | 0.612 | 0.492 | -0.0207 | 0.120 | 0.14 | -48.7 |
| logistic|h4|on_time | 600 | 10 | 600 | 0.457 | 0.42-0.50 | 0.612 | 0.492 | -0.0207 | 0.120 | 0.14 | -48.7 |
| momentum_24|h1|all | 780 | 13 | 780 | 0.582 | 0.55-0.62 | 0.551 | 0.501 | +0.0061 | 0.073 | 0.00 | - |
| momentum_24|h1|on_time | 720 | 12 | 720 | 0.572 | 0.54-0.61 | 0.543 | 0.500 | +0.0054 | 0.063 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 600 | 10 | 600 | 0.612 | 0.57-0.65 | 0.612 | 0.503 | -0.0000 | 0.108 | 0.00 | - |
| momentum_24|h4|on_time | 600 | 10 | 600 | 0.612 | 0.57-0.65 | 0.612 | 0.503 | -0.0000 | 0.108 | 0.00 | - |
| orthosys|h1|all | 780 | 13 | 26 | 0.500 | 0.32-0.68 | 0.551 | 0.500 | +0.0009 | 0.052 | 0.00 | - |
| orthosys|h1|on_time | 720 | 12 | 25 | 0.480 | 0.30-0.67 | 0.543 | 0.500 | +0.0006 | 0.043 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 600 | 10 | 18 | 0.389 | 0.20-0.61 | 0.612 | 0.500 | -0.0030 | 0.112 | 0.00 | - |
| orthosys|h4|on_time | 600 | 10 | 18 | 0.389 | 0.20-0.61 | 0.612 | 0.500 | -0.0030 | 0.112 | 0.00 | - |
| recent_base_rate_7d|h1|all | 720 | 12 | 720 | 0.457 | 0.42-0.49 | 0.543 | 0.472 | -0.0125 | 0.071 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 720 | 12 | 720 | 0.457 | 0.42-0.49 | 0.543 | 0.472 | -0.0125 | 0.071 | 0.00 | - |
| recent_base_rate_7d|h4|all | 540 | 9 | 540 | 0.354 | 0.31-0.39 | 0.646 | 0.433 | -0.0989 | 0.213 | 1.00 | -47.4 |
| recent_base_rate_7d|h4|on_time | 540 | 9 | 540 | 0.354 | 0.31-0.39 | 0.646 | 0.433 | -0.0989 | 0.213 | 1.00 | -47.4 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 998.76 | -0.12% | 208 | 94 | 8 |
| analog_k100|h4 | 998.76 | -0.12% | 185 | 81 | 5 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 13 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 10 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 8 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 5 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 8 |
| derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 5 |
| lgbm_calibrated|h1 | 968.57 | -3.14% | 61 | 13 | 13 |
| lgbm_calibrated|h4 | 992.01 | -0.80% | 161 | 82 | 10 |
| logistic|h1 | 943.89 | -5.61% | 48 | 23 | 13 |
| logistic|h4 | 993.71 | -0.63% | 85 | 30 | 10 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 13 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 10 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 13 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 10 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 12 |
| recent_base_rate_7d|h4 | 989.37 | -1.06% | 540 | 184 | 9 |
| benchmark_long_all_coins|h1 | 991.94 | -0.81% | 780 | 320 | 13 |
| benchmark_long_all_coins|h4 | 1004.83 | +0.48% | 600 | 315 | 10 |

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
