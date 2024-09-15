import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.set_page_config(page_title="아름다운 시각화", layout="wide")

st.title("🌈 데이터 시각화")

# 데이터 생성
np.random.seed(42)
df = pd.DataFrame({
    '날짜': pd.date_range(start='2023-01-01', periods=100),
    '값': np.cumsum(np.random.randn(100)),
    '카테고리': np.random.choice(['A', 'B', 'C'], 100)
})

# 인터랙티브 차트
st.subheader("🎨 인터랙티브 라인 차트")
chart = alt.Chart(df).mark_line().encode(
    x='날짜',
    y='값',
    color='카테고리',
    tooltip=['날짜', '값', '카테고리']
).interactive()

st.altair_chart(chart, use_container_width=True)

