import pandas as pd
import gdown
import streamlit as st

def Cargar_CSV(id):
    # URL del archivo en Google Drive usando el ID proporcionado
    url = f'https://drive.google.com/uc?export=download&id={id}'
    output = "archivo.csv"
    
    # Descargar el archivo desde Google Drive
    gdown.download(url, output, quiet=False)
    
    # Leer el archivo CSV descargado
    df = pd.read_csv(output)
    
    return df

# ID del archivo de Google Drive
id = "1LlKcNqJA3zlbC76KvaYbIF4ZGPyEZoHy"

# Cargar el archivo CSV
df = Cargar_CSV(id)

# Mostrar las primeras 5 filas del DataFrame en Streamlit
asd = df.head(5)
st.write(asd)

