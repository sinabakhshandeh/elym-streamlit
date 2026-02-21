import streamlit as st

pages = {
    "Section 1": [
        st.Page("home.py", title="Home"),
    ],
    "Section 2": [
        st.Page("graphical_analysis.py", title="Geographic Analysis"),
        st.Page("timeline-development.py", title="Temporal Trends"),
    ],
}

pg = st.navigation(pages)
pg.run()