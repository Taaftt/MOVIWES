import pandas as pd
import gdown
import streamlit as st

#ID del drive
id ="1LlKcNqJA3zlbC76KvaYbIF4ZGPyEZoHy"
url = f'https://drive.google.com/uc?export=download&id={id_url}'
output = "archivo.csv"
    
# Descargar el archivo de Google Drive con gdown
gdown.download(url, output, quiet=False)
    
# Leer el archivo CSV descargado
df = pd.read_csv(output)


# Mostrar las primeras 5 filas del DataFrame en Streamlit
asd = df.head(5)
st.write(asd)

