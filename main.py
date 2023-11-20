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


option = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)



#st.write(kipper)
#st.text(kipper)
