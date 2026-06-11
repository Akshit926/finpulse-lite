import pandas as pd


def generate_signals(df):
    """
    Generate SMA crossover signals.

    Parameters:
        df (pd.DataFrame): Must contain a 'Close' column.

    Returns:
        pd.Series: 1 = Buy, -1 = Sell, 0 = Hold
    """

    data = df.copy()

    # Moving averages
    data['SMA50'] = data['Close'].rolling(window=50).mean()
    data['SMA200'] = data['Close'].rolling(window=200).mean()

    # Initialize signals
    signals = pd.Series(0, index=data.index)

    # Buy condition
    buy_signal = (
        (data['SMA50'] > data['SMA200']) &
        (data['SMA50'].shift(1) <= data['SMA200'].shift(1))
    )

    # Sell condition
    sell_signal = (
        (data['SMA50'] < data['SMA200']) &
        (data['SMA50'].shift(1) >= data['SMA200'].shift(1))
    )

    signals[buy_signal] = 1
    signals[sell_signal] = -1

    return signals
