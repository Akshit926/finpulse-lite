import os
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

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

os.makedirs("images", exist_ok=True)

plt.figure(figsize=(12, 6))

plt.plot(
    drawdown.index,
    drawdown * 100
)

plt.title("RELIANCE Strategy Drawdown Curve")
plt.xlabel("Date")
plt.ylabel("Drawdown (%)")
plt.grid(True)

plt.savefig(
    "images/RELIANCE_drawdown.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nDrawdown chart saved to:")
print("images/RELIANCE_drawdown.png")