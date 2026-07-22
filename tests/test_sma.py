import yfinance as yf
from strategy_sma import generate_signals

df = yf.download(
    "RELIANCE.NS",
    start="2015-01-01",
    auto_adjust=True
)

signals = generate_signals(df)

print("BUY SIGNALS")
print(signals[signals == 1])

print("\nSELL SIGNALS")
print(signals[signals == -1])