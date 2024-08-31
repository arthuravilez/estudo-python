#%%

dados = ["Arthur", "Avilez", 31] # lista
nome = dados[0]

# %%
dados = { "nome": "Arthur", 
          "sobrenome": "Avilez", 
          "idade": 44,
          "animais": ["Ellus", "Natasha", "Billy"],
          "filhos": [ { "nome": "Lucas", "idade": 11 }, { "nome": "Rafael", "idade": 1 }  ]
        }

dados["filhos"][0]["idade"]


# %%

dados.keys()


# %%

dados.values()


# %%

dados.items()

# %%
