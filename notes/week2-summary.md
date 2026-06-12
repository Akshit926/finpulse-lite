## Week 2 Self-Assessment

### 1. What does "go long" mean?

Going long means buying a stock with the expectation that its price will increase in the future.

### 2. Why must you check whether you're already holding a stock before buying again?

To avoid creating duplicate positions. If the strategy is already invested, another buy signal should be ignored.

### 3. Why are transaction costs critical to model?

Because every trade has a cost. Ignoring them can make a strategy look more profitable than it would be in real trading.

### 4. What is an equity curve?

An equity curve is a graph showing how the portfolio value changes over time during a backtest.

### 5. If your strategy underperformed Buy-and-Hold, what does that tell you about the strategy?

It suggests that the strategy did not add enough value to justify active trading during the tested period. The benchmark performed better.

### 6. Which Level of the Learning Hierarchy helped me most this week?

Experimentation and implementation helped the most. Building the strategy, debugging errors, and analyzing results made the concepts much clearer than simply reading about them.

## Week 2 Progress

### Completed Tasks

* Implemented a 50-day / 200-day SMA crossover strategy.
* Generated buy, sell, and hold signals using historical stock data.
* Built a backtesting engine to simulate trades.
* Tracked cash, shares, and portfolio value over time.
* Added transaction cost modeling (0.1% per trade).
* Compared strategy performance against a Buy-and-Hold benchmark.
* Generated and analyzed the equity curve.
* Tested the strategy on Reliance stock data.

### Project Structure

* `download_data.py` – Downloads historical stock data.
* `strategy_sma.py` – Generates SMA crossover signals.
* `backtest.py` – Executes trades and tracks portfolio performance.
* `plot_results.py` – Plots equity curve and Buy-and-Hold comparison.
* `images/RELIANCE_backtest.png` – Strategy performance visualization.

### Key Findings

* The SMA crossover strategy successfully generated trading signals and executed trades.
* Transaction costs reduce overall profitability and must be included in realistic backtests.
* The strategy did not outperform Buy-and-Hold for Reliance during the tested period.
* Beating a simple Buy-and-Hold benchmark is more difficult than it initially appears.
