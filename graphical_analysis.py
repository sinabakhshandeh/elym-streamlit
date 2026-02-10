
import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st
import custom_style as cs


# Download and load Germany NUTS1 shapefile
@st.cache_data
def load_germany_nuts1():
    try:
        # Try to load from online source
        gdf = gpd.read_file('map.json')
        # Filter for Germany
        gdf = gdf[gdf['CNTR_CODE'] == 'DE'].copy()
        return gdf
    except:
        st.error("Could not load Germany NUTS1 shapefile from online source.")
        return None


st.write("# Geographic Analysis")
st.write("Spatial Distribution of PtX Projects Across Germany (2021-2024)")
st.write("Analysis at NUTS 1 (Federal States) and NUTS 3 (District) levels reveals strong regional concentration and significant disparities in project development.")
st.write("## Distribution of Announced Projects Across German NUTS1 Regions")

df = pd.read_csv("data/dist-ptx-nut1.csv")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Projects", df['Number of announced projects'].sum())
with col2:
    st.metric("Average per State", f"{df['Number of announced projects'].mean():.1f}")
with col3:
    st.metric("Max Projects (State)", f"{df.loc[df['Number of announced projects'].idxmax(), 'State name']}")




with st.spinner("Loading map data..."):
    germany_nuts1 = load_germany_nuts1()

if germany_nuts1 is not None:
    # Merge the data with the geodataframe
    germany_nuts1 = germany_nuts1.merge(
        df[['Code', 'Number of announced projects', 'State name']], 
        left_on='NUTS_ID', 
        right_on='Code', 
        how='left'
    )
    
    # Fill NaN values with 0 for regions without data
    germany_nuts1['Number of announced projects'] = germany_nuts1['Number of announced projects'].fillna(0)
    
    # Create the map with seaborn styling
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(1, 1, figsize=(14, 16))
    
    # Plot the choropleth
    germany_nuts1.plot(
        column='Number of announced projects',
        ax=ax,
        legend=True,
        cmap='YlOrRd',
        edgecolor='black',
        linewidth=0.5,
        legend_kwds={
            'label': "Number of Announced Projects",
            'orientation': "horizontal",
            'shrink': 0.6,
            'pad': 0.05
        }
    )
    
    # Add state labels
    for idx, row in germany_nuts1.iterrows():
        if pd.notna(row['State name']):
            centroid = row['geometry'].centroid
            projects = int(row['Number of announced projects'])
            ax.annotate(
                text=f"{row['State name']}\n({projects})",
                xy=(centroid.x, centroid.y),
                horizontalalignment='center',
                fontsize=8,
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7, edgecolor='none')
            )
    
    ax.set_title('Distribution of Announced Projects Across German NUTS1 Regions', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')
    
    # Display the map in Streamlit
    st.pyplot(fig)
    
    # Additional visualizations
    st.subheader("Project Distribution - Bar Chart")
    
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    df_sorted = df.sort_values('Number of announced projects', ascending=True)
    
    sns.barplot(
        data=df_sorted,
        y='State name',
        x='Number of announced projects',
        palette='YlOrRd',
        ax=ax2
    )
    
    ax2.set_xlabel('Number of Announced Projects', fontsize=12, fontweight='bold')
    ax2.set_ylabel('State', fontsize=12, fontweight='bold')
    ax2.set_title('Projects by State (Sorted)', fontsize=14, fontweight='bold')
    
    # Add value labels on bars
    for i, v in enumerate(df_sorted['Number of announced projects']):
        ax2.text(v + 0.3, i, str(v), va='center', fontsize=10)
    
    st.pyplot(fig2)
    
else:
    st.warning("Map could not be loaded. Showing data table and bar chart only.")
    
    # Show bar chart as alternative
    st.subheader("Project Distribution - Bar Chart")
    
    fig, ax = plt.subplots(figsize=(12, 6))
    df_sorted = df.sort_values('Number of announced projects', ascending=True)
    
    sns.barplot(
        data=df_sorted,
        y='State name',
        x='Number of announced projects',
        palette='YlOrRd',
        ax=ax
    )
    
    ax.set_xlabel('Number of Announced Projects', fontsize=12, fontweight='bold')
    ax.set_ylabel('State', fontsize=12, fontweight='bold')
    ax.set_title('Projects by State (Sorted)', fontsize=14, fontweight='bold')
    
    for i, v in enumerate(df_sorted['Number of announced projects']):
        ax.text(v + 0.3, i, str(v), va='center', fontsize=10)
    
    st.pyplot(fig)
