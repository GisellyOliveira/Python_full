numero = int(input('Fatorial de: '))

prod = 1
for c in range (1, numero+1):
    prod = prod * c
    print(prod)
print('{}! = {}' .format(numero, prod))