import streamlit as st
import plotly.graph_objects as go

st.title("st.html() 활용 예제")

st.header(" 사용자 정의 CSS 스타일링")
custom_html = """
<style>
.custom-box {
    background-color: #f0f0f0;
    border: 2px solid #333;
    padding: 20px;
    border-radius: 10px;
}
</style>
<div class="custom-box">
    <h2>환영합니다!</h2>
    <p>이것은 사용자 정의 스타일이 적용된 박스입니다.</p>
</div>
"""
st.html(custom_html)

