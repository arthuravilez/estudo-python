# Faça um programa que verifique se o item que a pessoa escolheu 
# para comprar na loja está na lista: laranja, cerveja, miojo, carvão, picanha

#%%
item = input("Digite o que quer comprar?  [laranja, cerveja, miojo, carvão, picanha] ")

lista = "laranja, cerveja, miojo, carvão, picanha"


if item in lista:
    print("Que legal! Pode se dirigir ao caixa!")
else:
    print("Ops! Estamos em falta desse item!!!")


# %%
