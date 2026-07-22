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

    for date in df.index:

        # Get closing price
        close_price = df.loc[date, "Close"]

        if isinstance(close_price, pd.Series):
            price = float(close_price.iloc[0])
        else:
            price = float(close_price)

        signal = signals.loc[date]

        # BUY
        if signal == 1 and not position:

            buy_amount = cash * (1 - transaction_cost)
            shares = buy_amount / price
            cash = 0
            position = True

            trades.append([
                date,
                "BUY",
                price,
                shares,
                cash
            ])

        # SELL
        elif signal == -1 and position:

            shares_sold = shares
            sale_value = shares_sold * price
            cash = sale_value * (1 - transaction_cost)

            trades.append([
                date,
                "SELL",
                price,
                shares_sold,
                cash
            ])

            shares = 0
            position = False

        # Portfolio Value
        portfolio_value = cash + (shares * price)
        portfolio_values.append(portfolio_value)

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