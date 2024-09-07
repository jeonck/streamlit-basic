import streamlit as st

# 기본 페이지 내용
st.title("Streamlit Modal Example")
st.write("This is the main page content.")

# 모달을 대체하는 expander
with st.expander("Open Modal", expanded=False):
    st.write("This is the modal content.")
    if st.button("Close Modal"):
        st.rerun()  # 모달 닫기 위해 페이지 새로고침
