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

option = st.sidebar.selectbox(
    'Select!',
    ('Batter','WicketKeeper', 'All-Rounder','Bowler')
)
st.write('Selected:', option)


genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")


agree = st.checkbox('I agree')
# if agree:
#     st.write('Great!')
if st.sidebar.button('Click Agree'):
    st.write(agree)


# on = st.toggle('Activate feature')
# if on:
#     st.write('Feature activated!')
