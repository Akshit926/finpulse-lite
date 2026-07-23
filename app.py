import streamlit as st
import pandas as pd
import plotly.express as px
import os

from src.pipeline import run_full_pipeline
from src.strategy_sma import generate_signals as sma_strategy
from src.strategy_rsi import generate_rsi_signals as rsi_strategy


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="FinPulse Lite",
    layout="wide"
)

st.title("FinPulse Lite")
st.subheader("Interactive Stock Strategy Dashboard")

st.write(
    """
Compare technical trading strategies with a Buy & Hold benchmark.
Adjust parameters in the sidebar and explore the results instantly.
"""
)
leaderboard = None

if os.path.exists("strategy_comparison.csv"):
    import os
import pandas as pd
import streamlit as st

leaderboard = None

if os.path.exists("strategy_comparison.csv") and os.path.getsize("strategy_comparison.csv") > 0:
    leaderboard = pd.read_csv("strategy_comparison.csv")
else:
    st.warning(
        "Leaderboard not found. Run 'python run_all_stocks.py' first."
    )
# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.header("⚙ Strategy Settings")

from src.nifty50 import NIFTY50

stock_list = NIFTY50

default_stock = st.session_state.get(
    "selected_stock",
    stock_list[0]
)

if default_stock not in stock_list:
    stock_list.append(default_stock)

stock = st.sidebar.selectbox(
    "Stock",
    stock_list,
    index=stock_list.index(default_stock)
)

strategy = st.sidebar.selectbox(
    "Strategy",
    [
        "SMA Crossover",
        "RSI"
    ]
)

# --------------------------------------------------
# Parameter Selection
# --------------------------------------------------
if strategy == "SMA Crossover":

    fast_window = st.sidebar.slider(
        "Fast SMA",
        5,
        100,
        50
    )

    slow_window = st.sidebar.slider(
        "Slow SMA",
        50,
        300,
        200
    )

    strategy_func = lambda df: sma_strategy(
        df,
        fast_window,
        slow_window
    )

else:

    rsi_period = st.sidebar.slider(
        "RSI Period",
        5,
        30,
        14
    )

    oversold = st.sidebar.slider(
        "Oversold",
        10,
        40,
        30
    )

    overbought = st.sidebar.slider(
        "Overbought",
        60,
        90,
        70
    )

    strategy_func = lambda df: rsi_strategy(
        df,
        rsi_period,
        oversold,
        overbought
    )

# --------------------------------------------------
# Run Pipeline
# --------------------------------------------------
with st.spinner("Running Backtest..."):

    output = run_full_pipeline(
        stock,
        strategy_func
    )

st.success("Backtest Completed Successfully!")

results = output["results"]
metrics = output["metrics"]
buy_hold_metrics = output["buy_hold_metrics"]

equity = results["PortfolioValue"]
buy_hold = results["BuyHoldValue"]

# --------------------------------------------------
# Tabs
# --------------------------------------------------
tab1, tab2, tab3 = st.tabs(
    [
        "Strategy Dashboard",
        "Comparison",
        "Leaderboard"
    ]
)

# ==================================================
# TAB 1
# ==================================================
with tab1:

    st.subheader("Selected Parameters")

    if strategy == "SMA Crossover":

        st.info(
            f"""
Strategy : SMA Crossover

Fast SMA : {fast_window}

Slow SMA : {slow_window}
"""
        )

    else:

        st.info(
            f"""
Strategy : RSI

RSI Period : {rsi_period}

Oversold : {oversold}

Overbought : {overbought}
"""
        )

    st.subheader("Performance Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Total Return",
        f"{metrics['Total Return']:.2f}%"
    )

    c2.metric(
        "Sharpe Ratio",
        f"{metrics['Sharpe Ratio']:.2f}"
    )

    c3.metric(
        "Max Drawdown",
        f"{metrics['Max Drawdown']:.2f}%"
    )

    c4, c5 = st.columns(2)

    c4.metric(
        "Win Rate",
        f"{metrics['Win Rate']:.2f}%"
    )

    c5.metric(
        "Trades",
        metrics["Total Trades"]
    )

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

