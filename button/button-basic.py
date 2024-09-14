import streamlit as st

# 일반 버튼
if st.button('일반 버튼'):
    st.write('일반 버튼이 클릭되었습니다!')

# 체크박스
if st.checkbox('체크박스'):
    st.write('체크박스가 선택되었습니다!')

# 라디오 버튼
option = st.radio('라디오 버튼', ['옵션1', '옵션2', '옵션3'])
st.write(f'선택된 옵션: {option}')

# 선택 박스
choice = st.selectbox('선택 박스', ['선택1', '선택2', '선택3'])
st.write(f'선택된 항목: {choice}')

# 다중 선택
options = st.multiselect('다중 선택', ['항목1', '항목2', '항목3', '항목4'])
st.write(f'선택된 항목들: {options}')

# 슬라이더
value = st.slider('슬라이더', min_value=0, max_value=100, value=50)
st.write(f'슬라이더 값: {value}')

# 파일 업로더
uploaded_file = st.file_uploader("파일 선택", type=['csv', 'txt'])
if uploaded_file is not None:
    st.write(f'업로드된 파일: {uploaded_file.name}')

# 날짜 입력
date = st.date_input('날짜 선택')
st.write(f'선택된 날짜: {date}')

# 색상 선택기
color = st.color_picker('색상 선택')
st.write(f'선택된 색상: {color}')
