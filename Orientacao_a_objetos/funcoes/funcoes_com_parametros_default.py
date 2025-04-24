# Funções com parâmetros default (padrão)

def multiplica(a, b=2):
    return a * b

print(multiplica(5, 84)) # retorna 420

# como b tem um valor padrão, podemos passar apenas um argumento
print(multiplica(7))  # retorna 14
