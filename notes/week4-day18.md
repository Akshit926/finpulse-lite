## What I worked on today

Today I implemented the **RSI (Relative Strength Index)** trading strategy and integrated it into my existing trading pipeline. I created the RSI signal generation logic using Wilder's smoothing method, where buy signals are generated when RSI falls below 30 and sell signals are generated when RSI rises above 70. I successfully tested the complete pipeline on five NIFTY stocks: **RELIANCE, TCS, INFY, HDFCBANK, and ICICIBANK**. I also fixed several package import issues by converting absolute imports to relative imports, improved the project structure, and added debugging statements to identify why the Total Return and Annualized Return metrics were showing `NaN`.

---

## What I learned

Today I learned how the **Relative Strength Index (RSI)** works as a momentum indicator and how Wilder's smoothing is used to calculate RSI values. I understood how a modular pipeline allows multiple strategies to be tested without changing the rest of the codebase by simply passing a different strategy function. I also learned that debugging a software project often involves tracing the flow of data through different modules to identify where incorrect values are introduced.

---

## Where I struggled

I faced multiple issues while integrating the RSI strategy into the pipeline. Initially, there were several import errors due to incorrect module references and package structure. After resolving those, the pipeline executed successfully, but the **Total Return** and **Annualized Return** metrics displayed `NaN`. Through debugging, I discovered that the last value in the portfolio equity curve was `NaN`, which caused these calculations to fail. Although the rest of the backtest metrics were computed correctly, identifying the exact source of the final missing value required additional debugging.

---

## How I solved problems (which Level helped most?)

I solved the problems by fixing one issue at a time instead of changing multiple files simultaneously. I verified each module individually before testing the complete pipeline again. I used debug print statements to inspect the portfolio values and confirmed that only the last portfolio value was missing. AI assistance helped me identify package import issues, improve the project structure, and narrow down the source of the `NaN` values in the performance metrics.

---

## What I'll do tomorrow

Tomorrow I will identify and fix the remaining `NaN` issue in the portfolio value calculation so that the **Total Return** and **Annualized Return** metrics are computed correctly. After resolving this bug, I will compare the performance of the SMA and RSI strategies across multiple stocks and analyze which strategy performs better under different market conditions.

---

## One-sentence reflection

Today I learned that successful algorithmic trading projects depend not only on implementing strategies but also on carefully debugging data flow and ensuring every module works correctly together.

# Multi-Stock RSI Strategy Results

**RELIANCE** generated a **Sharpe Ratio of -0.02**, a **Maximum Drawdown of -16.85%**, and achieved an **83.33%** win rate.

**TCS** generated a **Sharpe Ratio of -0.46**, a **Maximum Drawdown of -43.92%**, and achieved a **60.00%** win rate.

**INFY** generated a **Sharpe Ratio of -0.34**, a **Maximum Drawdown of -31.68%**, and achieved an **80.00%** win rate.

**HDFCBANK** generated a **Sharpe Ratio of -0.12**, a **Maximum Drawdown of -23.25%**, and achieved an **85.71%** win rate.

**ICICIBANK** delivered the best performance with a **Sharpe Ratio of 0.40**, a **Maximum Drawdown of -11.98%**, and a **100.00%** win rate.

> **Note:** Total Return and Annualized Return are temporarily unavailable due to a debugging issue where the last portfolio value is `NaN`.

# What do these results tell me?

Running the RSI strategy on five different stocks showed that the same trading strategy can produce very different outcomes depending on the stock. ICICI Bank achieved the strongest overall performance with a positive Sharpe Ratio and a perfect win rate, while TCS experienced the largest drawdown and weaker risk-adjusted returns. The comparison reinforced the importance of evaluating trading strategies across multiple stocks instead of relying on a single example. It also highlighted the value of building a reusable pipeline, making it easy to test and compare different strategies while focusing on improving the overall quality and reliability of the trading system.
