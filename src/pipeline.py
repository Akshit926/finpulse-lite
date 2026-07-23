from src.backtest import run_backtest
from src.download_data import download_stock_data
from src.metric import (
    total_return,
    annualized_return,
    max_drawdown,
    sharpe_ratio,
    trade_statistics,
)
from src.metric import summary_report


def run_full_pipeline(symbol, strategy_func):
    """
    Runs the complete trading pipeline.
    """

    print(f"\nRunning Pipeline for {symbol}")

    # -----------------------------------
    # Step 1: Download Data
    # -----------------------------------
    df = download_stock_data(symbol)

    # -----------------------------------
    # Step 2: Generate Signals
    # -----------------------------------
    signals = strategy_func(df)

    # -----------------------------------
    # Step 3: Run Backtest
    # -----------------------------------
    results, trades = run_backtest(df, signals)

    # -----------------------------------
    # Strategy Metrics
    # -----------------------------------
    total_ret = total_return(results["PortfolioValue"])

    annual_ret = annualized_return(
        results["PortfolioValue"]
    )

    sharpe = sharpe_ratio(
        results["PortfolioValue"]
    )

    max_dd, _, _, _ = max_drawdown(
        results["PortfolioValue"]
    )

    stats = trade_statistics(trades)

    summary_report(
        results["PortfolioValue"],
        trades
    )

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
    # Buy & Hold Metrics
    # -----------------------------------
    buy_hold = results["BuyHoldValue"]

    buy_hold_metrics = {
        "Total Return": total_return(buy_hold),
        "Annualized Return": annualized_return(buy_hold),
        "Sharpe Ratio": sharpe_ratio(buy_hold),
        "Max Drawdown": max_drawdown(buy_hold)[0],
    }

    # -----------------------------------
    # Return Everything
    # -----------------------------------
    return {
        "results": results,
        "trades": trades,
        "metrics": metrics,
        "buy_hold_metrics": buy_hold_metrics,
    }