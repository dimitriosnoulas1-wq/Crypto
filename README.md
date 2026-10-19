# Crypto intelligence engine (personal, local use)

Analysis and prediction engine for crypto markets. It does **not** place orders and holds no API keys.

- `engine/cil/` - data loading, features, labels, models, walk-forward validation, backtest, immutable prediction ledger, live data adapter (CCXT).
- `engine/run_research.py` - full offline validation on real historical data.
- `engine/paper_trade.py` - paper trading: `--mode replay` (day-by-day as if live) or `--mode live` (needs exchange network access).
- `engine/tests/` - look-ahead leakage and ledger tamper tests.
- `RESULTS.md` - what the tests actually showed.
- `results/` - JSON reports, out-of-sample predictions, paper-trading ledger.

Research notes (17 reference repositories, licenses, security, architecture) live in
`/home/user/crypto-intelligence-lab/`.

## Run

```bash
python3 -m venv ~/.venvs/cil && ~/.venvs/cil/bin/pip install numpy pandas scikit-learn lightgbm pyarrow ccxt pytest
cd engine
~/.venvs/cil/bin/python -m pytest -q tests
~/.venvs/cil/bin/python run_research.py
~/.venvs/cil/bin/python paper_trade.py --mode replay --start 2025-01-01 --end 2025-07-31
~/.venvs/cil/bin/python paper_trade.py --mode live      # daily, after 00:00 UTC
```

The historical data path defaults to the TrendScan clone in the research workspace (`cil/data.py`).
