import streamlit as st

pages = {
    "Section 1": [
        st.Page("home.py", title="Home"),
    ],
    "Section 2": [
        st.Page("graphical_analysis.py", title="Geographic Analysis"),
        st.Page("timeline-development.py", title="Temporal Trends"),
        st.Page("technology.py", title="Technology and Product Analysis"),
        st.Page("barriers-challanges.py", title="Barriers and Challenges"),
    ],
}

pg = st.navigation(pages)
pg.run()