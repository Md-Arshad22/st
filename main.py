import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st

df = pd.read_csv('cricket.csv')

if st.sidebar.button('Click'):
  st.write(df)

df1 = pd.read_csv('Squads.csv')

if st.sidebar.button('Squad'):
  st.write(df1)

option = st.sidebar.selectbox(
    ('Batter', 'WicketKeeper', 'All-Rounder','Bowler'))

st.write('You selected:', option)



