import streamlit as st

# 카드 데이터
cards = [
    {
        "title": "파이썬 기초",
        "content": "파이썬은 간결하고 읽기 쉬운 문법을 가진 프로그래밍 언어입니다. 초보자부터 전문가까지 널리 사용됩니다.",
        "tags": ["프로그래밍", "입문", "파이썬"]
    },
    {
        "title": "데이터 분석",
        "content": "데이터 분석은 raw 데이터로부터 의미 있는 정보를 추출하는 과정입니다. 파이썬의 pandas, numpy 라이브러리가 주로 사용됩니다.",
        "tags": ["데이터", "분석", "pandas"]
    },
    {
        "title": "머신러닝",
        "content": "머신러닝은 컴퓨터가 데이터로부터 학습하여 예측이나 결정을 내리는 기술입니다. scikit-learn, TensorFlow 등의 라이브러리가 유명합니다.",
        "tags": ["AI", "머신러닝", "딥러닝"]
    }
]

# 세션 상태로 현재 카드 인덱스 관리
if 'current_card' not in st.session_state:
    st.session_state.current_card = 0

# 이전/다음 버튼 함수
def change_card(direction):
    st.session_state.current_card = (st.session_state.current_card + direction) % len(cards)

# 카드 스타일
st.markdown("""
<style>
.card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
}
.card-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}
.card-content {
    font-size: 16px;
    margin-bottom: 15px;
}
.card-tags {
    display: flex;
    flex-wrap: wrap;
}
.tag {
    background-color: #f1f1f1;
    border-radius: 4px;
    padding: 5px 10px;
    margin-right: 5px;
    margin-bottom: 5px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# 현재 카드 표시
current_card = cards[st.session_state.current_card]
st.markdown(f"""
<div class="card">
    <div class="card-title">{current_card['title']}</div>
    <div class="card-content">{current_card['content']}</div>
    <div class="card-tags">
        {"".join([f'<span class="tag">{tag}</span>' for tag in current_card['tags']])}
    </div>
</div>
""", unsafe_allow_html=True)

# 버튼 표시 (하단에 배치, 중앙 정렬)
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col2:
    st.button("◀ 이전", on_click=change_card, args=(-1,), key="prev")
with col3:
    st.write(f"{st.session_state.current_card + 1}/{len(cards)}")
with col4:
    st.button("다음 ▶", on_click=change_card, args=(1,), key="next")
