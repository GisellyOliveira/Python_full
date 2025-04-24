# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# O randint vai gerar um número aleatório, mas será necessário verificar que não haja duplicatas.
from random import randint
from time import sleep

lista = []
jogos = [] # Vai receber os 6 números aleatórios da lista.

# Apresentação:
print('-' * 60)
print(f'{'>>> GERADOR DE JOGOS DA MEGA-SENA <<<':^60}')
print('-' * 60)

quant = int(input('Quantos jogos você quer sortear? '))
tot = 1 # total de vezes que será sorteado
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        # Verificando que o número não se repita na lista.
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort() # Organiza a lista em ordem crescente.
    jogos.append(lista[:]) # Faz a cópia dos números aleatórios da lista para dentro da lista jogos.
    lista.clear() # reseta os dados da lista.
    tot += 1 # Para não entrar em loop infinito.
# Apresentação do resultado:
print('-=' * 3, f'>>> SORTEANDO {quant} JOGOS <<<', '-=' * 3)
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice + 1}: {lista}')
    sleep(1) # Para dar uma pausa de 1 seg antes de apresentar o próximo laço.

print('-=' * 5, '> BOA SORTE! >', '-=' * 5)
