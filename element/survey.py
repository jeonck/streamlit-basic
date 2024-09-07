import streamlit as st
from streamlit_elements import elements, mui, html

# 페이지 설정
st.set_page_config(layout="wide")

st.title("실시간 설문 조사 시스템")

# 세션 상태에서 설문 데이터를 관리
if "survey_results" not in st.session_state:
    st.session_state["survey_results"] = {
        "항목 A": 0,
        "항목 B": 0,
        "항목 C": 0,
        "항목 D": 0
    }

# 설문 항목 리스트
survey_items = list(st.session_state["survey_results"].keys())

# 설문 응답 폼
with st.form("survey_form"):
    user_choice = st.radio("어느 항목에 투표하시겠습니까?", survey_items)
    submitted = st.form_submit_button("투표 제출")
    
    if submitted and user_choice:
        # 선택된 항목에 투표 수를 추가
        st.session_state["survey_results"][user_choice] += 1
        st.success(f"'{user_choice}'에 투표하셨습니다!")
        st.rerun()

# 설문 결과 표시
st.subheader("실시간 설문 결과")

# 총 투표 수 계산
total_votes = sum(st.session_state["survey_results"].values())

if total_votes > 0:
    with elements("survey_results"):
        mui.Grid(container=True, spacing=2)(
            *[
                mui.Grid(item=True, xs=12, sm=6, md=4, lg=3)(
                    mui.Paper(
                        elevation=2,
                        children=[
                            html.h3(f"{item}"),
                            html.p(f"투표 수: {st.session_state['survey_results'][item]}"),
                            html.p(f"퍼센트: {st.session_state['survey_results'][item] / total_votes * 100:.2f}%"),
                            html.progress(value=st.session_state["survey_results"][item] / total_votes, max=1)
                        ]
                    )
                ) for item in survey_items
            ]
        )
else:
    st.info("아직 투표된 항목이 없습니다.")

# 세션 초기화 (관리자용)
if st.button("설문 초기화"):
    st.session_state["survey_results"] = {item: 0 for item in survey_items}
    st.rerun()
