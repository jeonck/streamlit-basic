import streamlit as st
import random

# 인용구 데이터
quotes = [
    {
        "text": "상상력은 지식보다 중요하다. 지식은 제한되어 있지만 상상력은 세상의 모든 것을 아우른다.",
        "author": "알베르트 아인슈타인"
    },
    {
        "text": "네 자신을 알라.",
        "author": "소크라테스"
    },
    {
        "text": "생각하는 대로 살지 않으면, 사는 대로 생각하게 된다.",
        "author": "폴 부르제"
    },
    {
        "text": "가장 큰 위험은 위험 없는 삶을 사는 것이다.",
        "author": "스티븐 코비"
    },
    {
        "text": "실패는 성공의 어머니이다.",
        "author": "토마스 에디슨"
    }
]

# 세션 상태로 현재 인용구 인덱스 관리
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = 0

# 이전/다음 버튼 함수
def change_quote(direction):
    st.session_state.current_quote = (st.session_state.current_quote + direction) % len(quotes)

# 랜덤 버튼 함수
def random_quote():
    st.session_state.current_quote = random.randint(0, len(quotes) - 1)

# 스타일
st.markdown("""
<style>
.quote-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 400px;
    background-color: #f0f0f0;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
}
.quote {
    text-align: center;
    max-width: 600px;
}
.quote-text {
    font-size: 24px;
    font-style: italic;
    margin-bottom: 20px;
}
.quote-author {
    font-size: 18px;
    font-weight: bold;
}
.button-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
}
</style>
""", unsafe_allow_html=True)

# 현재 인용구 표시
current_quote = quotes[st.session_state.current_quote]
st.markdown(f"""
<div class="quote-container">
    <div class="quote">
        <div class="quote-text">"{current_quote['text']}"</div>
        <div class="quote-author">- {current_quote['author']}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 버튼 표시
button_container = st.container()
with button_container:
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    with col2:
        if st.button("◀ 이전"):
            change_quote(-1)
    with col3:
        if st.button("랜덤"):
            random_quote()
    with col4:
        if st.button("다음 ▶"):
            change_quote(1)
