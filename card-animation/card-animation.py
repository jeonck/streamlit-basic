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
            background-color: white;
            text-align: center;
        }

        .card:hover {
            transform: scale(1.05); /* 마우스 오버 시 확대 */
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        .card-title {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .card-content {
            font-size: 16px;
        }

        </style>
        """, unsafe_allow_html=True)

    # Streamlit 앱 본문
    st.title("Card Animation Example")

    # 카드 UI 만들기
    card_template = """
        <div class="card">
            <div class="card-title">{title}</div>
            <div class="card-content">{content}</div>
        </div>
    """

    # 카드 1
    st.markdown(card_template.format(title="Card 1", content="This is the content of card 1."), unsafe_allow_html=True)

    # 카드 2
    st.markdown(card_template.format(title="Card 2", content="This is the content of card 2."), unsafe_allow_html=True)

    # 카드 3
    st.markdown(card_template.format(title="Card 3", content="This is the content of card 3."), unsafe_allow_html=True)

example()