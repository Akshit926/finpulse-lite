import pandas as pd
import yfinance as yf

from strategy_sma import generate_signals
from backtest import run_backtest

# Download data
df = yf.download(
    "RELIANCE.NS",
    period="5y",
    auto_adjust=True
)

# Fix MultiIndex columns from yfinance
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

# Remove NaN rows
df = df.dropna()

# Generate signals
signals = generate_signals(df)

# Backtest WITHOUT transaction costs
results_no_cost, trades_no_cost = run_backtest(
    df,
    signals,
    transaction_cost=0
)

# Backtest WITH transaction costs
results_cost, trades_cost = run_backtest(
    df,
    signals,
    transaction_cost=0.001
)

# Final values
final_no_cost = results_no_cost["PortfolioValue"].iloc[-1]
final_cost = results_cost["PortfolioValue"].iloc[-1]

difference = final_no_cost - final_cost

print("\n===== BACKTEST COMPARISON =====")
print(f"Portfolio Value (No Cost): ₹{final_no_cost:,.2f}")
print(f"Portfolio Value (With Cost): ₹{final_cost:,.2f}")
print(f"Impact of Transaction Costs: ₹{difference:,.2f}")

print("\n===== TRADE LOG (WITH COSTS) =====")
print(trades_cost)