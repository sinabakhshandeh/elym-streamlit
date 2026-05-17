import streamlit as st


st.title(tr('abstract.title'))
st.subheader(tr('abstract.subtitle'))

# Metrics section for planned capacity, operational capacity, and
# ambition-implementation gap with expanders for descriptions and help text
col1, col2, col3 = st.columns(3)
with col1:
    with st.expander(tr('abstract.metrics.planned_capacity.label'), expanded=True):
        st.write(tr('abstract.metrics.planned_capacity.description'))
        st.metric(
            tr('abstract.metrics.planned_capacity.capacity_label'),
            "3.38 GW",
            chart_type="area",
        )
with col2:
    with st.expander(tr('abstract.metrics.operational_capacity.label'), expanded=True):
        st.write(tr('abstract.metrics.operational_capacity.description'))
        st.metric(
            tr('abstract.metrics.operational_capacity.capacity_label'),
            "0.44 GW",
        )
with col3:
    with st.expander(tr('abstract.metrics.ambition_impl_gap.label'), expanded=True):
        st.write(tr('abstract.metrics.ambition_impl_gap.description'))
        st.metric(
            tr('abstract.metrics.ambition_impl_gap.capacity_label'),
            "2.94 GW",
            delta="-86.9%",
            delta_color="off",
            help=tr('abstract.metrics.ambition_impl_gap.capacity_help'),
        )

# Stats section for projects, products, technologies, and data sources
cols = st.columns(3)
with cols[0]:
    st.metric(tr('abstract.stats.projects.label'), "1,238+")
with cols[1]:
    st.metric(tr('abstract.stats.products.label'), "3")
with cols[2]:
    st.metric(tr('abstract.stats.technologies.label'), "8")

cols2 = st.columns(3)
with cols2[0]:
    st.metric(tr('abstract.stats.data_sources.label'), "3")

# Key finding section with highlight and implementation rate
st.subheader(tr('abstract.key_finding.title'))
st.write(tr('abstract.key_finding.highlight'))
st.write(tr('abstract.key_finding.body'))
st.write(
    tr('abstract.key_finding.implementation_rate_label'),
    "85.7% (2022) → 65% (2023) → 13% (2024)"
)
