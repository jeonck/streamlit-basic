import streamlit as st
import random

st.title("AI 요리사 챗봇")

# 이전 대화 기록을 저장할 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 받기
prompt = st.chat_input("요리에 대해 무엇이든 물어보세요!")

if prompt:
    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI 응답 생성 (실제 AI 대신 간단한 랜덤 응답 사용)
    responses = [
        "그 요리에는 신선한 재료가 중요해요.",
        "조리 시간을 조금 더 늘려보는 건 어떨까요?",
        "소금 대신 간장을 사용해보세요. 풍미가 좋아질 거예요.",
        "그 요리에 약간의 레몬즙을 추가하면 맛이 더 산뜻해질 거예요.",
        "요리할 때 온도 조절이 매우 중요해요. 천천히 낮은 온도로 조리해보세요."
    ]
    ai_response = random.choice(responses)

    # AI 응답 표시
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    with st.chat_message("assistant"):
        st.markdown(ai_response)
