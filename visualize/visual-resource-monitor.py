import streamlit as st
import psutil
import time

# HTML 래퍼 정의
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 1rem; background-color: {bg_color};">{content}</div>"""

def create_metric_card(title, value, bg_color):
    card_content = f"""
    <h4 style="margin-top: 0; margin-bottom: 0.5rem; font-size: 1rem; color: #555;">{title}</h4>
    <p style="font-size: 2.5rem; font-weight: bold; margin: 0; color: #333;">{value:.1f}%</p>
    """
    return HTML_WRAPPER.format(bg_color=bg_color, content=card_content)

def get_system_metrics():
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return cpu_percent, memory.percent, disk.percent

def main():
    st.set_page_config(layout="wide")  # 와이드 모드 설정
    
    st.title("시스템 리소스 모니터링")

    # 전체 컨테이너에 대한 CSS 스타일 추가
    st.markdown("""
    <style>
    .stContainer > div > div {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

    placeholder = st.empty()

    while True:
        with placeholder.container():
            cpu, mem, disk = get_system_metrics()

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(create_metric_card("CPU 사용률", cpu, "#e6f2ff"), unsafe_allow_html=True)

            with col2:
                st.markdown(create_metric_card("메모리 사용률", mem, "#e6ffe6"), unsafe_allow_html=True)

            with col3:
                st.markdown(create_metric_card("디스크 사용률", disk, "#ffe6e6"), unsafe_allow_html=True)

        time.sleep(5)  # 5초마다 업데이트

if __name__ == "__main__":
    main()