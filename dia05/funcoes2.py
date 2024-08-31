# %%

def soma(a=0, b=0, c=0):
    return a + b + c

soma(10, 20, 100)

# %%

# *args
def somaN(*args):
    total = 0 

    for i in args:
        total += i
    return total

somaN(10, 20, 100)

# %%

def operacao(op, *num):
    total = 0

    if op == "soma":
        for i in num:
            total += i

    elif op == "mult":
        total = 1
        for i in num:
            total *= i
    return total

operacao("soma", 20, 50)
operacao("mult", 5, 5)


# %%

dados = ["Arthur", "Avilez", [1,2,3,4,5], [6,7,8,9]]

# nome = dados[0]
# sobrenome = dados[1]

# print(nome)
# print(sobrenome)

# unpack
nome, sobrenome, *_, final = dados

print(nome)
print(sobrenome)
print(final)



# %%

a = 10
b = 20

# Em outra linguagem para trocar o valor de a pelo de b é assim:
# c = a
# a = b
# b = c

# no python pode ser feito dessa maneira

a, b = b, a
print(a, b)


# %%
