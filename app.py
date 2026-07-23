import streamlit as st
import pandas as pd
import plotly.express as px

from src.pipeline import run_full_pipeline
from src.strategy_sma import generate_signals as sma_strategy
from src.strategy_rsi import generate_rsi_signals as rsi_strategy

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="FinPulse Lite",
    layout="wide"
)

st.title("📈 FinPulse Lite")
st.subheader("Interactive Stock Strategy Dashboard")

st.write(
    "Select a stock, choose a trading strategy, "
    "adjust the parameters, and view the results instantly."
)

# ---------------------------------
# Sidebar
# ---------------------------------
st.sidebar.header("Settings")

stock = st.sidebar.selectbox(
    "Select Stock",
    [
        "RELIANCE.NS",
        "TCS.NS",
        "INFY.NS",
        "HDFCBANK.NS",
        "ICICIBANK.NS"
    ]
)

strategy = st.sidebar.selectbox(
    "Select Strategy",
    [
        "SMA Crossover",
        "RSI"
    ]
)

# ---------------------------------
# Strategy Parameters
# ---------------------------------
if strategy == "SMA Crossover":

    fast_window = st.sidebar.slider(
        "Fast SMA Window",
        min_value=5,
        max_value=100,
        value=50
    )

    slow_window = st.sidebar.slider(
        "Slow SMA Window",
        min_value=50,
        max_value=300,
        value=200
    )

    strategy_func = lambda df: sma_strategy(
        df,
        fast_window,
        slow_window
    )

else:

    rsi_period = st.sidebar.slider(
        "RSI Period",
        min_value=5,
        max_value=30,
        value=14
    )

    oversold = st.sidebar.slider(
        "Oversold Level",
        min_value=10,
        max_value=40,
        value=30
    )

    overbought = st.sidebar.slider(
        "Overbought Level",
        min_value=60,
        max_value=90,
        value=70
    )

    strategy_func = lambda df: rsi_strategy(
        df,
        rsi_period,
        oversold,
        overbought
    )

# ---------------------------------
# Run Backtest Automatically
# ---------------------------------
with st.spinner("Running Backtest..."):

    output = run_full_pipeline(
        stock,
        strategy_func
    )

st.success("✅ Backtest Completed!")

# ---------------------------------
# Extract Results
# ---------------------------------
results = output["results"]
metrics = output["metrics"]

equity = results["PortfolioValue"]

# ---------------------------------
# Selected Parameters
# ---------------------------------
with st.expander("Selected Strategy Parameters", expanded=True):

    st.write(f"**Strategy:** {strategy}")

    if strategy == "SMA Crossover":

        st.write(f"**Fast SMA Window:** {fast_window}")
        st.write(f"**Slow SMA Window:** {slow_window}")

    else:

        st.write(f"**RSI Period:** {rsi_period}")
        st.write(f"**Oversold Level:** {oversold}")
        st.write(f"**Overbought Level:** {overbought}")

# ---------------------------------
# Performance Summary
# ---------------------------------
st.subheader("Performance Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Return",
    f"{metrics['Total Return']:.2f}%"
)

col2.metric(
    "Sharpe Ratio",
    f"{metrics['Sharpe Ratio']:.2f}"
)

col3.metric(
    "Max Drawdown",
    f"{metrics['Max Drawdown']:.2f}%"
)

col4, col5 = st.columns(2)

col4.metric(
    "Win Rate",
    f"{metrics['Win Rate']:.2f}%"
)

col5.metric(
    "Trades",
    metrics["Total Trades"]
)

# ---------------------------------
# Equity Curve
# ---------------------------------
st.subheader("Equity Curve")

fig = px.line(
    x=equity.index,
    y=equity.values,
    labels={
        "x": "Date",
        "y": "Portfolio Value"
    },
    title=f"{stock} - {strategy}"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------
# Performance Metrics Table
# ---------------------------------
st.subheader("Performance Metrics")

metrics_df = pd.DataFrame(
    [
        ["Total Return", f"{metrics['Total Return']:.2f}%"],
        ["Annualized Return", f"{metrics['Annualized Return']:.2f}%"],
        ["Sharpe Ratio", f"{metrics['Sharpe Ratio']:.2f}"],
        ["Max Drawdown", f"{metrics['Max Drawdown']:.2f}%"],
        ["Win Rate", f"{metrics['Win Rate']:.2f}%"],
        ["Total Trades", metrics["Total Trades"]],
        ["Average Win", f"₹{metrics['Average Win']:.2f}"],
        ["Average Loss", f"₹{metrics['Average Loss']:.2f}"],
        ["Profit Factor", f"{metrics['Profit Factor']:.2f}"],
    ],
    columns=["Metric", "Value"]
)

st.dataframe(
    metrics_df,
    use_container_width=True,
    hide_index=True
)