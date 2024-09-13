import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = "여기에_당신의_API_키를_입력하세요"

# 페이지 구성 설정
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# 스트림릿 앱 제목 설정
st.title("ChatGPT 인터페이스")

# 채팅 기록을 저장할 리스트
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 채팅 기록 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 채팅 입력
if prompt := st.chat_input("무엇을 도와드릴까요?"):
    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # ChatGPT API 호출
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "당신은 도움이 되는 AI 어시스턴트입니다."},
            *st.session_state.messages
        ]
    )

    # 봇 응답 추가
    bot_response = response.choices[0].message['content']
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)

# CSS를 사용하여 채팅 입력을 화면 하단에 고정
st.markdown(
    """
    <style>
    .stChatFloatingInputContainer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 1rem;
        background-color: white;
        z-index: 1000;
    }
    .main {
        padding-bottom: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
