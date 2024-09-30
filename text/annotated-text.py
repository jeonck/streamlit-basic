import streamlit as st
from annotated_text import annotated_text

annotated_text(
    "This ",
    ("is", "verb"),
    " some ",
    ("annotated", "adj"),
    ("text", "noun"),
    " for those of ",
    ("you", "pronoun"),
    " who ",
    ("like", "verb"),
    " this sort of ",
    ("thing", "noun"),
    "."
)

annotated_text(
    "You can now view your ",
    ("Streamlit", ""),
    " app in your ",
    ("browser", ""),
    "."
)