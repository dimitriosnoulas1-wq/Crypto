# Άλλα συστήματα trading στο GitHub (έρευνα 2026-10-19)

Επαληθευμένα με `git clone --depth 1 --no-checkout` (μόνο μεταδεδομένα, χωρίς εκτέλεση). «Τελευταίο commit» = default branch.

| Project | Τι είναι | Άδεια | Τελευταίο commit | Χρήσιμο για εμάς ως… |
|---|---|---|---|---|
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | LLM agents με debate bull/bear, risk team, μνήμη | Apache-2.0 | 2026-10-16 | πρότυπο «συμβουλίου»· κρίνεται μόνο live (LLM memorization) |
| [EthanXiang777/circuit-framework](https://github.com/EthanXiang777/circuit-framework) | fork του TradingAgents για paper trading με **ντετερμινιστική μηχανή ρίσκου** που εγκρίνει/απορρίπτει | Apache-2.0 | 2026-07-11 | ιδέα για το veto ρίσκου |
| [Tomortec/CryptoTradingAgents](https://github.com/Tomortec/CryptoTradingAgents) | multi-agent LLM για crypto | Apache-2.0 | 2025-11-07 | αναφορά (στάσιμο ~1 χρόνο) |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | agents-«επενδυτές» | MIT | 2026-10-19 | εκπαιδευτικό |
| [Xtra-Computing/CryptoTrade](https://github.com/Xtra-Computing/CryptoTrade) | LLM agent ETH/BTC/SOL με on-chain + news | CC BY-NC-SA 4.0 | 2024-12-01 | τεστ μέσα στην περίοδο εκπαίδευσης του LLM |
| [AI4Finance-Foundation/FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) | πλατφόρμα LLM agents για χρηματοοικονομικά | Apache-2.0 | 2026-09-28 | αναφορά |
| [pipiku915/FinMem-LLM-StockTrading](https://github.com/pipiku915/FinMem-LLM-StockTrading) | LLM agent με πολυεπίπεδη μνήμη ([paper](https://arxiv.org/abs/2311.13743v2)) | MIT | 2024-08-17 | ιδέα μνήμης· στάσιμο |
| [AI4Finance-Foundation/FinRL](https://github.com/AI4Finance-Foundation/FinRL) | deep reinforcement learning για trading (και crypto) | MIT | 2026-10-14 | το crypto παράδειγμα του [paper](https://arxiv.org/pdf/2111.09395) είναι backtest **10 ημερών** (103% vs 93% BTC) — δεν αποδεικνύει τίποτα |
| [microsoft/qlib](https://github.com/microsoft/qlib) | ερευνητική πλατφόρμα quant με πολλά μοντέλα (ALSTM, DoubleEnsemble…), Alpha158 χαρακτηριστικά | MIT | 2026-10-08 | πηγή ιδεών για features/μοντέλα· όχι έτοιμο για crypto live |
| [microsoft/RD-Agent](https://github.com/microsoft/RD-Agent) | LLM agent που **ψάχνει αυτόματα νέα features/μοντέλα** | MIT | 2026-09-23 | ενδιαφέρον για «agent ερευνητή», με κίνδυνο overfitting |
| [QuantConnect/Lean](https://github.com/QuantConnect/Lean) | επαγγελματική μηχανή backtest/live (C#/Python) | Apache-2.0 | 2026-10-19 | εναλλακτική του Nautilus για ρεαλιστικά backtests |
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | **foundation model για κεριά (OHLCV)**, εκπαιδευμένο σε 45+ χρηματιστήρια, 24.7M παράμετροι ([paper](https://huggingface.co/papers/2508.02739)) | MIT | 2026-04-13 | **υποψήφιος agent πρόβλεψης** |
| [amazon-science/chronos-forecasting](https://github.com/amazon-science/chronos-forecasting) | γενικό foundation model χρονοσειρών (Chronos-Bolt, Chronos-2) | Apache-2.0 | 2026-10-05 | **υποψήφιος agent πρόβλεψης** |
| [google-research/timesfm](https://github.com/google-research/timesfm) | γενικό foundation model χρονοσειρών | Apache-2.0 | 2026-09-29 | υποψήφιος agent |

## Σημεία προσοχής
- Κανένα δεν δημοσιεύει επαληθευμένη, ανεξάρτητη υψηλή ακρίβεια σε crypto.
- Τα LLM συστήματα και τα foundation models (Kronos, Chronos, TimesFM) έχουν εκπαιδευτεί σε ιστορικά δεδομένα που μπορεί να καλύπτουν τις περιόδους των backtests μας → τα κρίνουμε **μόνο live στο ledger**, μετά την ημερομηνία εκπαίδευσής τους.
- Τα βάρη των Kronos/Chronos/TimesFM φιλοξενούνται στο Hugging Face, που **είναι μπλοκαρισμένο** στο τρέχον δίκτυο (403). Για να τα δοκιμάσουμε χρειάζεται να προστεθούν τα `huggingface.co`, `cdn-lfs.huggingface.co`, `cdn-lfs-us-1.huggingface.co` στα Allowed domains. Τρέχουν σε CPU (Kronos-small, Chronos-Bolt-small), χωρίς κόστος.
