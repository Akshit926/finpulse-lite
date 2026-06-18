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