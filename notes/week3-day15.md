### What I worked on today

* Created a complete Strategy Report Card for my SMA crossover strategy.
* Implemented the `strategy_report()` function to generate a markdown report automatically.
* Combined all previously calculated metrics into a single summary report.
* Generated a comprehensive view of the strategy's performance, risk, and trade statistics.
* Debugged multiple Python errors related to imports, indentation, syntax, and file handling.
* Successfully generated and reviewed the final strategy report.

### What I learned

* A good trading strategy should be evaluated using multiple metrics rather than a single number.
* Total Return, Sharpe Ratio, Maximum Drawdown, Win Rate, and Profit Factor each measure different aspects of performance.
* A high win rate does not guarantee strong returns.
* Generating automated reports makes strategy evaluation much more efficient and professional.
* Small implementation details such as file encoding can cause unexpected issues.

### Where I struggled

* Debugging import errors caused by incorrect module names.
* Fixing indentation and syntax issues while integrating multiple functions into the same file.
* Resolving the Unicode encoding error caused by the ₹ symbol while saving the markdown report.
* Ensuring all metrics worked together correctly in the final report.

### How I solved problems (which Level helped most?)

* Careful debugging and reading Python error messages helped identify most issues.
* Experimentation helped verify that each metric was producing sensible results.
* AI assistance helped explain error messages and suggest fixes.
* Repeated testing ensured the report generation function worked correctly.

### What I'll do tomorrow

* Review the complete Week 3 project, clean up the codebase, and prepare for the next set of performance and risk analysis tasks.

### One-sentence reflection

Today I learned that building a strategy is only half the job; presenting and evaluating it through meaningful metrics is equally important.

# Strategy Report Card Results

Total Return: 4.55%

Annualized Return: 0.91%

Sharpe Ratio: -0.35

Maximum Drawdown: -20.26%

Win Rate: 66.67%

Number of Trades: 3

Average Win: ₹8,000.89

Average Loss: ₹-10,861.28

Profit Factor: 1.47

# What do these results tell me?

Although the strategy achieved a respectable win rate of 66.67% and a Profit Factor greater than 1, its overall performance remained weak. The annualized return was only 0.91%, which is lower than the assumed risk-free rate, resulting in a negative Sharpe Ratio.

The Maximum Drawdown of 20.26% shows that an investor would have experienced a significant decline in portfolio value during the testing period. While the strategy was profitable overall, it failed to deliver attractive risk-adjusted returns and underperformed a simple Buy-and-Hold investment.

This week's work taught me that successful investing is not just about making profitable trades but about generating consistent returns while effectively managing risk.
