import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"# Streamlit Magic 예제"

"""
## 이 앱은 Streamlit magic 명령어의 여러 사용 예를 보여줍니다.
"""

"### 1. 데이터프레임 표시"
df = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수'],
    '나이': [25, 30, 28]
})
df

"### 2. 차트 그리기"
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart

"### 3. 사용자 입력"
name = st.text_input("이름을 입력하세요")
f"안녕하세요, {name}님!"

age = st.slider('나이를 선택하세요', 0, 100, 25)
f"선택한 나이: {age}"

"### 4. 버튼 상호작용"
if st.button('클릭하세요'):
    "버튼이 클릭되었습니다!"

"### 5. 선택 색상"
option = st.selectbox(
    '좋아하는 색상을 선택하세요',
    ['빨강', '초록', '파랑']
)
f"당신이 선택한 색상: {option}"

"### 6. 체크박스"
if st.checkbox('추가 정보 보기'):
    """
    여기에 추가 정보가 표시됩니다.
    - 항목 1
    - 항목 2
    - 항목 3
    """

"### 끝"
