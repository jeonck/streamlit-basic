import streamlit as st
from streamlit_extras.bottom_container import bottom

def example():
    st.title("This is the title")

    # 'bottom' 컨테이너에서 입력을 받아 변수에 저장, label_visibility를 사용하여 라벨 숨김
    with bottom():
        user_input = st.text_input("Input", "오늘도 즐거운 하루 되세요!!!", label_visibility="hidden")

    # 메인 컨테이너에 입력된 내용을 표시
    st.write(f"{user_input}")

example()
