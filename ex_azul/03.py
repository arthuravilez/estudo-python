# %%

# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

escolha_tipo_sorvete = input("Escolha o tipo do sorvete: casquinha, cascão, cestinha: ")
escolha_sabor = input("Escolha o sabor: morango, creme, chocolate: ")
escolha_cobertura = input("Escolha a cobertura: caramelo, morango, chocolate, sem_cobertura: ")


tipo_sorvete = {
    "casquinha": 1.00,
    "cascão": 2.50,
    "cestinha": 4.00 
    }

sabor_sorvete = {
    "morango": 0.00, 
    "creme": 0.00,
    "chocolate": 0.00
}

cobertura = {
    "caramelo": 1.50,
    "morango": 1.50,
    "chocolate": 1.50,
    "sem_cobertura": 0.00
}


total = float(tipo_sorvete[escolha_tipo_sorvete]) + \
        float(sabor_sorvete[escolha_sabor]) + \
        float(cobertura[escolha_cobertura])


print("Seu sorvete é :" \
      "\n ----------------------------" \
    "\n tipo: ", escolha_tipo_sorvete, "R$", tipo_sorvete[escolha_tipo_sorvete], \
    "\n sabor: ",  escolha_sabor, "R$", sabor_sorvete[escolha_sabor], \
    "\n cobertura: ", escolha_cobertura, "R$", cobertura[escolha_cobertura], \
    "\n ----------------------------"
    "\n O valor a ser pago é: R$",total
    )


 # %%
