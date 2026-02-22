import streamlit as st

pages = {
    "Section 1": [
        st.Page("0-home.py", title="Home"),
    ],
    "Section 2": [
        st.Page("1-graphical_analysis.py", title="Geographic Analysis"),
        st.Page("2-timeline-development.py", title="Temporal Trends"),
        st.Page("3-technology.py", title="Technology and Product Analysis"),
        st.Page("4-barriers-challenges.py", title="Barriers and Challenges"),
    ],
}

pg = st.navigation(pages)
pg.run()