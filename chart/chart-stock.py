import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import requests

# Streamlit 페이지 설정
st.set_page_config(
    page_title="Stock Moving Averages",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)

# Streamlit 타이틀
st.title("Stock Moving Averages Visualization")

# 티커 입력 받기
ticker_input = st.text_input("Enter the stock ticker: msft aapl nvda googl tsla amzn tsm lly nov avgo orcl nflx meta qqq ", "QQQ")

# 기간 선택
period_options = {
    "3 years": 3,
    "6 years": 6,
    "9 years": 9,
    "12 years": 12,
    "Max": None
}
selected_period = st.selectbox("Select the period:", list(period_options.keys()))

# 기간 계산
if selected_period == "Max":
    start_date = None
else:
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=period_options[selected_period] * 365)).strftime('%Y-%m-%d')

# 주식 데이터 가져오기
ticker = yf.Ticker(ticker_input)
if start_date:
    yf_data = ticker.history(start=start_date, end=end_date)
else:
    yf_data = ticker.history(period='max')

# 데이터가 있는지 확인
if not yf_data.empty:
    # 종가 데이터만 사용
    yf_data = yf_data[['Close']]

    # 이동평균선 계산
    yf_data['120_MA'] = yf_data['Close'].rolling(window=120).mean()
    yf_data['200_MA'] = yf_data['Close'].rolling(window=200).mean()

    # 120일 이동평균선의 기울기 계산
    yf_data['120_MA_Slope'] = yf_data['120_MA'].diff()

    # 200일 이동평균선의 기울기 계산
    yf_data['200_MA_Slope'] = yf_data['200_MA'].diff()

    # 120일 이동평균선의 기울기가 가장 낮은 지점 찾기
    min_slope_120_idx = yf_data['120_MA_Slope'].idxmin()
    min_slope_120_date = yf_data.loc[min_slope_120_idx].name
    min_slope_120_value = yf_data.loc[min_slope_120_idx, '120_MA']

    # 200일 이동평균선의 기울기가 가장 낮은 지점 찾기
    min_slope_200_idx = yf_data['200_MA_Slope'].idxmin()
    min_slope_200_date = yf_data.loc[min_slope_200_idx].name
    min_slope_200_value = yf_data.loc[min_slope_200_idx, '200_MA']

    # 그래프 그리기
    st.subheader(f"{ticker_input} Stock Price with Moving Averages ({selected_period})")

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=yf_data.index, y=yf_data['Close'], mode='lines', name='Close Price',
                             line=dict(color='darkgray')))
    fig.add_trace(go.Scatter(x=yf_data.index, y=yf_data['120_MA'], mode='lines', name='120-day MA',
                             line=dict(color='red')))
    fig.add_trace(go.Scatter(x=yf_data.index, y=yf_data['200_MA'], mode='lines', name='200-day MA',
                             line=dict(color='blue')))

    # 120일 이동평균선의 기울기가 가장 낮은 지점 표시 (동그라미 모양)
    fig.add_trace(go.Scatter(x=[min_slope_120_date], y=[min_slope_120_value], mode='markers+text',
                             name='Lowest Slope Point 120 MA',
                             marker=dict(color='red', size=12, symbol='circle'),
                             text=["Lowest Slope 120 MA"],
                             textposition="top center"))

    # 200일 이동평균선의 기울기가 가장 낮은 지점 표시 (별 모양)
    fig.add_trace(go.Scatter(x=[min_slope_200_date], y=[min_slope_200_value], mode='markers+text',
                             name='Lowest Slope Point 200 MA',
                             marker=dict(color='blue', size=12, symbol='star'),
                             text=["Lowest Slope 200 MA"],
                             textposition="top center"))

    fig.update_layout(
        title=f"{ticker_input} Stock Price and Moving Averages ({selected_period})",
        xaxis_title="Date",
        yaxis_title="Price",
        legend_title="Legend",
        hovermode="x unified",
        height=800  # 그래프 높이를 조정
    )

    # 그래프를 Streamlit에 표시
    st.plotly_chart(fig)
else:
    st.error("No data found for the entered ticker.")

# # 뉴스 가져오기
# st.subheader(f"{ticker_input} News")

# try:
#     news = ticker.get_news()
#     if news:
#         for article in news:
#             st.markdown(f"### [{article['title']}]({article['link']})")
#             st.markdown(f"Published on: {article.get('provider_publish_time', 'N/A')}")
#             st.markdown(f"Source: {article.get('publisher', 'N/A')}")
#             st.write(article.get('summary', 'No summary available'))
#             st.markdown("---")
#     else:
#         st.write("No news found for the entered ticker.")
# except requests.exceptions.JSONDecodeError:
#     st.error("Failed to decode JSON response from the API.")
# except Exception as e:
#     st.error(f"An unexpected error occurred: {e}")