import yfinance as yf

from backtest import run_backtest

from metric import (
    total_return,
    annualized_return,
    sharpe_ratio,
    max_drawdown,
    trade_statistics
)

from summary_report import summary_report

def run_full_pipeline(symbol, strategy_func):

    print(f"\nRunning Pipeline for {symbol}")

    # Step 1: Load Stock Data
    df = yf.download(
        symbol,
        period="5y",
        auto_adjust=True
    )

    # Step 2: Generate Signals
    signals = strategy_func(df)

    # Step 3: Run Backtest
    results, trades = run_backtest(df, signals)

    # Step 4: Compute Metrics
    total_ret = total_return(results["PortfolioValue"])

    annual_ret = annualized_return(
        results["PortfolioValue"]
    )

    sharpe = sharpe_ratio(
        results["PortfolioValue"]
    )

    max_dd, start_date, end_date, drawdown = max_drawdown(
        results["PortfolioValue"]
    )

    stats = trade_statistics(trades)


    # Generate Markdown Report
    summary_report(
    results["PortfolioValue"],
    trades
)

    return results, trades