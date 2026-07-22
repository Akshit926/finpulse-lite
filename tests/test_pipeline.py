from pipeline import run_full_pipeline

from strategy_sma import generate_signals

stocks = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS"
]

for stock in stocks:

    print("=" * 60)

    run_full_pipeline(
        stock,
        generate_signals
    )