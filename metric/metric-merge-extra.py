import streamlit as st
import random
from datetime import datetime, timedelta
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(page_title="스마트 홈 에너지 대시보드", page_icon="🏠", layout="wide")

st.title("🏠 스마트 홈 에너지 모니터링 대시보드")

# 가상의 데이터 생성 함수
def generate_data():
    return {
        "전력 사용량": round(random.uniform(10, 30), 1),
        "실내 온도": round(random.uniform(18, 28), 1),
        "습도": round(random.uniform(30, 70), 1),
        "태양광 발전량": round(random.uniform(0, 5), 1)
    }

# 현재 시간과 1시간 전 데이터 생성
now = datetime.now()
current_data = generate_data()
previous_data = generate_data()

st.subheader(f"현재 시간: {now.strftime('%Y-%m-%d %H:%M')}")

# 메트릭 표시
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("전력 사용량", f"{current_data['전력 사용량']} kWh", 
              f"{current_data['전력 사용량'] - previous_data['전력 사용량']:.1f} kWh")

with col2:
    st.metric("실내 온도", f"{current_data['실내 온도']} °C", 
              f"{current_data['실내 온도'] - previous_data['실내 온도']:.1f} °C")

with col3:
    st.metric("습도", f"{current_data['습도']}%", 
              f"{current_data['습도'] - previous_data['습도']:.1f}%")

with col4:
    st.metric("태양광 발전량", f"{current_data['태양광 발전량']} kWh", 
              f"{current_data['태양광 발전량'] - previous_data['태양광 발전량']:.1f} kWh")

# 메트릭 카드 스타일 적용
style_metric_cards()

# 에너지 절약 팁
st.subheader("💡 에너지 절약 팁")
tips = [
    "사용하지 않는 전자기기의 플러그를 뽑아두세요.",
    "LED 조명을 사용하여 전력 소비를 줄이세요.",
    "냉난방 온도를 1-2도만 조절해도 큰 효과가 있습니다.",
    "자연 채광을 최대한 활용하세요.",
    "에너지 효율이 높은 가전제품을 사용하세요."
]
for tip in random.sample(tips, 3):
    st.info(tip)

# 시간대별 전력 사용량 차트
st.subheader("⏰ 시간대별 전력 사용량")
hours = [f"{h:02d}:00" for h in range(24)]
usage = [round(random.uniform(5, 25), 1) for _ in range(24)]
chart_data = {"시간": hours, "사용량 (kWh)": usage}
st.line_chart(chart_data, x="시간", y="사용량 (kWh)")

# 사용자 입력: 목표 전력 사용량 설정
st.subheader("🎯 일일 목표 전력 사용량 설정")
target_usage = st.slider("목표 전력 사용량 (kWh)", min_value=0, max_value=50, value=20, step=1)
current_total = sum(usage)
if current_total > target_usage:
    st.warning(f"현재 총 사용량 ({current_total:.1f} kWh)이 목표치를 초과했습니다. 에너지 절약이 필요합니다!")
else:
    st.success(f"잘하고 계십니다! 현재 총 사용량 ({current_total:.1f} kWh)이 목표치 이내입니다.")

st.caption("참고: 이 대시보드의 데이터는 시뮬레이션된 것입니다.")
