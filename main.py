from src.pipeline import run_full_pipeline
from src.strategies import generate_signals

stocks = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS"
]

for stock in stocks:
    run_full_pipeline(stock, generate_signals)