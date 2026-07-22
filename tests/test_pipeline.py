from src.pipeline import run_full_pipeline
from src.strategy_rsi import generate_rsi_signals

stocks = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS"
]

for stock in stocks:
    print("=" * 60)
    print(f"Running RSI Pipeline for {stock}")
    run_full_pipeline(stock, generate_rsi_signals)