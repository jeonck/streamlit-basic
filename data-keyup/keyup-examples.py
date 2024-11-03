# pip install streamlit-keyup

import pandas as pd
import streamlit as st
from st_keyup import st_keyup

def main():
    st.title("Keyup 데모 애플리케이션")
    
    # Case 1: 도시 데이터 실시간 필터링
    st.header("케이스 1: 도시 데이터 실시간 검색")
    
    @st.cache_data
    def get_cities() -> pd.DataFrame:
        url = "https://raw.githubusercontent.com/grammakov/USA-cities-and-states/master/us_cities_states_counties.csv"
        return pd.read_csv(url, sep="|")

    cities = get_cities()
    debounce = st.checkbox("0.5초 디바운스 추가")
    name = st_keyup("도시 이름 입력", debounce=500 if debounce else None)

    if name:
        filtered = cities[cities.City.str.lower().str.contains(name.lower(), na=False)]
    else:
        filtered = cities

    st.write(len(filtered), "개의 도시를 찾았습니다")
    st.write(filtered)

    # Case 2: 기본 텍스트 입력
    st.header("케이스 2: 기본 실시간 입력")
    value = st_keyup("텍스트를 입력하세요", key="basic_input")
    st.write("입력된 값:", value)
    
    # Case 3: 기본값이 있는 입력
    st.header("케이스 3: 기본값이 있는 입력")
    default_value = st_keyup("기본값이 있는 입력", 
                            value="여기에 텍스트를 입력하세요", 
                            key="default_input")
    st.write("기본값이 있는 입력:", default_value)
    
    # Case 4: 디바운스 입력
    st.header("케이스 4: 디바운스된 입력")
    debounced_value = st_keyup("디바운스된 입력 (500ms)", 
                              debounce=500, 
                              key="debounced_input")
    st.write("디바운스된 입력:", debounced_value)
    
    # Case 5: 실시간 텍스트 변환
    st.header("케이스 5: 실시간 대문자 변환")
    text_input = st_keyup("대문자 변환 예제", key="upper_input")
    if text_input:
        st.write("대문자 변환:", text_input.upper())

if __name__ == "__main__":
    main() 