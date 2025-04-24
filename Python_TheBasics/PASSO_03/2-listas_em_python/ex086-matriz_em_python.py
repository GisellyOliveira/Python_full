# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.

# Vamos declarar uma lista contendo 3 outras listas para cada uma das linahs da matriz.
# Vamos declarar valor 0 para cada um dos valores de cada linha que será somente substituído no laço mais abaixo:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a [linha {linha + 1}] [coluna {coluna + 1}]: '))

print('-' * 60)
# Este laço servirá para mostrar corretamente a matriz:
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='') # :^5 serve para determinar a apresentação de cada valor em 5 casas decimais e centralizado.
    print() # Este print serve somente para quebrar a linha toda vez que o laço terminar de ler uma linha.
