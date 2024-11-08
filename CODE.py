import pandas as pd
import gdown
import streamlit as st

# URL directa del archivo en Google Drive
url = "https://drive.google.com/uc?export=download&id=1LlKcNqJA3zlbC76KvaYbIF4ZGPyEZoHy"

# Descargamos el archivo usando gdown
output = 'archivo.csv'
gdown.download(url, output, quiet=False)

# Leemos el archivo CSV
df = pd.read_csv(output)

# Mostramos las primeras 5 filas en Streamlit
st.write(df.head())
