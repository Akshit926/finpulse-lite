def summary_report(
    equity_curve,
    trade_log
):

    from metric import (
    total_return,
    annualized_return,
    max_drawdown,
    sharpe_ratio,
    trade_statistics
)

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