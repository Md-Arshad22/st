import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st


df = pd.read_csv('cricket.csv')
st.title('ICC ODI MENS CRICKET WORLD CUP 2023')
st.subheader('POINTS TABLE WORLD CUP 2023')
df

df1 = pd.read_csv('Squads.csv')
if st.sidebar.button('Click Squad'):
    st.write(df1)

df2 = pd.read_csv('Bowler.csv')
if st.sidebar.button('Click Bowler'):
    st.write(df2)
    
df3 = pd.read_csv('All.csv')
if st.sidebar.button('All'):
    st.write(df3)

df4 = pd.read_csv('batter.csv')
if st.sidebar.button('Batter'):
    st.write(df4)

# cricket, Squads, = stream.get_data()
# user_menu = st.sidebar.radio(
#     'Select Option',
#     ('Overview', 'Overall Analysis', 'Teamwise Analysis', 'Yearwise Analysis')
# )
# cricket, Squads = stream.get_data()
# user_menu = st.sidebar.radio(
#     'Select Option',
#     ('Overview', 'Overall Analysis', 'Teamwise')
# )

# matches_per_year_df = helper.data_per_year(ball_df, match_df, 'Match No')

#     st.title('Total Matches per Year')
#     fig = px.line(matches_per_year_df, x = 'Year', y= 'Value', height=600, width=900, label
