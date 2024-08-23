import requests
import pandas as pd
from io import BytesIO

url = "https://raw.githubusercontent.com/tomonori-masui/entity-resolution/main/data/musicbrainz_200k.csv"
data = requests.get(url)
df = pd.read_csv(BytesIO(data.content))

print(df.head())