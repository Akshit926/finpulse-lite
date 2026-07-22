Here are concise but strong answers suitable for your Week 5 self-assessment.

### 1. Explain lookahead bias in your own words. Give an example.

Lookahead bias occurs when a trading strategy uses information that would not have been available at the time a trading decision was made. This makes the backtest unrealistically optimistic because it is effectively using future data.

**Example:** In my backtesting project, I initially generated a BUY signal and executed the trade using the same day's closing price. Since the closing price is only known after the market closes, the strategy was using future information. I fixed this by executing trades on the **next trading day's close**, making the backtest realistic.

---

### 2. Why is survivorship bias a problem for backtesting?

Survivorship bias occurs when a backtest uses only stocks that still exist today while ignoring companies that were delisted, went bankrupt, or were acquired. This makes historical performance appear better than it actually was because poor-performing companies are excluded from the analysis.

**Example:** If I backtest only today's NIFTY 50 companies over the last 10 years, I ignore companies that dropped out of the index due to poor performance. As a result, the strategy may appear more profitable than it would have been in real market conditions.

---

### 3. Why are unit tests valuable? (Beyond "to find bugs.")

Unit tests improve the reliability and maintainability of software by verifying that individual functions behave as expected. They act as a safety net when modifying code, help detect unintended side effects, make debugging easier by isolating problems, and increase confidence that existing functionality continues to work correctly. They also serve as documentation by clearly defining the expected behavior of each function.

---

### 4. If you change one line of code, how do unit tests help you sleep at night?

After making a change, I can run my unit tests to quickly verify that the rest of the system still works correctly. If all tests pass, I have confidence that the change did not accidentally break existing functionality. If a test fails, it immediately points me toward the affected part of the code, making debugging much faster. This allows me to refactor and improve the code with confidence instead of worrying about introducing hidden bugs.
