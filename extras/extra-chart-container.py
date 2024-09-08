import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.chart_container import chart_container

# 랜덤 데이터 생성을 위한 함수
def _get_random_data():
    # 임의의 데이터프레임 생성 (10개의 행과 3개의 열)
    chart_data = pd.DataFrame(
        np.random.randn(10, 3),  # 10행 3열의 난수 생성
        columns=['A', 'B', 'C']  # 열 이름 지정
    )
    return chart_data

# 차트를 표시하는 함수
def example_one():
    st.header("Chart container example")
    chart_data = _get_random_data()
    
    # 차트를 chart_container로 감싸기
    with chart_container(chart_data):
        st.write("Here's a cool chart")
        st.area_chart(chart_data)

# 함수 실행
example_one()
