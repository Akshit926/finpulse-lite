import yfinance as yf
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

stocks = [ "RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS","SBIN.NS","ITC.NS","LT.NS","HINDUNILVR.NS", "KOTAKBANK.NS"]

for stock in stocks:
    try:
        print(f"\nDownloading {stock}...")

        data = yf.download(stock,period="5y",interval="1d",auto_adjust=True)

        print("\nFirst 10 Rows:")
        print(data.head(10))

        filename = stock.replace(".NS", "") + ".csv"
        data.to_csv(f"data/{filename}")

        print(f"Saved to data/{filename}")
        print(f"Rows downloaded: {len(data)}")
        print(f"Columns: {list(data.columns)}")
        print("-" * 50)

    except Exception as e:
        print(f"Failed to download {stock}: {e}")
        print("-" * 50)
        continue

print("\nAll files processed!")