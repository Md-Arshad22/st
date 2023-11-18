import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st

df = pd.read_csv('cricket.csv')

if st.sidebar.button('Click'):
  st.write(df)

option3 =['Batter','Allrounder','WicketKeeper','Bowlers']
options =st.sidebar.selectbox('choose option',('option1','option2','option3'))
st.write(options)