# ==================================================
# TAB 2 : Comparison View
# ==================================================
with tab2:

    st.subheader("Strategy vs Buy & Hold")

    comparison_df = pd.DataFrame(
        {
            "Strategy": equity,
            "Buy & Hold": buy_hold
        }
    )

    fig_compare = px.line(
        comparison_df,
        x=comparison_df.index,
        y=["Strategy", "Buy & Hold"],
        labels={
            "index": "Date",
            "value": "Portfolio Value",
            "variable": "Portfolio"
        },
        title=f"{stock}: Strategy vs Buy & Hold"
    )

    st.plotly_chart(
        fig_compare,
        use_container_width=True
    )

    st.subheader("Performance Comparison")

    comparison_metrics = pd.DataFrame(
        {
            "Metric": [
                "Total Return",
                "Annualized Return",
                "Sharpe Ratio",
                "Max Drawdown",
            ],
            "Strategy": [
                f"{metrics['Total Return']:.2f}%",
                f"{metrics['Annualized Return']:.2f}%",
                f"{metrics['Sharpe Ratio']:.2f}",
                f"{metrics['Max Drawdown']:.2f}%"
            ],
            "Buy & Hold": [
                f"{buy_hold_metrics['Total Return']:.2f}%",
                f"{buy_hold_metrics['Annualized Return']:.2f}%",
                f"{buy_hold_metrics['Sharpe Ratio']:.2f}",
                f"{buy_hold_metrics['Max Drawdown']:.2f}%"
            ]
        }
    )

    st.dataframe(
        comparison_metrics,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Quick Summary")

    strategy_return = metrics["Total Return"]
    buy_hold_return = buy_hold_metrics["Total Return"]

    strategy_sharpe = metrics["Sharpe Ratio"]
    buy_hold_sharpe = buy_hold_metrics["Sharpe Ratio"]

    if strategy_return > buy_hold_return:
        st.success(
            f"Strategy outperformed Buy & Hold by "
            f"{strategy_return - buy_hold_return:.2f}%."
        )
    elif strategy_return < buy_hold_return:
        st.warning(
            f"Buy & Hold outperformed the strategy by "
            f"{buy_hold_return - strategy_return:.2f}%."
        )
    else:
        st.info("Both approaches produced the same total return.")

    if strategy_sharpe > buy_hold_sharpe:
        st.success(
            f"Strategy achieved a better risk-adjusted return "
            f"(Sharpe: {strategy_sharpe:.2f} vs "
            f"{buy_hold_sharpe:.2f})."
        )
    elif strategy_sharpe < buy_hold_sharpe:
        st.warning(
            f"Buy & Hold achieved a better risk-adjusted return "
            f"(Sharpe: {buy_hold_sharpe:.2f} vs "
            f"{strategy_sharpe:.2f})."
        )
    else:
        st.info("Both approaches have the same Sharpe Ratio.")

    st.markdown("---")

    st.caption(
        "FinPulse Lite • Week 4 • Strategy Comparison Dashboard"
    )
    
# ==================================================
# TAB 3 : Leaderboard
# ==================================================

with tab3:

    st.subheader("Strategy Leaderboard")

    if leaderboard is None:

        st.warning("Run run_all_stocks.py first.")

    else:

        strategy_choice = st.selectbox(
            "Strategy",
            [
                "SMA",
                "RSI"
            ],
            key="leaderboard_strategy"
        )

        sharpe_col = (
            "SMA Sharpe"
            if strategy_choice == "SMA"
            else "RSI Sharpe"
        )

        return_col = (
            "SMA Return"
            if strategy_choice == "SMA"
            else "RSI Return"
        )

        leaderboard_sorted = leaderboard.sort_values(
            by=sharpe_col,
            ascending=False
        )

        st.markdown("## Top 10 Stocks")

        st.dataframe(
            leaderboard_sorted[
                [
                    "Stock",
                    sharpe_col,
                    return_col,
                    "Better Strategy"
                ]
            ].head(10),
            use_container_width=True,
            hide_index=True
        )

        st.markdown("## Bottom 10 Stocks")

        st.dataframe(
            leaderboard_sorted[
                [
                    "Stock",
                    sharpe_col,
                    return_col,
                    "Better Strategy"
                ]
            ].tail(10),
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        st.subheader("View Stock Report")

        selected_stock = st.selectbox(
            "Choose Stock",
            leaderboard_sorted["Stock"],
            key="leaderboard_stock"
        )

        if st.button("Open Report"):

            st.session_state.selected_stock = selected_stock

            st.success(
                f"{selected_stock} selected.\n\nChoose it from the sidebar to view the complete dashboard."
            )