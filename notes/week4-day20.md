# Friday — Mid-Internship Review with Manager

## What's working?

The project has become much more organized and modular compared to the beginning of the internship. I have successfully built a reusable trading pipeline that can download stock data, generate trading signals, run backtests, calculate performance metrics, and generate strategy reports. Both the SMA Crossover and RSI strategies are integrated into the same pipeline, making it easy to test different strategies on multiple stocks without rewriting the code. The project is now able to backtest five NIFTY stocks automatically and generate meaningful performance statistics such as Sharpe Ratio, Maximum Drawdown, Win Rate, and Profit Factor.

---

## What's hard?

The most challenging part has been debugging the project as it has grown larger. Small issues such as incorrect imports, package structure, and missing values in the portfolio calculations can affect the final output significantly. Recently, I encountered a bug where the Total Return and Annualized Return metrics displayed `NaN` because the final portfolio value was missing. Finding the exact source of the issue required tracing data through multiple modules and understanding how each component interacted with the others.

---

## Am I enjoying it?

Yes. I have enjoyed working on this internship because it combines Python programming, financial markets, and software engineering. Building the project step by step has helped me understand how real-world trading systems are developed. Although debugging can sometimes be challenging, solving these problems has improved both my programming and analytical thinking skills.

---

## Any scope changes needed?

At this stage, I believe the project scope is appropriate. After fixing the remaining portfolio value issue, I would like to extend the project by adding more technical indicators, comparing additional trading strategies, visualizing the results with charts, and improving the reporting system. These enhancements would make the project more practical and closer to a real-world quantitative trading application.

---

# Project Summary

Over the first half of the internship, I have built a modular quantitative trading system capable of:

* Downloading historical stock data using Yahoo Finance.
* Implementing the SMA Crossover strategy.
* Implementing the RSI strategy.
* Running automated backtests with transaction costs.
* Calculating performance metrics including Total Return, Annualized Return, Sharpe Ratio, Maximum Drawdown, Win Rate, Average Win, Average Loss, and Profit Factor.
* Comparing strategies across multiple NIFTY stocks.
* Generating reusable strategy reports through a common pipeline.

---

# Code Structure

The project follows a modular structure where each component has a specific responsibility.

```text
finpulse-lite/
│
├── src/
│   ├── download_data.py
│   ├── strategy_sma.py
│   ├── strategy_rsi.py
│   ├── backtest.py
│   ├── metric.py
│   ├── summary_report.py
│   └── pipeline.py
│
├── tests/
│   ├── test_pipeline.py
│   ├── test_rsi.py
│   ├── test_metric.py
│   └── test_backtest.py
│
├── reports/
├── data/
├── main.py
└── README.md
```

This modular design makes it easy to add new strategies or performance metrics without changing the rest of the project.

---

# Report Card Examples

### Good Result – ICICIBANK (RSI Strategy)

The RSI strategy performed exceptionally well on ICICI Bank. It achieved a positive Sharpe Ratio of **0.40**, a **100% Win Rate**, a relatively low Maximum Drawdown of **11.98%**, and an infinite Profit Factor because no losing trades were recorded. This indicates that the RSI strategy matched the price behaviour of ICICI Bank very effectively.

### Challenging Result – TCS (RSI Strategy)

The RSI strategy on TCS produced mixed results. Although it achieved a **60% Win Rate**, it also experienced a large Maximum Drawdown of **43.92%** and a negative Sharpe Ratio of **−0.46**. This demonstrated that a higher win rate alone does not necessarily indicate better overall performance, as the losses were comparatively larger.

---

# My Learning So Far

Over the first half of the internship, I have gained experience in several important areas:

* Working with financial data using Pandas and Yahoo Finance.
* Implementing technical indicators such as SMA and RSI.
* Building reusable and modular Python projects.
* Writing backtesting logic for trading strategies.
* Measuring strategy performance using financial metrics.
* Comparing multiple trading strategies across different stocks.
* Debugging larger Python projects using a systematic approach.
* Understanding that software quality and clean architecture are as important as implementing the trading strategy itself.

---

# Mid-Internship Reflection

The first half of the internship has shown me that developing a quantitative trading system involves much more than writing trading logic. It requires clean software architecture, careful debugging, thorough testing, and continuous performance evaluation. I now have a much stronger understanding of how algorithmic trading systems are designed, tested, and improved, and I feel confident about building more advanced strategies during the remaining weeks of the internship.
