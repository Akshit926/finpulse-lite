import os
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

from strategy_sma import generate_signals
from backtest import run_backtest

df = yf.download(
    "RELIANCE.NS",
    period="5y",
    auto_adjust=True
)

if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

df = df.dropna()

signals = generate_signals(df)

results, trades = run_backtest(
    df,
    signals,
    transaction_cost=0.001
)

initial_capital = 100000

buy_hold = initial_capital * (
    df["Close"] / df["Close"].iloc[0]
)

os.makedirs("images", exist_ok=True)

plt.figure(figsize=(12, 6))

plt.plot(
    results.index,
    results["PortfolioValue"],
    label="SMA Strategy"
)

plt.plot(
    buy_hold.index,
    buy_hold,
    label="Buy & Hold"
)

plt.title("RELIANCE: SMA Strategy vs Buy & Hold")
plt.xlabel("Date")
plt.ylabel("Portfolio Value (₹)")
plt.legend()
plt.grid(True)

plt.savefig(
    "images/RELIANCE_backtest.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nStrategy Final Value:")
print(f"₹{results['PortfolioValue'].iloc[-1]:,.2f}")

print("\nBuy & Hold Final Value:")
print(f"₹{buy_hold.iloc[-1]:,.2f}")