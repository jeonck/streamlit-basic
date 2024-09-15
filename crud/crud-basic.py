import streamlit as st
import sqlite3
import pandas as pd

# 데이터베이스 연결
conn = sqlite3.connect('data.db')
c = conn.cursor()

# 테이블 생성 (3개 필드)
c.execute('''CREATE TABLE IF NOT EXISTS items
             (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, price REAL)''')

# CRUD 함수
def create(name, quantity, price):
    c.execute("INSERT INTO items (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
    conn.commit()

def read():
    c.execute("SELECT * FROM items")
    return c.fetchall()

def update(id, name, quantity, price):
    c.execute("UPDATE items SET name = ?, quantity = ?, price = ? WHERE id = ?", (name, quantity, price, id))
    conn.commit()

def delete(id):
    c.execute("DELETE FROM items WHERE id = ?", (id,))
    conn.commit()

# Streamlit 앱
st.title('CRUD 기본 예제')

# 2개의 열로 구성된 레이아웃 생성
col1, col2 = st.columns(2)

# 첫 번째 줄
with col1:
    st.header('아이템 추가')
    new_name = st.text_input('이름')
    new_quantity = st.number_input('수량', min_value=0)
    new_price = st.number_input('가격', min_value=0.0, format="%.2f")
    if st.button('추가'):
        create(new_name, new_quantity, new_price)
        st.success('아이템이 추가되었습니다.')

with col2:
    st.header('아이템 수정')
    update_id = st.number_input('수정할 아이템 ID', min_value=1)
    update_name = st.text_input('새 이름')
    update_quantity = st.number_input('새 수량', min_value=0)
    update_price = st.number_input('새 가격', min_value=0.0, format="%.2f")
    if st.button('수정'):
        update(update_id, update_name, update_quantity, update_price)
        st.success('아이템이 수정되었습니다.')

# 두 번째 줄
col3, col4 = st.columns(2)

with col3:
    st.header('아이템 삭제')
    delete_id = st.number_input('삭제할 아이템 ID', min_value=1, key='delete')
    if st.button('삭제'):
        delete(delete_id)
        st.success('아이템이 삭제되었습니다.')

with col4:
    st.header('아이템 목록')
    items = read()
    df = pd.DataFrame(items, columns=['ID', '이름', '수량', '가격'])
    st.dataframe(df)

# 연결 종료
conn.close()
