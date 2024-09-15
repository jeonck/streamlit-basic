import streamlit as st
import numpy as np
import time
import altair as alt
import pandas as pd

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield arr

def visualize_bubble_sort():
    st.title("버블 정렬 알고리즘 시각화")

    # 사용자 입력 받기
    num_elements = st.slider("요소의 개수", 5, 50, 7)
    speed = st.slider("애니메이션 속도", 0.1, 2.0, 0.5)

    # 랜덤 배열 생성
    arr = np.random.randint(1, 101, num_elements)

    # 정렬 시작 버튼
    if st.button("정렬 시작"):
        chart = st.empty()
        
        for step in bubble_sort(arr):
            df = pd.DataFrame({"index": range(len(step)), "value": step})
            
            c = alt.Chart(df).mark_bar().encode(
                x='index',
                y='value',
                color=alt.condition(
                    alt.datum.index == alt.datum.value - 1,
                    alt.value('orange'),
                    alt.value('steelblue')
                )
            ).properties(width=700, height=350)

            chart.altair_chart(c)
            time.sleep(speed)

        st.success("정렬 완료!")

if __name__ == "__main__":
    visualize_bubble_sort()
