import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st





option = st.sidebar.selectbox(
    'Select!',
    ('Batter', 'WicketKeeper', 'All-Rounder','Bowler'))

st.write('Selected:', option)



