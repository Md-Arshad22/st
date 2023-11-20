import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st


df = pd.read_csv('cricket.csv')
st.title("ICC ODI MEN'S CRICKET WORLD CUP 2023")
st.subheader('Points Table World Cup 2023')
# df 

if st.sidebar.button('Click'):
  st.write(df)

df1 = pd.read_csv('Squads.csv')

if st.sidebar.button('Squad'):
  st.write(df1)


option = st.sidebar.selectbox(
    'Select!',
    ('Batter', 'WicketKeeper', 'All-Rounder','Bowler'))

st.write('Selected:', option)



