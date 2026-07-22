## What I worked on today

Today I compared the performance of my **SMA Crossover** and **RSI (Relative Strength Index)** strategies across five NIFTY stocks: RELIANCE, TCS, INFY, HDFCBANK, and ICICIBANK. I ran the RSI strategy through the reusable trading pipeline that I developed earlier and analyzed its performance using metrics such as Sharpe Ratio, Maximum Drawdown, Win Rate, Average Win, Average Loss, and Profit Factor. I also compared these results with those obtained from the SMA strategy to understand how different strategies perform on different stocks. During testing, I identified a bug where the Total Return and Annualized Return metrics were showing `NaN` values and started debugging the issue by tracing the portfolio value calculations.

---

## What I learned

Today I learned that there is no single trading strategy that performs best across all stocks. While the RSI strategy performed better for some stocks like RELIANCE, INFY, and ICICIBANK, the SMA strategy remained more effective for HDFCBANK, and both strategies showed mixed performance on TCS. I also understood that evaluating a strategy requires considering multiple performance metrics instead of focusing only on returns. Metrics such as Sharpe Ratio, Maximum Drawdown, and Win Rate provide a more complete picture of a strategy's performance and risk.

---

## Where I struggled

The biggest challenge today was understanding why the Total Return and Annualized Return metrics were displaying `NaN` even though the backtesting process and the other performance metrics were working correctly. After investigating the issue, I found that the last value of the portfolio equity curve was `NaN`, which caused these calculations to fail. Identifying the exact source of this missing value required careful debugging of the pipeline and backtesting process.

---

## How I solved problems (which Level helped most?)

I solved the issues by debugging the project step by step instead of modifying multiple components simultaneously. I verified the outputs of each module individually, added debugging statements to inspect the portfolio values, and confirmed that only the last portfolio value was missing. AI assistance helped me understand the debugging process, interpret the outputs correctly, and narrow down the issue to the portfolio value calculation rather than the trading strategy itself.

---

## What I'll do tomorrow

Tomorrow I will fix the remaining `NaN` issue in the portfolio value calculation so that the Total Return and Annualized Return metrics are computed correctly. After resolving the bug, I will complete the final comparison between the SMA and RSI strategies and document the overall findings from the backtesting experiments.

---

## One-sentence reflection

Today I learned that comparing trading strategies effectively requires analyzing multiple performance metrics and carefully debugging the underlying calculations before drawing conclusions.

---

## What do these results tell me?

The comparison between the SMA and RSI strategies clearly showed that **no single strategy works best for every stock**. The RSI strategy generally produced better risk-adjusted performance on RELIANCE, INFY, and ICICIBANK by achieving higher win rates and better Sharpe Ratios. The SMA strategy remained more consistent for HDFCBANK, while TCS demonstrated that a higher win rate alone does not guarantee better overall performance because larger drawdowns can reduce the effectiveness of a strategy. This comparison helped me understand the importance of testing strategies across multiple stocks and evaluating them using several performance metrics rather than relying on a single measure. It also reinforced the value of building a reusable pipeline that makes experimenting with different trading strategies much easier.
