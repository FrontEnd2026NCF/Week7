# data_loader.py
# Shared data loader for the gated pages. Cached with st.cache_data so the CSV
# is only read from disk once per session, the same caching pattern from Week 6.

import pandas as pd
import streamlit as st


@st.cache_data
def load_astronauts():
    # Read the astronaut mission records from the data folder.
    astronaut_records = pd.read_csv("data/astronauts.csv")
    # Return the dataframe to whichever page called this function.
    return astronaut_records
