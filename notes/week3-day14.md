### What I worked on today

* Learned about trade statistics and how they help evaluate a trading strategy beyond returns.
* Implemented the `trade_statistics()` function.
* Calculated total trades, win rate, average win, average loss, and profit factor.
* Created a `summary_report()` function to display all strategy metrics in one place.
* Generated a complete strategy report card for my SMA crossover strategy.

### What I learned

* Win rate alone does not determine whether a strategy is profitable.
* A strategy can have a high win rate but still perform poorly if losses are larger than gains.
* Profit Factor measures how much profit is generated for every rupee lost.
* Trade statistics provide a deeper understanding of strategy behavior than returns alone.
* Evaluating a strategy requires looking at multiple metrics together rather than focusing on a single number.

### Where I struggled

* Understanding how to pair buy and sell trades into complete round-trips.
* Calculating profit for individual trades correctly.
* Debugging syntax and indentation errors while adding the summary report function.

### How I solved problems (which Level helped most?)

* Experimentation helped me understand how trade profits were calculated.
* Reading error messages carefully helped me fix syntax and indentation issues.
* AI assistance helped explain trade statistics and their interpretation.
* Testing the functions repeatedly helped verify the calculations.

### What I'll do tomorrow

* Complete the final strategy report card and review all metrics together to understand the strengths and weaknesses of the strategy.

### One-sentence reflection

Today I learned that a strategy's quality cannot be judged by win rate alone; risk, losses, and consistency matter just as much.

# Results

Total Return: 4.55%

Annualized Return: 0.91%

Sharpe Ratio: -0.35

Maximum Drawdown: -20.26%

Total Trades: 3

Win Rate: 66.67%

Average Win: ₹8,000.89

Average Loss: ₹-10,861.28

Profit Factor: 1.47

# What do these results tell me?

My strategy won 2 out of every 3 trades, giving it a healthy win rate of 66.67%. However, the overall returns remained low because the losing trade was larger than the average winning trade.

Although the Profit Factor of 1.47 suggests that the strategy made more money than it lost overall, the annualized return of only 0.91% and Sharpe Ratio of -0.35 indicate that the strategy did not generate attractive risk-adjusted returns.

The results show that winning frequently is not enough. A successful strategy must also control losses, generate consistent returns, and outperform simple alternatives such as Buy-and-Hold.
