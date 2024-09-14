import streamlit as st

def main():
    st.title("여행 계획 도우미")
    
    # 메인 페이지
    if 'page' not in st.session_state:
        st.session_state.page = 'main'

    if st.session_state.page == 'main':
        st.write("어떤 종류의 여행을 계획하고 계신가요?")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("도시 여행"):
                st.session_state.page = '도시_여행'
                st.rerun()
        
        with col2:
            if st.button("자연 여행"):
                st.session_state.page = '자연_여행'
                st.rerun()
        
        with col3:
            if st.button("문화 체험"):
                st.session_state.page = '문화_체험'
                st.rerun()
        
        st.write("---")
        st.write("나만의 여행 계획을 공유하고 싶으신가요?")
        
        if st.button("여행 계획 공유하기"):
            st.session_state.page = '계획_공유'
            st.rerun()

    # 도시 여행 페이지
    elif st.session_state.page == '도시_여행':
        st.write("도시 여행 페이지입니다.")
        if st.button("메인으로 돌아가기"):
            st.session_state.page = 'main'
            st.rerun()

    # 자연 여행 페이지
    elif st.session_state.page == '자연_여행':
        st.write("자연 여행 페이지입니다.")
        if st.button("메인으로 돌아가기"):
            st.session_state.page = 'main'
            st.rerun()

    # 문화 체험 페이지
    elif st.session_state.page == '문화_체험':
        st.write("문화 체험 페이지입니다.")
        if st.button("메인으로 돌아가기"):
            st.session_state.page = 'main'
            st.rerun()

    # 계획 공유 페이지
    elif st.session_state.page == '계획_공유':
        st.write("여행 계획 공유 페이지입니다.")
        if st.button("메인으로 돌아가기"):
            st.session_state.page = 'main'
            st.rerun()

if __name__ == "__main__":
    main()
