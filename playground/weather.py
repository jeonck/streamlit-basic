import streamlit as st
import requests

st.set_page_config(layout="wide")

def get_weather(city):
    url = f"http://wttr.in/{city}?T"
    response = requests.get(url)
    return response.text

st.title("주요 도시 날씨 확인 앱")

# 국가별 주요 도시 목록
cities = {
    "한국": ["서울", "부산", "인천", "대구", "대전", "광주", "울산", "제주"],
    "미국": ["Pittsburgh", "Atlanta", "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", 
           "San Diego", "Miami", "Seattle", "San Francisco", "Washington D.C."],
    "일본": ["Tokyo", "Osaka", "Kyoto", "Yokohama", "Nagoya", "Sapporo", "Fukuoka", "Kobe"],
    "중국": ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chengdu", "Hangzhou", "Xi'an", "Chongqing"],
    "동남아시아": {
        "태국": ["Bangkok", "Chiang Mai", "Phuket"],
        "베트남": ["Hanoi", "Ho Chi Minh City", "Da Nang"],
        "싱가포르": ["Singapore"],
        "인도네시아": ["Jakarta", "Bali"]
    },
    "유럽": {
        "프랑스": ["Paris", "Marseille", "Lyon"],
        "독일": ["Berlin", "Munich", "Hamburg"],
        "영국": ["London", "Manchester", "Edinburgh"],
        "이탈리아": ["Rome", "Milan", "Venice"]
    }
}

# 두 개의 컬럼 생성
col1, col2 = st.columns(2)

# 첫 번째 컬럼에 국가/지역 선택 드롭다운 배치
with col1:
    region = st.selectbox("국가/지역을 선택하세요", list(cities.keys()))

# 선택된 국가/지역에 따라 도시 목록 설정
if region in ["한국", "미국", "일본", "중국"]:
    city_list = cities[region]
else:
    country = st.selectbox(f"{region} 국가를 선택하세요", list(cities[region].keys()))
    city_list = cities[region][country]

# 두 번째 컬럼에 도시 선택 드롭다운 배치
with col2:
    selected_city = st.selectbox("도시를 선택하세요", city_list)

if st.button("날씨 확인하기"):
    weather = get_weather(selected_city)
    st.code(weather, language="")

st.markdown("""
<style>
    .stCode {
        white-space: pre !important;
        font-family: monospace !important;
        line-height: 1.2 !important;
        font-size: 0.8em !important;
    }
</style>
""", unsafe_allow_html=True)
