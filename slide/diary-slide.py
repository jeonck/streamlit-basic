import streamlit as st
import random

# 감정과 관련된 데이터
emotions = {
    "행복": {"color": "#FFD700", "emoji": "😊", "messages": [
        "오늘 하루도 행복하게!",
        "당신의 미소가 세상을 밝게 만듭니다.",
        "행복은 당신 안에 있어요."
    ]},
    "슬픔": {"color": "#4682B4", "emoji": "😢", "messages": [
        "힘든 시간도 지나갈 거예요.",
        "당신은 혼자가 아닙니다.",
        "내일은 더 나은 날이 될 거예요."
    ]},
    "화남": {"color": "#FF6347", "emoji": "😠", "messages": [
        "깊게 숨을 들이쉬고 내쉬어보세요.",
        "화는 일시적이지만, 당신의 평화가 더 중요해요.",
        "화를 다스리는 당신이 멋집니다."
    ]},
    "불안": {"color": "#9370DB", "emoji": "😰", "messages": [
        "지금 이 순간에 집중해보세요.",
        "당신은 이전에도 어려움을 극복했어요.",
        "불안은 지나갈 거예요, 당신은 강합니다."
    ]},
    "기대": {"color": "#98FB98", "emoji": "😃", "messages": [
        "새로운 기회가 당신을 기다리고 있어요!",
        "당신의 꿈을 향해 한 걸음 더!",
        "기대하는 마음으로 세상은 더 아름다워집니다."
    ]}
}

# 세션 상태 초기화
if 'current_emotion' not in st.session_state:
    st.session_state.current_emotion = "행복"
if 'diary_entries' not in st.session_state:
    st.session_state.diary_entries = []

# 스타일
st.markdown(f"""
<style>
.emotion-container {{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 300px;
    background-color: {emotions[st.session_state.current_emotion]["color"]};
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    transition: background-color 0.5s ease;
}}
.emotion-emoji {{
    font-size: 72px;
    margin-bottom: 20px;
}}
.emotion-message {{
    font-size: 24px;
    text-align: center;
    color: white;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
}}
</style>
""", unsafe_allow_html=True)

# 감정 선택
st.session_state.current_emotion = st.selectbox("오늘의 감정은?", list(emotions.keys()))

# 감정 표시
current_emotion = emotions[st.session_state.current_emotion]
st.markdown(f"""
<div class="emotion-container">
    <div class="emotion-emoji">{current_emotion["emoji"]}</div>
    <div class="emotion-message">{random.choice(current_emotion["messages"])}</div>
</div>
""", unsafe_allow_html=True)

# 일기 입력
diary_entry = st.text_area("오늘의 일기를 작성해주세요:")
if st.button("저장"):
    if diary_entry:
        st.session_state.diary_entries.append({
            "emotion": st.session_state.current_emotion,
            "entry": diary_entry
        })
        st.success("일기가 저장되었습니다!")
    else:
        st.warning("일기 내용을 입력해주세요.")

# 이전 일기 표시
if st.session_state.diary_entries:
    st.subheader("이전 일기")
    for i, entry in enumerate(reversed(st.session_state.diary_entries), 1):
        st.markdown(f"""
        <div style="background-color: {emotions[entry['emotion']]['color']}; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <p style="color: white;"><strong>{i}번째 일기</strong> - 감정: {entry['emotion']} {emotions[entry['emotion']]['emoji']}</p>
            <p style="color: white;">{entry['entry']}</p>
        </div>
        """, unsafe_allow_html=True)
