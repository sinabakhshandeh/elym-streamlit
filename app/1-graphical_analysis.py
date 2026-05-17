import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st


st.write("# Geographic Analysis")
st.write("""
Spatial Distribution of PtX Projects Across Germany (2021-2024)

Analysis at NUTS 1 (Federal States) and NUTS 3 (District) levels reveals strong regional concentration and significant disparities in project development."""
)

st.write("## Distribution of announced projects across Germany")

df = pd.read_csv("app/data/dist-ptx-nut1.csv")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Projects", df["Number of announced projects"].sum())
with col2:
    st.metric("Average per State", f"{df['Number of announced projects'].mean():.1f}")
with col3:
    st.metric(
        "Max Projects (State)",
        f"{df.loc[df['Number of announced projects'].idxmax(), 'State name']}",
    )

df11 = px.data.carshare()
df11 = pd.read_csv("app/data/project-distribution.csv")

fig = px.scatter_map(
    df11,
    lat="lat",
    lon="lon",
    color="projects",
    size="projects",
    color_continuous_scale=px.colors.cyclical.IceFire,
    size_max=15,
    zoom=4,
    template="plotly_dark",
    hover_name="NUTS_ID",
    hover_data={
        "projects": True,
        "lat": ":.2f",
        "lon": ":.2f",
    },
)
st.plotly_chart(fig)


st.subheader("Project Distribution")

df_sorted = df.sort_values("Number of announced projects", ascending=True)
fig = go.Figure(go.Bar(
    x=df_sorted["Number of announced projects"],
    y=df_sorted["State name"],
    orientation='h',
    marker=dict(
        color='mediumseagreen',
        line=dict(
            color='seagreen',
            width=1
        )
    )
))

st.plotly_chart(fig)
