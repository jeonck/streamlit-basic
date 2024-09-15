import streamlit as st
import psutil
import time

# Bootstrap 스타일을 모방한 CSS 정의
BOOTSTRAP_STYLE = """
<style>
    .container {
        padding: 2rem;
        border-radius: 0.5rem;
        background-color: #f8f9fa;
    }
    .card {
        border: 1px solid #dee2e6;
        border-radius: 0.25rem;
        padding: 1rem;
        margin-bottom: 1rem;
        background-color: #ffffff;
        box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
    }
    .card-title {
        font-size: 1rem;
        font-weight: 500;
        color: #6c757d;
        margin-bottom: 0.5rem;
    }
    .card-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #212529;
        margin: 0;
    }
    .bg-primary { background-color: #cfe2ff !important; }
    .bg-success { background-color: #d1e7dd !important; }
    .bg-warning { background-color: #fff3cd !important; }
</style>
"""

def create_metric_card(title, value, bg_class):
    card_content = f"""
    <div class="card {bg_class}">
        <div class="card-title">{title}</div>
        <div class="card-value">{value:.1f}%</div>
    </div>
    """
    return card_content

def get_system_metrics():
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return cpu_percent, memory.percent, disk.percent

def main():
    st.set_page_config(layout="wide")  # 와이드 모드 설정
    
    st.title("시스템 리소스 모니터링-bootstrap style")

    # Bootstrap 스타일 적용
    st.markdown(BOOTSTRAP_STYLE, unsafe_allow_html=True)

    placeholder = st.empty()

    while True:
        with placeholder.container():
            
            cpu, mem, disk = get_system_metrics()

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(create_metric_card("CPU 사용률", cpu, "bg-primary"), unsafe_allow_html=True)

            with col2:
                st.markdown(create_metric_card("메모리 사용률", mem, "bg-success"), unsafe_allow_html=True)

            with col3:
                st.markdown(create_metric_card("디스크 사용률", disk, "bg-warning"), unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)

        time.sleep(5)  # 5초마다 업데이트

if __name__ == "__main__":
    main()
