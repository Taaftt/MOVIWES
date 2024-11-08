import streamlit as st
import pandas as pd

# Carga el archivo CSV "top_hiphop_artists_tracks.csv" en un DataFrame de pandas.
df = pd.read_csv("imdb_top_1000.csv")
st.write(df)
