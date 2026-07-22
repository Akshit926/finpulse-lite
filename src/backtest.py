import pandas as pd


def run_backtest(
    df,
    signals,
    initial_capital=100000,
    transaction_cost=0.001
):
    # Handle empty input
    if df.empty:
        raise ValueError("Input DataFrame is empty")

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
        today_close = df.loc[date, "Close"]
        if isinstance(today_close, pd.Series):
            today_price = float(today_close.iloc[0])
        else:
            today_price = float(today_close)

        # Next day's closing price (for trade execution)
        next_close = df.loc[next_date, "Close"]
        if isinstance(next_close, pd.Series):
            next_price = float(next_close.iloc[0])
        else:
            next_price = float(next_close)

        # Today's signal
        signal = signals.loc[date]

        # BUY on next day's close
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

        # SELL on next day's close
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

    # Portfolio value on the final trading day
    last_close = df["Close"].iloc[-1]
    if isinstance(last_close, pd.Series):
        last_price = float(last_close.iloc[0])
    else:
        last_price = float(last_close)

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