# Live monitor (2026-10-20T04:06:31.770665+00:00)

## Alerts

- none

## Health

- **venue**: okx
- **symbols**: 64
- **universe_size**: 60
- **fetched_only_for_scoring**: ['CHIP', 'TRX', 'USELESS', 'W']
- **last_closed_bar**: 2026-10-20 03:00:00+00:00
- **minutes_since_bar_close_at_fetch**: 4.4
- **stale_symbols**: []
- **fetch_log**: ['fetch_seconds 112.2 instruments 64/64']
- **feature_nan_share_latest_bar**: 0.026
- **council_weights_h1**: {'base_rate': 0.131, 'recent_base_rate_7d': 0.106, 'momentum_24': 0.141, 'logistic': 0.131, 'lgbm_calibrated': 0.116, 'analog_k100': 0.106, 'derivatives': 0.135, 'orthosys': 0.133}
- **council_member_logloss_h1**: {'base_rate': 0.6937, 'recent_base_rate_7d': 0.7011, 'momentum_24': 0.6915, 'logistic': 0.6938, 'lgbm_calibrated': 0.6974, 'analog_k100': 0.7074, 'derivatives': 0.6942, 'orthosys': 0.6933}
- **council_calls_h1**: 19
- **council_abstain_h1**: {'no_edge': 38, 'spoke': 19, 'extreme_volatility': 3}
- **council_weights_h4**: {'base_rate': 0.151, 'recent_base_rate_7d': 0.058, 'momentum_24': 0.151, 'logistic': 0.121, 'lgbm_calibrated': 0.106, 'analog_k100': 0.12, 'derivatives': 0.146, 'orthosys': 0.147}
- **council_member_logloss_h4**: {'base_rate': 0.6923, 'recent_base_rate_7d': 0.7374, 'momentum_24': 0.6923, 'logistic': 0.7017, 'lgbm_calibrated': 0.707, 'analog_k100': 0.7141, 'derivatives': 0.6925, 'orthosys': 0.6934}
- **council_calls_h4**: 0
- **council_abstain_h4**: {'no_edge': 40, 'members_disagree': 17, 'extreme_volatility': 3}
- **prediction_latency_min**: 6.4
- **price_snapshot_age_s**: 0.4
- **train_rows_h1**: 93008
- **orthosys_hist_hit_h1**: 0.5278
- **p_spread_base_rate_h1**: 0.0
- **p_spread_recent_base_rate_7d_h1**: 0.0
- **p_spread_momentum_24_h1**: 0.0077
- **p_spread_logistic_h1**: 0.0203
- **p_spread_lgbm_calibrated_h1**: 0.0057
- **p_spread_analog_k100_h1**: 0.0573
- **p_spread_derivatives_h1**: 0.001
- **p_spread_orthosys_h1**: 0.0078
- **p_spread_council_h1**: 0.0118
- **train_rows_h4**: 92816
- **orthosys_hist_hit_h4**: 0.5165
- **p_spread_base_rate_h4**: 0.0
- **p_spread_recent_base_rate_7d_h4**: 0.0
- **p_spread_momentum_24_h4**: 0.0007
- **p_spread_logistic_h4**: 0.0309
- **p_spread_lgbm_calibrated_h4**: 0.0141
- **p_spread_analog_k100_h4**: 0.0767
- **p_spread_derivatives_h4**: 0.0036
- **p_spread_orthosys_h4**: 0.0046
- **p_spread_council_h4**: 0.0
- **predictions_written**: 1080
- **resolved_this_cycle**: 1080
- **ledger_chain_valid**: True
- **ledger_rows**: 12120

## Realized results (resolved predictions only)

**Not interpretable yet: only 1 scored hour(s).** Coins move together within an hour, so N coins in one hour is close to one observation; the confidence intervals below assume independence and are far too narrow at this stage.

Brier skill vs base rate = improvement over the naive base-rate model on the same rows (0 = no better, negative = worse). Paper P&L uses the live price at prediction time and 5 bps/side fees.

