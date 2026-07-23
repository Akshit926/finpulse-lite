# FinPulse Lite

## Project Goal

FinPulse Lite is a Python-based quantitative trading strategy backtesting platform designed to help users analyze stock market performance using technical analysis. The application downloads historical stock data, generates trading signals, backtests multiple trading strategies, evaluates portfolio performance, and compares results with a Buy-and-Hold benchmark through an interactive Streamlit dashboard.

The project focuses on learning quantitative finance, algorithmic trading concepts, financial data analysis, and Python application development. It provides an end-to-end workflow from data collection to strategy evaluation, enabling users to understand how different technical indicators perform on real market data.

---

## Features

### Week 1

* Downloads 5 years of historical stock data
* Supports NIFTY 50 stocks
* Stores downloaded data as CSV files
* Generates stock price charts
* Calculates 50-Day Simple Moving Average (SMA)
* Calculates 200-Day Simple Moving Average (SMA)
* Saves stock charts for analysis

### Week 2

* Implements a 50-Day / 200-Day SMA Crossover strategy
* Generates Buy, Sell, and Hold signals
* Builds a custom backtesting engine
* Simulates portfolio performance
* Models transaction costs (0.1% per trade)
* Compares strategy performance with Buy-and-Hold
* Generates equity curve visualizations

### Week 3

* Calculates Total Return
* Calculates Annualized Return (CAGR)
* Computes Sharpe Ratio
* Calculates Maximum Drawdown
* Generates trade statistics
* Computes Win Rate
* Calculates Average Win and Average Loss
* Computes Profit Factor
* Generates automated Strategy Report Cards

### Week 4

* Implements Relative Strength Index (RSI) strategy
* Supports configurable RSI parameters
* Compares SMA and RSI strategies
* Backtests multiple NIFTY 50 stocks
* Builds a strategy comparison leaderboard
* Identifies the better-performing strategy for each stock

### Week 5

* Develops an interactive Streamlit dashboard
* Allows stock selection from the sidebar
* Supports real-time strategy parameter tuning
* Displays performance metrics
* Visualizes portfolio equity curves
* Compares Strategy vs Buy-and-Hold interactively

### Week 6

* Adds strategy comparison dashboard
* Displays comparative performance tables
* Generates Top 10 and Bottom 10 strategy leaderboards
* Enables stock-wise report selection
* Automates performance comparison across multiple stocks

### Week 7

* Improves application structure
* Modularizes project components
* Enhances error handling
* Optimizes data processing pipeline
* Improves project maintainability

### Week 8

* Professional project documentation
* Comprehensive README
* Function docstrings
* Architecture overview
* Local setup guide
* Project limitations and future enhancements
* MIT License

---

## Technologies Used

* Python
* Pandas
* NumPy
* Plotly
* Streamlit
* yfinance
* Git
* GitHub

---

## Project Structure

```
finpulse-lite/

├── app.py
├── run_all_stocks.py
├── strategy_comparison.csv
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│
├── docs/
│   └── dashboard.png
│
└── src/
    ├── backtest.py
    ├── download_data.py
    ├── metric.py
    ├── nifty50.py
    ├── pipeline.py
    ├── strategy_rsi.py
    ├── strategy_sma.py
    └── summary_report.py
```

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/finpulse-lite.git
cd finpulse-lite
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Generate Leaderboard

```bash
python run_all_stocks.py
```

### 6. Run the Dashboard

```bash
python -m streamlit run app.py
```

---

## Sample Output

The project generates:

* Historical stock price datasets
* SMA and RSI trading signals
* Portfolio equity curves
* Buy-and-Hold benchmark comparison
* Performance metrics dashboard
* Strategy comparison tables
* Interactive Plotly visualizations
* Multi-stock leaderboard
* Strategy report cards

---

## Key Findings

### Reliance Industries Limited (5-Year Backtest)

* Initial Capital: ₹100,000
* Final Portfolio Value: ₹102,026.61
* Total Return: 2.03%
* Annualized Return: 0.41%
* Sharpe Ratio: -0.39
* Maximum Drawdown: -20.35%
* Total Trades: 3
* Win Rate: 33.33%

The project demonstrates how different technical trading strategies perform under realistic market conditions. It highlights that strategy evaluation should consider multiple performance metrics rather than relying solely on returns. Comparing strategies against a Buy-and-Hold benchmark provides valuable insights into their effectiveness.

---

## Learning Outcomes

* Python application development
* Financial data analysis using Pandas
* Technical analysis using SMA and RSI
* Trading signal generation
* Quantitative strategy development
* Portfolio backtesting
* Transaction cost simulation
* Risk-adjusted performance evaluation
* Strategy benchmarking
* Interactive dashboard development with Streamlit
* Data visualization using Plotly
* Git and GitHub version control
* Software documentation and project packaging