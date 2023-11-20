import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st

df = pd.read_csv('cricket.csv')

if st.sidebar.button('Click'):
  st.write(df)
  
# WicketKeeper=['kl rahul', 'kishan']
# kipper=', '.join(WicketKeeper)

# Allrounder=['Arshad']
# All=', '.join(Allrounder)
# options =st.sidebar.selectbox('Batter','Wicketkeeper','Allrounder','Bowler')
# st.write('options you selected:',options)

df1 = pd.read_csv('Squads.csv')

if st.sidebar.button('Squad'):
  st.write(df1)


options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)




#st.write(kipper)
#st.text(kipper)
