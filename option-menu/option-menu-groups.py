import streamlit as st
from streamlit_option_menu import option_menu

# 사이드바에 그룹핑된 메뉴 설정
with st.sidebar:
    selected = option_menu(
        menu_title="작업 메뉴",  # 메뉴 타이틀
        options=[
            "--- 데이터 처리 ---",  # 그룹화
            "전처리",
            "임베딩",
            "업로드",
            "--- 데이터 검색 ---",  # 그룹화
            "BM25",
            "벡터",
            "하이브리드"
        ],
        icons=["", "filter", "graph-up", "cloud-upload", "", "search", "compass", "layers"],
        menu_icon="cast",
        default_index=0,  # 기본 선택 없음
        key="main_menu"
    )

# 선택된 메뉴에 따라 작업 실행
if selected is not None:
    if "---" not in selected:  # 그룹 헤더가 선택되지 않도록 필터링
        # 선택된 메뉴에 따라 실행할 작업
        if selected == "전처리":
            st.write("전처리 작업을 수행합니다.")
        elif selected == "임베딩":
            st.write("임베딩 작업을 수행합니다.")
        elif selected == "업로드":
            st.write("데이터 업로드 작업을 수행합니다.")
        elif selected == "BM25":
            st.write("BM25 검색을 수행합니다.")
        elif selected == "벡터":
            st.write("벡터 검색을 수행합니다.")
        elif selected == "하이브리드":
            st.write("하이브리드 검색을 수행합니다.")
else:
    st.write("메뉴에서 작업을 선택해주세요.")
