import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import pytz

# Set the page configuration as the first Streamlit command
st.set_page_config(
    page_title="US Stock Market Cap Rankings",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)

# Define the CSS styles as a string
style = """
div.css-1r6slb0.e1tzin5v2 {
    background-color: #EEEEEE;
    border: 2px solid #CCCCCC;
    padding: 5% 5% 5% 10%;
    border-radius: 5px;
    margin-bottom: 10px;
}
"""

# Apply the CSS styles
st.markdown(f'<style>{style}</style>', unsafe_allow_html=True)

# Predefined list of top 10 tickers for ace7plus
ace7plus_tickers = [
    'NVDA', 'AAPL', 'GOOGL', 'MSFT', 'AMZN', 'AVGO', 'META', 'NFLX', 'TSLA', 'AMD'
]

# Function to fetch market cap and additional info for a given ticker
@st.cache_data(ttl=24*3600)
def get_stock_info(ticker):
    try:
        stock = yf.Ticker(ticker)
        market_cap = stock.info.get('marketCap', None)
        hist = stock.history(period='5y')

        if hist.empty:
            raise ValueError(f"No historical data for {ticker}")

        # Ensure datetime objects are timezone-aware
        jan_2 = datetime(datetime.now().year, 1, 2, tzinfo=pytz.UTC)
        hist.index = hist.index.tz_convert(pytz.UTC)

        if jan_2 not in hist.index:
            jan_2 = hist.index[hist.index.searchsorted(jan_2)]

        # Calculate YTD return
        ytd_return = (hist['Close'].iloc[-1] / hist['Close'].loc[jan_2] - 1) * 100

        # Calculate 1-year return
        one_year_return = (hist['Close'].iloc[-1] / hist['Close'].iloc[-252] - 1) * 100

        # Calculate 5-year return
        five_year_return = (hist['Close'].iloc[-1] / hist['Close'].iloc[0] - 1) * 100

        return market_cap, ytd_return, one_year_return, five_year_return
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {e}")
        return None, None, None, None

# Function to fetch USD to KRW exchange rate
@st.cache_data(ttl=24*3600)
def get_exchange_rate():
    try:
        end_date = datetime.now(pytz.timezone('America/New_York')).strftime("%Y-%m-%d")
        start_date = (datetime.now(pytz.timezone('America/New_York')) - timedelta(days=1)).strftime("%Y-%m-%d")
        exchange_rate_data = yf.download('USDKRW=X', start=start_date, end=end_date)
        if not exchange_rate_data.empty:
            exchange_rate = exchange_rate_data['Close'].iloc[-1]
            return exchange_rate, end_date
        else:
            raise ValueError("No exchange rate data available")
    except Exception as e:
        st.error(f"Error fetching exchange rate: {e}")
        return None, None

# Fetch market caps and additional info for ace7plus tickers
@st.cache_data(ttl=24*3600)
def fetch_market_caps(tickers):
    market_caps = []
    for ticker in tickers:
        cap, ytd, one_year, five_year = get_stock_info(ticker)
        if cap:
            market_caps.append((ticker, cap, ytd, one_year, five_year))
        else:
            st.error(f"Failed to fetch data for {ticker}")
    return market_caps

# Fetch the market caps
market_caps = fetch_market_caps(ace7plus_tickers)

# Fetch the USD to KRW exchange rate
exchange_rate, exchange_rate_fetch_date = get_exchange_rate()
if exchange_rate is None:
    exchange_rate = 1380  # Fallback to a default value if fetching fails
    exchange_rate_fetch_date = datetime.now(pytz.timezone('America/New_York')).strftime("%Y-%m-%d %H:%M:%S")

# Create a DataFrame
df = pd.DataFrame(market_caps, columns=['Ticker', 'Market Cap', 'YTD Return', '1-Year Return', '5-Year Return'])
df = df.dropna()
df['Market Cap'] = df['Market Cap'].astype(float)
df = df.sort_values(by='Market Cap', ascending=False).reset_index(drop=True)
df.index += 1
df['Market Cap ($B)'] = df['Market Cap'] / 1e9
df['Market Cap (₩조원)'] = df['Market Cap'] * exchange_rate / 1e12  # Use dynamic exchange rate

# Format the numbers for better readability without decimals
df['Market Cap ($B)'] = df['Market Cap ($B)'].apply(lambda x: f"{round(x)}B")
df['Market Cap (₩조원)'] = df['Market Cap (₩조원)'].apply(lambda x: f"{round(x)}조원")
df['YTD Return'] = df['YTD Return'].apply(lambda x: f"{x:.1f}%")
df['1-Year Return'] = df['1-Year Return'].apply(lambda x: f"{x:.1f}%")
df['5-Year Return'] = df['5-Year Return'].apply(lambda x: f"{x:.1f}%")

# Extract additional data for the ace7plus companies
additional_data = df.copy()
additional_data.reset_index(drop=True, inplace=True)
additional_data['Rank'] = additional_data.index + 1
additional_data['Company Info'] = additional_data.apply(
    lambda row: f"{row['Ticker']} |\n년초대비: {row['YTD Return']}, 1년전: {row['1-Year Return']}, 5년전: {row['5-Year Return']}",
    axis=1)

# Streamlit title
st.title("US Stock Market Cap Rankings - ACE7Plus")

# Add the current timestamp
nasdaq_time = datetime.now(pytz.timezone('America/New_York')).strftime("%Y-%m-%d %H:%M:%S")
st.write(f"Data fetched on: {nasdaq_time}")
st.write(f"Exchange rate Data fetched on: {exchange_rate_fetch_date}")

# Display the additional table for the ace7plus companies
st.subheader("ACE7Plus Companies Detailed Information")
cols = st.columns(5)
for idx, row in additional_data.iterrows():
    col = cols[idx % 5]
    col.markdown(f"""
    <div class="css-1r6slb0 e1tzin5v2">
        <b>{row['Ticker']} ({row['Ticker']})</b><br>
        {row['Company Info']}
    </div>
    """, unsafe_allow_html=True)

# Display the table for ace7plus companies
st.subheader("Market Cap Rankings")
st.dataframe(df[['Ticker', 'Market Cap ($B)', 'Market Cap (₩조원)']], width=800)