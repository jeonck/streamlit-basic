import streamlit as st

# 페이지 정의
page_home = st.Page("pages/page1.py", title="홈", icon="🏠")
page_north_star = st.Page("pages/page2.py", title="노스 스타", icon="⭐")
page_core_metrics = st.Page("pages/page3.py", title="핵심 지표", icon="📊")
page_movie_explorer = st.Page("pages/page4.py", title="영화 탐색", icon="🎬")
page_statuses = st.Page("pages/page5.py", title="앱 상태", icon="⏳")
page_leaderboard = st.Page("pages/page6.py", title="클라우드 앱 리더보드", icon="📈")

# 메뉴 구조 정의
menu_structure = {
    "개요": [page_home, page_north_star],
    "메트릭스": [page_core_metrics, page_movie_explorer, page_statuses, page_leaderboard]
}

# 내비게이션 생성
navigation = st.navigation(menu_structure)

# 페이지 기본 설정 (favicon 포함)
st.set_page_config(page_title="멀티페이지 앱 데모", page_icon="📖", layout="wide")

# 선택된 페이지 실행
navigation.run()