| model / horizon / subset | resolved | bars | calls | hit rate | 95% CI | up rate | mean p | Brier skill vs base | ECE | coverage | mean paper pnl bps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| analog_k100|h1|all | 420 | 7 | 420 | 0.514 | 0.47-0.56 | 0.640 | 0.494 | -0.0143 | 0.157 | 0.43 | -1.9 |
| analog_k100|h1|on_time | 420 | 7 | 420 | 0.514 | 0.47-0.56 | 0.640 | 0.494 | -0.0143 | 0.157 | 0.43 | -1.9 |
| analog_k100|h4|all | 240 | 4 | 240 | 0.487 | 0.42-0.55 | 0.617 | 0.445 | -0.0452 | 0.176 | 0.64 | -17.8 |
| analog_k100|h4|on_time | 240 | 4 | 240 | 0.487 | 0.42-0.55 | 0.617 | 0.445 | -0.0452 | 0.176 | 0.64 | -17.8 |
| base_rate|h1|all | 720 | 12 | 720 | 0.415 | 0.38-0.45 | 0.585 | 0.498 | +0.0000 | 0.087 | 0.00 | - |
| base_rate|h1|on_time | 660 | 11 | 660 | 0.421 | 0.38-0.46 | 0.579 | 0.498 | +0.0000 | 0.081 | 0.00 | - |
| base_rate|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.498 | +0.0000 | 0.152 | 0.00 | - |
| base_rate|h4|all | 540 | 9 | 540 | 0.602 | 0.56-0.64 | 0.602 | 0.503 | +0.0000 | 0.098 | 0.00 | - |
| base_rate|h4|on_time | 540 | 9 | 540 | 0.602 | 0.56-0.64 | 0.602 | 0.503 | +0.0000 | 0.098 | 0.00 | - |
| council|h1|all | 420 | 7 | 43 | 0.326 | 0.20-0.47 | 0.640 | 0.497 | -0.0019 | 0.143 | 0.00 | - |
| council|h1|on_time | 420 | 7 | 43 | 0.326 | 0.20-0.47 | 0.640 | 0.497 | -0.0019 | 0.143 | 0.00 | - |
| council|h4|all | 240 | 4 | 11 | 0.818 | 0.52-0.95 | 0.617 | 0.499 | -0.0003 | 0.140 | 0.00 | - |
| council|h4|on_time | 240 | 4 | 11 | 0.818 | 0.52-0.95 | 0.617 | 0.499 | -0.0003 | 0.140 | 0.00 | - |
| derivatives|h1|all | 420 | 7 | 420 | 0.345 | 0.30-0.39 | 0.640 | 0.498 | -0.0004 | 0.157 | 0.00 | - |
| derivatives|h1|on_time | 420 | 7 | 420 | 0.345 | 0.30-0.39 | 0.640 | 0.498 | -0.0004 | 0.157 | 0.00 | - |
| derivatives|h4|all | 240 | 4 | 240 | 0.617 | 0.55-0.68 | 0.617 | 0.503 | -0.0006 | 0.114 | 0.00 | - |
| derivatives|h4|on_time | 240 | 4 | 240 | 0.617 | 0.55-0.68 | 0.617 | 0.503 | -0.0006 | 0.114 | 0.00 | - |
| lgbm_calibrated|h1|all | 720 | 12 | 720 | 0.458 | 0.42-0.49 | 0.585 | 0.476 | -0.0086 | 0.109 | 0.08 | -33.8 |
| lgbm_calibrated|h1|on_time | 660 | 11 | 660 | 0.468 | 0.43-0.51 | 0.579 | 0.477 | -0.0060 | 0.102 | 0.09 | -33.8 |
| lgbm_calibrated|h1|late | 60 | 1 | 60 | 0.350 | 0.24-0.48 | 0.650 | 0.467 | -0.0372 | 0.183 | 0.00 | - |
| lgbm_calibrated|h4|all | 540 | 9 | 540 | 0.394 | 0.35-0.44 | 0.602 | 0.457 | -0.0367 | 0.148 | 0.30 | -10.0 |
| lgbm_calibrated|h4|on_time | 540 | 9 | 540 | 0.394 | 0.35-0.44 | 0.602 | 0.457 | -0.0367 | 0.148 | 0.30 | -10.0 |
| logistic|h1|all | 720 | 12 | 720 | 0.511 | 0.47-0.55 | 0.585 | 0.489 | -0.0057 | 0.098 | 0.05 | -68.8 |
| logistic|h1|on_time | 660 | 11 | 660 | 0.486 | 0.45-0.52 | 0.579 | 0.486 | -0.0115 | 0.095 | 0.05 | -73.4 |
| logistic|h1|late | 60 | 1 | 60 | 0.783 | 0.66-0.87 | 0.650 | 0.519 | +0.0580 | 0.258 | 0.05 | -21.5 |
| logistic|h4|all | 540 | 9 | 540 | 0.472 | 0.43-0.51 | 0.602 | 0.493 | -0.0217 | 0.109 | 0.15 | -65.2 |
| logistic|h4|on_time | 540 | 9 | 540 | 0.472 | 0.43-0.51 | 0.602 | 0.493 | -0.0217 | 0.109 | 0.15 | -65.2 |
| momentum_24|h1|all | 720 | 12 | 720 | 0.565 | 0.53-0.60 | 0.585 | 0.501 | +0.0047 | 0.083 | 0.00 | - |
| momentum_24|h1|on_time | 660 | 11 | 660 | 0.553 | 0.51-0.59 | 0.579 | 0.501 | +0.0039 | 0.078 | 0.00 | - |
| momentum_24|h1|late | 60 | 1 | 60 | 0.700 | 0.57-0.80 | 0.650 | 0.502 | +0.0143 | 0.192 | 0.00 | - |
| momentum_24|h4|all | 540 | 9 | 540 | 0.602 | 0.56-0.64 | 0.602 | 0.503 | -0.0000 | 0.099 | 0.00 | - |
| momentum_24|h4|on_time | 540 | 9 | 540 | 0.602 | 0.56-0.64 | 0.602 | 0.503 | -0.0000 | 0.099 | 0.00 | - |
| orthosys|h1|all | 720 | 12 | 21 | 0.429 | 0.24-0.63 | 0.585 | 0.500 | +0.0008 | 0.085 | 0.00 | - |
| orthosys|h1|on_time | 660 | 11 | 20 | 0.400 | 0.22-0.61 | 0.579 | 0.500 | +0.0004 | 0.079 | 0.00 | - |
| orthosys|h1|late | 60 | 1 | 1 | 1.000 | 0.21-1.00 | 0.650 | 0.500 | +0.0046 | 0.166 | 0.00 | - |
| orthosys|h4|all | 540 | 9 | 16 | 0.375 | 0.18-0.61 | 0.602 | 0.500 | -0.0028 | 0.102 | 0.00 | - |
| orthosys|h4|on_time | 540 | 9 | 16 | 0.375 | 0.18-0.61 | 0.602 | 0.500 | -0.0028 | 0.102 | 0.00 | - |
| recent_base_rate_7d|h1|all | 660 | 11 | 660 | 0.421 | 0.38-0.46 | 0.579 | 0.472 | -0.0189 | 0.107 | 0.00 | - |
| recent_base_rate_7d|h1|on_time | 660 | 11 | 660 | 0.421 | 0.38-0.46 | 0.579 | 0.472 | -0.0189 | 0.107 | 0.00 | - |
| recent_base_rate_7d|h4|all | 480 | 8 | 480 | 0.360 | 0.32-0.40 | 0.640 | 0.432 | -0.0968 | 0.208 | 1.00 | -44.3 |
| recent_base_rate_7d|h4|on_time | 480 | 8 | 480 | 0.360 | 0.32-0.40 | 0.640 | 0.432 | -0.0968 | 0.208 | 1.00 | -44.3 |

