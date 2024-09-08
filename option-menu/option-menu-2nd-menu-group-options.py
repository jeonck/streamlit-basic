import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(layout="wide")

# 첫 번째 옵션 그룹
with st.sidebar:
    st.markdown("### Main Menu")
    selected_main = option_menu(
        menu_title=None,  # 메뉴 타이틀 없음 (그룹의 헤더는 따로 마크다운으로 처리)
        options=["Home", "Data Analysis", "Visualization"],  
        icons=["house", "clipboard-data", "bar-chart"],  
        menu_icon="cast",  
        default_index=0,  
        key="main_menu"
    )

# 두 번째 옵션 그룹
with st.sidebar:
    st.markdown("### Advanced Options")
    selected_advanced = option_menu(
        menu_title=None,  # 메뉴 타이틀 없음
        options=["Settings", "About", "Contact"],  
        icons=["gear", "info-circle", "envelope"],  
        menu_icon="cast",  
        default_index=0,  
        key="advanced_menu"
    )

# 첫 번째 메뉴에 따른 동적 UI 구성
if selected_main == "Home":
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

elif selected_main == "Data Analysis":
    st.title("Data Analysis")
    data_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if data_file is not None:
        df = pd.read_csv(data_file)
        st.write("Data Preview:")
        st.dataframe(df.head())
        
        if st.button("Show Statistics"):
            st.write(df.describe())

elif selected_main == "Visualization":
    st.title("Data Visualization")
    rows = st.slider("Number of rows", 10, 100, 10)
    cols = st.slider("Number of columns", 1, 10, 3)
    df = pd.DataFrame(np.random.randn(rows, cols), columns=[f"Col {i+1}" for i in range(cols)])
    
    chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Area Chart"])
    
    if chart_type == "Line Chart":
        st.line_chart(df)
    elif chart_type == "Bar Chart":
        st.bar_chart(df)
    elif chart_type == "Area Chart":
        st.area_chart(df)

# 두 번째 그룹 메뉴에 따른 UI 구성
if selected_advanced == "Settings":
    st.title("App Settings")
    theme = st.radio("Choose Theme", ["Light", "Dark"], index=0)

elif selected_advanced == "About":
    st.title("About This App")
    st.write("This app is designed to demonstrate advanced Streamlit features using the option menu.")

elif selected_advanced == "Contact":
    st.title("Contact Us")
    st.write("You can contact us at example@example.com.")
