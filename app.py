import streamlit as st
import plotly.express as px
import pandas as pd

st.header('Demographic Details')

df = pd.read_csv('india.csv')
#Sidebar
st.sidebar.header('Choose Demographic Features')
states_list = list(df['State'].unique())
states_list.insert(0,'Overall India')
state = st.sidebar.selectbox('India/State - Literacy and Population',states_list)
btn_lp= st.sidebar.button('Plot for Literacy and Population')

st.sidebar.header('Choose Other Parameters')
param_list = df.columns.drop(['Unnamed: 0','State','District','Latitude','Longitude','District code'])
param1 = st.sidebar.selectbox('Choose Other Parameter 1 ',param_list)
param2 = st.sidebar.selectbox('Choose Other Parameter 2',param_list.drop(param1))
btn_oth = st.sidebar.button('Plot The Chosen Parameters')

if btn_lp:
    if state == 'Overall India':
        df = pd.read_csv('india.csv')
        st.subheader('Size of the circle represents population')
        st.subheader('Color of the circle represents literacy percentage')
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size='Population', color='Literacy_Percentage', zoom=4,
                                size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name='District',
                                title='Literacy and Population')

        # fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,size_max=35,
        #                               mapbox_style="carto-positron",width=1200,height=700,hover_name='District')
        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = df[df['State'] == state]
        st.subheader('Size of the circle represents population')
        st.subheader('Color of the circle represents literacy percentage')
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size='Population', color='Literacy_Percentage',
                                zoom=4,
                                size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name='District',
                                title='Size of the circle represents population')
        st.plotly_chart(fig, use_container_width=True)

if btn_oth:
    if state == 'Overall India':
        df = pd.read_csv('india.csv')
        st.subheader('Size of the circle represents '+param1)
        st.subheader('Color of the circle represents '+param2)
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=param1, color=param2, zoom=4,
                                size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name='District',
                                title=param1 +' and '+param2)

        # fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,size_max=35,
        #                               mapbox_style="carto-positron",width=1200,height=700,hover_name='District')
        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = df[df['State'] == state]
        st.subheader('Size of the circle represents ' + param1)
        st.subheader('Color of the circle represents ' + param2)
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=param1, color=param2, zoom=4,
                                size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name='District',
                                title=param1 +' and '+param2)

        # fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,size_max=35,
        #                               mapbox_style="carto-positron",width=1200,height=700,hover_name='District')
        st.plotly_chart(fig, use_container_width=True)
