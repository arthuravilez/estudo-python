#%%

numero_sorte = 7

for i in range(3):

    while True:
        try:
            numero = int(input("Entre com um número de 1 e 15: "))
            break
        except ValueError:
            print("Favor digitar somente um número!!!")

    if numero == numero_sorte:
        print("Você acertou!!")
        break
    elif numero > numero_sorte:
        print("Você errou! Tente um número menor!")
    else:
        print("Você errou! Tente um número maior")


# %%
