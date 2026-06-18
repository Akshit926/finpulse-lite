import pandas as pd

def total_return(equity_curve):

    initial_value = equity_curve.iloc[0]
    final_value = equity_curve.iloc[-1]

    return ((final_value / initial_value) - 1) * 100


def annualized_return(equity_curve):

    initial_value = equity_curve.iloc[0]
    final_value = equity_curve.iloc[-1]

    years = len(equity_curve) / 252

    return (((final_value / initial_value) ** (1 / years)) - 1) * 100


def max_drawdown(equity_curve):

    rolling_max = equity_curve.cummax()

    drawdown = (
        (equity_curve - rolling_max)
        / rolling_max
    )

    end_date = drawdown.idxmin()

    start_date = equity_curve.loc[:end_date].idxmax()

    max_dd = drawdown.min() * 100

    return max_dd, start_date, end_date, drawdown

import numpy as np

def sharpe_ratio(
    equity_curve,
    risk_free_rate=0.065
):

    daily_returns = equity_curve.pct_change().dropna()

    annual_return = (
        daily_returns.mean() * 252
    )

    annual_volatility = (
        daily_returns.std() * np.sqrt(252)
    )

    sharpe = (
        annual_return - risk_free_rate
    ) / annual_volatility

    return sharpe

    
def trade_statistics(trade_log):

    profits = []

    for i in range(0, len(trade_log) - 1, 2):

        buy_trade = trade_log.iloc[i]
        sell_trade = trade_log.iloc[i + 1]

        buy_price = buy_trade["Price"]
        sell_price = sell_trade["Price"]

        shares = buy_trade["Shares"]

        profit = (
            sell_price - buy_price
        ) * shares

        profits.append(profit)

    total_trades = len(profits)

    winning_trades = [
        p for p in profits if p > 0
    ]

    losing_trades = [
        p for p in profits if p < 0
    ]

    win_rate = (
        len(winning_trades)
        / total_trades
        * 100
    ) if total_trades > 0 else 0

    avg_win = (
        sum(winning_trades)
        / len(winning_trades)
    ) if winning_trades else 0

    avg_loss = (
        sum(losing_trades)
        / len(losing_trades)
    ) if losing_trades else 0

    profit_factor = (
        sum(winning_trades)
        / abs(sum(losing_trades))
    ) if losing_trades else float("inf")

    return {
        "Total Trades": total_trades,
        "Win Rate": win_rate,
        "Average Win": avg_win,
        "Average Loss": avg_loss,
        "Profit Factor": profit_factor
    }
    
def summary_report(
    equity_curve,
    trade_log
):

    stats = trade_statistics(
        trade_log
    )

    max_dd, start_date, end_date, _ = (
        max_drawdown(equity_curve)
    )

    print("\n===== STRATEGY REPORT CARD =====")

    print(
        f"Total Return: {total_return(equity_curve):.2f}%"
    )

    print(
        f"Annualized Return: {annualized_return(equity_curve):.2f}%"
    )

    print(
        f"Sharpe Ratio: {sharpe_ratio(equity_curve):.2f}"
    )

    print(
        f"Max Drawdown: {max_dd:.2f}%"
    )

    print(
        f"Total Trades: {stats['Total Trades']}"
    )

    print(
        f"Win Rate: {stats['Win Rate']:.2f}%"
    )

    print(
        f"Average Win: ₹{stats['Average Win']:.2f}"
    )

    print(
        f"Average Loss: ₹{stats['Average Loss']:.2f}"
    )

    print(
        f"Profit Factor: {stats['Profit Factor']:.2f}"
    )