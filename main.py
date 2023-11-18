import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st

df = pd.read_csv('cricket.csv')

if st.sidebar.button('Click'):
  st.write(df)
batters=['kl rahul','kishan']
# options =st.sidebar.selectbox('choose option',('Batter':batters,'Allrounder','WicketKeeper','Bowlers'))
# st.write(options)
st.write(batters)
