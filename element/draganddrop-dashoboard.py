import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_elements import elements, dashboard, mui, html

# 페이지 설정
st.set_page_config(layout="wide")

st.title("드래그 앤 드롭 대시보드 예시")

# 샘플 데이터 생성
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 12, 56]
})

# Plotly 그래프 생성
fig = px.bar(df, x='Category', y='Values', title='카테고리 별 값')

# Plotly 그래프를 HTML로 변환
plotly_html = fig.to_html(full_html=False)

# 데이터프레임을 HTML로 변환
table_html = df.to_html()

# 드래그 앤 드롭 대시보드 레이아웃
layout = [
    dashboard.Item("plot", 0, 0, 6, 3),  # 차트 위젯
    dashboard.Item("table", 6, 0, 6, 3),  # 테이블 위젯
    dashboard.Item("text", 0, 3, 12, 2),  # 텍스트 위젯
]

# Streamlit Elements 활용
with elements("dashboard"):
    # 대시보드 컨테이너 생성
    with dashboard.Grid(layout, draggable=True, resizable=True, rowHeight=150):
        
        # 첫 번째 위젯: Plotly 차트 (HTML로 렌더링)
        mui.Paper(
            elevation=2,
            children=[
                html.h2("실시간 그래프"),
                html.div(dangerouslySetInnerHTML={"__html": plotly_html})
            ],
            key="plot"
        )
        
        # 두 번째 위젯: 데이터 테이블 (HTML로 렌더링)
        mui.Paper(
            elevation=2,
            children=[
                html.h2("데이터 테이블"),
                html.div(dangerouslySetInnerHTML={"__html": table_html})
            ],
            key="table"
        )

        # 세 번째 위젯: 텍스트 위젯
        mui.Paper(
            elevation=2,
            children=[
                html.h2("설명 텍스트"),
                html.p("이 대시보드는 드래그 앤 드롭 기능을 통해 위젯을 자유롭게 배치할 수 있습니다.")
            ],
            key="text"
        )
