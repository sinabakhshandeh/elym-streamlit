import streamlit as st
from PIL import Image

Image.MAX_IMAGE_PIXELS = 500_000_000  

st.write("# Power-to-X in Germany")

image_caption = "Image source: Birett, F., Goppel, G., & Toperngpong, F. (2024). PtX - Die Zukunft der Energie im Wasserstoffatlas (Version 1). Zenodo. https://doi.org/10.5281/zenodo.13960175"
image_path = Image.open("files/ptx.jpg")
st.image(image_path, caption=image_caption, width="content")
# image_url = "https://zenodo.org/records/13960175/files/PTX%20_%20Die%20Zukunft%20der%20Energie%20groß.jpg?download=1"
# st.image(image_url, caption=image_caption, width="content")

st.write("## What is Power-to-X?")
st.write("""**Power-to-X (PtX)** technologies convert surplus renewable electricity into 
storable and transportable energy carriers such as hydrogen, synthetic fuels, 
and chemicals. These technologies are essential for Germany's energy transition, 
enabling the decarbonization of sectors that cannot be directly electrified, 
including industrial processes, aviation, and long-distance shipping.""")

st.write("## Why It Matters for Germany")
st.write("""Germany has committed to climate neutrality by 2045 and aims to achieve a 10 GW 
electrolysis capacity by 2030 as part of its National Hydrogen Strategy. PtX 
technologies are critical for achieving these goals while reducing dependence 
on imported fossil fuels and supporting the integration of variable renewable 
energy sources (wind and solar).""")

st.write("### Status Review & Analysis of the Implementation-Ambition Gap (2021-2024)")

with st.expander("Planned Capacity", expanded=True):
    st.write("All PtX projects announced between 2021 and 2024")
    st.metric("Capacity", "3.38 GW", chart_type="area")
with st.expander("Operational Capacity", expanded=True):
    st.write("Projects that are currently operational")
    st.metric("Capacity", "0.44 GW")
with st.expander("Ambition-Implementation Gap", expanded=True):
    st.write("Difference between planned and operational capacity")
    st.metric("Capacity", "2.94 GW", delta="-86.9%", delta_color="off", help="Significant gap between planned and operational capacity")

st.markdown("---")

cols = st.columns(3)
with cols[0]:
    st.metric("📊 Projects", "1,238+")
with cols[1]:
    st.metric("🏛️ Federal States", "16")
with cols[2]:
    st.metric("📍 Districts", "107")

cols2 = st.columns(3)
with cols2[0]:
    st.metric("📦 Products", "3")
with cols2[1]:
    st.metric("🔧 Technologies", "8")
with cols2[2]:
    st.metric("📊 Data Sources", "3")

st.markdown("---")
st.markdown("### 🎯 KEY FINDING")
st.warning("""**By 2024, only 0.44 GW of the planned 3.38 GW capacity is operational.**

At the current trajectory, Germany will miss its 10 GW target by 2030 unless urgent action is taken to accelerate implementation.

**Implementation rate has stalled:** 85.7% (2022) → 65% (2023) → 13% (2024)
""")





import pandas as pd

data = {
    "State name": [
        "Baden-Württemberg","Bavaria","Berlin","Brandenburg","Bremen","Hamburg",
        "Hessen","Mecklenburg-Vorpommern","Lower Saxony","Nordrhein-Westfalen",
        "Rheinland-Pfalz","Saarland","Saxony","Saxony-Anhalt","Schleswig-Holstein","Thüringen"
    ],
    "Code": [
        "DE1","DE2","DE3","DE4","DE5","DE6","DE7","DE8",
        "DE9","DEA","DEB","DEC","DED","DEE","DEF","DEG"
    ],
    "projects": [8,13,0,6,9,1,3,1,19,16,4,1,6,9,2,1]
}
