import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st

st.title('ICC ODI MENS CRICKET WORLD CUP 2023')
st.subheader('POINT TABLE WORLD CUP 2023')

df = pd.read_csv('cricket.csv')
df

if st.sidebar.button('load description'):
  st.write(df.describe())

df1 = pd.read_csv('Squads.csv')
if st.sidebar.button('Squad'):
  st.write(df1)

df2 = pd.read_csv('Bowler.csv')

if st.sidebar.button('Bowler'):
  st.write(df2)



