import streamlit as st
import datetime
import pandas as pd
import altair as alt
import random  # random 모듈 추가

st.title('🌈 일일 기분 추적기')

# 세션 상태 초기화
if 'mood_history' not in st.session_state:
    st.session_state.mood_history = []

# 현재 날짜
today = datetime.date.today()

st.write(f"오늘 날짜: {today}")

# 기분 선택
mood = st.radio(
    "오늘의 기분을 선택하세요:",
    ["😄 행복해요", "😊 좋아요", "😐 그저 그래요", "😔 슬퍼요", "😠 화나요"],
    index=2,
    format_func=lambda x: x.split()[1]  # 이모지만 표시
)

# 선택한 기분에 대한 피드백
if mood == "😄 행복해요":
    st.success("멋져요! 오늘 하루도 행복하게 보내세요.")
elif mood == "😊 좋아요":
    st.info("좋은 하루 되세요!")
elif mood == "😐 그저 그래요":
    st.warning("기분 전환을 위해 산책을 해보는 건 어떨까요?")
elif mood == "😔 슬퍼요":
    st.error("힘내세요. 어려운 시간은 곧 지나갈 거예요.")
else:
    st.error("심호흡을 하고 긍정적인 것에 집중해보세요.")

# 기분 저장
if st.button('오늘의 기분 저장하기'):
    st.session_state.mood_history.append({'date': today, 'mood': mood})
    st.success("오늘의 기분이 저장되었습니다!")

# 기분 히스토리 표시
if st.session_state.mood_history:
    st.write("### 기분 히스토리")
    df = pd.DataFrame(st.session_state.mood_history)
    df['mood_score'] = df['mood'].map({
        "😄 행복해요": 5, 
        "😊 좋아요": 4, 
        "😐 그저 그래요": 3, 
        "😔 슬퍼요": 2, 
        "😠 화나요": 1
    })
    
    # 차트 생성
    chart = alt.Chart(df).mark_line().encode(
        x='date:T',
        y='mood_score:Q',
        tooltip=['date', 'mood']
    ).properties(
        width=600,
        height=300,
        title='기분 변화 추이'
    )
    
    st.altair_chart(chart)

# 기분 통계
if st.session_state.mood_history:
    st.write("### 기분 통계")
    mood_counts = df['mood'].value_counts()
    st.write(mood_counts)

# 기분 개선 팁
st.write("### 오늘의 기분 개선 팁")
tips = [
    "10분 동안 명상을 해보세요.",
    "좋아하는 음악을 들어보세요.",
    "가까운 사람에게 연락해보세요.",
    "간단한 운동을 해보세요.",
    "감사한 일 3가지를 적어보세요."
]
st.info(random.choice(tips))  # st.secrets.choice 대신 random.choice 사용
