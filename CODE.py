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
id = "1LlKcNqJA3zlbC76KvaYbIF4ZGPyEZoHy"

# Cargar el archivo CSV
df = Cargar_CSV(id)



id_peli =5
# Filtrar el DataFrame para obtener la fila correspondiente al ID seleccionado
pelicula = df[df["id"] == id_peli].iloc[0]

# Obtener la imagen y el título de la película
imagen = pelicula["poster_path"]
titulo = pelicula['title']  # Asumiendo que hay una columna llamada 'titulo' para el nombre de la película

# Mostrar la imagen de la película seleccionada
st.image(imagen, caption=f"Película: {titulo}", use_column_width=True)
