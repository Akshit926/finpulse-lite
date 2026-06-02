import yfinance as yf
import pandas as pd
data = yf.download("RELIANCE.NS",period="5y",interval="1d")
print("\nFirst 10 Rows : \n")
print(data.head(10))
print("\nColumns : \n")
print(list(data.columns))
data.to_csv("data/Reliance.csv")