## Virtual wallets (paper only, start 1000, fees 5 bps/side)

| model / horizon | value | return | trades | wins | scored hours |
|---|---|---|---|---|---|
| analog_k100|h1 | 998.41 | -0.16% | 180 | 84 | 7 |
| analog_k100|h4 | 998.24 | -0.18% | 153 | 65 | 4 |
| base_rate|h1 | 1000.00 | +0.00% | 0 | 0 | 12 |
| base_rate|h4 | 1000.00 | +0.00% | 0 | 0 | 9 |
| council|h1 | 1000.00 | +0.00% | 0 | 0 | 7 |
| council|h4 | 1000.00 | +0.00% | 0 | 0 | 4 |
| derivatives|h1 | 1000.00 | +0.00% | 0 | 0 | 7 |
| derivatives|h4 | 1000.00 | +0.00% | 0 | 0 | 4 |
| lgbm_calibrated|h1 | 968.57 | -3.14% | 61 | 13 | 12 |
| lgbm_calibrated|h4 | 992.01 | -0.80% | 161 | 82 | 9 |
| logistic|h1 | 940.19 | -5.98% | 34 | 13 | 12 |
| logistic|h4 | 988.36 | -1.16% | 80 | 27 | 9 |
| momentum_24|h1 | 1000.00 | +0.00% | 0 | 0 | 12 |
| momentum_24|h4 | 1000.00 | +0.00% | 0 | 0 | 9 |
| orthosys|h1 | 1000.00 | +0.00% | 0 | 0 | 12 |
| orthosys|h4 | 1000.00 | +0.00% | 0 | 0 | 9 |
| recent_base_rate_7d|h1 | 1000.00 | +0.00% | 0 | 0 | 11 |
| recent_base_rate_7d|h4 | 991.17 | -0.88% | 480 | 173 | 8 |
| benchmark_long_all_coins|h1 | 996.97 | -0.30% | 720 | 309 | 12 |
| benchmark_long_all_coins|h4 | 1003.52 | +0.35% | 540 | 270 | 9 |

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
