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
# st.write(options,Batter)

df1 = pd.read_csv('Squads.csv')

if st.sidebar.button('Squad'):
  st.write(df1)

import streamlit as st

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )




#st.write(kipper)
#st.text(kipper)
