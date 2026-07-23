from pathlib import Path
import streamlit as st
import pandas as pd
import yfinance as yf
@st.cache_data
def download_stock_data(ticker, period="5y"):
    df = yf.download(ticker, period=period)

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.dropna(inplace=True)
    return df

DATA_DIR = Path("data")


def _candidate_cache_paths(symbol):
    base_name = symbol.replace(".NS", "")
    variants = {
        base_name,
        base_name.upper(),
        base_name.lower(),
        base_name.title(),
        symbol,
        symbol.upper(),
        symbol.lower(),
    }

    if DATA_DIR.exists():
        for path in DATA_DIR.glob("*.csv"):
            if path.stem.lower() in {variant.lower() for variant in variants}:
                return [path]

    return [
        DATA_DIR / f"{base_name}.csv",
        DATA_DIR / f"{base_name.upper()}.csv",
        DATA_DIR / f"{base_name.title()}.csv",
    ]


def _normalize_price_frame(df):
    if df is None or df.empty:
        return pd.DataFrame()

    frame = df.copy()

    if isinstance(frame.columns, pd.MultiIndex):
        frame.columns = [col[0] if isinstance(col, tuple) else col for col in frame.columns]

    if "Adj Close" in frame.columns and "Close" not in frame.columns:
        frame = frame.rename(columns={"Adj Close": "Close"})

    first_col = frame.columns[0] if len(frame.columns) else None

    if first_col in {"Price", "Date"} or "Date" in frame.columns:
        if first_col in {"Price", "Date"} and first_col in frame.columns:
            date_col = first_col
        else:
            date_col = "Date"

        frame = frame.copy()
        frame[date_col] = frame[date_col].astype(str).str.strip()
        frame = frame[frame[date_col].str.lower() != "date"]
        frame[date_col] = pd.to_datetime(frame[date_col], errors="coerce")
        frame = frame.dropna(subset=[date_col])
        frame = frame.set_index(date_col)
    elif isinstance(frame.index, pd.DatetimeIndex):
        frame.index = pd.to_datetime(frame.index, errors="coerce")
        frame = frame[frame.index.notna()].copy()
    else:
        converted_index = pd.to_datetime(frame.index, errors="coerce")
        if converted_index.notna().any():
            frame.index = converted_index
            frame = frame[frame.index.notna()].copy()

    if not isinstance(frame.index, pd.DatetimeIndex):
        try:
            frame.index = pd.to_datetime(frame.index, errors="coerce")
            frame = frame[frame.index.notna()].copy()
        except Exception:
            return pd.DataFrame()

    frame = frame.loc[:, ~frame.columns.astype(str).str.startswith("Unnamed")]
    frame = frame.sort_index()
    frame = frame.dropna(how="all")

    return frame


def load_cached_stock_data(symbol):
    """Load cached stock data from data/ if a usable file already exists."""

    for path in _candidate_cache_paths(symbol):
        if not path.exists():
            continue

        for read_kwargs in ({"header": [0, 1]}, {"header": 0}):
            try:
                cached = pd.read_csv(path, **read_kwargs)
            except Exception:
                continue

            normalized = _normalize_price_frame(cached)
            if not normalized.empty:
                print(f"Loaded cached data from {path}")
                return normalized

    return pd.DataFrame()


def download_stock_data(symbol):
    """Download 5 years of daily stock data and save it to data/.
    Returns the downloaded DataFrame.
    """

    DATA_DIR.mkdir(exist_ok=True)

    cached = load_cached_stock_data(symbol)
    if not cached.empty:
        return cached

    print(f"\nDownloading {symbol}...")

    try:
        df = yf.download(
            symbol,
            period="5y",
            interval="1d",
            auto_adjust=True,
            progress=False,
        )
    except Exception as exc:
        print(f"Live download failed for {symbol}: {exc}")
        return pd.DataFrame()
    df.columns = df.columns.get_level_values(0)
    print(df.columns)

    df = _normalize_price_frame(df)

    filename = symbol.replace(".NS", "") + ".csv"
    cache_path = DATA_DIR / filename

    if not df.empty:
        df.to_csv(cache_path)
        print(f"Saved to {cache_path}")
    else:
        print(f"No usable rows downloaded for {symbol}")

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
        "KOTAKBANK.NS",
    ]

    for stock in stocks:
        try:
            download_stock_data(stock)
        except Exception as e:
            print(f"Failed to download {stock}: {e}")

    print("\nAll files processed!")
