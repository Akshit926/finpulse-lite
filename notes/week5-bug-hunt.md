Here's a clean **`notes/week5-bug-hunt.md`** that you can directly add to your project.

````markdown
# Week 5 – Bug Hunt

## Objective

The objective of today's task was to learn about **Lookahead Bias**, **Survivorship Bias**, and audit my existing trading system to identify whether my backtesting implementation suffers from any of these issues.

---

## What is Lookahead Bias?

Lookahead bias occurs when a trading strategy accidentally uses information from the future to make decisions in the past. This makes the backtest results appear much better than they would be in real-world trading because the strategy has access to information that would not have been available at the time of making the trade.

A common example is generating a trading signal using today's closing price and executing the trade at the same closing price. Since the closing price is only known after the market closes, it cannot be used to place a trade at that same price.

---

## What is Survivorship Bias?

Survivorship bias occurs when a trading strategy is tested only on companies that currently exist while ignoring companies that were delisted or failed in the past. This can produce overly optimistic backtesting results because unsuccessful companies are excluded from the analysis.

My current project uses a few existing NIFTY stocks for learning purposes, so survivorship bias is not directly addressed in this project.

---

# Code Audit

## 1. Signal and Execution Timing

### Current Implementation

In my `run_backtest()` function, trading signals are generated using the current day's closing price and the trade is executed immediately using the same day's closing price.

```python
signal = signals.loc[date]
price = df.loc[date, "Close"]

if signal == 1:
    buy(price)
```

### Finding

This introduces **Lookahead Bias**.

The strategy assumes that today's closing price is already known before placing the trade, which is not possible in real trading. The closing price is only available after the trading session has ended.

### Correct Approach

The signal should be generated using today's available data, but the trade should be executed on the next trading day (Day t+1). This removes the future information leak and makes the backtest more realistic.

---

## 2. Indicator Computation

The SMA strategy uses rolling moving averages and the RSI strategy uses exponential moving averages (EWM).

These indicators are calculated only using historical data up to the current trading day.

### Finding

No lookahead bias was found in the indicator calculations.

---

## 3. Data Preprocessing

The project currently downloads historical stock prices directly from Yahoo Finance and does not perform normalization or scaling before backtesting.

### Finding

No lookahead bias was found in the preprocessing stage.

---

## Additional Issue Found

During the audit, I also noticed that the last portfolio value occasionally becomes `NaN`, causing the Total Return and Annualized Return metrics to return `NaN`. This issue is unrelated to lookahead bias and will be investigated separately.

---

## Impact of Lookahead Bias

If lookahead bias is not removed, the backtest can produce unrealistically high returns, higher win rates, and better Sharpe Ratios than would be achievable in live trading. This can lead to incorrect conclusions about a strategy's performance.

---

## Plan to Fix

To eliminate lookahead bias, I will modify the backtesting engine so that:

- Trading signals are generated using today's available data.
- Trades are executed on the next trading day instead of the same day.
- Signal generation and trade execution are treated as separate steps.

This change will make the backtesting results more realistic and representative of actual market conditions.

---

## Discussion with Manager

After auditing my project, I found that my backtesting engine currently suffers from **signal/execution timing lookahead bias** because trades are executed using the same day's closing price that generated the signal. The indicator calculations (SMA and RSI) and data preprocessing do not introduce lookahead bias. My next step will be to update the backtesting logic so that trades are executed on the following trading day, making the simulation more realistic.
````