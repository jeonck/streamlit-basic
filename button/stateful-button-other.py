import streamlit as st
from streamlit_extras.stateful_button import button
import random

def text_adventure_game():
    st.title("미스터리 저택 탈출")
    
    if button("게임 시작", key="start"):
        st.write("당신은 어두운 저택의 현관에 서 있습니다. 세 개의 문이 보입니다.")
        
        if button("왼쪽 문", key="left_door"):
            st.write("거대한 도서관에 들어섰습니다. 책장 사이로 비밀 통로가 보입니다.")
            if button("비밀 통로로 들어가기", key="secret_passage"):
                st.write("좁은 통로를 지나 보물 방에 도착했습니다!")
                if button("보물 상자 열기", key="open_treasure"):
                    if random.random() < 0.5:
                        st.success("축하합니다! 값진 보물을 찾아 탈출에 성공했습니다!")
                        st.balloons()
                    else:
                        st.error("함정이었습니다! 게임 오버.")
            elif button("도서관 더 탐색하기", key="explore_library"):
                st.write("오래된 책을 발견했습니다. 탈출 힌트가 있을까요?")
                if button("책 읽기", key="read_book"):
                    st.info("책에서 저택의 비밀 지도를 발견했습니다. 탈출구가 표시되어 있습니다!")
                    if button("지도 따라가기", key="follow_map"):
                        st.success("탈출에 성공했습니다! 축하합니다!")
                        st.balloons()
        
        elif button("가운데 문", key="middle_door"):
            st.write("으스스한 거울 방에 들어왔습니다. 거울 속 당신의 모습이 이상합니다.")
            if button("거울 속으로 들어가기", key="enter_mirror"):
                st.write("거울 세계로 들어왔습니다. 모든 것이 뒤집혀 있습니다.")
                if button("뒤로 걷기", key="walk_backwards"):
                    st.success("거꾸로 걸어 탈출구를 찾았습니다! 탈출 성공!")
                    st.balloons()
                elif button("앞으로 걷기", key="walk_forwards"):
                    st.error("미로에 빠졌습니다. 게임 오버.")
            elif button("다른 거울 보기", key="look_other_mirror"):
                st.write("한 거울이 빛나기 시작합니다.")
                if button("빛나는 거울로 가기", key="go_to_shining_mirror"):
                    st.success("빛나는 거울이 포털이었습니다! 탈출 성공!")
                    st.balloons()
        
        elif button("오른쪽 문", key="right_door"):
            st.write("어두운 지하실입니다. 멀리서 이상한 소리가 들립니다.")
            if button("소리 쫓아가기", key="follow_sound"):
                st.write("비밀 실험실을 발견했습니다. 이상한 기계가 있습니다.")
                if button("기계 작동시키기", key="operate_machine"):
                    if random.random() < 0.7:
                        st.success("기계가 당신을 안전한 곳으로 텔레포트시켰습니다! 탈출 성공!")
                        st.balloons()
                    else:
                        st.error("기계가 폭발했습니다. 게임 오버.")
            elif button("돌아가기", key="go_back"):
                st.write("현관으로 돌아왔습니다. 다시 선택하세요.")

if __name__ == "__main__":
    text_adventure_game()
