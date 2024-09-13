import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# 인터넷 이미지 링크 목록
image_urls = [
    "https://cdn.pixabay.com/photo/2024/08/18/14/34/folkstone-8978132_1280.jpg",
    "https://cdn.pixabay.com/photo/2024/09/03/09/03/deer-9018759_1280.jpg",
    "https://cdn.pixabay.com/photo/2024/09/05/08/24/mountain-9024209_1280.jpg"
]

# 세션 상태로 현재 이미지 인덱스 관리
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 이전/다음 버튼 함수
def change_image(direction):
    st.session_state.current_index = (st.session_state.current_index + direction) % len(image_urls)

# 현재 선택된 이미지 URL
selected_url = image_urls[st.session_state.current_index]

try:
    # 이미지 다운로드
    response = requests.get(selected_url)
    image = Image.open(BytesIO(response.content))
    
    # 이미지 표시
    st.image(image, use_column_width=True)
    
    # 버튼 표시 (하단에 배치, 중앙 정렬)
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    with col2:
        st.button("◀", on_click=change_image, args=(-1,), key="prev")
    with col3:
        st.write(f"이미지 {st.session_state.current_index + 1}/{len(image_urls)}")
    with col4:
        st.button("▶", on_click=change_image, args=(1,), key="next")

except Exception as e:
    st.error(f"이미지를 불러오는 데 실패했습니다: {e}")
