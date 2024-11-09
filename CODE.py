import pandas as pd
from mega import Mega
import streamlit as st
import os

def Cargar_CSV(url_mega):
    """
    Función que descarga el archivo CSV desde Mega y lo carga en un DataFrame.
    El archivo se descarga solo una vez, ya que la función usa Streamlit cache.
    """
    # Iniciar sesión en Mega
    mega = Mega()

    # Descargar el archivo CSV desde Mega (se descarga en una ubicación temporal)
    archivo_mega = mega.download_url(url_mega)

    # Leer el archivo CSV descargado
    df = pd.read_csv(archivo_mega)
    return df

# URL del archivo de Mega (archivo público)
url_mega = "https://mega.nz/file/wwoCBCxC#-67PBibMLweJpc30l6rvt5KapRG29aUcmGcQm9S8fGA"

# Cargar el archivo CSV desde Mega
df = Cargar_CSV(url_mega)

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
