import pandas as pd
import requests
from io import BytesIO
import streamlit as st

# Enlace directo de descarga de Google Drive
url = "https://drive.google.com/uc?export=download&id=1LlKcNqJA3zlbC76KvaYbIF4ZGPyEZoHy"
response = requests.get(url)

# Leer el archivo CSV desde la respuesta
df = pd.read_csv(BytesIO(response.content))

# Mostrar las primeras 5 filas en Streamlit
st.write(df.head(5))

