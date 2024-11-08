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

# Selector de ID
selected_id = st.selectbox("Selecciona el ID", df['id'].unique())

# Filtra el DataFrame según el ID seleccionado
selected_movie = df[df['id'] == selected_id].iloc[0]

url_img = f"https://image.tmdb.org/t/p/w342/{id_img}"
# Muestra los detalles de la película
st.write("### Título:", selected_movie['title'])
st.write("**Fecha de Lanzamiento:**", selected_movie['release_date'])
st.image(url_img +selected_movie['poster_path'], caption=selected_movie['title'])

