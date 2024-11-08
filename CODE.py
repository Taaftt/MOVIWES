import pandas as pd
import requests
from io import BytesIO

# Reemplaza la URL con el enlace de descarga directo de Google Drive
url = "https://drive.google.com/uc?export=download&id=1LlKcNqJA3zlbC76KvaYbIF4ZGPyEZoHy"
response = requests.get(url)
df = pd.read_csv(BytesIO(response.content))
ol= df.head(5)
st.write(ol)
