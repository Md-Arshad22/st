import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st


df = pd.read_csv('cricket.csv')
st.title('ICC ODI MENS CRICKET WORLD CUP 2023')
st.subheader('POINTS TABLE WORLD CUP 2023')
df

x = [50,60,70,80,90]
plt.boxplot(x, notch=True)
plt.show()

df1 = pd.read_csv('Squads.csv')
if st.sidebar.button('Click Squad'):
    st.write(df1)
    
df2 = pd.read_csv('Bowler.csv')
if st.sidebar.button('Click Bowler'):
    st.write(df2)

# genre = st.sidebar.selectbox(
#     "Your Favorite Team!",
#     [":rainbow[India] : Rohit Virat Shami", "***Australia***", "Final Match : Ind vs Aus:"],
#     index=None,
# )
# st.write("You selected:", genre)

