import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# 페이지 제목 설정
st.title('머티리얼 테이블 예시')

# 샘플 데이터 생성
data = {
    '이름': ['김철수', '이영희', '박민수', '정지원'],
    '나이': [25, 30, 35, 28],
    '직업': ['개발자', '디자이너', '매니저', '연구원'],
    '급여': [3000, 3500, 4000, 3200]
}

# DataFrame 생성
df = pd.DataFrame(data)

# 머티리얼 테이블 대신 AgGrid 사용
st.subheader('데이터 테이블')
gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=True)
gd.configure_default_column(sorteable=True, filterable=True)
gridOptions = gd.build()
AgGrid(df, gridOptions=gridOptions, theme='material')

# 추가 설명 텍스트
st.markdown("""
### 참고사항:
- 이 테이블은 기본적으로 Dracula 테마를 사용합니다
- 정렬, 필터링, 검색 기능이 내장되어 있습니다
- 반응형 디자인으로 모바일에서도 잘 작동합니다
""") 