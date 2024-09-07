import streamlit as st

# 페이지 설정: wide 레이아웃 적용
st.set_page_config(layout="wide")

def sidebar_menu():
    st.sidebar.title("Documentation")

    # "Get started" 섹션
    with st.sidebar.expander("Get started", expanded=True):
        st.write("Installation")
        st.write("Use command line")
        st.write("Use Anaconda Distribution")
        st.write("Use GitHub Codespaces")
        st.write("Use Snowflake")

    # "Fundamentals" 섹션
    with st.sidebar.expander("Fundamentals"):
        st.write("First steps")
        st.write("Core concepts")

    # "API reference" 섹션
    with st.sidebar.expander("API reference"):
        st.write("Function 1")
        st.write("Function 2")

def main_content():
    st.title("Streamlit Documentation")
    st.write("""
        Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver dynamic data apps in minutes.
        Let's get started!
    """)

    # 카드 스타일 정의
    st.markdown("""
        <style>
        .card {
            transition: transform 0.2s ease-in-out;
            padding: 20px;
            margin: 10px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: left;
            color: white;
        }

        .card:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        .card-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .card-content {
            font-size: 18px;
        }

        .setup-card {
            background-color: #fca311;
        }

        .api-card {
            background-color: #9b5de5;
        }

        .gallery-card {
            background-color: #00bbf9;
        }
        </style>
        """, unsafe_allow_html=True)

    # 카드 구성
    card_template = """
        <div class="card {card_class}">
            <div class="card-title">{title}</div>
            <div class="card-content">{content}</div>
        </div>
    """

    # 카드들
    st.markdown(card_template.format(card_class="setup-card", title="Setup and installation", content="Get set up to start working with Streamlit."), unsafe_allow_html=True)
    st.markdown(card_template.format(card_class="api-card", title="API reference", content="Learn about our APIs, with actionable explanations of specific functions and features."), unsafe_allow_html=True)

# 사이드바 메뉴와 메인 콘텐츠 호출
sidebar_menu()
main_content()
