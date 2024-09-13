import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import altair as alt

# 페이지 설정
st.set_page_config(layout="wide")

# 데이터 생성
np.random.seed(0)
df = pd.DataFrame({
    'date': pd.date_range(start='2023-01-01', periods=100),
    'value': np.random.randn(100).cumsum(),
    'category': np.random.choice(['A', 'B', 'C'], 100),
    'size': np.random.randint(10, 100, 100)
})

# 범주형 데이터를 숫자로 매핑
category_map = {'A': 0, 'B': 1, 'C': 2}
df['category_num'] = df['category'].map(category_map)

st.title('고급 Streamlit 차트 예시')

# 4개의 컬럼 생성
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# 1. Plotly 시계열 차트
with col1:
    st.subheader('Plotly 시계열 차트')
    fig = px.line(df, x='date', y='value', title='시간에 따른 값 변화')
    st.plotly_chart(fig, use_container_width=True)

# 2. Plotly 산점도 매트릭스
with col2:
    st.subheader('Plotly 산점도 매트릭스')
    fig = px.scatter_matrix(df, dimensions=['value', 'size'], color='category')
    st.plotly_chart(fig, use_container_width=True)

# 3. Altair 인터랙티브 산점도
with col3:
    st.subheader('Altair 인터랙티브 산점도')
    chart = alt.Chart(df).mark_circle().encode(
        x='date:T',
        y='value:Q',
        size='size:Q',
        color='category:N',
        tooltip=['date', 'value', 'category', 'size']
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

# 4. Plotly 3D 산점도
with col4:
    st.subheader('Plotly 3D 산점도')
    fig = go.Figure(data=[go.Scatter3d(
        x=df['date'],
        y=df['value'],
        z=df['size'],
        mode='markers',
        marker=dict(
            size=5,
            color=df['category_num'],  # 숫자로 매핑된 카테고리 사용
            colorscale='Viridis',
            opacity=0.8
        ),
        text=df['category'],
        hoverinfo='text'
    )])
    fig.update_layout(scene=dict(xaxis_title='Date', yaxis_title='Value', zaxis_title='Size'))
    st.plotly_chart(fig, use_container_width=True)
