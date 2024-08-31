#%%
import requests
import pandas as pd

url = "https://api.opendota.com/api/heroes"

resposta = requests.get(url)

# %%
resposta.status_code

# %%
dados = resposta.json()
dados


# %%
dados[0]

# %%
for i in dados:
    print(i['localized_name'])

# %%

df = pd.DataFrame(dados)

# %%

df.to_csv("heores_dota.csv", sep=";")


# %%
