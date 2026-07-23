import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="FinPulse Lite",
    layout="wide"
)

st.title("FinPulse Lite")
st.subheader("Interactive Stock Strategy Dashboard")

st.write(
    "Welcome to FinPulse Lite! "
    "Select a stock from the sidebar to begin."
)

# Sidebar
st.sidebar.title("Settings")

stock = st.sidebar.selectbox(
    "Choose a Stock",
    [
        "RELIANCE.NS",
        "TCS.NS",
        "INFY.NS",
        "HDFCBANK.NS",
        "ICICIBANK.NS"
    ]
)

st.success(f"Selected Stock: {stock}")

# Sample chart
df = pd.DataFrame({
    "Day": [1, 2, 3, 4, 5],
    "Price": [100, 104, 101, 109, 115]
})

fig = px.line(
    df,
    x="Day",
    y="Price",
    title="Sample Stock Price"
)

st.plotly_chart(fig, use_container_width=True)