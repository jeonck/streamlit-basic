import streamlit as st
import pandas as pd
from streamlit_elements import elements, mui, html

# 페이지 설정
st.set_page_config(layout="wide")

st.title("실시간 파일 업로드 및 데이터 처리")

# 파일 업로드 위젯
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

# 파일이 업로드되었을 때 처리
if uploaded_file is not None:
    # CSV 파일을 읽어들이기
    df = pd.read_csv(uploaded_file)
    
    # 각 열을 수치형으로 변환, 변환 불가한 값은 NaN 처리
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # 파일 내용 미리보기
    st.subheader("업로드된 파일 내용")
    st.dataframe(df)
    
    # 데이터 처리 (예: 데이터 요약)
    st.subheader("데이터 요약")
    st.write(df.describe())

    # 실시간 데이터 처리 UI (Streamlit-Elements 사용)
    with elements("processed_data"):
        mui.Grid(container=True, spacing=2)(
            # 데이터 처리 결과 1: 최대값 계산
            mui.Grid(item=True, xs=12, md=6)(
                mui.Card(
                    mui.CardContent(
                        html.h2("최대값 데이터"),
                        html.p(f"최대값: {df.max().to_dict()}")
                    )
                )
            ),
            # 데이터 처리 결과 2: 최소값 계산
            mui.Grid(item=True, xs=12, md=6)(
                mui.Card(
                    mui.CardContent(
                        html.h2("최소값 데이터"),
                        html.p(f"최소값: {df.min().to_dict()}")
                    )
                )
            )
        )

else:
    st.info("CSV 파일을 업로드하세요.")
