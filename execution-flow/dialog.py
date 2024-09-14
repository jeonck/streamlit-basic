import streamlit as st

@st.dialog("영화 투표하기")
def vote(movie):
    st.write(f"왜 '{movie}'가 당신의 최고의 영화인가요?")
    reason = st.text_input("이유:")
    genre = st.selectbox("이 영화의 장르는?", ["액션", "코미디", "드라마", "SF", "로맨스"])
    rating = st.slider("이 영화에 몇 점을 주시겠습니까?", 1, 10, 5)
    
    if st.button("제출"):
        st.session_state.vote = {"movie": movie, "reason": reason, "genre": genre, "rating": rating}
        st.rerun()

if "vote" not in st.session_state:
    st.title("2023년 최고의 영화를 선택해주세요!")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("오펜하이머"):
            vote("오펜하이머")
    with col2:
        if st.button("바비"):
            vote("바비")
else:
    st.title("투표 결과")
    vote_data = st.session_state.vote
    st.write(f"당신이 선택한 영화: **{vote_data['movie']}**")
    st.write(f"선택 이유: {vote_data['reason']}")
    st.write(f"장르: {vote_data['genre']}")
    st.write(f"평점: {vote_data['rating']}/10")
    
    if st.button("다시 투표하기"):
        del st.session_state.vote
        st.rerun()
