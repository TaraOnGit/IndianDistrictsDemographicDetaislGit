import streamlit as st
import plotly.express as px
import pandas as pd

st.header('Demographic Details')

df = pd.read_csv('india.csv')
#Sidebar
st.sidebar.header('Choose Demographic Features')

states_list = list(df['State'].unique())
states_list.insert(0,'Overall India')
state = st.sidebar.selectbox('Choose India/State',states_list)
plot_btn = st.sidebar.button('Plot Now')

if plot_btn:
    if state == 'Overall India':
        df = pd.read_csv('india.csv')
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size='Population', color='Literacy_Percentage', zoom=4,
                                size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name='District',
                                title='Size of the circle represents population')

        # fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,size_max=35,
        #                               mapbox_style="carto-positron",width=1200,height=700,hover_name='District')

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write('Selected State Map and Demographic Details')
