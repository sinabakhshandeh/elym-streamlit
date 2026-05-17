import streamlit as st

from utils.i18n import tr, SUPPORTED_LANGS

LANG_FLAGS = {"en": "🇬🇧", "de": "🇩🇪"}

def render_language_selector():
    lang = st.radio(
        "lang",
        options=list(LANG_FLAGS.keys()),
        format_func=lambda x: LANG_FLAGS[x],
        horizontal=True,
        label_visibility="collapsed",
        key="lang"
    )
    return lang

render_language_selector()

exec(open("app/abstract.py").read())
st.divider()


st.title(tr("geographic.title"))
st.subheader(tr("geographic.subtitle"))
st.write(tr("geographic.description"))

st.subheader(tr("geographic.distribution_section.title"))

# Load the dataset for the geographic distribution of projects
project_df = pd.read_csv("app/data/dist-ptx-nut1.csv")

# Display key statistics about the project distribution
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        tr("geographic.distribution_section.stats.total_projects.label"),
        project_df["Number of announced projects"].sum(),
    )
with col2:
    st.metric(
        tr("geographic.distribution_section.stats.average_per_state.label"),
        f"{project_df['Number of announced projects'].mean():.1f}",
    )
with col3:
    st.metric(
        tr("geographic.distribution_section.stats.max_projects_state.label"),
        f"{project_df.loc[project_df['Number of announced projects'].idxmax(), 'State name']}",
    )

project_dist_df = pd.read_csv("app/data/project-distribution.csv")

# Create a scatter map to visualize the geographic distribution of projects
fig = px.scatter_map(
    project_dist_df,
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

st.subheader(tr("geographic.project_distribution_section.title"))

df_sorted = project_df.sort_values(
    "Number of announced projects",
    ascending=True,
)

# Create a horizontal bar chart to show the distribution of projects across states
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


# exec(open("app/graphical_analysis.py").read())
st.divider()

exec(open("app/2-timeline-development.py").read())
st.divider()

exec(open("app/3-technology.py").read())
st.divider()

exec(open("app/faq.py").read())
