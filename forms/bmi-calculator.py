import streamlit as st

# st.set_page_config(layout="wide")
st.markdown("""
<style>
    .stApp {
        background-color: #F0F0F0;
        color: #333333;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        width: 100%;
    }
    .stTextInput>div>div>input, .stDateInput>div>div>input, .stNumberInput>div>div>input {
        background-color: white;
        color: #333333;
        border: 1px solid #CCCCCC;
        border-radius: 4px;
    }
    .row-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
    h3 {
        color: #2C3E50;
</style>
""", unsafe_allow_html=True)

def calculate_bmi(weight, height):
    return weight / (height/100)**2

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<h3>사용자 정보</h3>', unsafe_allow_html=True)
    
    with st.form(key='user_info_form'):
        first_name = st.text_input("이름")
        last_name = st.text_input("성")
        dob = st.date_input("생년월일")
        email = st.text_input("이메일")
        submit_button = st.form_submit_button(label='가입하기')
    
    if submit_button:
        st.success("가입이 완료되었습니다!")
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<h3>BMI 계산</h3>', unsafe_allow_html=True)

    with st.form(key='bmi_form'):
        col_height, col_weight = st.columns(2)
        with col_height:
            st.markdown('키 (cm)', unsafe_allow_html=True)
            height = st.number_input("", min_value=1.0, max_value=300.0, value=170.0, key="height", label_visibility="collapsed")

        with col_weight:
            st.markdown('체중 (kg)', unsafe_allow_html=True)
            weight = st.number_input("", min_value=1.0, max_value=300.0, value=60.0, key="weight", label_visibility="collapsed")

        calculate_button = st.form_submit_button(label='계산하기')

    if calculate_button:
        bmi = weight / (height/100)**2
        st.markdown(f'<div>BMI: {bmi:.2f}</div>', unsafe_allow_html=True)
        
        if bmi < 18.5:
            st.markdown('<div>저체중</div>', unsafe_allow_html=True)
        elif 18.5 <= bmi < 25:
            st.markdown('<div>정상</div>', unsafe_allow_html=True)
        elif 25 <= bmi < 30:
            st.markdown('<div>과체중</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div>비만</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
