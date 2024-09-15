import streamlit as st
import pandas as pd
import sqlite3

# 페이지 설정을 wide 모드로 변경
st.set_page_config(layout="wide")

# Bootstrap 테마 적용 (배경색 흰색)
st.markdown("""
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<style>
    .stApp { background-color: #ffffff; }
    .sidebar .sidebar-content { background-color: #f8f9fa; }
    .st-bb { border-bottom: 1px solid #dee2e6; }
    .st-bw { border-width: 1px; }
    .st-br { border-right: 1px solid #dee2e6; }
</style>
""", unsafe_allow_html=True)

# 데이터베이스 연결
conn = sqlite3.connect(':memory:')
c = conn.cursor()

# 샘플 테이블 생성 및 데이터 삽입
c.execute('''CREATE TABLE city
             (ID INTEGER PRIMARY KEY, Name TEXT, CountryCode TEXT, District TEXT, Population INTEGER)''')

c.execute('''CREATE TABLE country
             (Code TEXT PRIMARY KEY, Name TEXT, Continent TEXT, Population INTEGER)''')

# city 테이블에 임시 데이터 3개 추가 
c.execute("INSERT INTO city VALUES (1, '서울', 'KOR', '서울특별시', 9776000)")
c.execute("INSERT INTO city VALUES (2, '부산', 'KOR', '부산광역시', 3429000)")
c.execute("INSERT INTO city VALUES (3, '인천', 'KOR', '인천광역시', 2923000)")

# country 테이블에 임시 데이터 3개 추가
c.execute("INSERT INTO country VALUES ('KOR', '대한민국', 'Asia', 51780579)")
c.execute("INSERT INTO country VALUES ('JPN', '일본', 'Asia', 125360000)")
c.execute("INSERT INTO country VALUES ('CHN', '중국', 'Asia', 1439323776)")

conn.commit()

# 페이지 제목
st.title('SQL-PlayGround')

# 2개의 컬럼 생성
col1, col2 = st.columns(2)

with col1:
    # SQL 입력 영역 (예시 쿼리 추가)
    default_query = "SELECT * FROM city WHERE Population > 3000000"
    sql_query = st.text_area("SQL Code Here", value=default_query, height=200)

    # 실행 버튼
    if st.button('Execute'):
        try:
            df = pd.read_sql_query(sql_query, conn)
            st.success("Query Submitted")
            st.code(sql_query, language='sql')
            
            with col2:
                # 결과 표시
                st.subheader("Results")
                st.dataframe(df)
                
                # Pretty Table
                st.subheader("Pretty Table")
                st.table(df)
        except Exception as e:
            st.error(f"Error: {str(e)}")

st.markdown("---")

# DDL, DML 예시 커맨드 제공
st.subheader("SQL 명령어 예시")
example_commands = """
# DDL 예시:
CREATE TABLE employee (id INTEGER PRIMARY KEY, name TEXT, department TEXT);
ALTER TABLE employee ADD COLUMN salary REAL;
DROP TABLE employee;

# DML 예시:
INSERT INTO employee (name, department, salary) VALUES ('홍길동', 'IT', 50000);
UPDATE employee SET salary = 55000 WHERE name = '홍길동';
DELETE FROM employee WHERE department = 'IT';

# 조회 예시:
SELECT name, salary FROM employee WHERE department = 'IT' ORDER BY salary DESC;
SELECT department, AVG(salary) as avg_salary FROM employee GROUP BY department HAVING avg_salary > 50000;
"""
st.text_area("DDL, DML 예시", value=example_commands, height=350)

# 테이블 정보 표시 (country 테이블 정보 추가)
st.sidebar.subheader("Table Info")
table_info = {
    "city": ["ID", "Name", "CountryCode", "District", "Population"],
    "country": ["Code", "Name", "Continent", "Population"]
}
st.sidebar.json(table_info)

# 스트림릿 앱 실행 방법:
# streamlit run sql-playground.py
