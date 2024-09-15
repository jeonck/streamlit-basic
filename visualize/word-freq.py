import streamlit as st
import pandas as pd
import spacy
import nltk
import altair as alt
from konlpy.tag import Okt

# NLTK 데이터 다운로드
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# 간단한 감성 사전
positive_words = set(['좋다', '훌륭하다', '멋지다', '행복하다', '즐겁다'])
negative_words = set(['나쁘다', '슬프다', '화나다', '불행하다', '싫다'])

def analyze_sentiment(text):
    okt = Okt()
    tokens = okt.morphs(text)
    positive_score = sum(1 for word in tokens if word in positive_words)
    negative_score = sum(1 for word in tokens if word in negative_words)
    return (positive_score - negative_score) / (positive_score + negative_score + 1e-6)

# 텍스트 분석 및 시각화 앱
def main():
    st.title("텍스트 분석 대시보드")
    
    # 사용자 입력
    text = st.text_area("분석할 텍스트를 입력하세요:")
    
    if text:
        # 텍스트 처리
        try:
            nlp = spacy.load("ko_core_news_sm")
            doc = nlp(text)
            
            # 개체명 인식
            entities = [(ent.text, ent.label_) for ent in doc.ents]
            st.subheader("개체명 인식 결과")
            st.write(pd.DataFrame(entities, columns=["텍스트", "레이블"]))
        except OSError:
            st.error("한국어 모델을 로드할 수 없습니다. 'ko_core_news_sm' 모델이 설치되어 있는지 확인하세요.")
        # 단어 빈도수 시각화
        try:
            okt = Okt()
            words = okt.nouns(text)
            freq_dist = nltk.FreqDist(words)
            
            chart_data = pd.DataFrame(list(freq_dist.items()), columns=["단어", "빈도수"])
            chart = alt.Chart(chart_data).mark_bar().encode(
                x="빈도수",
                y=alt.Y("단어", sort="-x")
            ).properties(height=500)  # 차트 높이 조정
            st.subheader("단어 빈도수")
            st.altair_chart(chart, use_container_width=True)
        except Exception as e:
            st.error(f"텍스트 처리 중 오류가 발생했습니다: {str(e)}")
            
        # 감성 분석
        sentiment = analyze_sentiment(text)
        st.subheader("감성 분석 결과")
        st.write(f"감성 점수: {sentiment:.2f}")
        


if __name__ == "__main__":
    main()
