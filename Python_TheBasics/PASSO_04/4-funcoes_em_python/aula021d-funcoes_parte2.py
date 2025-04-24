### RETORNANDO VALORES: ###
# O return dentro da função retornará um valor que precisará ser guardada dentro de uma variável ou passada diretamente dentro de um print.
# Exemplo 1 - retornando resultados dentro de uma variável:

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

resultado1 = somar(3, 2, 5)
resultado2 = somar(1, 7)
resultado3 = somar(4)
print(f'Meus cálculos deram {resultado1}, {resultado2} e {resultado3}.')

# Exemplo 2 - retornando resultados dentro de um print:

def subtrair(d=0, e=0, f=0):
    t = d + e + f
    return t

print(subtrair(10, 2, 5))