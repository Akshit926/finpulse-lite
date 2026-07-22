### What I worked on today

Today I focused on improving the overall structure of my project by making it more modular and reusable. I created a `run_full_pipeline()` function that performs the complete workflow of downloading stock data, generating trading signals, running the backtest, calculating performance metrics, and generating the final report. I integrated all the modules developed during the previous weeks into a single pipeline and successfully tested it on five NIFTY stocks: RELIANCE, TCS, INFY, HDFCBANK, and ICICIBANK. I also fixed import issues, cleaned up the code, and resolved the warning that appeared during backtesting.

### What I learned

Today I understood why software projects should be divided into smaller, independent modules instead of writing everything in one large file. I learned about the Separation of Concerns principle and how it makes code easier to maintain and extend. I also learned that by passing the strategy function as an argument, the same pipeline can be reused for different trading strategies without changing the rest of the project. Testing the SMA strategy on multiple stocks also showed me that one strategy does not perform the same way across every stock.

### Where I struggled

I initially faced import errors because different files were using different function names. While combining all the modules, I had to ensure that every function accepted the correct parameters and worked together properly. I also encountered a Pandas warning while reading stock prices during backtesting and spent some time understanding why it occurred.

### How I solved problems (which Level helped most?)

I carefully read each Python error message and fixed the issues one by one instead of trying to solve everything at once. I tested every module separately before connecting them to the pipeline. AI assistance helped me understand the import issues, improve the project structure, and remove the warning from the backtesting code. Running the pipeline on five different stocks confirmed that everything was working correctly.

### What I'll do tomorrow

Tomorrow I will implement the RSI (Relative Strength Index) strategy and integrate it into the existing pipeline so that I can compare the performance of both the SMA and RSI strategies on the same set of stocks.

### One-sentence reflection

Today I learned that writing clean, modular, and reusable code is just as important as building the trading strategy itself.

# Multi-Stock SMA Strategy Results

RELIANCE generated a total return of **4.55%** with a Sharpe Ratio of **-0.35** and a win rate of **66.67%**.

TCS generated a total return of **4.72%** with a Sharpe Ratio of **-0.34** and a win rate of **33.33%**.

INFY generated a total return of **-30.27%** with a Sharpe Ratio of **-0.88** and did not produce any profitable trades.

HDFCBANK generated a total return of **9.05%** with a Sharpe Ratio of **-0.31** and achieved a **100%** win rate.

ICICIBANK generated the best performance with a total return of **50.24%**, a Sharpe Ratio of **0.20**, and a win rate of **50%**.

# What do these results tell me?

Running the same SMA crossover strategy on five different stocks clearly showed that the effectiveness of a trading strategy depends on the stock being tested. While ICICI Bank delivered excellent returns, Infosys performed poorly with a significant loss. This comparison helped me understand that no single strategy can be expected to work well for every stock. It also highlighted the importance of testing strategies across multiple stocks before making investment decisions. By creating a reusable pipeline, I have also made it much easier to test new strategies like RSI in the coming days without rewriting the entire project.
