import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

stocks = [
    "Reliance.NS",
    "TCS",
    "INFY",
    "HDFCBANK",
    "ICICIBANK",
    "SBIN",
    "ITC",
    "LT",
    "HINDUNILVR",
    "KOTAKBANK"
]

for stock in stocks:
    try:
        print(f"Processing {stock}...")

        file_path = f"data/{stock}.csv"

        data = pd.read_csv(file_path)

        # Calculate moving averages
        data["MA50"] = data["Close"].rolling(window=50).mean()
        data["MA200"] = data["Close"].rolling(window=200).mean()

        plt.figure(figsize=(12, 6))

        plt.plot(data["Close"], label="Close Price")
        plt.plot(data["MA50"], label="50 Day MA")
        plt.plot(data["MA200"], label="200 Day MA")

        plt.title(f"{stock} Stock Price")
        plt.xlabel("Days")
        plt.ylabel("Price (INR)")
        plt.legend()

        plt.savefig(f"images/{stock}_chart.png")

        plt.close()

        print(f"Saved images/{stock}_chart.png")

    except Exception as e:
        print(f"Error processing {stock}: {e}")

print("All charts generated successfully!")