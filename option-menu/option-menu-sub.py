import streamlit as st
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu
import pandas as pd
import numpy as np
import time

# 페이지 설정
st.set_page_config(layout="wide")

# 상태를 유지하는 함수
def rerun_app():
    st.rerun()

# 사이드바 메뉴
with st.sidebar:
    selected_main = option_menu(
        menu_title="Main Menu",  # 메인 메뉴 타이틀
        options=["Home", "Analysis", "Visualization", "Settings"],  # 메인 메뉴 옵션들
        icons=["house", "clipboard-data", "graph-up", "gear"],  # 메인 메뉴 아이콘들
        menu_icon="cast",  # 메인 메뉴 아이콘
        default_index=0,  # 기본 선택 옵션
    )

# 서브메뉴 설정
if selected_main == "Analysis":
    selected_sub = option_menu(
        menu_title="Choose Analysis Type",  # 서브 메뉴 타이틀
        options=["Data Upload", "Show Statistics"],  # 서브 메뉴 옵션들
        icons=["cloud-upload", "bar-chart"],  # 서브 메뉴 아이콘들
        menu_icon="bi-list",  # 서브 메뉴 아이콘
        default_index=0,  # 기본 선택 옵션
        orientation="horizontal"  # 서브메뉴는 가로로 배치
    )
elif selected_main == "Visualization":
    selected_sub = option_menu(
        menu_title="Choose Chart Type",  # 서브 메뉴 타이틀
        options=["Line Chart", "Bar Chart", "Area Chart"],  # 서브 메뉴 옵션들
        icons=["graph-up-arrow", "bar-chart-fill", "area-chart"],  # 서브 메뉴 아이콘들
        menu_icon="bar-chart-line",  # 서브 메뉴 아이콘
        default_index=0,  # 기본 선택 옵션
        orientation="horizontal"  # 서브메뉴는 가로로 배치
    )

# 선택한 메뉴에 따라 동적 UI 구성
if selected_main == "Home":
    st.title("Welcome to the Home Page!")
    st.write("Choose an option from the sidebar to explore.")

elif selected_main == "Analysis":
    st.title("Data Analysis Section")
    
    if selected_sub == "Data Upload":
        st.write("Upload your CSV file for analysis.")
        data_file = st.file_uploader("Upload a CSV file", type=["csv"])
        if data_file is not None:
            df = pd.read_csv(data_file)
            st.write("Data Preview:")
            st.dataframe(df.head())
    
    elif selected_sub == "Show Statistics":
        st.write("Upload a file to display statistics.")
        data_file = st.file_uploader("Upload a CSV file", type=["csv"])
        if data_file is not None:
            df = pd.read_csv(data_file)
            st.write("Data Statistics:")
            st.write(df.describe())

elif selected_main == "Visualization":
    st.title("Data Visualization Section")
    
    # 샘플 데이터 생성
    data = np.random.randn(10, 3)
    df = pd.DataFrame(data, columns=["A", "B", "C"])

    if selected_sub == "Line Chart":
        st.line_chart(df)
    elif selected_sub == "Bar Chart":
        st.bar_chart(df)
    elif selected_sub == "Area Chart":
        st.area_chart(df)

elif selected_main == "Settings":
    st.title("App Settings")
    st.write("Adjust your app settings here.")
    
    theme = st.radio("Select Theme", ["Light", "Dark"], index=0)
    
    # 재실행 버튼
    if st.button("Reset App"):
        st.write("App is being reset...")
        time.sleep(1)
        rerun_app()

# rerun이 실행되면 앱이 재실행됩니다.
