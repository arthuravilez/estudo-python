# %%
# Números
# 1
# 10.0
# -5
# -7.54

# Booleanos
True
False

idade = 18 > 30
print(idade)

# %%

idade = int(input("Entre com sua idade: "))
cnh = input("Você tem CNH? ")

if idade >= 18 and cnh == "sim":
    print("Siga em frente")

else:
    print("Preso em nome da lei!")

# %%
# Tabela verdade de duas condições usando AND
print("True AND True =   ",   bool(1 * 1))
print("False AND True =  ",   bool(0 * 1))
print("True AND False =  ",   bool(1 * 0))
print("False AND False = ",   bool(0 * 0))


# %%
# Tabela verdade usando 2 condições OR
print("True OR True =   ",   bool(1 + 1))
print("False OR True =  ",   bool(0 + 1))
print("True OR False =  ",   bool(1 + 0))
print("False OR False = ",   bool(0 + 0))

# %%
