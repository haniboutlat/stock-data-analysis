"""IBM Lab: Extracting and Visualizing Stock Data

Install the required packages before running this file:
    python -m pip install yfinance pandas requests beautifulsoup4 matplotlib
"""

import warnings

import matplotlib.pyplot as plt
import pandas as pd
import requests
import yfinance as yf
from bs4 import BeautifulSoup

# Ignore FutureWarnings, as in the original notebook.
warnings.filterwarnings("ignore", category=FutureWarning)


# -----------------------------------------------------------------------------
# Define the graphing function
# -----------------------------------------------------------------------------

def make_graph(stock_data, revenue_data, stock):
    # The graphs only show stock data up to June 14, 2021,
    # and revenue data up to April 30, 2021.
    stock_data_specific = stock_data[stock_data.Date <= "2021-06-14"]
    revenue_data_specific = revenue_data[revenue_data.Date <= "2021-04-30"]

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Stock price graph
    axes[0].plot(
        pd.to_datetime(stock_data_specific.Date),
        stock_data_specific.Close.astype("float"),
        label="Share Price",
        color="blue",
    )
    axes[0].set_ylabel("Price ($US)")
    axes[0].set_title(f"{stock} - Historical Share Price")

    # Revenue graph
    axes[1].plot(
        pd.to_datetime(revenue_data_specific.Date),
        revenue_data_specific.Revenue.astype("float"),
        label="Revenue",
        color="green",
    )
    axes[1].set_ylabel("Revenue ($US Millions)")
    axes[1].set_xlabel("Date")
    axes[1].set_title(f"{stock} - Historical Revenue")

    plt.tight_layout()
    plt.show()


# -----------------------------------------------------------------------------
# Question 1: Use yfinance to extract Tesla stock data
# -----------------------------------------------------------------------------

print("\nQUESTION 1: TESLA STOCK DATA")

tesla = yf.Ticker("TSLA")  # Tesla ticker symbol
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
print(tesla_data.head(5))


# -----------------------------------------------------------------------------
# Question 2: Use web scraping to extract Tesla revenue data
# -----------------------------------------------------------------------------

print("\nQUESTION 2: TESLA REVENUE DATA")

url = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
)
response = requests.get(url, timeout=30)
response.raise_for_status()
html_data = response.text
soup = BeautifulSoup(html_data, "html.parser")

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
table = soup.find_all("tbody")[1]

for row in table.find_all("tr"):
    cols = row.find_all("td")
    if cols:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip()

        new_row = pd.DataFrame([{"Date": date, "Revenue": revenue}])
        tesla_revenue = pd.concat([tesla_revenue, new_row], ignore_index=True)

# Remove commas and dollar signs from Revenue.
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(r",|\$", "", regex=True)

# Remove missing values and empty strings from Revenue.
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]

print(tesla_revenue.tail(5))


# -----------------------------------------------------------------------------
# Question 3: Use yfinance to extract GameStop stock data
# -----------------------------------------------------------------------------

print("\nQUESTION 3: GAMESTOP STOCK DATA")

gamestop = yf.Ticker("GME")
gme_data = gamestop.history(period="max")
gme_data.reset_index(inplace=True)
print(gme_data.head(5))


# -----------------------------------------------------------------------------
# Question 4: Use web scraping to extract GameStop revenue data
# -----------------------------------------------------------------------------

print("\nQUESTION 4: GAMESTOP REVENUE DATA")

url2 = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
)
response2 = requests.get(url2, timeout=30)
response2.raise_for_status()
html_data_2 = response2.text
soup = BeautifulSoup(html_data_2, "html.parser")

gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
table = soup.find_all("tbody")[1]

for row in table.find_all("tr"):
    cols = row.find_all("td")
    if cols:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip()

        new_row = pd.DataFrame([{"Date": date, "Revenue": revenue}])
        gme_revenue = pd.concat([gme_revenue, new_row], ignore_index=True)

# Remove commas and dollar signs from Revenue.
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(r",|\$", "", regex=True)

# Remove missing values and empty strings from Revenue.
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue["Revenue"] != ""]

print(gme_revenue.tail(5))


# -----------------------------------------------------------------------------
# Question 5: Plot Tesla stock and revenue data
# -----------------------------------------------------------------------------

print("\nQUESTION 5: TESLA GRAPH")
make_graph(tesla_data, tesla_revenue, "Tesla Stock Data")


# -----------------------------------------------------------------------------
# Question 6: Plot GameStop stock and revenue data
# -----------------------------------------------------------------------------

print("\nQUESTION 6: GAMESTOP GRAPH")
make_graph(gme_data, gme_revenue, "GameStop")
