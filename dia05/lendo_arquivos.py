#%% 

# O "w" reescreve coisas e o "a" ele adiciona novas coisas
arquivo = open("arquivo.txt", "w")

arquivo.write("Que legal, estou escrevendo!!!!")

# Fechando o arquivo
arquivo.close()

# %%

# lendo um arquivo

arquivo = open("arquivo.txt", "r")
conteudo = arquivo.read()
arquivo.close()

print(conteudo)


# %%

arquivo = open("arquivo.txt", "r")
linhas = arquivo.readlines()
arquivo.close()

print(linhas)

# %%

with open("arquivo.txt", "r") as file:
    conteudo = file.read()

print(conteudo)


# %%
