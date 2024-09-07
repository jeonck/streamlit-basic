import streamlit as st
from streamlit_elements import elements, mui, html

# 페이지 설정
st.set_page_config(layout="wide")

st.title("실시간 채팅 시스템")

# 세션 상태에서 채팅 메시지 목록을 관리
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 사용자 이름 설정
if "username" not in st.session_state:
    st.session_state["username"] = st.text_input("이름을 입력하세요", value="사용자")

# 채팅 메시지 입력 폼
with st.form("chat_form"):
    user_message = st.text_input("메시지를 입력하세요", "")
    submitted = st.form_submit_button("보내기")
    
    if submitted and user_message:
        # 새로운 메시지를 세션 상태에 추가
        st.session_state["messages"].append({
            "username": st.session_state["username"],
            "message": user_message
        })
        st.rerun()

# 채팅 메시지 목록 표시
st.subheader("채팅창")

if st.session_state["messages"]:
    with elements("chat_display"):
        mui.Grid(container=True, spacing=2)(
            *[
                mui.Grid(item=True, xs=12)(
                    mui.Paper(
                        elevation=2,
                        children=[
                            html.h4(f"{msg['username']}"),
                            html.p(f"{msg['message']}")
                        ]
                    )
                ) for msg in st.session_state["messages"]
            ]
        )
else:
    st.info("아직 메시지가 없습니다.")

# 세션 초기화 (관리자용)
if st.button("채팅 초기화"):
    st.session_state["messages"] = []
    st.rerun()
