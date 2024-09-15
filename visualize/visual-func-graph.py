import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt

# 페이지 설정
st.set_page_config(layout="wide", page_title="창의적인 데이터 시각화")

# 제목
st.title("🎨 함수 시각화 대시보드")


# 사용자 입력 또는 선택을 통한 함수 시각화
st.subheader("사용자 정의 함수 시각화")

function_examples = [
    "x**2", "np.sin(x)", "np.cos(x)", "np.tan(x)", "np.exp(x)",
    "np.log(x)", "x**3 - 2*x + 1", "np.sqrt(abs(x))", "np.sin(x) * np.cos(x)",
    "1 / (1 + np.exp(-x))", "np.sinh(x)", "np.cosh(x)", "np.tanh(x)",
    "np.arcsin(x)", "np.arccos(x)", "np.arctan(x)", "np.sinc(x)",
    "np.sign(x)", "np.ceil(x)", "np.floor(x)", "np.abs(x)",
    "np.log10(abs(x))", "np.log2(abs(x))", "np.exp2(x)", "np.power(x, 3)"
]

col1, col2 = st.columns(2)

with col1:
    function1 = st.selectbox("함수 1 선택:", options=function_examples + ["직접 입력"], index=0, key="func1")
    if function1 == "직접 입력":
        function1 = st.text_input("함수 1을 입력하세요:", "x**2", key="input1")

with col2:
    function2 = st.selectbox("함수 2 선택:", options=function_examples + ["직접 입력"], index=1, key="func2")
    if function2 == "직접 입력":
        function2 = st.text_input("함수 2를 입력하세요:", "np.sin(x)", key="input2")

x_range = st.slider("x 범위", -10.0, 10.0, (-5.0, 5.0))
x = np.linspace(x_range[0], x_range[1], 200)

fig = px.line()
y1 = eval(function1)
fig.add_scatter(x=x, y=y1, name=function1)
y2 = eval(function2)
fig.add_scatter(x=x, y=y2, name=function2)

fig.update_layout(
    title="함수 비교",
    xaxis_title="X",
    yaxis_title="Y",
    legend_title="함수"
)

st.plotly_chart(fig, use_container_width=True)

#
