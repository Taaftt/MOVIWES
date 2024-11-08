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

asd =df.head(10)
st.write(asd)

"""
# ID de la película seleccionada
pelicula_id = 299536

# Filtrar la película seleccionada
pelicula_seleccionada = df[df["id"] == pelicula_id].iloc[0]

# Construir la URL de la imagen usando el backdrop_path de la película seleccionada
id_img = pelicula_seleccionada["backdrop_path"]
"""
id_img = "/vL5LR6WdxWPjLPFRLe133jXWsh5.jpg"
url_img = f"https://image.tmdb.org/t/p/w342/{id_img}"

# Mostrar la imagen de la película seleccionada
st.image(url_img, caption="Imagen de la película seleccionada")
"""
