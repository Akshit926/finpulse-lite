from src.backtest import run_backtest
from src.download_data import download_stock_data
from src.metric import (
    total_return,
    annualized_return,
    max_drawdown,
    sharpe_ratio,
    trade_statistics,
)
from src.summary_report import summary_report


def run_full_pipeline(symbol, strategy_func):
    """
    Runs the complete trading pipeline.

    Parameters
    ----------
    symbol : str
        Stock symbol (e.g. RELIANCE.NS)

    strategy_func : function
        Trading strategy function (SMA or RSI)

    Returns
    -------
    dict
        {
            "results": Backtest DataFrame,
            "trades": Trade Log,
            "metrics": Performance Metrics
        }
    """

    print(f"\nRunning Pipeline for {symbol}")

    # -----------------------------------
    # Step 1: Download Data
    # -----------------------------------
    df = download_stock_data(symbol)

    # -----------------------------------
    # Step 2: Generate Trading Signals
    # -----------------------------------
    signals = strategy_func(df)

    # -----------------------------------
    # Step 3: Run Backtest
    # -----------------------------------
    results, trades = run_backtest(df, signals)

    # -----------------------------------
    # Step 4: Calculate Metrics
    # -----------------------------------
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

    # -----------------------------------
    # Print Strategy Report
    # -----------------------------------
    summary_report(
        results["PortfolioValue"],
        trades
    )

    # -----------------------------------
    # Store Metrics
    # -----------------------------------
    metrics = {
        "Total Return": total_ret,
        "Annualized Return": annual_ret,
        "Sharpe Ratio": sharpe,
        "Max Drawdown": max_dd,
        "Win Rate": stats["Win Rate"],
        "Total Trades": stats["Total Trades"],
        "Average Win": stats["Average Win"],
        "Average Loss": stats["Average Loss"],
        "Profit Factor": stats["Profit Factor"],
    }

    # -----------------------------------
    # Return Everything
    # -----------------------------------
    return {
        "results": results,
        "trades": trades,
        "metrics": metrics,
    }