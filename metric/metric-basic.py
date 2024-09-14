import streamlit as st

st.header("기본 메트릭")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="온도", value="70 °F", delta="1.2 °F")

with col2:
    st.metric(label="습도", value="60%", delta="-5%")

with col3:
    st.metric(label="기압", value="1013 hPa", delta="3 hPa")
