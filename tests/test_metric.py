import pandas as pd
import pytest

from src.metric import (
    total_return,
    annualized_return,
    sharpe_ratio,
    max_drawdown
)
from src.strategy_rsi import generate_rsi_signals
from src.strategy_sma import generate_signals
from src.backtest import run_backtest


def test_total_return_basic():
    equity = pd.Series([100000, 110000])

    assert total_return(equity) == pytest.approx(10.0)


def test_sharpe_ratio_zero():
    equity = pd.Series([100000] * 100)

    assert sharpe_ratio(equity) == pytest.approx(0.0)


def test_max_drawdown_no_drawdown():
    equity = pd.Series([100, 110, 120, 130, 140])

    drawdown, peak_idx, trough_idx, drawdown_series = max_drawdown(equity)

    assert drawdown == pytest.approx(0.0)


def test_max_drawdown_known_case():
    equity = pd.Series([100, 110, 90, 95])

    drawdown, peak_idx, trough_idx, drawdown_series = max_drawdown(equity)

    assert drawdown == pytest.approx(-18.1818, abs=0.1)


def test_rsi_overbought():
    prices = pd.DataFrame({
        "Close": list(range(1, 101))
    })

    signals = generate_rsi_signals(prices)

    assert len(signals) == len(prices)


def test_signal_generation_basic():
    prices = pd.DataFrame({
        "Close": [100] * 250
    })

    signals = generate_signals(prices)

    assert len(signals) == len(prices)


def test_transaction_costs_applied():
    df = pd.DataFrame({
        "Close": [100, 105, 110, 115, 120]
    })

    signals = pd.Series([1, 0, 0, -1, 0])

    result_no_cost, _ = run_backtest(
        df,
        signals,
        transaction_cost=0
    )

    result_cost, _ = run_backtest(
        df,
        signals,
        transaction_cost=0.001
    )

    assert (
        result_cost["PortfolioValue"].iloc[-1]
        <
        result_no_cost["PortfolioValue"].iloc[-1]
    )


def test_no_lookahead():
    df = pd.DataFrame({
        "Close": [100, 105, 110, 115]
    })

    signals = pd.Series([1, 0, -1, 0])

    results, trades = run_backtest(df, signals)

    assert trades.iloc[0]["Date"] == df.index[1]


def test_empty_dataframe():
    df = pd.DataFrame(columns=["Close"])
    signals = pd.Series(dtype=int)

    with pytest.raises(ValueError):
        run_backtest(df, signals)


def test_single_stock_backtest():
    df = pd.DataFrame({
        "Close": [100, 101, 102, 103, 104]
    })

    signals = pd.Series([1, 0, 0, -1, 0])

    results, trades = run_backtest(df, signals)

    assert len(results) == len(df)