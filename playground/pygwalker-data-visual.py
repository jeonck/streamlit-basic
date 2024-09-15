import streamlit as st
import pandas as pd
import pygwalker as pyg
import streamlit.components.v1 as components
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 맑은고딕 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

st.set_page_config(layout="wide")

st.title("🎨 창의적인 데이터 시각화 도구")

# 데이터 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("데이터 미리보기:")
    st.dataframe(df.head())

    # PyGWalker 시각화
    pyg_html = pyg.to_html(df)
    components.html(pyg_html, height=1000, scrolling=True)

    # 추가 분석 옵션
    st.header("추가 분석 옵션")
    
    # 상관관계 히트맵
    if st.checkbox("상관관계 히트맵 보기"):
        st.write("수치형 열의 상관관계:")
        corr = df.select_dtypes(include=['float64', 'int64']).corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        plt.title("상관관계 히트맵", fontsize=16)
        st.pyplot(fig)

    # 기본 통계 정보
    if st.checkbox("기본 통계 정보 보기"):
        st.write(df.describe())

    # 결측치 정보
    if st.checkbox("결측치 정보 보기"):
        missing_data = df.isnull().sum()
        st.write(missing_data[missing_data > 0])

st.sidebar.header("앱 정보")
st.sidebar.info("이 앱은 Streamlit과 PyGWalker를 사용하여 데이터를 시각화하고 분석합니다. CSV 파일을 업로드하고 다양한 시각화 옵션을 탐색해보세요!")

