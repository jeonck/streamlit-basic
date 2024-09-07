import streamlit as st
from streamlit_elements import elements, mui, html

# 페이지 설정
st.set_page_config(layout="wide")

st.title("실시간 투표 시스템")

# 세션 상태에서 투표 데이터를 관리
if "votes" not in st.session_state:
    st.session_state["votes"] = {
        "항목 A": 0,
        "항목 B": 0,
        "항목 C": 0,
        "항목 D": 0
    }

# 투표 선택지
options = list(st.session_state["votes"].keys())

# 투표 선택 폼
with st.form("vote_form"):
    st.write("어떤 항목에 투표하시겠습니까?")
    
    vote_choice = st.radio("항목 선택", options)
    
    # 투표 제출 버튼
    submitted = st.form_submit_button("투표 제출")
    if submitted:
        # 선택된 항목에 투표 추가
        st.session_state["votes"][vote_choice] += 1
        st.success(f"{vote_choice}에 투표가 반영되었습니다!")
        st.rerun()

# 총 투표 수 계산
total_votes = sum(st.session_state["votes"].values())

# 실시간 투표 결과 대시보드
st.subheader("실시간 투표 결과")

if total_votes > 0:
    with elements("vote_dashboard"):
        mui.Grid(container=True, spacing=2)(
            *[
                mui.Grid(item=True, xs=12)(
                    mui.Paper(
                        elevation=2,
                        children=[
                            html.h3(f"{option}"),
                            html.p(f"투표 수: {st.session_state['votes'][option]}"),
                            html.p(f"퍼센트: {st.session_state['votes'][option] / total_votes * 100:.2f}%"),
                            html.progress(value=st.session_state["votes"][option] / total_votes, max=1)
                        ]
                    )
                ) for option in options
            ]
        )
else:
    st.info("아직 투표된 항목이 없습니다.")
