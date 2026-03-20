import streamlit as st

exec(open("app/0-home.py").read())
st.divider()

exec(open("app/1-graphical_analysis.py").read())
st.divider()

exec(open("app/2-timeline-development.py").read())
st.divider()

exec(open("app/3-technology.py").read())
st.divider()

exec(open("app/4-barriers-challenges.py").read())
