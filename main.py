import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st


df = pd.read_csv('cricket.csv')
st.title('ICC ODI MENS CRICKET WORLD CUP 2023')
st.subheader('POINT TABLE WORLD CUP2023')
df

df1 = pd.read_csv('Squads.csv')

if st.sidebar.button('Click Squad'):
    st.write(df1)
    
df2 = pd.read_csv('Bowler.csv')
if st.sidebar.button('Click Bowler'):
    st.write(df2)

# option = st.sidebar.selectbox(
#     'Select!',
#     ('Batter','WicketKeeper', 'All-Rounder','Bowler')
# )
# st.write('Selected:', option)


genre = st.radio(
    "Your Favorite Team!",
    [":rainbow[India] : Rohit Virat Shami", "***Australia***", "Final Match : Ind vs Aus:"],
    index=None,
)
st.write("You selected:", genre)

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
if st.sidebar.button('Press'):
    st.write(option)


on = st.toggle('Activate feature')
if on:
    st.write('Feature activated!')
