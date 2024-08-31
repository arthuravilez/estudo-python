# %%

# Isso é uma função na matemática, podemos fazer a mesma coisa com funções em python

# y = f(x) = x + 10

# x = 0  -> y = 10
# x = 1  -> y = 11
# x = 10 -> y = 20

# -----------

# y = f(x) = x * x + 1

# x = 0 -> y = 1
# x = 1 -> y = 2
# x = 2 -> y = 5

#%% 
def funcao(x):
    res = x + 10
    return res

y = funcao(10)
print(y)

# %%

def teste():
    print("Que legal!!")

teste()
# %%

# nesta funcao os argumento a está como obrigatório
# e o b está como default
def soma(a, b = 0): 
    return a + b

print(soma(10))

print(soma(10, 20))

# %%


