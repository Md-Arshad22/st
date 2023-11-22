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

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15,30,45,10]
explode = (0, 0.1, 0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode= explode, labels = labels, autopct='%1.1f%',
        shadow= True, startangle=90)
ax1.axis('equal')
st.pyplot(fig1)


