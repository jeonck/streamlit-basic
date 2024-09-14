import streamlit as st
from textblob import TextBlob

st.title("감정 분석 채팅")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "user":
            sentiment = TextBlob(message["content"]).sentiment.polarity
            if sentiment > 0:
                st.caption("긍정적인 메시지입니다.")
            elif sentiment < 0:
                st.caption("부정적인 메시지입니다.")
            else:
                st.caption("중립적인 메시지입니다.")

if prompt := st.chat_input("메시지를 입력하세요:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        sentiment = TextBlob(prompt).sentiment.polarity
        if sentiment > 0:
            st.caption("긍정적인 메시지입니다.")
        elif sentiment < 0:
            st.caption("부정적인 메시지입니다.")
        else:
            st.caption("중립적인 메시지입니다.")
