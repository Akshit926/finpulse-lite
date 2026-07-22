import yfinance as yf
import pandas as pd
import os


def download_stock_data(symbol):
    """
    Download 5 years of daily stock data and save it to data/.
    Returns the downloaded DataFrame.
    """

    os.makedirs("data", exist_ok=True)

    print(f"\nDownloading {symbol}...")

    df = yf.download(
        symbol,
        period="5y",
        interval="1d",
        auto_adjust=True,
        progress=False
    )

    filename = symbol.replace(".NS", "") + ".csv"
    df.to_csv(f"data/{filename}")

    print(f"Saved to data/{filename}")
    print(f"Rows downloaded: {len(df)}")

    return df


if __name__ == "__main__":
    stocks = [
        "RELIANCE.NS",
        "TCS.NS",
        "INFY.NS",
        "HDFCBANK.NS",
        "ICICIBANK.NS",
        "SBIN.NS",
        "ITC.NS",
        "LT.NS",
        "HINDUNILVR.NS",
        "KOTAKBANK.NS"
    ]

    for stock in stocks:
        try:
            download_stock_data(stock)
        except Exception as e:
            print(f"Failed to download {stock}: {e}")

    print("\nAll files processed!")