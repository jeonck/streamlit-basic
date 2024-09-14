import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# 데이터 생성 (세션 상태 유지)
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame({
        "날짜": pd.date_range(start="2023-01-01", periods=100),
        "판매량": np.random.randint(50, 200, 100),
        "수익": np.random.randint(1000, 5000, 100),
        "제품": np.random.choice(["A", "B", "C"], 100)
    })
df = st.session_state.data

# 차트 생성
brush = alt.selection_interval(name="brush")
click = alt.selection_multi(fields=['제품'], name="click")

color_scale = alt.Scale(domain=['A', 'B', 'C'], range=['#1f77b4', '#ff7f0e', '#2ca02c'])

chart = alt.Chart(df).mark_circle(size=60).encode(
    x='날짜:T',
    y='판매량:Q',
    color=alt.condition(brush, '제품:N', alt.value('lightgray'), scale=color_scale),
    size='수익:Q',
    tooltip=['날짜', '판매량', '수익', '제품']
).properties(
    width=700,
    height=400,
    title='제품별 판매량 및 수익 추이'
).add_selection(
    brush, click
)

# Streamlit 앱
st.title('인터랙티브 판매 데이터 분석')

# 차트 표시
st.altair_chart(chart, use_container_width=True)




