def total_return(equity_curve):

    initial_value = equity_curve.iloc[0]
    final_value = equity_curve.iloc[-1]

    return ((final_value / initial_value) - 1) * 100


def annualized_return(equity_curve):

    initial_value = equity_curve.iloc[0]
    final_value = equity_curve.iloc[-1]

    trading_days = len(equity_curve)
    years = trading_days / 252

    cagr = ((final_value / initial_value) ** (1 / years)) - 1

    return cagr * 100