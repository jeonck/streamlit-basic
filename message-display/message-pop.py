import streamlit as st
import time

st.title('섹션 내 팝업 유사 효과 예시')

# 메인 섹션
with st.expander("메인 섹션", expanded=True):
    st.write("이것은 메인 섹션의 내용입니다.")
    
    # 팝업을 표시할 빈 공간 생성
    popup_container = st.empty()
    
    # 팝업 트리거 버튼
    if st.button("팝업 메시지 표시"):
        # 팝업 내용
        with popup_container.container():
            st.warning("이것은 팝업 메시지입니다!")
            st.write("3초 후에 자동으로 사라집니다.")
            close_button = st.button("닫기")
            
            # 닫기 버튼이나 3초 후 팝업 제거
            if close_button or time.sleep(3):
                popup_container.empty()
    
    st.write("메인 섹션의 다른 내용이 여기에 표시됩니다.")

# 추가 섹션
with st.expander("추가 정보"):
    st.write("여기에 추가 정보가 들어갑니다.")
    
    # 다른 유형의 팝업 메시지
    info_container = st.empty()
    
    if st.button("정보 메시지 표시"):
        with info_container.container():
            st.info("이것은 정보 메시지입니다.")
            st.write("확인을 누르면 사라집니다.")
            if st.button("확인"):
                info_container.empty()

# 대화상자 유사 효과
with st.expander("대화상자 예시"):
    st.write("대화상자와 유사한 효과를 만들 수 있습니다.")
    
    dialog_container = st.empty()
    
    if st.button("대화상자 열기"):
        with dialog_container.container():
            st.subheader("확인이 필요합니다")
            st.write("정말로 이 작업을 수행하시겠습니까?")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("예"):
                    st.success("작업이 수행되었습니다!")
                    time.sleep(2)
                    dialog_container.empty()
            with col2:
                if st.button("아니오"):
                    dialog_container.empty()

st.write("메인 페이지의 다른 내용들...")
