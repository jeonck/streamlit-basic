import streamlit as st
import time

@st.fragment
def exercise_timer(exercise, duration):
    st.write(f"{exercise} 운동 중...")
    progress_bar = st.progress(0)
    for i in range(duration):
        time.sleep(1)
        progress_bar.progress((i + 1) / duration)
    st.success(f"{exercise} 완료!")

st.title("간단한 운동 앱")

exercise_options = ["팔굽혀펴기", "스쿼트", "플랭크"]
selected_exercise = st.selectbox("운동을 선택하세요", exercise_options)

duration = st.slider("운동 시간 (초)", 5, 60, 30)

if st.button("운동 시작", help="Fragment rerun"):
    exercise_timer(selected_exercise, duration)

st.button("새로운 운동 선택", help="Full rerun")
