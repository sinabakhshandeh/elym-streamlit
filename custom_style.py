import streamlit as st


ENPNDR_BG_COLOR = """<style>
[data-testid="stExpander"] {
    background-color: %s;
}
</style>"""

def set_expander_bg_color(color: str) -> str:
    return st.markdown(ENPNDR_BG_COLOR % color, unsafe_allow_html=True)     
