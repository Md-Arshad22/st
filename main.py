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

x = np.array(['SNO','TEAM','M','W','L','NRR','Pts','Last 5'])
y = np.array([17,10,15,50,15,28,30,45])
plt.bar(x,y)
plt.show()





