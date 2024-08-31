#%%

# Código espaguete, é o código que faz uma dança na sua tela, vai e volta

def valida_entrada():
    while True:
        try:
            numero = int(input("Entre com um número de 1 e 15: "))
            
        except ValueError:
            print("Favor digitar somente um número!!!")
            continue
        
        if 1 <= numero <= 15:
            return numero
        
        else:
            print("Entre com um número válido")


numero_sorte = 7

for i in range(3):

    numero = valida_entrada()

    if numero == numero_sorte:
        print("Você acertou!!")
        break
    elif numero > numero_sorte:
        print("Você errou! Tente um número menor!")
    else:
        print("Você errou! Tente um número maior")


# %%
