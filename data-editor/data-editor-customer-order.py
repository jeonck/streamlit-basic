import streamlit as st
import pandas as pd
import numpy as np

# 초기 고객 주문 데이터 생성
order_data = pd.DataFrame({
    "Order ID": [1, 2, 3, 4],
    "Customer Name": ["Alice", "Bob", "Charlie", "David"],
    "Product": ["Laptop", "Headphones", "Monitor", "Keyboard"],
    "Quantity": [1, 2, 1, 5],
    "Price per Unit": [1200, 150, 300, 50],
    "Order Status": ["Shipped", "Processing", "Delivered", "Processing"]
})

# 세션 상태로 데이터 유지
if "orders" not in st.session_state:
    st.session_state.orders = order_data

# 데이터 편집기
edited_orders = st.data_editor(
    st.session_state.orders,
    num_rows="dynamic"  # 주문 행 추가 가능
)

# 데이터 편집 후 자동 갱신
if not edited_orders.equals(st.session_state.orders):
    st.session_state.orders = edited_orders
    st.success("Orders updated!")
    st.rerun()

# 편집된 주문 내역 표시
st.write("Current Orders:")
st.write(st.session_state.orders)

# 주문의 총 금액 계산
st.write("Order Summary:")
total_revenue = np.sum(edited_orders["Quantity"] * edited_orders["Price per Unit"])
st.metric("Total Revenue", f"${total_revenue:.2f}")

# 사이드바에서 주문 추가
st.sidebar.write("Add New Order")
new_order_id = st.sidebar.number_input("Order ID", min_value=1, step=1)
new_customer_name = st.sidebar.text_input("Customer Name")
new_product = st.sidebar.text_input("Product")
new_quantity = st.sidebar.number_input("Quantity", min_value=1, step=1)
new_price = st.sidebar.number_input("Price per Unit", min_value=0, value=100, step=10)
new_status = st.sidebar.selectbox("Order Status", ["Shipped", "Processing", "Delivered", "Cancelled"])

if st.sidebar.button("Add Order"):
    new_order = pd.DataFrame({
        "Order ID": [new_order_id],
        "Customer Name": [new_customer_name],
        "Product": [new_product],
        "Quantity": [new_quantity],
        "Price per Unit": [new_price],
        "Order Status": [new_status]
    })
    
    # 새로운 행을 추가하기 위해 concat 사용
    st.session_state.orders = pd.concat([st.session_state.orders, new_order], ignore_index=True)
    st.rerun()  # 새 주문 추가 후 자동 갱신

# 특정 주문 상태 필터링 옵션
st.sidebar.write("Filter Orders by Status")
filter_status = st.sidebar.selectbox("Select Status", ["All", "Shipped", "Processing", "Delivered", "Cancelled"])

if filter_status != "All":
    filtered_orders = st.session_state.orders[st.session_state.orders["Order Status"] == filter_status]
    st.write(f"Orders with status '{filter_status}':")
    st.write(filtered_orders)
else:
    st.write("All Orders:")
    st.write(st.session_state.orders)
