import streamlit as st
from streamlit_extras.stateful_button import button

def quiz_game():
    st.title("한국 역사 퀴즈")
    
    if button("시작하기", key="start"):
        st.write("1번 문제: 조선의 제4대 왕은 누구일까요?")
        if button("세종대왕", key="q1_correct"):
            st.success("정답입니다!")
            st.write("2번 문제: 한글을 창제한 해는?")
            if button("1443년", key="q2_correct"):
                st.success("정답입니다!")
                st.write("3번 문제: 임진왜란이 일어난 해는?")
                if button("1592년", key="q3_correct"):
                    st.success("축하합니다! 모든 문제를 맞추셨습니다.")
                    st.balloons()
                elif button("다른 답", key="q3_wrong"):
                    st.error("틀렸습니다. 정답은 1592년입니다.")
            elif button("다른 답", key="q2_wrong"):
                st.error("틀렸습니다. 정답은 1443년입니다.")
        elif button("다른 왕", key="q1_wrong"):
            st.error("틀렸습니다. 정답은 세종대왕입니다.")

if __name__ == "__main__":
    quiz_game()