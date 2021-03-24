import json
import numpy as np
import pandas as pd
import geopandas as gpd
import plotly.express as px
import streamlit as st

df = gpd.read_file('election_data.csv')

def color(alliance):
    if alliance == 'LDF': color = 'red'
    elif alliance == 'UDF': color = 'blue'
    elif alliance == 'NDA': color = 'gold'
    else: color = 'sliver'
    return 'color: %s' % color

st.dataframe(df.style.applymap(color, subset=['winner_alliance',
                                              'runner_up_alliance',
                                              'third_alliance',
                                              'fourth_alliance']))



with open("kerala_geojson.json") as f:
    map_data = json.load(f)

cmap_alliance = {"LDF": "#fa1e0e",  "UDF": "#28527a",
                 "IND": "#75cfb8", "NDA": "#f4d160"}
fig = px.choropleth_mapbox(df, geojson=map_data, featureidkey="properties.AC_NAME",
                           locations="AC_NAME", mapbox_style="carto-positron",
                           color="winner_alliance", opacity = 0.7,
                           color_discrete_map=cmap_alliance,
                           center={"lat":10.5, "lon":76.3},
                           zoom=6.5, height = 780, width = 700)
st.plotly_chart(fig)

districts = df['DIST_NAME'].unique()
sl_dist = st.selectbox('District', districts)
st.write(sl_dist)
st.write(df[df['DIST_NAME'] == sl_dist])

fig = px.choropleth_mapbox(df[df['DIST_NAME'] == sl_dist],
                           geojson=map_data, featureidkey="properties.AC_NAME",
                           locations="AC_NAME", mapbox_style="carto-positron",
                           color="winner_alliance", opacity = 0.7,
                           color_discrete_map=cmap_alliance,
                           center={"lat":10.5, "lon":76.3}, zoom=6.5,
                           height = 780, width = 700)
st.plotly_chart(fig)

parl_consts = df['PC_NAME'].unique()
sl_pc = st.selectbox('Parliment constituency', parl_consts)
st.write(sl_pc)
st.write(df[df['PC_NAME'] == sl_pc])

fig = px.choropleth_mapbox(df[df['PC_NAME'] == sl_pc],
                           geojson=map_data, featureidkey="properties.AC_NAME",
                           locations="AC_NAME", mapbox_style="carto-positron",
                           color="winner_alliance", opacity = 0.7,
                           color_discrete_map=cmap_alliance,
                           center={"lat":10.5, "lon":76.3}, zoom=6.5,
                           height = 780, width = 700)
st.plotly_chart(fig)
