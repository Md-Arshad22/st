import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st

st.title('ICC ODI MENS CRICKET WORLD CUP 2023')
st.subheader('POINT TABLE WORLD CUP2023')
df = pd.read_csv('cricket.csv')
plt.bar(df['TEAM'],df['M'],df['W'],df['L'],df['NRR'],df['Plt'],df['Last 5'])
plt.show()

df1 = pd.read_csv('Squads.csv')
if st.sidebar.button('Click Squad'):
    st.write(df1)
    
df2 = pd.read_csv('Bowler.csv')
if st.sidebar.button('Click Bowler'):
    st.write(df2)

genre = st.sidebar.selectbox(
    "Your Favorite Team!",
    [":rainbow[India] : Rohit Virat Shami", "***Australia***", "Final Match : Ind vs Aus:"],
    index=None,
)
st.write("You selected:", genre)
# if st.sidebar.selectbox('radio'):
#     st.write(genre)


# option = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone'))

# st.write('You selected:', option)
# if st.sidebar.button('Press'):
#     st.write(option)
