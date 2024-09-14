import streamlit as st
from streamlit_extras.stylable_container import stylable_container

def voting_app():
    st.title("🗳️ 창의적인 투표 앱")

    with stylable_container(
        key="question_container",
        css_styles="""
            {
                background-color: #f0f2f6;
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
            }
            """,
    ):
        st.markdown("### 오늘의 질문: 가장 좋아하는 프로그래밍 언어는?")

    options = ["Python", "JavaScript", "Java", "C++", "기타"]
    
    for option in options:
        with stylable_container(
            key=f"vote_button_{option}",
            css_styles="""
                button {
                    background-color: #4CAF50;
                    color: white;
                    border-radius: 20px;
                    transition: all 0.3s;
                }
                button:hover {
                    background-color: #45a049;
                    transform: scale(1.05);
                }
                """,
        ):
            if st.button(f"{option}에 투표"):
                st.balloons()
                st.success(f"{option}에 투표해 주셔서 감사합니다!")

    with stylable_container(
        key="results_container",
        css_styles="""
            {
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 20px;
                margin-top: 30px;
            }
            """,
    ):
        st.markdown("### 현재 투표 결과")
        st.bar_chart({"Python": 30, "JavaScript": 25, "Java": 20, "C++": 15, "기타": 10})

if __name__ == "__main__":
    voting_app()
