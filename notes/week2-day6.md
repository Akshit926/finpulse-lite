### What I worked on today

* Completed reading about Simple Moving Averages (SMA) and crossover strategies.
* Studied the Pandas `rolling()` method for calculating moving averages.
* Learned the Pandas `shift()` method and its use in comparing current and previous values.
* Implemented the `generate_signals(df)' function in `strategy_sma.py`.
* Created buy and sell signal logic based on 50-day and 200-day SMA crossovers.
* Set up a test script to run the strategy on RELIANCE stock data.
* Debugged issues related to undefined variables and missing Python packages.

### What I learned

* How moving averages are calculated using Pandas `rolling()`.
* How `shift(1)` can be used to access previous-day values.
* How SMA crossovers generate trading signals.
* The importance of separating reusable functions from testing scripts.
* Basic debugging techniques for Python errors such as `NameError` and `ModuleNotFoundError`.

### Where I struggled

* Understanding how crossover conditions should be expressed in code.
* Confusion about why `df` was undefined when running `strategy_sma.py`.
* Difficulty running the test script because `yfinance` and `pip` were not configured correctly.

### How I solved problems (which Level helped most?)

* Pandas documentation helped me understand `rolling()` and `shift()`.
* Experimentation with small code snippets clarified the crossover logic.
* AI assistance helped identify coding mistakes and debug error messages.
* Terminal outputs were useful in locating the exact source of errors.

### What I'll do tomorrow

* Install and configure the required Python packages properly.
* Successfully test the SMA crossover strategy on RELIANCE data.
* Start analyzing the generated buy and sell signals.

### One-sentence reflection

Today I learned that understanding data manipulation functions like `rolling()` and `shift()` is essential for implementing trading strategies correctly.
