import streamlit as st
import pandas as pd
import altair as alt

# 데이터 생성
data = pd.DataFrame({
    '과일': ['사과', '바나나', '오렌지', '딸기'],
    '판매량': [20, 35, 15, 25]
})

# Streamlit 앱 제목
st.title('과일 판매량 차트')

# Vega-Lite 차트 생성
chart = alt.Chart(data).mark_bar().encode(
    x='과일',
    y='판매량',
    color='과일'
).properties(
    width=600,
    height=400
)

# 차트 표시
st.altair_chart(chart)
