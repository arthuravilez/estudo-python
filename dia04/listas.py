#%%

minha_lista = []
print(minha_lista)

#%%
minha_lista = ["Arthur", "Avilez", 44, 1.71]
print(minha_lista)


# %%

# primeiro elemento
minha_lista[0]

# %%

# segundo elemento
minha_lista[1]


# %%

# último elemento
minha_lista[-1]


# %%

# nova lista

nova_lista = minha_lista[:]
print(nova_lista)


# %%

# start, stop, step
minha_lista[::-1] # inversão da lista

# %%

notas = []
nota = 7.75

# mutável
notas.append(nota)

print(notas)

notas.append(10)
print(notas)

# adicionando duas notas na lista
# notas.append(5.56, 6.78) # vai dar erro, pois só aceita um único elemento

# Neste caso ficou uma lista dentro de outra lista, não é isso que queriamos
# notas.append([5.75, 6.24])
# print(notas)

notas.extend([5.75, 6.24])
print(notas)

notas = notas + [10, 9.25]
print(notas)

#%%
notas.remove(10)
print(notas)

# %%

# imutável
nome = 'arthur'
nome.upper()
print(nome)


nome = 'arthur'
nome = nome.upper()
print(nome)


# %%

nomes = ["arthur", "Maria", "João"]

for nome in nomes:
    print(nome.title())


# %%

dados = ['Arthur', 'Avilez', 44, ['Ellos', 'Nathasha', 'Billy'], ['Lucas']]
animais_estimacao = dados[3]
animais_estimacao[-1]



# %%

# Como pegar a primeira letra do nome do meu filho

dados[-1][0][0]

# %%
