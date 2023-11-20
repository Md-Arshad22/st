import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st

def set_background():
    page_bg_img = '''
    <style>
    body {
    background-image: url("CUP.jpg");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Set the background image
set_background()


df = pd.read_csv('cricket.csv')
st.title('ICC ODI MENS CRICKET WORLD CUP 2023')
st.subheader('POINT TABLE WORLD CUP2023')
df

df1 = pd.read_csv('Squads.csv')

if st.sidebar.button('Click Squad'):
    st.write(df1)
    
df2 = pd.read_csv('Bowler.csv')
if st.sidebar.button('Click Bowler'):
    st.write(df2)

option = st.sidebar.selectbox(
    'Select!',
    ('Batter','WicketKeeper', 'All-Rounder','Bowler')
)
st.write('Selected:', option)





