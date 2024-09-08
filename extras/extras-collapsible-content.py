import streamlit as st 
from markdownlit import mdlit  # pip install markdownlit
import textwrap  # textwrap 모듈을 import


st.header("Collapsible content example")
def example_collapsible_content():
    mdlit(
        textwrap.dedent(
            """
    ??? Bonus
        @(🎁)(A very insightful tutorial)(https://www.youtube.com/watch?v=dQw4w9WgXcQ)
    """
        )
    )

example_collapsible_content()