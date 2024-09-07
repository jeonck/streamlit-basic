import streamlit as st
from streamlit_elements import elements, mui, html, editor

# 페이지 설정
st.set_page_config(layout="wide")

st.title("실시간 코드 리뷰 시스템")

# 세션 상태에서 코드 및 리뷰 관리
if "code_submissions" not in st.session_state:
    st.session_state["code_submissions"] = []

if "code_reviews" not in st.session_state:
    st.session_state["code_reviews"] = []

# 코드 제출 폼
with st.form("code_form"):
    submitted_code = st.text_area("코드를 입력하세요", height=200)
    submitted = st.form_submit_button("코드 제출")
    
    if submitted and submitted_code:
        # 새로운 코드 제출 저장
        st.session_state["code_submissions"].append(submitted_code)
        st.session_state["code_reviews"].append([])  # 코멘트를 위한 빈 리스트 추가
        st.success("코드가 제출되었습니다!")
        st.rerun()

# 코드 리뷰 섹션
st.subheader("제출된 코드 목록")

if st.session_state["code_submissions"]:
    for idx, code in enumerate(st.session_state["code_submissions"]):
        with elements(f"code_{idx}"):
            mui.Grid(container=True, spacing=2)(
                mui.Grid(item=True, xs=12)(
                    mui.Paper(
                        elevation=2,
                        children=[
                            html.h3(f"제출된 코드 #{idx + 1}"),
                            # Monaco Editor를 사용해 코드 블록을 표시
                            editor.Monaco(
                                language="python",
                                value=code,
                                height=200,
                                readOnly=True
                            )
                        ]
                    )
                )
            )
        
        # 리뷰 추가 폼
        with st.form(f"review_form_{idx}"):
            review_comment = st.text_area("리뷰 코멘트를 추가하세요", height=100, key=f"review_{idx}")
            review_submitted = st.form_submit_button(f"리뷰 제출 #{idx + 1}")
            
            if review_submitted and review_comment:
                st.session_state["code_reviews"][idx].append(review_comment)
                st.success(f"리뷰가 코드 #{idx + 1}에 추가되었습니다.")
                st.rerun()

        # 기존 리뷰 표시
        st.write(f"코드 #{idx + 1}에 대한 리뷰:")
        if st.session_state["code_reviews"][idx]:
            for review in st.session_state["code_reviews"][idx]:
                st.write(f"- {review}")
        else:
            st.info(f"아직 코드 #{idx + 1}에 대한 리뷰가 없습니다.")
else:
    st.info("아직 제출된 코드가 없습니다.")
