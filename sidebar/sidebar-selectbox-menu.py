import streamlit as st

def small_text(text):
    return ''.join([chr(ord('ᴀ') + (ord(c) - ord('a'))) if c.islower() else c for c in text])

def main():
    st.title("맛있는 요리 세계")

    # 첫 번째 선택 상자 (요리 종류)
    cuisine_type = st.sidebar.selectbox(
        "요리 종류를 선택하세요:",
        ("한식", "양식", "일식")
    )

    # 두 번째 선택 상자 (요리 메뉴)
    if cuisine_type == "한식":
        dish = st.sidebar.selectbox(
            "　▸ 한식 메뉴:",
            ("비빔밥", "김치찌개", "불고기"),
            format_func=small_text
        )
    elif cuisine_type == "양식":
        dish = st.sidebar.selectbox(
            "　▸ 양식 메뉴:",
            ("스테이크", "파스타", "샐러드"),
            format_func=small_text
        )
    elif cuisine_type == "일식":
        dish = st.sidebar.selectbox(
            "　▸ 일식 메뉴:",
            ("스시", "라멘", "돈카츠"),
            format_func=small_text
        )

    # 선택된 옵션에 따라 내용 표시
    st.header(f"{cuisine_type} - {dish}")
    st.write(f"{cuisine_type} 요리 중 {dish}에 대한 정보입니다.")

    # 추가 정보 표시 (예시)
    if cuisine_type == "한식" and dish == "비빔밥":
        st.write("비빔밥은 밥에 여러 가지 나물과 고기를 얹고 고추장을 넣어 비벼 먹는 한국의 대표적인 음식입니다.")
    elif cuisine_type == "양식" and dish == "스테이크":
        st.write("스테이크는 고기를 굽거나 석쇠에 구워 만든 요리로, 주로 쇠고기를 사용합니다.")
    elif cuisine_type == "일식" and dish == "스시":
        st.write("스시는 식초로 맛을 낸 밥에 생선이나 해산물을 얹거나 말아서 만든 일본의 대표적인 요리입니다.")

if __name__ == "__main__":
    main()
