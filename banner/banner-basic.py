import streamlit as st
import streamlit.components.v1 as stc

# HTML 배너 정의
HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;">스트림릿 배너 예제</h1>
        <p style="color:white;text-align:center;">streamlit.components.v1을 사용한 커스텀 HTML 배너</p>
    </div>
"""

def main():
    # 배너 표시
    stc.html(HTML_BANNER)
    
    # 페이지 내용
    st.write("이 아래에 페이지의 주요 내용이 들어갑니다.")

if __name__ == "__main__":
    main()
