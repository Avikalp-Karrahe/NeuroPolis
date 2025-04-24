import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# Load your dataset
df = pd.read_csv("final_merged_with_zones.csv")
df = df.dropna(subset=["latitude", "longitude", "zone_id"])

# ----------------------------------------
# Step 1: Classify Events by Risk
# ----------------------------------------

df["risk_level"] = "low"

df.loc[
    ((df["wind_speed_kmph"] > 75) | (df["precipitation_mm"] > 150)) &
    (df["severity"] >= 4.5) &
    (df["casualties"] > 10),
    "risk_level"
] = "high"

df.loc[
    (df["wind_speed_kmph"] < 25) &
    (df["precipitation_mm"] < 50) &
    (df["severity"] <= 3.0) &
    (df["casualties"] <= 5),
    "risk_level"
] = "safe"

# ----------------------------------------
# Step 2: Color map
# ----------------------------------------

risk_colors = {
    "safe": "green",
    "low": "orange",
    "high": "darkred"
}

# ----------------------------------------
# Step 3: Streamlit Sidebar
# ----------------------------------------

st.set_page_config(layout="wide")
st.title("🌍 Interactive Disaster Risk Map")

# Dropdown or multi-select for filtering
selected_risks = st.multiselect(
    "Filter by Risk Level",
    options=["safe", "low", "high"],
    default=["safe", "low", "high"]
)

# Filter data
filtered_df = df[df["risk_level"].isin(selected_risks)]

# ----------------------------------------
# Step 4: Create Map
# ----------------------------------------

center_lat = filtered_df["latitude"].mean()
center_lon = filtered_df["longitude"].mean()
m = folium.Map(location=[center_lat, center_lon], zoom_start=10, tiles="CartoDB positron")

marker_cluster = MarkerCluster().add_to(m)

for _, row in filtered_df.iterrows():
    risk = row["risk_level"]
    popup_html = (
        f"<b>Disaster:</b> {row['disaster_type']}<br>"
        f"<b>Zone:</b> {int(row['zone_id'])}<br>"
        f"<b>Severity:</b> {row['severity']}<br>"
        f"<b>Casualties:</b> {row['casualties']}<br>"
        f"<b>Risk:</b> {risk.capitalize()}"
    )
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=popup_html,
        icon=folium.Icon(color=risk_colors[risk], icon="exclamation-sign")
    ).add_to(marker_cluster)

# ----------------------------------------
# Step 5: Render Map in Streamlit
# ----------------------------------------

st_folium(m, width=1000, height=600)
