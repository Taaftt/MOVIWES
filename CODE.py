#puede:
#buscar peliculas por generos - actores
#hacer listas de peliculas q ya viste / quieres ver
#dejar reseñas de peliculas y ver las reseñas de otras personas
#poner donde se puede ver cada pelicula
#poner el trailer, sinopsis y promedio de reseñas
#en google un wn tenia una forma de poner archivos grandes en github no me acuerdo como era

import requests
import pandas as pd
import streamlit as st
from io import StringIO

# Función para descargar el archivo CSV desde Google Drive
def csv_drive(file_id):
    # Construir la URL de descarga directa
    url = f'https://drive.google.com/uc?export=download&id={file_id}'
    # Realizar la solicitud HTTP
    response = requests.get(url)
    # Usamos StringIO para tratar el contenido como archivo en memoria
    csv_content = StringIO(response.text)
    # Intentar leer el archivo CSV en un DataFrame
    df = pd.read_csv(csv_content, sep=',',encoding='ISO-8859-1',engine='python', on_bad_lines='skip').fillna(0)
    return df
  st.write(df)

# Diccionario de ID de archivo de Google Drive y nombres de archivo
file = {
    "1LlKcNqJA3zlbC76KvaYbIF4ZGPyEZoHy": "movie.csv",
}

# Iterar sobre el diccionario de enlaces
for file_id, file_name in file.items():
    # Descargar y leer el CSV en un DataFrame
    df = csv_drive(file_id)
    st.write(df)