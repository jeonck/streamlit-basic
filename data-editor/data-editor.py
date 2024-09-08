import streamlit as st
import pandas as pd
import numpy as np

# 데이터 생성
np.random.seed(42)
data = pd.DataFrame({
    "Column A": np.random.randint(1, 100, 10),
    "Column B": np.random.randn(10),
    "Column C": np.random.choice(["Option 1", "Option 2", "Option 3"], 10),
    "Column D": np.random.choice([True, False], 10)
})

# Streamlit Data Editor를 활용하여 데이터 편집
st.title("Advanced Streamlit Data Editor")
st.write("Edit the data below:")

# 데이터 편집기
edited_data = st.data_editor(data, num_rows="dynamic")

# 인덱스를 제거하고 일반적인 테이블처럼 데이터 표시
st.write("Edited Data (in table format, without index):")
st.table(edited_data.reset_index(drop=True))

# 변경된 데이터를 특정 조건에 맞춰 처리
if st.button("Apply Changes"):
    st.write("Processing edited data...")
    
    # 예시로, Column A 값이 50 이상인 행들만 필터링
    filtered_data = edited_data[edited_data["Column A"] >= 50]
    
    # 인덱스를 제거한 필터링된 데이터를 일반 테이블 형식으로 표시
    st.write("Filtered Data (Column A >= 50, in table format, without index):")
    st.table(filtered_data.reset_index(drop=True))

    # 특정 조건을 만족할 경우 rerun
    if filtered_data.empty:
        st.warning("No data matches the condition. Rerunning the app...")
        st.rerun()

# 추가적으로 데이터 요약 통계 제공
if st.checkbox("Show Summary Statistics"):
    st.write("Summary Statistics:")
    st.write(edited_data.describe())
