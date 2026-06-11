import pandas as pd 
import yfinance as yf

from strategy_sma import generate_signals
from backtest import run_backtest

df = yf.download(
"RELIANCE.NS",
period="5y",
auto_adjust=True
)
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)
df =df.dropna()
signals = generate_signals(df)

results, trades = run_backtest(df, signals)

print("\nTRADE LOG")
print(trades)

print("\nFINAL PORTFOLIO VALUE")
print(f"{results['PortfolioValue'].iloc[-1]:,.2f}")
