import streamlit as st

st.title("피드백 폼")
c1, c2 = st.columns(2)

with c1:
    with st.expander("오늘의 기분"):
        st.write("오늘 하루는 어떠셨나요?")
        st.write("기분 평가:")
        st.feedback("faces")

with c2:
    with st.expander("서비스 만족도"):
        st.write("우리 서비스에 대해 어떻게 생각하시나요?")
        st.write("서비스 평가:")
        st.feedback("stars")

st.write("---")
st.write("이 페이지가 도움이 되셨나요?")
st.feedback("thumbs")
