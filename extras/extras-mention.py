import streamlit as st 
from streamlit_extras.mention import mention

def example():
    st.header("streamlit-extras mention example")
    mention(
        label="example-app-cv-model",
        icon="github",  # GitHub is also featured!
        url="https://github.com/streamlit/example-app-cv-model",
    )

example()