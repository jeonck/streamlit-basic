import streamlit as st
import streamlit.components.v1 as components

def html_iframe(url: str):
    # CSS를 사용하여 iframe을 전체 화면으로 설정
    iframe_style = """
        <style>
            iframe {
                position: fixed;
                top: 0;
                left: 0;
                bottom: 0;
                right: 0;
                width: 100vw;
                height: 100vh;
                border: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                z-index: 999999;
            }
        </style>
    """
    
    iframe_html = f'{iframe_style}<iframe src="{url}"></iframe>'
    
    # 전체 화면 모드 설정
    st.set_page_config(layout="wide")
    st.title("iframe 예제")

    # HTML 컴포넌트 렌더링
    components.html(iframe_html, height=1000, scrolling=True)

if __name__ == "__main__":
    html_iframe("https://example.com")