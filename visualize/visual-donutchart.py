import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# 페이지 설정
st.set_page_config(page_title="시나리오 창의성 점수 시각화", layout="wide")

# 한글 폰트 설정
font_names = ['맑은 고딕', 'Malgun Gothic', 'AppleGothic', 'NanumGothic', 'Arial Unicode MS']
font_prop = fm.FontProperties(family=font_names)

plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# Streamlit 앱 제목 설정
st.title('시나리오 창의성 점수 시각화')

# 사용자 입력 받기
st.sidebar.header('시나리오 데이터 입력')
scenarios = st.sidebar.text_input('시나리오 이름 (쉼표로 구분)', 'A,B,C,D,E').split(',')
creativity_scores = st.sidebar.text_input('창의성 점수 (쉼표로 구분)', '7,9,5,8,6').split(',')
creativity_scores = [int(score) for score in creativity_scores]

# 시각화 함수
def visualize_creativity(scenarios, scores):
    colors = plt.cm.viridis(np.linspace(0, 1, len(scenarios)))
    
    fig, ax = plt.subplots(figsize=(6, 4))
    wedges, texts, autotexts = ax.pie(scores, labels=scenarios, autopct='%1.1f%%',
                                      startangle=90, colors=colors)
    
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    
    ax.set_title('시나리오별 창의성 점수 분포', fontsize=14, fontproperties=font_prop)
    
    ax.legend(wedges, scenarios,
              title="시나리오",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1),
              prop=font_prop,
              fontsize=10)
    
    plt.setp(autotexts, size=8, weight="bold")
    plt.setp(texts, fontproperties=font_prop, size=10)
    
    plt.tight_layout()
    return fig

# 레이아웃 설정
col1, col2 = st.columns(2)

# 시각화 생성 및 표시
if len(scenarios) == len(creativity_scores):
    fig = visualize_creativity(scenarios, creativity_scores)
    with col1:
        st.pyplot(fig)
else:
    st.error('시나리오 수와 점수 수가 일치하지 않습니다.')

# 데이터 테이블 표시
with col2:
    st.subheader('입력 데이터')
    data = {'시나리오': scenarios, '창의성 점수': creativity_scores}
    st.table(data)
