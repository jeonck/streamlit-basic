import streamlit as st
from streamlit_elements import elements, mui, html
from datetime import datetime

# 페이지 설정
st.set_page_config(layout="wide")

st.title("실시간 작업 할당 및 관리 대시보드")

# 세션 상태에서 작업 관리
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

# 작업 할당 폼
with st.form("task_form"):
    task_title = st.text_input("작업 제목")
    task_assignee = st.text_input("담당자 이름")
    due_date = st.date_input("마감일", min_value=datetime.now().date())
    task_status = st.selectbox("작업 상태", ["할당됨", "진행 중", "완료"])

    submitted = st.form_submit_button("작업 추가")
    
    if submitted and task_title and task_assignee:
        # 새로운 작업 추가
        task_info = {
            "title": task_title,
            "assignee": task_assignee,
            "due_date": due_date,
            "status": task_status
        }
        st.session_state["tasks"].append(task_info)
        st.success(f"작업 '{task_title}'이(가) {task_assignee}에게 할당되었습니다.")
        st.rerun()

# 작업 삭제 함수
def delete_task(index):
    st.session_state["tasks"].pop(index)
    st.rerun()

# 작업 상태 변경 함수
def update_task_status(index, new_status):
    st.session_state["tasks"][index]["status"] = new_status
    st.rerun()

# 작업 목록 표시
st.subheader("작업 목록")

if st.session_state["tasks"]:
    with elements("task_board"):
        mui.Grid(container=True, spacing=2)(
            *[
                mui.Grid(item=True, xs=12)(
                    mui.Paper(
                        elevation=2,
                        children=[
                            html.h3(f"작업 #{i + 1}: {task['title']}"),
                            html.p(f"담당자: {task['assignee']}"),
                            html.p(f"마감일: {task['due_date']}"),
                            html.p(f"상태: {task['status']}"),
                            # 작업 상태 변경 버튼
                            mui.Button("진행 중으로 변경", onClick=lambda i=i: update_task_status(i, "진행 중")),
                            mui.Button("완료로 변경", onClick=lambda i=i: update_task_status(i, "완료")),
                            # 작업 삭제 버튼
                            mui.Button("삭제", onClick=lambda i=i: delete_task(i), style={"color": "red"})
                        ]
                    )
                ) for i, task in enumerate(st.session_state["tasks"])
            ]
        )
else:
    st.info("현재 할당된 작업이 없습니다.")

# 세션 초기화 (관리자용)
if st.button("모든 작업 삭제"):
    st.session_state["tasks"] = []
    st.rerun()
