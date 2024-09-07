import streamlit as st
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu
import time
import pandas as pd

# 페이지 설정
st.set_page_config(layout="wide")

# Streamlit-Option-Menu 사이드바에 여러 옵션 구성
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # 메뉴 타이틀
        options=["Home", "Data Analysis", "Visualization", "Settings"],  # 옵션들
        icons=["house", "bar-chart-line", "graph-up", "gear"],  # 아이콘들
        menu_icon="cast",  # 메인 메뉴 아이콘
        default_index=0,  # 기본 선택 옵션
    )

# 상태를 유지하는 함수
def rerun_app():
    st.rerun()

# 선택한 메뉴에 따라 UI가 동적으로 변경
if selected == "Home":
    st.title("Welcome to the Home Page!")
    st.write("Choose an option from the sidebar to explore.")

elif selected == "Data Analysis":
    st.title("Data Analysis Section")
    st.write("Perform data analysis here.")
    
    # 데이터 파일 업로드 및 분석
    data_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if data_file is not None:
        import pandas as pd
        df = pd.read_csv(data_file)
        st.write("Data Preview:")
        st.dataframe(df.head())
        
        # 데이터 통계
        if st.button("Show Statistics"):
            st.write(df.describe())

elif selected == "Visualization":
    st.title("Data Visualization Section")
    st.write("Visualize data here.")
    
    chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Area Chart"])
    
    # 샘플 데이터 생성
    import numpy as np
    data = np.random.randn(10, 3)
    df = pd.DataFrame(data, columns=["A", "B", "C"])

    # 선택한 차트 유형에 따라 시각화
    if chart_type == "Line Chart":
        st.line_chart(df)
    elif chart_type == "Bar Chart":
        st.bar_chart(df)
    elif chart_type == "Area Chart":
        st.area_chart(df)

elif selected == "Settings":
    st.title("App Settings")
    st.write("Adjust your app settings here.")
    
    # 예시 설정 옵션
    theme = st.radio("Select Theme", ["Light", "Dark"], index=0)
    
    # 재실행 버튼
    if st.button("Reset App"):
        st.write("App is being reset...")
        time.sleep(1)
        rerun_app()

# rerun이 실행되면 앱이 재실행됩니다.
