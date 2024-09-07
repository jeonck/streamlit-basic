import streamlit as st
import pathlib

# 현재 디렉토리 경로 가져오기
CURRENT_DIR = pathlib.Path(__file__).parent.resolve()

# 로고에 링크와 아이콘 이미지 추가
st.logo(
    str(CURRENT_DIR / "images/st-logo.svg"),  # 로고 이미지 경로
    link="https://docs.streamlit.io/",  # 클릭 시 이동할 링크
    icon_image=str(CURRENT_DIR / "images/st-logo.svg")  # 아이콘 이미지
)
