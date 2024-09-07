import streamlit as st
from streamlit_elements import elements, mui, html
from datetime import datetime

# 페이지 설정
st.set_page_config(layout="wide")

st.title("실시간 프로젝트 타임라인 관리")

# 세션 상태에서 프로젝트 마일스톤 관리
if "milestones" not in st.session_state:
    st.session_state["milestones"] = []

# 마일스톤 추가 폼
with st.form("milestone_form"):
    milestone_title = st.text_input("마일스톤 제목")
    milestone_description = st.text_area("마일스톤 설명")
    start_date = st.date_input("시작 날짜", min_value=datetime.now().date())
    end_date = st.date_input("종료 날짜", min_value=start_date)

    submitted = st.form_submit_button("마일스톤 추가")
    if submitted:
        if milestone_title and start_date and end_date:
            # 새로운 마일스톤 정보를 세션 상태에 저장
            milestone_info = {
                "title": milestone_title,
                "description": milestone_description,
                "start_date": start_date,
                "end_date": end_date
            }
            st.session_state["milestones"].append(milestone_info)
            st.success(f"마일스톤 '{milestone_title}'이 추가되었습니다.")
            st.rerun()

# 실시간 타임라인 표시
st.subheader("프로젝트 타임라인")

if st.session_state["milestones"]:
    # 가로로 10개의 타임라인이 표시되도록 설정
    with elements("timeline_dashboard"):
        mui.Grid(container=True, spacing=2, direction="row", wrap="wrap")(
            *[
                mui.Grid(item=True, xs=12, sm=6, md=4, lg=1)(  # 10개의 열로 설정하여 왼쪽부터 채워지도록 조정
                    mui.Paper(
                        elevation=2,
                        children=[
                            html.h3(f"{milestone['title']}"),
                            html.p(f"설명: {milestone['description']}"),
                            html.p(f"시작 날짜: {milestone['start_date']}"),
                            html.p(f"종료 날짜: {milestone['end_date']}")
                        ]
                    )
                ) for milestone in st.session_state["milestones"]
            ]
        )
else:
    st.info("아직 추가된 마일스톤이 없습니다.")

# 세션 초기화 (관리자용)
if st.button("타임라인 초기화"):
    st.session_state["milestones"] = []
    st.rerun()
