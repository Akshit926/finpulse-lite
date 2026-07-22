## Week 4 Self-Assessment Questions

### 1. Why is "separation of concerns" important in software design?

Separation of concerns is important because it divides a software project into smaller, independent modules where each module is responsible for a single task. In my trading project, I created separate files for downloading stock data, generating trading signals, running backtests, calculating performance metrics, and generating reports. This modular structure makes the code easier to understand, debug, maintain, and extend. For example, I was able to add the RSI strategy without modifying the backtesting or reporting modules, demonstrating the advantage of keeping different responsibilities separate.

---

### 2. What's the difference between an SMA crossover (trend-following) and an RSI-based strategy (mean-reversion)?

An **SMA crossover** is a **trend-following strategy**. It generates buy signals when a short-term moving average crosses above a long-term moving average, indicating the beginning of an upward trend. It performs best when the market is moving strongly in one direction.

An **RSI strategy** is a **mean-reversion strategy**. It generates buy signals when the RSI falls below the oversold level (typically 30) and sell signals when it rises above the overbought level (typically 70). It assumes that prices will eventually return to their average after becoming overbought or oversold, making it more effective in sideways or range-bound markets.

---

### 3. If SMA works on TCS but RSI works on HDFC Bank, what does that suggest about TCS vs HDFC Bank's price behavior?

If the SMA strategy performs better on TCS, it suggests that **TCS exhibits stronger and more sustained price trends**, allowing a trend-following strategy to capture long-term market movements effectively.

If the RSI strategy performs better on HDFC Bank, it suggests that **HDFC Bank experiences more frequent short-term price reversals or oscillations**, making a mean-reversion strategy more suitable. This comparison shows that different stocks have different price behaviours, and selecting an appropriate trading strategy depends on the characteristics of the stock rather than applying the same strategy everywhere.

---

### 4. How am I doing with the Learning Hierarchy? Am I jumping to AI too quickly, or working through Levels 1–4 first?

I believe I have been following the Learning Hierarchy appropriately. I first completed the required reading and understood the underlying concepts before implementing them in code. I attempted to solve coding problems independently and used Python error messages and debugging techniques to identify issues before seeking AI assistance. AI was mainly used to clarify concepts, understand error messages, improve code organization, and verify my approach rather than generating complete solutions from scratch. This process helped me strengthen my understanding while still benefiting from AI as a learning and debugging assistant.
