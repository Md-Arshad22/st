import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st

df = pd.read_csv('cricket.csv')

if st.sidebar.button('Click'):
  st.write(df)
options =['option1','option2','option3']
selectoption =st.selectbox('select and option',options)

st.sidebar.write(selectoption)
