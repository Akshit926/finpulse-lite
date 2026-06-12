# FinPulse Lite

## Project Goal

FinPulse Lite is a beginner-friendly stock market analysis and backtesting project built using Python. The project downloads historical stock data, analyzes market trends using technical indicators, generates trading signals, backtests a trading strategy, and compares its performance against a Buy-and-Hold benchmark.

The objective is to understand financial data, learn quantitative trading concepts, and build practical skills in data analysis, strategy development, and performance evaluation.

---

## Features

### Week 1

* Downloads 5 years of historical stock data
* Supports major NIFTY stocks
* Stores stock data as CSV files
* Generates stock price charts
* Calculates 50-day Moving Average (MA50)
* Calculates 200-day Moving Average (MA200)
* Saves charts as PNG images

### Week 2

* Implements a 50-day / 200-day SMA crossover strategy
* Generates Buy, Sell, and Hold signals
* Builds a custom backtesting engine
* Tracks cash, positions, and portfolio value
* Models transaction costs (0.1% per trade)
* Compares strategy performance with Buy-and-Hold
* Generates an equity curve for performance visualization

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* yfinance
* Git & GitHub

---

## Project Structure

finpulse-lite/

data/
images/
notes/
backtest.py
download_data.py
plot_backtest.py
plot_stock.py
strategy_sma.py
test_backtest.py
test_sma.py
requirements.txt
README.md
.gitignore

---

## How to Run

### 1. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Download Stock Data

```bash
python download_data.py
```

### 4. Generate Stock Charts

```bash
python plot_stock.py
```

### 5. Run SMA Strategy

```bash
python test_sma.py
```

### 6. Run Backtest

```bash
python test_backtest.py
```

### 7. Plot Strategy vs Buy-and-Hold

```bash
python plot_backtest.py
```

---

## Sample Output

The project generates:

* Stock price charts
* 50-Day Moving Average
* 200-Day Moving Average
* Buy/Sell signals
* Backtesting results
* Equity curve comparison
* Buy-and-Hold benchmark comparison

---

## Key Findings

### Reliance Backtest (5 Years)

* Initial Capital: ₹100,000
* SMA Strategy Final Value: ~₹105,000
* Buy-and-Hold Final Value: ~₹124,000

The SMA crossover strategy generated valid trading signals and executed trades successfully. However, it did not outperform a simple Buy-and-Hold approach during the tested period, highlighting the importance of benchmarking trading strategies against passive investing.

---

## Learning Outcomes

* Python scripting
* Data analysis using Pandas
* Data visualization using Matplotlib
* Technical indicators and moving averages
* Trading signal generation
* Backtesting fundamentals
* Transaction cost modeling
* Performance benchmarking
* Git version control
* Financial market basics
