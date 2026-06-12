### What I worked on today

* Learned about transaction costs and their impact on trading strategies.
* Studied Zerodha's brokerage structure and common trading charges in India.
* Read about transaction costs and realistic backtesting practices.
* Modified the backtesting engine to support transaction costs.
* Added a 0.1% trading cost on every buy and sell transaction.
* Compared portfolio performance with and without transaction costs.
* Debugged issues related to NaN portfolio values and yfinance data formatting.
* Improved the reliability of the backtesting workflow.

### What I learned

* Real-world trading always involves costs that reduce profitability.
* Even small costs can accumulate significantly over multiple trades.
* The difference between gross returns and net returns.
* Why realistic assumptions are essential in backtesting.
* How MultiIndex columns and missing values can affect financial data analysis.
* The importance of validating backtest results before drawing conclusions.

### Where I struggled

* Identifying why the final portfolio value was showing NaN.
* Understanding how yfinance structures downloaded data.
* Ensuring transaction costs were correctly incorporated into buy and sell logic.
* Debugging why the initial comparison showed no difference in returns.

### How I solved problems (which Level helped most?)

* Documentation helped me understand transaction costs conceptually.
* Experimentation and printing intermediate outputs helped identify data issues.
* AI assistance helped debug code and explain backtesting concepts.
* Reading error messages carefully made it easier to locate problems in the implementation.

### What I'll do tomorrow

* Verify the transaction cost implementation and calculate the actual reduction in returns.
* Begin evaluating additional performance metrics such as total return, CAGR, and drawdown.

### One-sentence reflection

Today I learned that a strategy's true performance is determined not by its gross returns but by how it performs after accounting for real-world trading costs.

## Concept Check

### Why do transaction costs matter?

Transaction costs reduce profits every time a trade is executed. Even small fees accumulate over time, especially in strategies that trade frequently. Ignoring these costs can lead to an overly optimistic assessment of a strategy's performance.

### Why is this one of the most important lessons in quant finance?

A strategy that looks profitable in a backtest may become unprofitable once real-world costs are included. Quantitative finance focuses on realistic modeling, and transaction costs are one of the most important factors separating theoretical performance from actual performance. A successful strategy must generate positive returns even after accounting for all trading expenses.
