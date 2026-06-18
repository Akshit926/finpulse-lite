import pandas as pd
import yfinance as yf

from strategy_sma import generate_signals
from backtest import run_backtest
from metric import total_return, annualized_return

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

print("\n===== PERFORMANCE METRICS =====")

print(
    f"Total Return: {total_return(results['PortfolioValue']):.2f}%"
)

print(
    f"Annualized Return (CAGR): {annualized_return(results['PortfolioValue']):.2f}%"
)