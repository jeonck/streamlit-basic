import streamlit as st
from streamlit_elements import elements, mui, html, editor
import plotly.express as px
import pandas as pd

# 페이지 설정
st.set_page_config(layout="wide")

st.title("실시간 코드 편집기와 대화형 차트")

# 기본적으로 실행될 Plotly 코드
default_code = """
import plotly.express as px
import pandas as pd

# 데이터 생성
df = pd.DataFrame({
    'x': range(10),
    'y': [i**2 for i in range(10)]
})

# 그래프 그리기
fig = px.line(df, x='x', y='y', title='기본 그래프')
st.plotly_chart(fig)
"""

# 사용자 코드 입력 받기
with elements("editor"):
    # Monaco 코드 편집기
    with mui.Grid(item=True, xs=12, md=6):
        mui.Card(
            mui.CardContent(
                html.h2("Plotly 코드 편집기"),
                editor.Monaco(
                    language="python",
                    value=default_code,
                    height=300,
                    theme="vs-dark",
                    key="monaco_editor"
                )
            )
        )

# 코드 실행을 위해 사용자가 편집한 코드 가져오기
user_code = st.session_state.get('monaco_editor', default_code)

# 코드 실행 및 결과 표시
try:
    exec(user_code)
except Exception as e:
    st.error(f"코드를 실행하는 중 오류가 발생했습니다: {e}")

