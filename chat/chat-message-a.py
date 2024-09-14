import streamlit as st

faq_data = {
    "제품 반품은 어떻게 하나요?": "구매일로부터 14일 이내에 고객센터로 연락 주시면 안내해 드리겠습니다.",
    "배송은 얼마나 걸리나요?": "일반적으로 2-3일 소요되며, 도서산간 지역은 1-2일 추가될 수 있습니다.",
    # 더 많은 FAQ 항목 추가
}

st.title("대화형 FAQ")

for question in faq_data:
    user_message = st.chat_message("user")
    user_message.write(question)
    
    bot_message = st.chat_message("assistant")
    bot_message.write(faq_data[question])