import pandas as pd

def run_backtest(df, signals, initial_capital=100000):

    cash = initial_capital
    shares = 0
    position = False

    portfolio_values = []
    trades = []

    for date in df.index:

        price = float(df.loc[date, 'Close'])
        signal = signals.loc[date]

        # BUY
        if signal == 1 and not position:

            shares = cash / price
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

            cash = shares * price
            shares = 0
            position = False

            trades.append([
                date,
                "SELL",
                price,
                shares,
                cash
            ])

        portfolio_value = cash + shares * price
        portfolio_values.append(portfolio_value)

    results = pd.DataFrame(index=df.index)
    results["PortfolioValue"] = portfolio_values

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