Today's Goal

Expand FinPulse Lite to support all NIFTY 50 stocks by automating strategy execution across multiple companies. The focus was on eliminating manual testing and generating comparative performance results for every stock.

Tasks Completed
Created a complete list of NIFTY 50 stock tickers.
Developed a script to execute both SMA and RSI strategies for every stock.
Automated the collection of key performance metrics, including Total Return and Sharpe Ratio.
Generated a consolidated CSV report containing results for all stocks.
Compared the performance of both strategies to identify the better-performing strategy for each stock.
Key Learnings
Automation significantly reduces the effort required to evaluate multiple assets.
Organizing stock symbols into a dedicated module improves code maintainability.
Exporting results to CSV enables further analysis using spreadsheet tools or Python.
Challenges Faced
Handling errors for individual stocks without interrupting the execution of the entire batch.
Managing execution time when running backtests across 50 stocks.
How the Challenges Were Solved
Used try-except blocks so that failures for one stock did not stop the remaining executions.
Stored results in a list of dictionaries and converted them into a Pandas DataFrame for easy export and analysis.
Reflection

Today's work transformed FinPulse Lite from a single-stock analysis tool into a scalable portfolio evaluation system. By automating strategy testing across all NIFTY 50 stocks, the project became more efficient and capable of generating broader market insights, laying the foundation for portfolio-level analysis and future deployment.