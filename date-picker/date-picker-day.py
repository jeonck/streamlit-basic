import streamlit as st
from datetime import datetime, timedelta
from streamlit_date_picker import date_range_picker, PickerType

st.title('날짜 범위 선택기')

# 기본 날짜 설정
default_start = datetime.now()
default_end = default_start + timedelta(days=7)

# 날짜 범위 선택
date_range_string = date_range_picker(
    picker_type=PickerType.date,
    start=default_start,
    end=default_end,
    key='date_range_picker',
    refresh_button={'is_show': True, 
                   'button_name': '최근 7일로 새로고침',
                   'refresh_value': timedelta(days=7)}
)

# 선택된 날짜 범위 표시
if date_range_string:
    start, end = date_range_string
    st.write(f"선택된 기간: {start} ~ {end}")
    
    # 날짜 문자열을 datetime 객체로 변환
    start_date = datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.strptime(end, '%Y-%m-%d')
    
    # 기간 계산
    days_diff = (end_date - start_date).days + 1
    st.write(f"총 {days_diff}일")