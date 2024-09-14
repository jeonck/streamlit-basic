import streamlit as st

st.title('Streamlit Popover 예제')

st.write("이것은 메인 페이지의 내용입니다.")

# Popover 생성
with st.popover("메타정보", use_container_width=True):
    st.write("이것은 팝오버 내용입니다.")
    st.info("중요한 정보를 여기에 표시할 수 있습니다.")
    
    # 팝오버 내 차트 예시
    import pandas as pd
    import numpy as np
    
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    st.line_chart(chart_data)
    
    # 팝오버 내 버튼
    if st.button("확인"):
        st.success("확인 버튼이 클릭되었습니다!")

# 메인 페이지의 다른 내용
st.write("팝오버를 닫으면 이 내용이 다시 보입니다.")
