import streamlit as st

st.title('MBTI 성격 유형 테스트')

questions = [
    # E vs I 질문
    "1. 새로운 사람들을 만나는 것을 즐깁니다.",
    "2. 대화를 먼저 시작하는 편입니다.",
    "3. 많은 친구들과 넓은 인맥을 가지고 있습니다.",
    "4. 파티나 사교 모임에 자주 참석합니다.",
    "5. 그룹 활동에 참여하는 것을 좋아합니다.",
    "6. 혼자 있는 것보다 다른 사람들과 함께 있는 것을 선호합니다.",
    "7. 새로운 환경에 쉽게 적응합니다.",
    
    # S vs N 질문
    "8. 세부사항에 주의를 기울이는 편입니다.",
    "9. 현실적이고 실용적인 해결책을 선호합니다.",
    "10. 미래보다는 현재에 집중합니다.",
    "11. 추상적인 개념보다 구체적인 사실을 선호합니다.",
    "12. 상상력을 발휘하는 것보다 실제 경험을 중요시합니다.",
    "13. 전체적인 그림보다 세부사항에 집중합니다.",
    "14. 새로운 아이디어보다 검증된 방법을 선호합니다.",
    
    # T vs F 질문
    "15. 결정을 내릴 때 감정보다 논리를 중요시합니다.",
    "16. 객관적인 사실에 근거하여 판단합니다.",
    "17. 다른 사람의 감정보다 진실을 말하는 것이 더 중요합니다.",
    "18. 감정적인 상황에서도 냉철함을 유지할 수 있습니다.",
    "19. 논리적 일관성을 중요하게 여깁니다.",
    "20. 다른 사람의 감정을 고려하기보다 효율성을 우선시합니다.",
    "21. 비판을 받아들이는 것이 어렵지 않습니다.",
    
    # J vs P 질문
    "22. 일정과 계획을 세우는 것을 좋아합니다.",
    "23. 마감 기한을 정확히 지키는 편입니다.",
    "24. 체계적으로 일을 처리하는 것을 선호합니다.",
    "25. 결정을 빨리 내리는 편입니다.",
    "26. 즉흥적인 행동보다 계획된 행동을 선호합니다.",
    "27. 일을 시작하기 전에 모든 옵션을 고려합니다.",
    "28. 정리정돈을 중요하게 여깁니다.",
    "29. 목표를 세우고 그에 따라 행동합니다.",
    "30. 융통성 있게 대처하는 것보다 규칙을 따르는 것을 선호합니다."
]

# 세션 상태 초기화
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

# 진행 상황 표시
st.progress(st.session_state.current_question / len(questions))

# 현재 질문 표시
if st.session_state.current_question < len(questions):
    question = questions[st.session_state.current_question]
    st.markdown(f"<h3 style='text-align: left; color: #32CD32;'>{question}</h3>", unsafe_allow_html=True)
    
    options = ["매우 그렇지 않다", "그렇지 않다", "보통이다", "그렇다", "매우 그렇다"]
    answer = st.radio("응답을 선택하세요", options, index=2, label_visibility="collapsed")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button('다음'):
            st.session_state.answers.append(options.index(answer) + 1)
            st.session_state.current_question += 1
            st.rerun()
    with col2:
        st.write(f"질문 {st.session_state.current_question + 1}/{len(questions)}")

# 모든 질문에 답변했을 때 결과 표시
if st.session_state.current_question == len(questions):
    st.markdown("<h3 style='text-align: center; color: #32CD32;'>모든 질문에 답변하셨습니다. 결과를 확인해보세요!</h3>", unsafe_allow_html=True)
    
    if st.button('결과 보기'):
        answers = st.session_state.answers
        e_i = sum(answers[:7])
        s_n = sum(answers[7:14])
        t_f = sum(answers[14:21])
        j_p = sum(answers[21:])
        
        mbti = ""
        mbti += "E" if e_i > 21 else "I"
        mbti += "S" if s_n > 21 else "N"
        mbti += "T" if t_f > 21 else "F"
        mbti += "J" if j_p > 21 else "P"
        
        st.markdown(f"<h3 style='text-align: center; color: #FF4500;'>당신의 MBTI 유형은 {mbti}입니다.</h3>", unsafe_allow_html=True)
        
        st.markdown("<h4 style='color: #4B0082;'>각 지표별 점수:</h4>", unsafe_allow_html=True)
        
        # 프로그레스 바를 사용하여 각 지표의 점수를 시각화
        st.markdown("<h5>E/I:</h5>", unsafe_allow_html=True)
        st.progress(e_i / 35)
        st.write(f"E 성향: {e_i/35*100:.1f}%")
        
        st.markdown("<h5>S/N:</h5>", unsafe_allow_html=True)
        st.progress(s_n / 35)
        st.write(f"S 성향: {s_n/35*100:.1f}%")
        
        st.markdown("<h5>T/F:</h5>", unsafe_allow_html=True)
        st.progress(t_f / 35)
        st.write(f"T 성향: {t_f/35*100:.1f}%")
        
        st.markdown("<h5>J/P:</h5>", unsafe_allow_html=True)
        st.progress(j_p / 35)
        st.write(f"J 성향: {j_p/35*100:.1f}%")
