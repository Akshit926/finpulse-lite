import yfinance as yf

from src.strategy_rsi import generate_rsi_signals

df = yf.download(
    "RELIANCE.NS",
    period="5y",
    auto_adjust=True
)

signals = generate_rsi_signals(df)

print(signals[signals != 0])