import pandas as pd
import gdown
import streamlit as st

def Cargar_CSV(id_url):
    # Link del archivo de Google Drive
    url = f'https://drive.google.com/uc?export=download&id={id_url}'
    output = "archivo.csv"
    
    # Descargar el archivo de Google Drive con gdown
    gdown.download(url, output, quiet=False)
    
    # Leer el archivo CSV descargado
    df = pd.read_csv(output)
    return df

# Cargar el archivo CSV con el ID proporcionado
a = Cargar_CSV("1LlKcNqJA3zlbC76KvaYbIF4ZGPyEZoHy")

# Mostrar las primeras 5 filas del DataFrame en Streamlit
asd = a.head(5)
st.write(asd)
