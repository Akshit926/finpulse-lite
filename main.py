from src.pipeline import run_full_pipeline
from src.strategy_sma import generate_signals
from src.strategy_rsi import generate_rsi_signals

stocks = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS"
]

print("\n===== SMA STRATEGY =====\n")
for stock in stocks:
    run_full_pipeline(stock, generate_signals)

print("\n===== RSI STRATEGY =====\n")
for stock in stocks:
    run_full_pipeline(stock, generate_rsi_signals)