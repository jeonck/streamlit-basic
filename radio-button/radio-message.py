import streamlit as st
import random

st.title('🌤️ 오늘의 날씨 정보')

# 도시 선택
city = st.selectbox(
    "도시를 선택하세요:",
    ["서울", "부산", "인천", "대구", "대전"]
)

# 날씨 정보
weather_info = {
    "서울": ["맑음", "흐림", "비", "눈"],
    "부산": ["맑음", "흐림", "비", "강풍"],
    "인천": ["맑음", "흐림", "비", "안개"],
    "대구": ["맑음", "흐림", "비", "더움"],
    "대전": ["맑음", "흐림", "비", "쌀쌀함"]
}

# 날씨 아이콘
weather_icons = {
    "맑음": "☀️",
    "흐림": "☁️",
    "비": "🌧️",
    "눈": "❄️",
    "강풍": "🌬️",
    "안개": "🌫️",
    "더움": "🌡️",
    "쌀쌀함": "🥶"
}

if st.button('날씨 확인하기'):
    weather = random.choice(weather_info[city])
    icon = weather_icons[weather]
    temp = random.randint(0, 35)
    
    st.success(f"{city}의 현재 날씨")
    st.markdown(f"### {icon} {weather}")
    st.info(f"현재 기온: {temp}°C")
    
    if weather == "비":
        st.warning("우산을 챙기세요!")
    elif weather == "눈":
        st.warning("미끄러움 주의하세요!")
    elif weather == "강풍":
        st.warning("외출 시 주의하세요!")
    elif temp > 30:
        st.warning("더위 조심하세요!")
    elif temp < 5:
        st.warning("따뜻하게 입으세요!")

# 일기 예보
st.subheader("주간 날씨 전망")
days = ["월", "화", "수", "목", "금"]
for day in days:
    forecast = random.choice(list(weather_icons.keys()))
    st.text(f"{day}요일: {weather_icons[forecast]} {forecast}")

# 사용자 피드백
feedback = st.text_input("날씨 정��에 대한 의견을 남겨주세요:")
if feedback:
    st.write("의견 주셔서 감사합니다!")
