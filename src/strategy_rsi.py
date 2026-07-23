import pandas as pd


def generate_rsi_signals(
    df,
    period=14,
    oversold=30,
    overbought=70
):
    """
    Generate RSI trading signals.

    Parameters:
        df (pd.DataFrame): DataFrame containing a 'Close' column.
        period (int): RSI lookback period.
        oversold (int): Buy threshold.
        overbought (int): Sell threshold.

    Returns:
        pd.Series: 1 = Buy, -1 = Sell, 0 = Hold
    """

    data = df.copy()

    delta = data["Close"].diff()

    gain = delta.where(delta > 0, 0)

    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period).mean()

    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss

    data["RSI"] = 100 - (100 / (1 + rs))

    signals = pd.Series(0, index=data.index)

    # Buy when RSI crosses above oversold
    buy_signal = (
        (data["RSI"] > oversold)
        &
        (data["RSI"].shift(1) <= oversold)
    )

    # Sell when RSI crosses below overbought
    sell_signal = (
        (data["RSI"] < overbought)
        &
        (data["RSI"].shift(1) >= overbought)
    )

    signals[buy_signal] = 1
    signals[sell_signal] = -1

    return signals