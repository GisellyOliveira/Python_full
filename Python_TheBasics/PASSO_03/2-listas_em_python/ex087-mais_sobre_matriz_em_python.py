# Aprimore o desafio anterior, mostrando no final:                                                    
# A) A soma de todos os valores pares digitados.                                                                                                  
# B) A soma dos valores da terceira coluna.                                                                                                                
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacoluna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número para [linha {linha + 1}] [coluna {coluna + 1}]: '))
    print()

print('-' * 60)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        # A) A soma de todos os valores pares digitados.    
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print()

print('-' * 60)
print(f'A soma dos valores pares é {somapar}')

# B) A soma dos valores da terceira coluna. 
# Faremos um for para a terceira coluna somente:
for linha in range(0, 3):
    somacoluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {somacoluna}')

# C) O maior valor da segunda linha.
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maior}')
