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
# st.write(options)

df1 = pd.read_csv('Squads.csv')

if st.sidebar.button('Squad'):
  st.write(df1)


def get_place(value):
    print("I am called")
    print("Received option", value)

st.set_page_config(page_title="Code of Cosmos", layout="wide")

with st.sidebar:
    print("I am called from sidebar")
    native_name = st.text_input("Name")
    native_place = st.selectbox("Place of Birth", options=[], key="place").on_change(get_place)
    native_dob = st.date_input("Date of Birth")
    native_tob = st.time_input("Time of Birth", "now")
# option = st.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone'))

# st.write('You selected:', option)



#st.write(kipper)
#st.text(kipper)
