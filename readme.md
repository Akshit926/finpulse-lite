# FinPulse Lite

## Project Goal

FinPulse Lite is a beginner-friendly stock market analysis project built using Python. The project downloads historical stock data for major NIFTY stocks, stores the data in CSV format, and generates charts with technical indicators such as 50-day and 200-day moving averages.

The objective is to understand financial data, practice data analysis using Pandas, and create visualizations using Matplotlib.

---

## Features

* Downloads 5 years of historical stock data
* Supports 10 major NIFTY stocks
* Stores stock data as CSV files
* Generates stock price charts
* Calculates 50-day Moving Average (MA50)
* Calculates 200-day Moving Average (MA200)
* Saves charts as PNG images

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* yfinance
* Git & GitHub

---

## Project Structure

finpulse-lite/

data/
images/
notes/
download_data.py
plot_stock.py
requirements.txt
README.md
.gitignore

---

## How to Run

### 1. Activate Virtual Environment

Windows:

venv\Scripts\activate

### 2. Install Dependencies

python -m pip install -r requirements.txt

### 3. Download Stock Data

python download_data.py

### 4. Generate Charts

python plot_stock.py

---

## Sample Output

The project generates charts showing:

* Closing Price
* 50-Day Moving Average
* 200-Day Moving Average

These indicators help visualize stock trends and market momentum.

---

## Learning Outcomes

* Python scripting
* Data analysis using Pandas
* Data visualization using Matplotlib
* Git version control
* Financial market basics

