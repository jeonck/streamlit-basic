import streamlit as st
from streamlit_antd.tabs import st_antd_tabs

def main():
    st.title("안트 디자인 탭 데모")

    # 탭 옵션 정의
    options = ["탭 1", "탭 2", "탭 3"]
    
    # 탭 생성
    selected_tab = st_antd_tabs([{"Label": op} for op in options], key="demo_tabs")
    
    # 선택된 탭에 따른 컨텐츠 표시
    if selected_tab == "탭 1":
        st.write("탭 1의 컨텐츠입니다")
        st.write("여기에 원하는 내용을 추가하세요")
    
    elif selected_tab == "탭 2":
        st.write("탭 2의 컨텐츠입니다")
        st.write("다른 컴포넌트도 추가할 수 있습니다")
        st.button("버튼 예시")
    
    elif selected_tab == "탭 3":
        st.write("탭 3의 컨텐츠입니다")
        st.slider("슬라이더 예시", 0, 100, 50)

if __name__ == "__main__":
    main()
