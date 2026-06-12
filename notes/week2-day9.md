### What I worked on today

* Learned how to visualize backtesting results using Matplotlib.
* Generated the equity curve for my SMA crossover strategy.
* Created a Buy-and-Hold benchmark for Reliance.
* Compared the performance of both approaches on the same graph.
* Saved the visualization as `RELIANCE_backtest.png`.
* Analyzed whether my strategy actually added value compared to simply holding the stock.

### What I learned

* An equity curve is one of the best ways to understand a strategy's performance over time.
* Buy-and-Hold serves as a strong benchmark that every trading strategy should be compared against.
* Moving average strategies can miss large parts of a trend because they react after the market has already moved.
* Building a strategy is only the first step; proving that it beats a simple benchmark is much harder.

### Where I struggled

* Initially, I expected the SMA strategy to outperform because it actively generated trading signals.
* Understanding why the strategy underperformed despite having a reasonable trading logic took some analysis.
* Interpreting the graph and connecting it to the actual trades required careful observation.

### How I solved problems (which Level helped most?)

* Experimentation helped the most by visualizing both curves on the same chart.
* Documentation helped me understand Matplotlib plotting.
* AI assistance helped interpret the results and understand why Buy-and-Hold performed better.

### What I'll do tomorrow

* Start calculating additional performance metrics such as total return, CAGR, and maximum drawdown to evaluate the strategy more thoroughly.

### One-sentence reflection

Today I learned that creating a strategy is easy compared to the challenge of consistently beating a simple Buy-and-Hold investment.

# Results
SMA Strategy

Final Portfolio Value: ~₹1,05,000

Buy-and-Hold

Final Portfolio Value: ~₹1,24,000

# Did the strategy beat Buy-and-Hold?

No, the SMA crossover strategy did not beat Buy-and-Hold for Reliance.

My strategy grew ₹1,00,000 to about ₹1.05 lakh, while Buy-and-Hold reached around ₹1.24 lakh. Although the strategy generated valid buy and sell signals, it missed several strong upward moves because moving averages react after a trend has already started.

This was a valuable lesson for me. I realized that building a strategy is one thing, but outperforming a simple Buy-and-Hold investment is much harder. Sometimes the simplest approach can outperform a more complex one.
