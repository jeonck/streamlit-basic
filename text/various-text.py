import streamlit as st

# App title
st.title("Streamlit Text Formatting Examples")

# Section 1: Expander for color formatting
with st.expander(":rainbow[**Click to see color formatting examples**]"):
    st.markdown(":blue[**Bold blue text**]")
    st.markdown(":green[**Bold green text**]")
    st.markdown(":red[**Bold red text**]")
    st.markdown(":yellow[**Highlighted yellow text**]")
    st.markdown(":orange[**Highlighted orange text**]")
    st.markdown(":violet[**Bold violet text**]")
    st.markdown(":cyan[**Bold cyan text**]")

# Section 2: Expander for text emphasis
with st.expander(":yellow[**Click to see text emphasis examples**]"):
    st.markdown("**Bold Text**")
    st.markdown("*Italic Text*")
    st.markdown("***Bold and Italic Text***")

# Section 3: Expander for background colors
with st.expander(":blue[**Click to see background color examples**]"):
    st.markdown(":background-orange[Text with orange background]")
    st.markdown(":background-yellow[Text with yellow background]")

# Section 4: Expander for custom title example
with st.expander(":red[**Custom Title Example with Rainbow**]"):
    st.markdown(":rainbow[**Refine your output here**]")

import streamlit as st

# 방문자 카운터 배지 이미지 삽입
st.image("https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fyour-site-url.com&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=visits&edge_flat=false", caption="Visitor Count")
