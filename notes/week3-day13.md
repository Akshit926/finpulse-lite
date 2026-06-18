### What I worked on today

* Learned about the Sharpe Ratio and its importance in evaluating trading strategies.
* Studied how risk-adjusted returns are calculated.
* Understood the difference between absolute returns and returns earned per unit of risk.
* Implemented the `sharpe_ratio()` function in `metrics.py`.
* Calculated daily returns from the equity curve.
* Annualized returns and volatility using 252 trading days.
* Tested the Sharpe Ratio on my Reliance SMA strategy.

### What I learned

* The Sharpe Ratio measures how much return a strategy generates for each unit of risk taken.
* Daily returns can be annualized by multiplying the mean by 252.
* Volatility is annualized by multiplying the standard deviation by √252.
* A strategy with high returns is not necessarily a good strategy if it takes excessive risk.
* Risk-adjusted performance is often more important than raw returns.

### Where I struggled

* Understanding why volatility is annualized using √252 instead of 252.
* Interpreting what a negative Sharpe Ratio actually means.
* Connecting the mathematical formula to the practical performance of my strategy.

### Which Level helped most?

* Investopedia articles helped me understand the theory behind the Sharpe Ratio.
* Working through examples helped me understand annualization.
* AI assistance helped clarify the intuition behind risk-adjusted returns and the √252 factor.
* Testing the metric on my own strategy made the concept much easier to understand.

### What I'll do tomorrow

* Calculate additional strategy statistics such as win rate and number of trades to continue building the strategy report card.

### One-sentence reflection

Today I learned that a strategy should not only make money but also justify the risk taken to earn those returns.

# Results

### Sharpe Ratio

-0.35

# What does my Sharpe Ratio mean?

My strategy's Sharpe Ratio was **-0.35**, which is considered poor.

A negative Sharpe Ratio means the strategy failed to generate enough return relative to the amount of risk taken. In fact, the strategy underperformed the assumed risk-free rate of 6.5%.

This tells me that although the strategy was functional and generated valid trading signals, it did not provide attractive risk-adjusted returns. An investor would likely have been better off investing in a safer asset rather than taking the additional risk of this strategy.

This was an important lesson because it showed me that returns alone do not tell the full story. Risk-adjusted metrics provide a much better picture of a strategy's overall quality.

# What does the Sharpe Ratio mean intuitively?

The Sharpe Ratio measures how much return a strategy generates for each unit of risk taken.

A higher Sharpe Ratio means the strategy is producing better returns relative to its volatility.

As a general rule:

* Sharpe < 1 → Weak
* Sharpe > 1 → Good
* Sharpe > 2 → Excellent
* Sharpe > 3 → Unusually high and should be examined carefully

In simple terms, Sharpe Ratio answers the question:

"Was the return worth the risk I took to achieve it?"

A strategy with high returns but extremely high volatility may have a lower Sharpe Ratio than a strategy with slightly lower returns but much more consistent performance.

This makes Sharpe Ratio one of the most widely used measures of risk-adjusted performance in quantitative finance.


