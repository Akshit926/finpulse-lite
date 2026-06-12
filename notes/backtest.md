# Week 2 - Day 8: Adding Transaction Costs

## Objective

The goal was to make the backtesting framework more realistic by incorporating transaction costs into every trade execution.

---

## What Are Transaction Costs?

Transaction costs are expenses incurred whenever a trade is executed in the market.

Common costs in Indian stock trading include:

* Brokerage charges
* Securities Transaction Tax (STT)
* GST
* Exchange transaction charges
* SEBI charges
* Stamp duty

Although each cost appears small individually, their cumulative effect can significantly impact portfolio returns.

For this project, a flat transaction cost of **0.1%** was applied to every buy and sell trade.

---

## Why Use 0.1%?

A 0.1% transaction cost is a reasonable approximation of the combined trading expenses faced by retail investors in India.

Transaction Cost Rate:

0.1% = 0.001

This helps simulate real-world trading conditions rather than assuming frictionless markets.

---

## Modifications Made

### Buy Execution

Before:

Shares = Cash / Price

After:

Buy Amount = Cash × (1 − Transaction Cost)

Shares = Buy Amount / Price

A portion of capital is deducted before purchasing shares.

---

### Sell Execution

Before:

Cash = Shares × Price

After:

Cash = (Shares × Price) × (1 − Transaction Cost)

A portion of sale proceeds is deducted as trading expenses.

---

## Results

### Portfolio Value Without Transaction Costs

₹105,179.48

### Portfolio Value With Transaction Costs

₹105,179.48

### Difference

₹0.00

---

## Observation

The portfolio value remained unchanged after introducing transaction costs.

This indicates that either:

1. Transaction costs were not applied correctly in the backtesting logic, or
2. The updated code was not executed after modification.

Further debugging is required to verify that transaction costs are deducted from both buy and sell transactions.

---

## Why Transaction Costs Matter

Transaction costs directly reduce portfolio returns.

Every trade incurs a cost, meaning:

* Less capital is available for investment after buying.
* Less money is received after selling.
* Frequent trading increases cumulative costs.

Ignoring transaction costs can lead to unrealistic performance estimates.

---

## Why Is This One of the Most Important Lessons in Quant Finance?

Many trading strategies appear highly profitable when tested without costs.

However, after accounting for:

* Brokerage
* Taxes
* Slippage
* Market impact

their profitability can decrease significantly or disappear entirely.

A strategy is only truly profitable if it continues to generate returns after all real-world trading costs are considered.

For this reason, realistic transaction modeling is one of the most critical aspects of quantitative finance and algorithmic trading.

---

## Key Concepts Learned

### Backtesting Assumptions Matter

Even a small change in assumptions can materially affect strategy performance.

### Real Markets Are Not Free

Every trade has a cost attached to it.

### Gross Returns vs Net Returns

Gross Return:
Return before costs.

Net Return:
Return after all trading expenses.

Professional traders focus on net returns because they represent actual profitability.

---

## End-of-Day Outcome

Learned about real-world transaction costs in Indian markets
Modified the backtester to support transaction costs
Compared portfolio performance with and without cost
Understood the importance of realistic assumptions in quantitative finance
Learned why transaction costs are one of the biggest reasons strategies fail in live trading
