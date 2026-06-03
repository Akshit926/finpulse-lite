# June 3, 2026

### What I worked on today

* Modified my stock data downloader to handle multiple stocks instead of just one.
* Downloaded 5 years of daily stock data for 10 NIFTY stocks using yfinance.
* Saved each stock's data as a separate CSV file in the data/ folder.
* Implemented error handling using try/except to ensure the script continues running even if one stock fails to download.
* Created a basic README.md file describing the project and its purpose.

### What I learned

* How to use loops to automate repetitive tasks for multiple stock tickers.
* How to save multiple datasets into separate CSV files using Pandas.
* The importance of exception handling and how try/except prevents a program from crashing.
* Better understanding of Pandas file I/O operations and data indexing concepts.
* How project documentation helps make code easier to understand and maintain.

### Where I struggled

* I initially placed the except block incorrectly, which caused a syntax error.
* Understanding where the try block should begin and end took some debugging.
* I had to verify that each CSV file was being saved correctly with the expected filename.

### How I solved problems (which Level helped most?)

* Re-read the official Python documentation on Exceptions.
* Checked yfinance examples and compared them with my implementation.
* Used experimentation and debugging to identify the incorrect placement of the except block.
* AI assistance helped me quickly understand the syntax issue and correct it.

### What I'll do tomorrow

* Read all generated CSV files using Pandas.
* Combine or analyze the stock datasets.
* Explore basic data analysis such as summary statistics, missing values, and plotting stock prices.

### One-sentence reflection

Today I learned that a small amount of error handling can make a program much more reliable and professional.
