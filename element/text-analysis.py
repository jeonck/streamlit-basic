import streamlit as st
from streamlit_elements import elements, mui, html
from textblob import TextBlob

# 페이지 설정
st.set_page_config(layout="wide")

st.title("실시간 텍스트 감성 분석 대시보드")

# 텍스트 입력
input_text = st.text_area("텍스트를 입력하세요", value="이 앱은 정말 유용해요!")

# 텍스트가 입력되었을 때만 분석
if input_text:
    # 감성 분석 수행
    blob = TextBlob(input_text)
    sentiment_polarity = blob.sentiment.polarity
    sentiment_subjectivity = blob.sentiment.subjectivity

    # 감성 분석 결과에 따른 상태 설정
    if sentiment_polarity > 0:
        sentiment_result = "긍정적"
    elif sentiment_polarity < 0:
        sentiment_result = "부정적"
    else:
        sentiment_result = "중립적"
    
    # Streamlit-Elements를 사용해 결과를 실시간으로 보여줌
    with elements("sentiment_analysis"):
        mui.Grid(container=True, spacing=2)(
            # 분석 결과 텍스트
            mui.Grid(item=True, xs=12, md=6)(
                mui.Card(
                    mui.CardContent(
                        html.h2("분석 결과"),
                        html.p(f"텍스트 감정: {sentiment_result}"),
                        html.p(f"감정 점수 (Polarity): {sentiment_polarity:.2f}"),
                        html.p(f"주관성 점수 (Subjectivity): {sentiment_subjectivity:.2f}")
                    )
                )
            ),
            # 감정 점수 시각화
            mui.Grid(item=True, xs=12, md=6)(
                mui.Card(
                    mui.CardContent(
                        html.h2("감정 점수 시각화"),
                        html.p(f"Polarity: {'긍정적' if sentiment_polarity > 0 else '부정적' if sentiment_polarity < 0 else '중립적'}"),
                        html.progress(value=sentiment_polarity, max=1, min=-1),  # 감정 점수 시각화 (Polarity)
                        html.p(f"Subjectivity: {sentiment_subjectivity:.2f}"),
                        html.progress(value=sentiment_subjectivity, max=1)  # 주관성 점수 시각화
                    )
                )
            )
        )

else:
    st.info("텍스트를 입력하세요.")
