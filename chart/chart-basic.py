import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 페이지 설정을 앱의 가장 상단에 배치
st.set_page_config(layout="wide")

# 데이터 생성
np.random.seed(0)
df = pd.DataFrame({
    'x': range(100),
    'y': np.random.randn(100).cumsum(),
    'category': np.random.choice(['A', 'B', 'C', 'D'], 100)
})

st.title('Streamlit 차트 예시')

# 8개의 컬럼 생성 (2행 4열)
col1, col2, col3, col4 = st.columns(4)
col5, col6, col7, col8 = st.columns(4)

# 첫 번째 행
with col1:
    st.subheader('선 차트')
    st.line_chart(df[['x', 'y']])

with col2:
    st.subheader('영역 차트')
    st.area_chart(df[['x', 'y']])

with col3:
    st.subheader('막대 차트')
    st.bar_chart(df[['x', 'y']])

with col4:
    st.subheader('산점도')
    st.scatter_chart(df[['x', 'y']])

# 두 번째 행
with col5:
    st.subheader('히스토그램')
    fig, ax = plt.subplots()
    ax.hist(df['y'], bins=20)
    st.pyplot(fig)

with col6:
    st.subheader('파이 차트')
    fig, ax = plt.subplots()
    df['category'].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%')
    st.pyplot(fig)

with col7:
    st.subheader('히트맵')
    corr = df[['x', 'y']].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, ax=ax)
    st.pyplot(fig)

with col8:
    st.subheader('박스플롯')
    fig, ax = plt.subplots()
    sns.boxplot(x='category', y='y', data=df, ax=ax)
    st.pyplot(fig)
