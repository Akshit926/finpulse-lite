# Conceptual Question

What if a buy signal happens but you already hold the stock?
No action should be taken.
Reason:
The strategy has already invested all available capital. Buying again would either require leverage or create duplicate positions, which our simple backtester does not support.
Therefore:
Ignore the signal
Continue holding the existing position

What if a sell signal happens but you have no position?
No action should be taken.
Reason:
There are no shares available to sell. Executing a sell order without ownership would create a short position, which our simple backtester does not support.
Therefore:
Ignore the signal
Remain in cash

### What I worked on today

* Learned the fundamentals of backtesting trading strategies.
* Implemented the run_backtest() function.
* Added buy and sell execution logic.
* Tracked cash, shares, and portfolio value over time.
* Created a trade log to record all transactions.
* Debugged Python indentation and file structure issues.

### What I learned

* How backtesting simulates historical trading performance.
* The importance of state management in trading systems.
* How portfolio value is calculated using cash and holdings.
* Why signals and trades are not always the same thing.

### Where I struggled

* Understanding the transition between cash and stock-holding states.
* Fixing indentation and formatting issues caused by copied markdown code.
* Ensuring trades only occur under valid conditions.

### How I solved problems (which Level helped most?)

* Investopedia helped build the conceptual understanding of backtesting.
* Experimentation with code clarified the trading workflow.
* AI assistance helped debug implementation errors quickly.

### What I'll do tomorrow

* Run the completed backtest on Reliance data and analyze performance metrics.

### One-sentence reflection

Today I learned that a successful trading strategy depends not only on generating signals but also on correctly managing positions and capital.

