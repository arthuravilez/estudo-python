# %%

# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50
# Altere o programa anterior para considerar a quantidade de água

escolha = input("Você gostaria de uma garrafa de água mineral ou com gás? [mineral/gas: ]")
litros = int(input("E quantos litros vai querer de água? [1, 2, ...]"))

mineral = 1.50
gas = 2.50
total = 0

if escolha == "mineral":
    total = litros * mineral

elif escolha == "gas":
    total = litros * gas
    
else:
    print("Faça uma escolha válida!!!")

print("Você me deve R$", total)

# %%
