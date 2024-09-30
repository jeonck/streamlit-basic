import streamlit as st
from streamlit_navigation_bar import st_navbar

page = st_navbar(
    pages=["Home", "Documentation", "Examples", "Community", "About"],
    options={"use_padding": False}
    )
st.write(page)