import streamlit as st

st.title("섹션 폼 예제")
# 사용자 정보 폼을 위한 바깥 테두리 박스
with st.form(key='user-info'):
    # 사용자 정보 입력 폼
    user_name = st.text_input('이름')
    user_height = st.number_input('키', step=0.1)
    user_weight = st.number_input('몸무게', step=0.1)
    submit_button = st.form_submit_button(label='제출')

# 제출 버튼이 눌리면 실행되는 코드
if submit_button:
    # 사용자 정보 폼 제출 처리
    st.write(f'이름: {user_name}, 키: {user_height}, 몸무게: {user_weight}')

    # BMI 계산
    bmi = user_weight / (user_height ** 2)
    st.write(f'BMI: {bmi:.2f}')

    # BMI 등급 판정
    if bmi < 18.5:
        st.write('저체중')
    elif 18.5 <= bmi < 25:
        st.write('정상')
    elif 25 <= bmi < 30:
        st.write('과체중')
    else:
        st.write('비만')