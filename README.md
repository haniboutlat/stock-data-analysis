# Stock Data Analysis: Tesla & GameStop

## Overview

This project explores historical stock market data and quarterly revenue for Tesla (TSLA) and GameStop (GME).

Using Python, I collected stock market data, extracted revenue information through web scraping, cleaned and prepared datasets, and visualized the results using Matplotlib.

The project was completed as part of my learning journey in Python and Data Science, following a guided IBM Skills Network lab.

## Project Objectives

- Extract historical stock data using the `yfinance` library.
- Collect quarterly revenue data through web scraping.
- Clean and prepare datasets using Pandas.
- Visualize historical stock prices and company revenue.
- Explore stock price and revenue trends.

## Technologies & Libraries

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation and preparation |
| yfinance | Stock market data extraction |
| Requests | Retrieving webpage content |
| BeautifulSoup | HTML parsing and web scraping |
| Matplotlib | Data visualization |
| Jupyter Notebook | Interactive development environment |

## Project Structure

```text
stock-data-analysis/
│
├── README.md
├── stock_data_analysis.ipynb
├── stock_data_analysis.py
├── Tesla Historical Revenue & Stock Data.png
└── GameStop Historical Revenue & Stock Data.png
```

- `.ipynb` – Interactive Jupyter Notebook version.
- `.py` – Standalone Python script version.
- `.png` – Generated stock price and revenue visualizations.

## Visualizations

The project includes visualizations comparing historical share prices and quarterly revenue for both companies.

### Tesla – Historical Revenue & Stock Data

![Tesla Historical Revenue & Stock Data](Tesla%20Historical%20Revenue%20%26%20Stock%20Data.png)

### GameStop – Historical Revenue & Stock Data

![GameStop Historical Revenue & Stock Data](GameStop%20Historical%20Revenue%20%26%20Stock%20Data.png)

## Data Sources

- Stock market data: Yahoo Finance, accessed through `yfinance`.
- Revenue data: IBM Skills Network-provided datasets and web scraping exercises.

**Note:** The visualizations are limited to historical data up to June 2021, as specified by the original lab.

## What I Learned

Through this project, I gained practical experience with:

- Retrieving data from external sources.
- Web scraping using Requests and BeautifulSoup.
- Working with Pandas DataFrames.
- Cleaning and filtering datasets.
- Extracting and preparing financial data.
- Creating data visualizations using Matplotlib.
- Working with both Jupyter Notebooks and standalone Python scripts.

## Installation

Install the required dependencies:

```bash
python -m pip install yfinance pandas requests beautifulsoup4 matplotlib
```

## Disclaimer

This project is for educational purposes only and does not provide financial advice or investment recommendations.
