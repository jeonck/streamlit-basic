import streamlit as st

def example():
    # CSS를 사용하여 카드와 애니메이션 스타일 정의
    st.markdown("""
        <style>
        .card {
            transition: transform 0.2s ease-in-out;
            padding: 20px;
            margin: 10px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            color: white;
            text-align: left;
        }

        .card:hover {
            transform: scale(1.05); /* 마우스 오버 시 확대 */
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
            background-color: #fca311; /* 주황색 */
        }

        .api-card {
            background-color: #9b5de5; /* 보라색 */
        }

        .gallery-card {
            background-color: #00bbf9; /* 파란색 */
        }
        </style>
        """, unsafe_allow_html=True)

    # Streamlit 앱 본문
    st.title("Card Animation Example with Colors")

    # 카드 HTML 템플릿 정의
    card_template = """
        <div class="card {card_class}">
            <div class="card-title">{title}</div>
            <div class="card-content">{content}</div>
        </div>
    """

    # 카드 1 (Setup and installation)
    st.markdown(card_template.format(card_class="setup-card", title="Setup and installation", content="Get set up to start working with Streamlit."), unsafe_allow_html=True)

    # 카드 2 (API reference)
    st.markdown(card_template.format(card_class="api-card", title="API reference", content="Learn about our APIs, with actionable explanations of specific functions and features."), unsafe_allow_html=True)

    # 카드 3 (App gallery)
    st.markdown(card_template.format(card_class="gallery-card", title="App gallery", content="Try out awesome apps created by our users, and curated from our forums or Twitter."), unsafe_allow_html=True)

# 함수 호출
example()
