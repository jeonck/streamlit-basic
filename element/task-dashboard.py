import streamlit as st
from streamlit_elements import elements, mui, html

# 페이지 설정
st.set_page_config(layout="wide")

st.title("실시간 작업 추적 대시보드")

# 세션 상태에서 작업 목록을 관리
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

# 새로운 작업 추가
new_task = st.text_input("새 작업 추가", "")
if st.button("추가"):
    if new_task:
        st.session_state["tasks"].append({"task": new_task, "completed": False})
        st.rerun()  # 작업 추가 후 페이지 새로고침

# 작업 목록 삭제
if st.button("모두 삭제"):
    st.session_state["tasks"] = []
    st.rerun()  # 작업 목록 삭제 후 페이지 새로고침

# 작업 완료 상태 업데이트 함수
def toggle_task_status(index):
    st.session_state["tasks"][index]["completed"] = not st.session_state["tasks"][index]["completed"]
    st.rerun()  # 상태 변경 후 페이지 새로고침

# 작업 목록 UI
with elements("task_tracker"):
    # 작업 목록을 행(row) 단위로 추가
    mui.Grid(container=True, spacing=2)(
        # 작업 목록의 각 항목을 row 단위로 처리
        *[
            mui.Grid(item=True, xs=12)(
                mui.Paper(
                    elevation=2,
                    children=[
                        mui.Box(
                            display="flex",
                            alignItems="center",
                            children=[
                                mui.Checkbox(
                                    checked=task["completed"],
                                    onChange=lambda _, index=i: toggle_task_status(index)
                                ),
                                mui.Typography(
                                    task["task"],
                                    style={
                                        "textDecoration": "line-through" if task["completed"] else "none",
                                        "marginLeft": "8px"
                                    }
                                )
                            ]
                        )
                    ]
                )
            ) for i, task in enumerate(st.session_state["tasks"])
        ]
    )