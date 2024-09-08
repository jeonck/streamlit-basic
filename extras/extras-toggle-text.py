import streamlit as st
from streamlit_extras.stoggle import stoggle

st.header("Toggle text example")
def example():
    stoggle(
        "Click me!",
        """🥷 Surprise! Here's some additional content""",
    )

example()