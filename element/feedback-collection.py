import streamlit as st
from streamlit_elements import elements, mui, html

# 페이지 설정
st.set_page_config(layout="wide")

st.title("실시간 피드백 수집 대시보드")

# 세션 상태에서 피드백 목록을 관리
if "feedbacks" not in st.session_state:
    st.session_state["feedbacks"] = []

# 피드백 입력 폼
with st.form("feedback_form"):
    st.write("피드백을 입력해주세요!")
    
    feedback_text = st.text_area("피드백", "")
    feedback_rating = st.slider("평점 (1-5)", 1, 5, 3)
    feedback_category = st.selectbox("피드백 카테고리", ["기능", "UI/UX", "성능", "기타"])
    
    # 폼 제출 버튼
    submitted = st.form_submit_button("제출")
    if submitted:
        # 피드백을 세션 상태에 저장
        st.session_state["feedbacks"].append({
            "text": feedback_text,
            "rating": feedback_rating,
            "category": feedback_category
        })
        st.success("피드백이 제출되었습니다!")
        st.rerun()

# 제출된 피드백 목록
st.subheader("제출된 피드백")

if st.session_state["feedbacks"]:
    with elements("feedback_dashboard"):
        mui.Grid(container=True, spacing=2)(
            *[
                mui.Grid(item=True, xs=12)(
                    mui.Paper(
                        elevation=2,
                        children=[
                            html.h3(f"피드백 #{i + 1}"),
                            html.p(f"내용: {feedback['text']}"),
                            html.p(f"평점: {feedback['rating']}"),
                            html.p(f"카테고리: {feedback['category']}")
                        ]
                    )
                ) for i, feedback in enumerate(st.session_state["feedbacks"])
            ]
        )
else:
    st.info("아직 제출된 피드백이 없습니다.")
