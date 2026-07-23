import pandas as pd


def generate_signals(
    df,
    fast_window=50,
    slow_window=200
):
    """
    Generate SMA crossover signals.

    Parameters:
        df (pd.DataFrame): DataFrame containing a 'Close' column.
        fast_window (int): Fast SMA window.
        slow_window (int): Slow SMA window.

    Returns:
        pd.Series: 1 = Buy, -1 = Sell, 0 = Hold
    """

    data = df.copy()

    # Moving averages
    data["SMA Fast"] = data["Close"].rolling(
        window=fast_window
    ).mean()

    data["SMA Slow"] = data["Close"].rolling(
        window=slow_window
    ).mean()

    # Initialize signals
    signals = pd.Series(
        0,
        index=data.index
    )

    # Buy condition
    buy_signal = (
        (data["SMA Fast"] > data["SMA Slow"])
        &
        (data["SMA Fast"].shift(1) <= data["SMA Slow"].shift(1))
    )

    # Sell condition
    sell_signal = (
        (data["SMA Fast"] < data["SMA Slow"])
        &
        (data["SMA Fast"].shift(1) >= data["SMA Slow"].shift(1))
    )

    signals[buy_signal] = 1
    signals[sell_signal] = -1

    return signals