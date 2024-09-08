import streamlit as st
import pandas as pd
import numpy as np
import time

# 페이지 설정
st.set_page_config(layout="wide")

# 상태를 유지하는 함수
def rerun_app():
    st.rerun()

# 사이드바에서 메뉴 그룹을 구성
with st.sidebar:
    st.title("Menu")
    
    # 첫 번째 메뉴 그룹 (Group 1)
    with st.expander("Group 1", expanded=True):
        home_selected = st.checkbox("Home")
        data_analysis_selected = st.checkbox("Data Analysis")
    
    # 두 번째 메뉴 그룹 (Group 2)
    with st.expander("Group 2", expanded=False):
        visualization_selected = st.checkbox("Visualization")
        settings_selected = st.checkbox("Settings")

# Main Container에 동적 UI 표시
if home_selected:
    st.title("Home")
    st.write("Welcome to the Home Page!")
    st.write("Explore the menu options from the sidebar to display different content here.")

if data_analysis_selected:
    st.title("Data Analysis")
    st.write("Perform data analysis here.")
    
    # CSV 파일 업로드 및 분석
    data_file = st.file_uploader("Upload a CSV file for analysis", type=["csv"])
    if data_file is not None:
        df = pd.read_csv(data_file)
        st.write("Data Preview:")
        st.dataframe(df.head())
        if st.button("Show Statistics"):
            st.write(df.describe())

if visualization_selected:
    st.title("Data Visualization")
    st.write("Visualize data here.")
    
    # 데이터 시각화 옵션
    chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Area Chart"])
    
    # 샘플 데이터 생성
    data = np.random.randn(10, 3)
    df = pd.DataFrame(data, columns=["A", "B", "C"])

    # 선택한 차트 유형에 따라 시각화
    if chart_type == "Line Chart":
        st.line_chart(df)
    elif chart_type == "Bar Chart":
        st.bar_chart(df)
    elif chart_type == "Area Chart":
        st.area_chart(df)

if settings_selected:
    st.title("App Settings")
    st.write("Adjust your app settings here.")
    
    # 테마 선택 옵션
    theme = st.radio("Select Theme", ["Light", "Dark"], index=0)
    
    # 앱 재실행 버튼
    if st.button("Reset App"):
        st.write("App is being reset...")
        time.sleep(1)
        rerun_app()
