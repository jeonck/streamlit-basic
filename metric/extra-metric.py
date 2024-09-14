import streamlit as st
import pandas as pd
import random
from streamlit_extras.metric_cards import style_metric_cards

st.header("📚 온라인 서점 대시보드")

# 가상의 데이터 생성
def generate_data():
    return {
        "일일 판매량": random.randint(50, 200),
        "평균 고객 평점": round(random.uniform(3.5, 5.0), 1),
        "재고 회전율": round(random.uniform(2.0, 8.0), 1),
        "신규 회원 수": random.randint(10, 50)
    }

today_data = generate_data()
yesterday_data = generate_data()

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.metric("일일 판매량", f"{today_data['일일 판매량']}권", 
              f"{today_data['일일 판매량'] - yesterday_data['일일 판매량']}권")

with col2:
    st.metric("평균 고객 평점", f"{today_data['평균 고객 평점']}⭐", 
              f"{today_data['평균 고객 평점'] - yesterday_data['평균 고객 평점']:.1f}")

with col3:
    st.metric("재고 회전율", f"{today_data['재고 회전율']}회", 
              f"{today_data['재고 회전율'] - yesterday_data['재고 회전율']:.1f}회")

with col4:
    st.metric("신규 회원 수", f"{today_data['신규 회원 수']}명", 
              f"{today_data['신규 회원 수'] - yesterday_data['신규 회원 수']}명")

# 메트릭 카드 스타일 적용
style_metric_cards()

