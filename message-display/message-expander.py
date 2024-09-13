import streamlit as st

st.title('확장 가능한 섹션 예시')

# 기본 정보
st.write('이것은 항상 보이는 기본 정보입니다.')

# 확장 가능한 섹션 1: 상세 정보
with st.expander("상세 정보 보기"):
    st.write("이 섹션에는 추가적인 상세 정보가 들어갑니다.")
    st.info("중요한 정보를 강조할 수 있습니다.")
    st.markdown("""
    - 항목 1
    - 항목 2
    - 항목 3
    """)

# 확장 가능한 섹션 2: 사용 방법
with st.expander("사용 방법"):
    st.write("이 앱의 사용 방법을 설명합니다.")
    st.warning("주의사항을 표시할 수 있습니다.")
    st.code("""
    # 예시 코드
    def hello_world():
        print("Hello, World!")
    """, language="python")

# 확장 가능한 섹션 3: FAQ
with st.expander("자주 묻는 질문"):
    st.subheader("Q1: 이 앱은 무엇인가요?")
    st.write("A1: 이 앱은 Streamlit의 expander 기능을 보여주는 예시입니다.")
    
    st.subheader("Q2: expander는 어떻게 사용하나요?")
    st.write("A2: st.expander() 함수를 사용하여 확장 가능한 섹션을 만들 수 있습니다.")

# 확장 가능한 섹션 4: 연락처
with st.expander("연락처"):
    st.write("문의사항이 있으시면 아래로 연락주세요:")
    st.text("이메일: example@example.com")
    st.text("전화: 010-1234-5678")
