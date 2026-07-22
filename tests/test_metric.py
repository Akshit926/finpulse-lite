import pandas as pd
import yfinance as yf

from strategy_sma import generate_signals
from backtest import run_backtest
from metric import max_drawdown

df = yf.download(
    "RELIANCE.NS",
    period="5y",
    auto_adjust=True
)

if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

df = df.dropna()

signals = generate_signals(df)

results, trades = run_backtest(df, signals)

max_dd, start_date, end_date, drawdown = max_drawdown(
    results["PortfolioValue"]
)

print("\n===== MAXIMUM DRAWDOWN =====")
print(f"Max Drawdown: {max_dd:.2f}%")
print(f"Start Date: {start_date}")
print(f"End Date: {end_date}")