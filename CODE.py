import pandas as pd
import gdown
import streamlit as st
def Cargar_CSV(id_url):
  #Link del df del google drive
  url = f'https://drive.google.com/uc?export=download&id={id_url}'
  output = "archivo.csv"
  
  #Descargar nuestro drive con gdown
  gdown.download(url, output, quiet=False)

  #Leer el drive
  Lectura = pd.read_csv(output)
  return lectura

df = Cargar_CSV("1LlKcNqJA3zlbC76KvaYbIF4ZGPyEZoHy")


# Mostrar las primeras 5 filas en Streamlit
st.write(df.head(5))

