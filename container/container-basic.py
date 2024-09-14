import streamlit as st

# 전체 페이지를 감싸는 외부 컨테이너
with st.container():
    st.title("온라인 쇼핑몰 - 상품 상세")

    # 상품 정보를 표시하는 내부 컨테이너
    with st.container():
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image("https://placehold.co/300x300", caption="상품 이미지")
        
        with col2:
            st.header("고급 가죽 지갑")
            st.write("품번: LW-001")
            st.write("가격: 89,000원")
            st.write("소재: 천연 가죽")
            st.write("색상: 브라운")
    
    # 상품 설명을 위한 내부 컨테이너
    with st.container():
        st.subheader("상품 설명")
        st.write("최고급 천연 가죽으로 제작된 고급 지갑입니다. 내구성이 뛰어나며 세련된 디자인으로 일상생활과 비즈니스 상황 모두에 적합합니다.")
    
    # 구매 옵션을 위한 내부 컨테이너
    with st.container():
        st.subheader("구매 옵션")
        quantity = st.number_input("수량", min_value=1, max_value=10, value=1)
        color = st.selectbox("색상 선택", ["브라운", "블랙", "네이비"])
    
    # 구매 버튼
    if st.button("장바구니에 담기"):
        st.success(f"{quantity}개의 {color} 고급 가죽 지갑을 장바구니에 담았습니다.")

