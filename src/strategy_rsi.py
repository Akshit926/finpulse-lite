import pandas as pd


def generate_rsi_signals(
    df,
    period=14,
    oversold=30,
    overbought=70
):

    data = df.copy()

    # Daily price change
    delta = data["Close"].diff()

    # Gains and losses
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # Wilder's smoothing using exponential weighted moving average
    avg_gain = gain.ewm(
        alpha=1 / period,
        adjust=False
    ).mean()

    avg_loss = loss.ewm(
        alpha=1 / period,
        adjust=False
    ).mean()

    # Relative Strength
    rs = avg_gain / avg_loss

    # RSI
    rsi = 100 - (100 / (1 + rs))

    data["RSI"] = rsi

    # Generate signals
    signals = pd.Series(
        0,
        index=data.index
    )

    signals[data["RSI"] < oversold] = 1
    signals[data["RSI"] > overbought] = -1

    return signals