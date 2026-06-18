### 1. Why is annualized return more meaningful than total return?

Total return only tells us how much money was gained overall, but it doesn't tell us how long it took to achieve that return.

For example, a 50% return in one year is much better than a 50% return in five years. Annualized return (CAGR) converts performance into an average yearly growth rate, making it easier to compare different investments fairly.

---

### 2. If a strategy has 20% return but 50% max drawdown, would you use it? Why?

Probably not.

A 50% drawdown means losing half of the portfolio value at some point. Even though the returns are attractive, such a large drawdown can be emotionally difficult to tolerate and may cause investors to exit the strategy at the worst possible time.

I would prefer a strategy with slightly lower returns but significantly lower drawdowns.

---

### 3. What does a Sharpe of 0.5 vs 2.0 represent intuitively?

A Sharpe Ratio of 0.5 means the strategy is generating relatively low returns for the amount of risk taken.

A Sharpe Ratio of 2.0 means the strategy is generating strong returns while taking risk efficiently.

Intuitively, a higher Sharpe Ratio means I am being rewarded more for every unit of risk I take.

---

### 4. Why might a strategy with 80% win rate still lose money?

Because win rate only tells us how often we win, not how much we win.

For example:

```text
8 winning trades = +₹1,000 each
2 losing trades = -₹10,000 each
```

Total Profit:

```text
₹8,000 - ₹20,000 = -₹12,000
```

Even with an 80% win rate, the strategy loses money because the losses are much larger than the gains.

This is why average win and average loss are important metrics.

---

### 5. What does the formula std × √252 represent?

The formula:

is used to convert daily volatility into annual volatility.

Since there are approximately 252 trading days in a year, multiplying daily standard deviation by √252 gives an estimate of yearly volatility.

This allows us to compare risk on an annual basis and is required when calculating metrics such as the Sharpe Ratio.

---

### 6. Did I use the Learning Hierarchy properly this week?

Yes.

I first studied the concepts through documentation and educational resources such as Investopedia and Pandas documentation. I implemented the code myself, tested it on my own strategy, and used AI only to clarify concepts, understand formulas, interpret results, and debug issues when necessary.

The majority of the learning came from reading, experimentation, and implementation rather than copying solutions, which aligns with the Learning Hierarchy principles.
