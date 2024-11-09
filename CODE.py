import pandas as pd
from mega import Mega
import streamlit as st

def Cargar_CSV(id):
    # URL del arhivo pal drive
    url = mega.download_url(url_mega)
    

    # Leer el archivo CSV descargado
    df = pd.read_csv(archivo_mega)
    return df

# ID del archivo de Google Drive
id = "https://mega.nz/file/wwoCBCxC#-67PBibMLweJpc30l6rvt5KapRG29aUcmGcQm9S8fGA"

# Cargar el archivo CSV
df = Cargar_CSV(id)

url_img = f"https://image.tmdb.org/t/p/w342/"
# Selector de ID
titulo_seleccion = st.selectbox("Selecciona la película", df["title"].unique())

# Filtra segun lo seleccionada
selected_movie = df[df["title"] == titulo_seleccion].iloc[0]

# Mostrar cosas basicas de la peli
st.write("### Título:", selected_movie["title"])
st.write("**Fecha de Lanzamiento:**", selected_movie["release_date"])
st.image(url_img +selected_movie["poster_path"], caption=selected_movie["title"])

#BUSCAR COMO OPTIMIZAR LA PAG, VA LENTISIMO
