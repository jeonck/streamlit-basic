import streamlit as st
import pandas as pd

# 샘플 데이터
data = [
    {
        "content": "르브론은 우주 배경으로 전쟁하는 영화를 보고 싶어합니다.",
        "time_stamp": 1724903384,
        "category": "Hopes",
        "priority": 10,
        "order_idx": 0,
        "date": "2024-08-29 12:49:43 KST"
    },
    {
        "content": "연아는 '스타워즈'와 '인터스텔라'를 추천하며 이러한 스타일의 영화를 좋다고 물었습니다.",
        "time_stamp": 1724903384,
        "category": "Favorites",
        "priority": 10,
        "order_idx": 0,
        "date": "2024-08-29 12:49:44 KST"
    },
    {
        "content": "르브론은 영화 중에서 화려한 비주얼과 매력적인 스토리를 가진 것을 선호합니다.",
        "time_stamp": 1724903383,
        "category": "Favorites",
        "priority": 10,
        "order_idx": 0,
        "date": "2024-08-29 12:49:43 KST"
    },
    {
        "content": "연아는 '바빌론'과 '오펜하이머'와 같은 최근의 인기 영화를 추천했습니다.",
        "time_stamp": 1724903383,
        "category": "Favorites",
        "priority": 10,
        "order_idx": 0,
        "date": "2024-08-29 12:49:43 KST"
    },
    {
        "content": "르브론은 최근 농구 경기에 많은 변화가 있었다고 생각합니다.",
        "time_stamp": 1724901860,
        "category": "Opinions",
        "priority": 10,
        "order_idx": 0,
        "date": "2024-08-29 12:24:20 KST"
    },
    {
        "content": "르브론은 오프 시즌 동안의 농구 경기 변화에 대한 소감을 듣고 싶어합니다.",
        "time_stamp": 1724901860,
        "category": "Event",
        "priority": 10,
        "order_idx": 0,
        "date": "2024-08-29 12:24:20 KST"
    }
]

st.header("only data frame")
st.dataframe(data)

st.header("pandas data frame")
st.dataframe(pd.DataFrame(data))
