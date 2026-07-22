# Week 5 – Day 3: Bug Hunting & Code Audit

## Objective

Today's task focused on testing the backtesting engine for different edge cases instead of adding new features. The objective was to verify that the strategy behaves correctly under unusual situations and document the assumptions made in the code.

---

## Bug 1: Consecutive Buy Signals

The first investigation was to check what happens when multiple BUY signals are generated before any SELL signal.

The backtester executes a BUY only when no position is currently open. Once a position is entered, additional BUY signals are ignored until a SELL signal closes the existing position. This prevents the strategy from purchasing additional shares repeatedly and ensures that only one long position is maintained at a time.

**Assumption:** Only one long position can exist at a time. Repeated BUY signals while already holding a position are ignored.

---

## Bug 2: Open Position at the End of the Backtest

The second investigation examined the situation where a BUY signal occurs near the end of the dataset without a corresponding SELL signal.

The backtester records the BUY transaction, but since the position remains open, it is not treated as a completed trade. As a result, the unrealized profit or loss is excluded from the win rate and other trade statistics. This behaviour is consistent with standard backtesting practices where only completed trades are evaluated.

**Assumption:** Only closed trades are included while calculating win rate and trade statistics.

---

## Bug 3: Missing Market Data

The final investigation focused on missing market data.

Missing trading days caused by weekends or market holidays do not affect the backtester because it automatically proceeds to the next available trading day. However, if a closing price is missing (`NaN`), portfolio calculations can also become `NaN`, leading to incorrect performance metrics. Additional validation should be added before performing calculations to handle missing values safely.

**Assumption:** The input dataset contains valid closing prices. Missing price values should be checked and handled before portfolio calculations.

---

## Key Learnings

Testing edge cases is an essential part of building reliable trading software. Position management in the current implementation correctly prevents duplicate BUY orders, and open positions are appropriately excluded from trade statistics until they are closed. The primary improvement identified during today's audit is the need to validate missing price values before calculations to prevent `NaN` values from propagating through the portfolio and performance metrics.

Overall, today's debugging session improved the robustness of the backtesting engine and highlighted the importance of documenting assumptions for future maintenance and development.
