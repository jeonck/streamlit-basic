import streamlit as st
import pandas as pd
from streamlit_extras.word_importances import format_word_importances

def create_importance_table(words, importances):
    data = {
        '중요도': [-1, 0, 0.1, 0.2, 0.3, 0.6, 0.8, 0.9],
        '예시 단어': [''] * 8
    }
    df = pd.DataFrame(data)
    
    for i, importance in enumerate(importances):
        idx = df['중요도'].searchsorted(importance)
        if idx < len(df) and df.loc[idx, '예시 단어'] == '':
            df.loc[idx, '예시 단어'] = words[i]
    
    return df

def example():
    text = "Streamlit Extras는 Streamlit 코드 조각을 발견하고 배우고 공유하고 사용하는 데 도움을 주는 라이브러리입니다"
    words = text.split()
    importances = [0.1, 0.2, 0, -1, 0.1, 0, 0, 0.2, 0.3, 0.8, 0.9, 0.6, 0.3, 0.1, 0]
    
    # words와 importances의 길이를 확인하고 출력
    st.write(f"단어 수: {len(words)}")
    st.write(f"중요도 값 수: {len(importances)}")
    
    # 길이가 다르면 조정
    if len(words) > len(importances):
        importances.extend([0] * (len(words) - len(importances)))
    elif len(words) < len(importances):
        importances = importances[:len(words)]
    
    importance_table = create_importance_table(words, importances)
    html = format_word_importances(
        words=words,
        importances=importances,
    )
    st.write(html, unsafe_allow_html=True)
    st.table(importance_table)

st.title("단어 중요도 표시의 여러 예")
example()
