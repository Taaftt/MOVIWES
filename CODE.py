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


