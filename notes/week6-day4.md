Here are your **Thursday internship notes** in the same style as the previous days.

---

# **Thursday – Strategy Comparison Dashboard**

## **Today's Goal**

Build a comparison view to evaluate the trading strategy against a simple Buy & Hold investment. The objective was to help users understand whether the selected strategy actually adds value compared to holding the stock throughout the investment period.

---

## **Tasks Completed**

* Enhanced the backtesting engine to calculate the Buy & Hold portfolio value alongside the strategy portfolio.
* Updated the pipeline to compute performance metrics for both Strategy and Buy & Hold.
* Added a new **Comparison** tab in the Streamlit dashboard.
* Created a dual-line Plotly chart showing Strategy Portfolio vs Buy & Hold Portfolio.
* Built a comparison table displaying:

  * Total Return
  * Annualized Return
  * Sharpe Ratio
  * Maximum Drawdown
* Added a quick summary section highlighting which approach performed better based on returns and risk-adjusted performance.

---

## **Key Learnings**

* A trading strategy should always be compared against a benchmark instead of being evaluated independently.
* Buy & Hold provides a simple baseline for measuring whether active trading creates additional value.
* Plotly allows multiple time series to be visualized together, making performance comparison much easier.
* Presenting results through charts and summary tables improves the usability of analytical applications.

---

## **Challenges Faced**

* Integrating Buy & Hold calculations into the existing backtesting workflow without affecting previous functionality.
* Ensuring both portfolios used the same initial capital and identical time period for fair comparison.
* Managing additional metrics while keeping the Streamlit interface clean and easy to understand.

---

## **How the Challenges Were Solved**

* Added Buy & Hold portfolio calculation directly within the backtesting module.
* Extended the pipeline to calculate benchmark metrics separately.
* Used Streamlit tabs to organize the dashboard and avoid clutter.
* Combined both equity curves into a single interactive Plotly chart for easier comparison.

---

## **Reflection**

Today's work transformed the project from a basic backtesting tool into a more practical investment analysis dashboard. By introducing a benchmark comparison, the application now provides better insights into whether a strategy truly outperforms passive investing. This feature significantly improves the usefulness of FinPulse Lite for evaluating trading strategies and makes the dashboard more suitable for demonstrations and future enhancements.
