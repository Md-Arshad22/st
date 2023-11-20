import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st

df = pd.read_csv('cricket.csv')
df 
# if st.sidebar.button('Click'):
#   st.write(df.describe())

df1 = pd.read_csv('Squads.csv')
st.pyplot(df1)
if st.sidebar.button('Squad'):
  st.write(df1)

# arr = np.random.normal(1, 1,size=100)
# fig, ax = plt.subplots()
# ax.hist(arr, bins=20)
# st.pyplot(fig)

# a1 = pd.DataFrame(df['year'],df['Total Price'])
# st.line_chart(a1)
# st.pyplot(fig)

option = st.sidebar.selectbox(
    'Select!',
    ('Batter', 'WicketKeeper', 'All-Rounder','Bowler'))

st.write('Selected:', option)



