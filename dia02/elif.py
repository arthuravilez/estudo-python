# %%
idade = int(input("Entre com sua idade: "))

if idade < 18:
    print("Você é menor de idade!")
    print("Vá para casa beber leite!")

elif idade > 90:
    print("Cuidade, você já tem certa idade!")

else:
    print("Você é maior de idade")
    print("Beba a vontade!")


# %%
# Como fazer uma comparação de idade entre 18 e 89 anos
if 18 <= idade <= 89:
    print("Você é maior de idade")
    print("Beba a vontade!")

elif idade >= 90:
    print("Você precisa se cuidar!!")

else:
    print("Você é uma criança, vá para casa!!!")
    
# %%
