from src.nifty50 import NIFTY50
from src.pipeline import run_full_pipeline
from src.strategy_sma import generate_signals
from src.strategy_rsi import generate_rsi_signals

import pandas as pd

results = []

print("=" * 60)
print("Running strategies on all NIFTY 50 stocks")
print("=" * 60)

for stock in NIFTY50:

    print(f"Running {stock}...")

    try:
        sma = run_full_pipeline(stock, generate_signals)
        rsi = run_full_pipeline(stock, generate_rsi_signals)

        sma_metrics = sma["metrics"]
        rsi_metrics = rsi["metrics"]

        results.append({
            "Stock": stock,

            # SMA Metrics
            "SMA Return": sma_metrics["Total Return"],
            "SMA Annualized Return": sma_metrics["Annualized Return"],
            "SMA Sharpe": sma_metrics["Sharpe Ratio"],
            "SMA Max Drawdown": sma_metrics["Max Drawdown"],
            "SMA Trades": sma_metrics["Total Trades"],

            # RSI Metrics
            "RSI Return": rsi_metrics["Total Return"],
            "RSI Annualized Return": rsi_metrics["Annualized Return"],
            "RSI Sharpe": rsi_metrics["Sharpe Ratio"],
            "RSI Max Drawdown": rsi_metrics["Max Drawdown"],
            "RSI Trades": rsi_metrics["Total Trades"],

            # Best Strategy
            "Better Strategy": (
                "SMA"
                if sma_metrics["Total Return"] >= rsi_metrics["Total Return"]
                else "RSI"
            )
        })

        print("✓ Completed")

    except Exception as e:
        print(f"✗ Error processing {stock}: {e}")

leaderboard = pd.DataFrame(results)

leaderboard.sort_values(
    by="SMA Sharpe",
    ascending=False,
    inplace=True
)

leaderboard.to_csv(
    "strategy_comparison.csv",
    index=False
)

print("\n" + "=" * 60)
print("Analysis Complete!")
print("=" * 60)

print(f"Stocks Processed: {len(leaderboard)}")

print("\nTop 5 Stocks (SMA Sharpe)")
print(
    leaderboard[
        ["Stock", "SMA Sharpe", "SMA Return"]
    ].head(5)
)

print("\nSaved to strategy_comparison.csv")