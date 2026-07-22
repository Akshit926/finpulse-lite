from .backtest import run_backtest
from .download_data import download_stock_data
from .metric import (
    total_return,
    annualized_return,
    max_drawdown,
    sharpe_ratio,
    trade_statistics,
)
from .summary_report import summary_report


def run_full_pipeline(symbol, strategy_func):

    print(f"\nRunning Pipeline for {symbol}")

    # Step 1: Load Stock Data
    df = download_stock_data(symbol)

    # Step 2: Generate Signals
    signals = strategy_func(df)

    # Step 3: Run Backtest
    results, trades = run_backtest(df, signals)

    # Step 4: Compute Metrics
    total_ret = total_return(results["PortfolioValue"])
    annual_ret = annualized_return(results["PortfolioValue"])
    sharpe = sharpe_ratio(results["PortfolioValue"])
    max_dd, start_date, end_date, drawdown = max_drawdown(
        results["PortfolioValue"]
    )
    stats = trade_statistics(trades)

    # Debug
    print("\nPortfolioValue (first 5):")
    print(results["PortfolioValue"].head())

    print("\nPortfolioValue (last 5):")
    print(results["PortfolioValue"].tail())

    print("\nNaN count:")
    print(results["PortfolioValue"].isna().sum())

    print("\nInitial value:", results["PortfolioValue"].iloc[0])
    print("Final value:", results["PortfolioValue"].iloc[-1])

    # Strategy Report
    summary_report(results["PortfolioValue"], trades)

    return results, trades