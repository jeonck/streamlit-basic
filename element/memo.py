import streamlit as st
from streamlit_elements import elements, mui, html

# 페이지 설정
st.set_page_config(layout="wide")

st.title("실시간 메모 공유 대시보드")

# 세션 상태에서 메모 관리
if "notes" not in st.session_state:
    st.session_state["notes"] = []

# 새로운 메모 추가 폼
with st.form("note_form"):
    note_text = st.text_area("메모를 입력하세요", "")
    submitted = st.form_submit_button("메모 추가")
    
    if submitted and note_text:
        # 새로운 메모 추가
        st.session_state["notes"].append({"text": note_text})
        st.success("메모가 추가되었습니다!")
        st.rerun()

# 메모 삭제 함수
def delete_note(index):
    st.session_state["notes"].pop(index)
    st.rerun()

# 메모 목록 표시
st.subheader("메모 목록")

if st.session_state["notes"]:
    with elements("note_board"):
        mui.Grid(container=True, spacing=2)(
            *[
                mui.Grid(item=True, xs=12)(
                    mui.Paper(
                        elevation=2,
                        children=[
                            html.h3(f"메모 #{i + 1}"),
                            html.p(f"{note['text']}")
                        ]
                    )
                ) for i, note in enumerate(st.session_state["notes"])
            ]
        )
    
    # 별도의 삭제 섹션
    st.subheader("메모 삭제")
    delete_index = st.number_input("삭제할 메모 번호", min_value=1, max_value=len(st.session_state["notes"]), value=1, step=1)
    if st.button("선택한 메모 삭제"):
        delete_note(delete_index - 1)  # 인덱스는 0부터 시작하므로 1을 빼줍니다.
        st.success(f"메모 #{delete_index}가 삭제되었습니다.")
else:
    st.info("현재 작성된 메모가 없습니다.")

# 세션 초기화 (관리자용)
if st.button("모든 메모 삭제"):
    st.session_state["notes"] = []
    st.rerun()