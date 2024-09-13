import streamlit as st
import random
import time

st.title('🧠 창의적 퀴즈 게임')

# 퀴즈 데이터
quizzes = [
    {"question": "대한민국의 수도는?", "answer": "서울", "difficulty": "쉬움"},
    {"question": "1 + 1 = ?", "answer": "2", "difficulty": "쉬움"},
    {"question": "지구에서 가장 큰 대양은?", "answer": "태평양", "difficulty": "보통"},
    {"question": "물의 화학식은?", "answer": "H2O", "difficulty": "보통"},
    {"question": "빛의 속도는? (숫자만 입력, 단위: km/s)", "answer": "299792", "difficulty": "어려움"},
]

# 게임 상태 초기화
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = random.choice(quizzes)

# 점수 표시
st.metric("현재 점수", st.session_state.score)

# 퀴즈 표시
st.markdown(f"### {st.session_state.current_question['question']}")
st.caption(f"난이도: {st.session_state.current_question['difficulty']}")

# 사용자 입력
user_answer = st.text_input("답변을 입력하세요:")

if st.button("제출"):
    with st.spinner("답변 확인 중..."):
        time.sleep(1)  # 잠시 대기 효과
    
    if user_answer.lower() == st.session_state.current_question['answer'].lower():
        st.success("정답입니다! 🎉")
        st.balloons()
        st.session_state.score += 1
        if st.session_state.score % 5 == 0:
            st.snow()
            st.success(f"축하합니다! {st.session_state.score}점 달성!")
    else:
        st.error("틀렸습니다. 😢")
        st.info(f"정답은 '{st.session_state.current_question['answer']}' 입니다.")
    
    # 다음 문제 준비
    st.session_state.current_question = random.choice(quizzes)
    st.rerun()  # 여기를 수정했습니다

# 힌트 제공
if st.button("힌트 보기"):
    hint = st.session_state.current_question['answer'][:2] + "..."
    st.warning(f"힌트: {hint}")

# 게임 규칙
with st.expander("게임 규칙 보기"):
    st.markdown("""
    1. 질문에 대한 답변을 입력하세요.
    2. 정답을 맞추면 1점을 얻습니다.
    3. 5점마다 특별한 축하 효과가 나타납니다.
    4. 힌트를 볼 수 있지만, 가능하면 스스로 해결해보세요!
    """)

# 게임 재시작
if st.button("게임 재시작"):
    st.session_state.score = 0
    st.session_state.current_question = random.choice(quizzes)
    st.success("게임이 재시작되었습니다. 행운을 빕니다!")
    st.rerun()  # 여기도 수정했습니다

# 진행 상황 표시
st.write("---")
st.subheader("게임 진행 상황")
progress = st.session_state.score / 10  # 10점을 만점으로 가정
st.progress(progress)

if progress == 1:
    st.success("축하합니다! 만점을 달성했습니다! 🏆")
elif progress >= 0.8:
    st.info("거의 다 왔어요! 조금만 더 힘내세요.")
elif progress >= 0.5:
    st.info("절반 이상 달성했습니다. 잘 하고 있어요!")
elif progress > 0:
    st.info("계속 도전하세요!")

# 코드 예시
with st.expander("파이썬 코드 예시 보기"):
    st.code("""
    def check_answer(question, user_answer):
        if user_answer.lower() == question['answer'].lower():
            return True
        return False
    
    # 사용 예:
    result = check_answer(current_question, user_input)
    if result:
        print("정답입니다!")
    else:
        print("틀렸습니다.")
    """, language="python")
