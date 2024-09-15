import streamlit as st

# HTML 래퍼 정의
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

def highlight_text(text, keyword):
    highlighted = text.replace(keyword, f'<span style="background-color: yellow;">{keyword}</span>')
    return HTML_WRAPPER.format(highlighted)

# Streamlit 앱
st.title("텍스트 하이라이트 데모")

# 사용자 입력
text_input = st.text_area("텍스트를 입력하세요:", "안녕하세요. 오늘은 날씨가 좋습니다.")
keyword = st.text_input("하이라이트할 단어를 입력하세요:", "날씨")

if st.button("하이라이트"):
    # 텍스트 하이라이트 수행
    result = highlight_text(text_input, keyword)
    
    # 결과 표시
    st.write("하이라이트 결과:")
    st.markdown(result, unsafe_allow_html=True)

st.markdown("---")
st.write("이 앱은 간단한 텍스트 하이라이트 기능을 제공합니다.")
