import pandas as pd
import gdown
import streamlit as st

def Cargar_CSV(id):
    # URL del arhivo pal drive
    url = f'https://drive.google.com/uc?export=download&id={id}'
    output = "archivo.csv"

    # Descargar el df de google drive
    gdown.download(url, output, quiet=False)

    # Leer el archivo CSV descargado
    df = pd.read_csv(output)
    return df

# ID del archivo de Google Drive
id = "1GtL6SWSG0u7ozN5_8aQVGnYSDYt6VW8x"

# Cargar el archivo CSV
df = Cargar_CSV(id)

st.write(df.head())
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
