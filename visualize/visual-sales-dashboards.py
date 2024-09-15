import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# 페이지 설정
st.set_page_config(layout="wide")

# 데이터 생성
@st.cache_data
def generate_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    sales = np.random.randint(100, 1000, size=len(dates))
    return pd.DataFrame({'date': dates, 'sales': sales})

df = generate_data()

# 대시보드 제목
st.title('판매 데이터 대시보드')

# 날짜 범위 선택
date_range = st.date_input('날짜 범위 선택', [df['date'].min(), df['date'].max()])

# 선택된 날짜로 데이터 필터링
filtered_df = df[(df['date'].dt.date >= date_range[0]) & (df['date'].dt.date <= date_range[1])]

# 2개의 컬럼 생성
col1, col2 = st.columns(2)

# 첫 번째 줄
with col1:
    # 라인 차트
    fig_line = px.line(filtered_df, x='date', y='sales', title='일별 판매량')
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    # 막대 차트
    monthly_df = filtered_df.set_index('date').resample('M')['sales'].sum().reset_index()
    fig_bar = px.bar(monthly_df, x='date', y='sales', title='월별 판매량')
    st.plotly_chart(fig_bar, use_container_width=True)

# 두 번째 줄
with col1:
    # 통계 정보
    st.subheader('판매 통계')
    stat_col1, stat_col2, stat_col3 = st.columns(3)
    stat_col1.metric('총 판매량', f"{filtered_df['sales'].sum():,}")
    stat_col2.metric('평균 일일 판매량', f"{filtered_df['sales'].mean():.2f}")
    stat_col3.metric('최고 판매일', filtered_df.loc[filtered_df['sales'].idxmax(), 'date'].strftime('%Y-%m-%d'))

with col2:
    # 상위 판매일 테이블
    st.subheader('상위 5 판매일')
    st.dataframe(filtered_df.nlargest(5, 'sales')[['date', 'sales']], use_container_width=True)
