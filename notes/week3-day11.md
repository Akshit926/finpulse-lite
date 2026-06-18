### What I worked on today

* Learned about Maximum Drawdown and why it is one of the most important risk metrics in investing.
* Read about peak-to-trough declines and how they affect investors psychologically and financially.
* Implemented the `max_drawdown()` function in `metrics.py`.
* Used Pandas' `cummax()` method to track the highest portfolio value reached so far.
* Calculated the drawdown percentage for every day in the backtest.
* Identified the worst drawdown along with its start and end dates.
* Generated and saved a drawdown curve visualization.

### What I learned

* Maximum Drawdown measures the largest percentage decline from a portfolio's peak to its lowest point before recovery.
* A strategy can have good returns but still be difficult to hold if its drawdowns are too large.
* `cummax()` is useful for tracking the highest portfolio value reached up to any point in time.
* Risk metrics are just as important as return metrics when evaluating a trading strategy.
* Investors often care more about avoiding large losses than maximizing gains.

### Where I struggled

* Understanding the difference between a temporary decline and the actual maximum drawdown.
* Visualizing how the rolling maximum is used to calculate drawdowns.
* Debugging file naming issues while generating the drawdown chart.

### How I solved problems (which Level helped most?)

* Investopedia articles helped me understand the concept of Maximum Drawdown.
* Drawing the algorithm on paper made the calculation much easier to understand.
* Experimenting with the drawdown curve helped me connect the formula to the actual portfolio performance.
* AI assistance helped clarify the intuition behind drawdowns and risk measurement.

### What I'll do tomorrow

* Implement volatility calculations and begin working on the Sharpe Ratio to measure risk-adjusted returns.

### One-sentence reflection

Today I learned that earning returns is important, but understanding the worst losses experienced along the way is equally important.


# Why does Maximum Drawdown matter?

Maximum Drawdown measures the worst decline an investor would have experienced while following a strategy. It helps answer an important question: "How much pain would I have had to tolerate to achieve these returns?"

A strategy might generate high returns, but if it experiences very large drawdowns, many investors would struggle to stay invested during those periods. For example, a strategy earning 30% annually may look attractive, but if it loses 70% of its value at some point, most people would likely panic and exit before the recovery.

This is why Maximum Drawdown is such an important risk metric. It shows the downside risk of a strategy and helps investors understand whether the returns are worth the emotional and financial stress required to achieve them.


# Results

===== MAXIMUM DRAWDOWN =====
Maximum Drawdown: -20.26%
Start Date: 2024-07-08 00:00:00
End Date: 2026-03-04 00:00:00