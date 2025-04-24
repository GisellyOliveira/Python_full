# Oeradores de igualdade

variavel_um = 1
variavel_dois = 2
variavel_tres = 3

print(1 == variavel_um)
print(2 == variavel_um)

equal = (variavel_um == variavel_dois)
print(equal)

not_equal = (variavel_um != variavel_dois)
print(not_equal)

print("Um é igual a dois? " + str(equal))
print("Um é diferente de dois? " + str(not_equal))


# Operadores lógicos and (e) e or (ou)
### Operador AND
teste1 = ((2 > 1) and (3 < 5))
print(("2 é maior que 1 E também 3 é menor que 5? ") + str(teste1))

teste2 = ((2 > 1) and (1 > 3))
print("2 é maior que 1 E também 1 é maior que 3? " + str(teste2))

### Operador OR
teste3 = ((3 < 5) or (2 > 1))
print("3 é menor que 5 OU 2 maior que 1? " + str(teste3))

teste4 = ((0 > 1) or (0 == -1))
print("0 é maior que 1 OU 0 é igual a -1? " + str(teste4))

teste5 = ((0 > 1) or (0 == -1))
print("0 é maior que 1 OU 0 é igual a -1? " + str(teste5))