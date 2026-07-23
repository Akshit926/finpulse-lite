import pandas as pd


def run_backtest(
    df,
    signals,
    initial_capital=100000,
    transaction_cost=0.001
):
    """
    Run backtest with next-day execution.

    Parameters
    ----------
    df : pd.DataFrame
        Stock price data.

    signals : pd.Series
        Trading signals.
        1 = Buy
       -1 = Sell
        0 = Hold

    initial_capital : float
        Starting capital.

    transaction_cost : float
        Transaction cost (default 0.1%).

    Returns
    -------
    results : pd.DataFrame
        Portfolio values and Buy & Hold values.

    trades_df : pd.DataFrame
        Trade log.
    """

    if df.empty:
        raise ValueError("Input DataFrame is empty")

    cash = initial_capital
    shares = 0
    position = False

    portfolio_values = []
    trades = []

    # ---------------------------------
    # Backtest Loop
    # ---------------------------------
    for i in range(len(df) - 1):

        date = df.index[i]
        next_date = df.index[i + 1]

        # Today's close
        today_close = df.loc[date, "Close"]

        if isinstance(today_close, pd.Series):
            today_price = float(today_close.iloc[0])
        else:
            today_price = float(today_close)

        # Next day's close (trade execution)
        next_close = df.loc[next_date, "Close"]

        if isinstance(next_close, pd.Series):
            next_price = float(next_close.iloc[0])
        else:
            next_price = float(next_close)

        signal = signals.loc[date]

        # ---------------- BUY ----------------
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

        # ---------------- SELL ----------------
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

        portfolio_value = cash + (shares * today_price)

        portfolio_values.append(portfolio_value)

    # ---------------------------------
    # Final Portfolio Value
    # ---------------------------------
    last_close = df["Close"].iloc[-1]

    if isinstance(last_close, pd.Series):
        last_price = float(last_close.iloc[0])
    else:
        last_price = float(last_close)

    portfolio_values.append(
        cash + (shares * last_price)
    )

    # ---------------------------------
    # Results DataFrame
    # ---------------------------------
    results = pd.DataFrame(index=df.index)

    results["PortfolioValue"] = portfolio_values

    # ---------------------------------
    # Buy & Hold Portfolio
    # ---------------------------------
    initial_price = float(df["Close"].iloc[0])

    buy_hold_shares = initial_capital / initial_price

    results["BuyHoldValue"] = (
        buy_hold_shares * df["Close"]
    )

    # ---------------------------------
    # Trade Log
    # ---------------------------------
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