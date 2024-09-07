import streamlit as st
from streamlit_elements import elements, mui, html
from datetime import datetime

# 페이지 설정
st.set_page_config(layout="wide")

st.title("실시간 화상 회의 예약 시스템")

# 세션 상태에서 회의 일정 관리
if "meetings" not in st.session_state:
    st.session_state["meetings"] = []

# 회의 예약 입력 폼
with st.form("meeting_form"):
    meeting_title = st.text_input("회의 제목")
    meeting_description = st.text_area("회의 설명")
    meeting_date = st.date_input("회의 날짜", min_value=datetime.now().date())
    meeting_time = st.time_input("회의 시간")

    submitted = st.form_submit_button("회의 예약")
    if submitted:
        if meeting_title and meeting_date and meeting_time:
            # 회의 정보를 세션 상태에 저장
            meeting_info = {
                "title": meeting_title,
                "description": meeting_description,
                "datetime": datetime.combine(meeting_date, meeting_time)
            }
            st.session_state["meetings"].append(meeting_info)
            st.success(f"회의 '{meeting_title}'가 예약되었습니다.")
            st.rerun()

# 실시간 회의 일정 표시
st.subheader("예약된 회의 일정")

if st.session_state["meetings"]:
    with elements("meeting_schedule"):
        mui.Grid(container=True, spacing=2)(
            *[
                mui.Grid(item=True, xs=12)(
                    mui.Paper(
                        elevation=2,
                        children=[
                            html.h3(f"{meeting['title']}"),
                            html.p(f"설명: {meeting['description']}"),
                            html.p(f"날짜: {meeting['datetime'].strftime('%Y-%m-%d %H:%M')}")
                        ]
                    )
                ) for meeting in st.session_state["meetings"]
            ]
        )
else:
    st.info("예약된 회의가 없습니다.")

# 세션 초기화 (관리자용)
if st.button("회의 일정 초기화"):
    st.session_state["meetings"] = []
    st.rerun()
