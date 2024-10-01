import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import pytz
import sqlite3

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
        current_price = stock.history(period='1d')['Close'].iloc[-1]  # 현재가 정보 추가

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

        return market_cap, ytd_return, one_year_return, five_year_return, current_price  # 현재가 정보 반환
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {e}")
        return None, None, None, None, None

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
        cap, ytd, one_year, five_year, current_price = get_stock_info(ticker)
        if cap:
            market_caps.append((ticker, cap, ytd, one_year, five_year, current_price))
        else:
            st.error(f"Failed to fetch data for {ticker}")
    return market_caps

# SQLite 데이터베이스 연결 설정
def get_db_connection():
    conn = sqlite3.connect('high_points.db')
    conn.row_factory = sqlite3.Row
    return conn

# SQLite 데이터베이스 테이블 생성
def create_high_points_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS high_points (
            ticker TEXT PRIMARY KEY,
            high_point REAL
        )
    ''')
    conn.commit()
    conn.close()

# 전고점 값을 저장하는 함수
def save_high_point(ticker, high_point):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO high_points (ticker, high_point)
        VALUES (?, ?)
        ON CONFLICT(ticker)
        DO UPDATE SET high_point=excluded.high_point
    ''', (ticker, high_point))
    conn.commit()
    conn.close()

# 전고점 값을 불러오는 함수
@st.cache_data(ttl=24*3600)
def get_high_points():
    create_high_points_table()  # Ensure table exists
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM high_points')
    rows = cursor.fetchall()
    high_points = {row['ticker']: row['high_point'] for row in rows}
    conn.close()
    return high_points

# Fetch the market caps
market_caps = fetch_market_caps(ace7plus_tickers)

# Fetch the USD to KRW exchange rate
exchange_rate, exchange_rate_fetch_date = get_exchange_rate()
if exchange_rate is None:
    exchange_rate = 1380  # Fallback to a default value if fetching fails
    exchange_rate_fetch_date = datetime.now(pytz.timezone('America/New_York')).strftime("%Y-%m-%d %H:%M:%S")

# Create a DataFrame
df = pd.DataFrame(market_caps, columns=['Ticker', 'Market Cap', 'YTD Return', '1-Year Return', '5-Year Return', 'Current Price'])
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
df['Current Price'] = df['Current Price'].apply(lambda x: f"${x:.2f}")  # 현재가 정보 형식화

# Extract additional data for the ace7plus companies
additional_data = df.copy()
additional_data.reset_index(drop=True, inplace=True)
additional_data['Rank'] = additional_data.index + 1
additional_data['Company Info'] = additional_data.apply(
    lambda row: f"{row['Ticker']} |\n현재가: {row['Current Price']}, 연초대비: {row['YTD Return']}, 1년전: {row['1-Year Return']}, 5년전: {row['5-Year Return']}",
    axis=1)

# 전고점 값을 불러오기
high_points = get_high_points()

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
    high_point_value = high_points.get(row['Ticker'], 0.0) # default to 0.0 if not in the database
    high_point_input = col.number_input(
        f"전고점 ({row['Ticker']})",
        min_value=0.0,
        value=high_point_value,
        key=row['Ticker']
    )
    if high_point_input and high_point_input != high_point_value:
        save_high_point(row['Ticker'], high_point_input)
    if high_point_input > 0:
        percentage_of_high = (float(row['Current Price'][1:]) / high_point_input) * 100  # 현재가 대비 전고점 비율 계산
        percentage_display = f"{percentage_of_high:.1f}%"
    else:
        percentage_display = "N/A"
    col.markdown(f"""
    <div class="css-1r6slb0 e1tzin5v2">
        <b>{row['Ticker']} ({row['Ticker']})</b><br>
        {row['Company Info']}<br>
        전고점: {high_point_input}$<br>
        현재가/전고점: {percentage_display}
    </div>
    """, unsafe_allow_html=True)

# Display the table for ace7plus companies
st.subheader("Market Cap Rankings")
st.dataframe(df[['Ticker', 'Market Cap ($B)', 'Market Cap (₩조원)']], width=800)

# 한국 ETF 종목 추가
korean_etf_tickers = ['465580.KS', '457480.KS', '381180.KS', '371460.KS', '453850.KS']  # 대표적인 5개 ETF

# 한국 ETF 시장 정보 가져오는 함수
@st.cache_data(ttl=24*3600)
def get_korean_etf_info(ticker):
    try:
        df_stock = yf.download(ticker, start='2000-01-01', end=datetime.now().strftime('%Y-%m-%d'))
        if df_stock.empty:
            raise ValueError(f"No historical data for {ticker}")

        current_price = df_stock['Close'].iloc[-1]
        jan_2 = df_stock[df_stock.index.month == 1].iloc[0].name  # Use the first entry in January

        ytd_return = (df_stock['Close'].iloc[-1] / df_stock['Close'].loc[jan_2] - 1) * 100
        one_year_return = (df_stock['Close'].iloc[-1] / df_stock['Close'].iloc[-252] - 1) * 100
        five_year_return = (df_stock['Close'].iloc[-1] / df_stock['Close'].iloc[0] - 1) * 100

        return ytd_return, one_year_return, five_year_return, current_price
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {e}")
        return None, None, None, None

# Korean ETF 데이터 가져오기
korean_etf_market_caps = []
for ticker in korean_etf_tickers:
    ytd, one_year, five_year, current_price = get_korean_etf_info(ticker)
    if ytd is not None:
        korean_etf_market_caps.append((ticker, ytd, one_year, five_year, current_price))

# DataFrame 생성
korean_etf_df = pd.DataFrame(korean_etf_market_caps, columns=['티커', 'YTD Return', '1-Year Return', '5-Year Return', 'Current Price'])
korean_etf_df = korean_etf_df.dropna()

# 숫자 포맷 변경
korean_etf_df['YTD Return'] = korean_etf_df['YTD Return'].apply(lambda x: f"{x:.1f}%")
korean_etf_df['1-Year Return'] = korean_etf_df['1-Year Return'].apply(lambda x: f"{x:.1f}%")
korean_etf_df['5-Year Return'] = korean_etf_df['5-Year Return'].apply(lambda x: f"{x:.1f}%")
korean_etf_df['Current Price'] = korean_etf_df['Current Price'].apply(lambda x: f"₩{x:.2f}")

# 한국 ETF 종목 카드 형식으로 정보 표시
st.subheader("한국 ETF 종목 정보")
cols = st.columns(5)

for idx, row in korean_etf_df.iterrows():
    col = cols[idx % 5]
    high_point_value = high_points.get(row['티커'], 0.0)  # default to 0.0 if not in the database
    high_point_input = col.number_input(
        f"전고점 ({row['티커']})",
        min_value=0.0,
        value=high_point_value,
        key=row['티커']
    )
    if high_point_input and high_point_input != high_point_value:
        save_high_point(row['티커'], high_point_input)
    if high_point_input > 0:
        percentage_of_high = (float(row['Current Price'][1:].replace(',', '')) / high_point_input) * 100  # 현재가 대비 전고점 비율 계산
        percentage_display = f"{percentage_of_high:.1f}%"
    else:
        percentage_display = "N/A"
    col.markdown(f"""
    <div class="css-1r6slb0 e1tzin5v2">
        <b>{row['티커']}</b><br>
        현재가: {row['Current Price']}<br>
        연초대비: {row['YTD Return']}<br>
        1년전: {row['1-Year Return']}<br>
        5년전: {row['5-Year Return']}<br>
        전고점: {high_point_input}₩<br>
        현재가/전고점: {percentage_display}
    </div>
    """, unsafe_allow_html=True)