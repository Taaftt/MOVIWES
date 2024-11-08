import pandas as pd
import gdown
import streamlit as st

# Enlace directo de Google Drive
url = "https://drive.google.com/uc?export=download&id=1LlKcNqJA3zlbC76KvaYbIF4ZGPyEZoHy"

# Descargar el archivo usando gdown
output = 'archivo.csv'
gdown.download(url, output, quiet=False)

# Leer el archivo CSV
df = pd.read_csv(output)

# Mostrar las primeras 5 filas en Streamlit
st.write(df.head(5))

