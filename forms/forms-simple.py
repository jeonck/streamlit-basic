import streamlit as st
import datetime

# 고객 피드백 폼
st.title("고객 피드백 폼")

name = st.text_input("이름")
email = st.text_input("이메일")
rating = st.slider("서비스 만족도", 1, 5, 3)
feedback = st.text_area("피드백 내용")
submit_feedback = st.button("피드백 제출")

if submit_feedback:
    st.success("피드백이 제출되었습니다. 감사합니다!")

st.divider()

# 간단한 설문조사
st.title("간단한 설문조사")

age = st.number_input("나이", min_value=0, max_value=120)
gender = st.radio("성별", ["남성", "여성", "기타"])
interests = st.multiselect("관심사", ["기술", "예술", "스포츠", "요리", "여행"])
submit_survey = st.button("설문 제출")

if submit_survey:
    st.write("설문에 참여해 주셔서 감사합니다!")

st.divider()

# 예약 시스템
st.title("예약 시스템")

date = st.date_input("예약 날짜")
time = st.time_input("예약 시간")
service = st.selectbox("서비스 선택", ["헤어컷", "염색", "파마"])
reservation_name = st.text_input("예약자 이름")
phone = st.text_input("전화번호")
submit_reservation = st.button("예약하기")

if submit_reservation:
    st.success(f"{date} {time}에 {service} 예약이 완료되었습니다.")

st.divider()

# 간단한 계산기
st.title("간단한 계산기")

num1 = st.number_input("첫 번째 숫자")
num2 = st.number_input("두 번째 숫자")
operation = st.selectbox("연산 선택", ["+", "-", "*", "/"])

if st.button("계산"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    else:
        result = num1 / num2 if num2 != 0 else "0으로 나눌 수 없습니다"
    
    st.write(f"결과: {result}")
