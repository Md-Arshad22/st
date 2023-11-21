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

df2 pd.read_csv('Bowler.csv')
if st.sidebar.button('Click Bowler'):
    st.write(df1)
    
# df2 = pd.read_csv('Bowler.csv')
# if st.sidebar.button('Click Bowler'):
#     st.write(df2)

# ball_df, match_df, summary, city_df = dataset.get_data()
# user_menu = st.sidebar.radio(
#     'Select Option',
#     ('Overview', 'Overall Analysis','Teamwise Analysis' , 'Yearwise Analysis')
# )





    
# genre = st.sidebar.selectbox(
#     "Your Favorite Team!",
#     [":rainbow[India] : Rohit Virat Shami", "***Australia***", "Final Match : Ind vs Aus:"],
#     index=None,
# )
# st.write("You selected:", genre)

# matches_per_year_df = helper.data_per_year(ball_df, match_df, 'Match No')

#     st.title('Total Matches per Year')
#     fig = px.line(matches_per_year_df, x = 'Year', y= 'Value', height=600, width=900, label
