import pandas as pd


def run_backtest(
    df,
    signals,
    initial_capital=100000,
    transaction_cost=0.001
):

    cash = initial_capital
    shares = 0
    position = False

    portfolio_values = []
    trades = []

    # Loop until the second-last day
    for i in range(len(df) - 1):

        date = df.index[i]
        next_date = df.index[i + 1]

        # Today's closing price (for portfolio valuation)
        today_price = float(df.loc[date, "Close"])

        # Next day's closing price (for trade execution)
        next_price = float(df.loc[next_date, "Close"])

        # Today's signal
        signal = signals.loc[date]

        # BUY on next day's price
        if signal == 1 and not position:

            buy_amount = cash * (1 - transaction_cost)
            shares = buy_amount / next_price
            cash = 0
            position = True

            trades.append([
                next_date,
                "BUY",
                next_price,
                shares,
                cash
            ])

        # SELL on next day's price
        elif signal == -1 and position:

            shares_sold = shares
            sale_value = shares_sold * next_price
            cash = sale_value * (1 - transaction_cost)

            trades.append([
                next_date,
                "SELL",
                next_price,
                shares_sold,
                cash
            ])

            shares = 0
            position = False

        # Portfolio value at today's close
        portfolio_value = cash + (shares * today_price)
        portfolio_values.append(portfolio_value)

    # Add portfolio value for the final trading day
    last_price = float(df["Close"].iloc[-1])
    portfolio_values.append(cash + (shares * last_price))

    # Results DataFrame
    results = pd.DataFrame(index=df.index)
    results["PortfolioValue"] = portfolio_values

    # Trade Log
    trades_df = pd.DataFrame(
        trades,
        columns=[
            "Date",
            "Action",
            "Price",
            "Shares",
            "Cash"
        ]
    )

    return results, trades_df