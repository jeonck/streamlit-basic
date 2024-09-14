import streamlit as st

st.title("자주 묻는 질문 (FAQ)")

faq_data = [
    ("스트림릿이란 무엇인가요?", "스트림릿은 데이터 앱을 쉽게 만들 수 있는 파이썬 라이브러리입니다."),
    ("expander는 어떻게 사용하나요?", "expander는 접을 수 있는 섹션을 만들어 내용을 정리하는 데 도움을 줍니다."),
    ("스트림릿 앱을 배포하려면 어떻게 해야 하나요?", "스트림릿 클라우드나 Heroku 같은 플랫폼을 이용해 배포할 수 있습니다.")
]

for question, answer in faq_data:
    with st.expander(question):
        st.write(answer)

st.write("더 궁금한 점이 있으시면 문의해 주세요!")