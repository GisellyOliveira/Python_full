# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# Utilizamos a biblioteca random e sua funcionalidade "randint" para gerar um número aleatório de 0 a 10.
from random import randint

# Apresentação
titulo = '\033[1;41m >>> VAMOS JOGAR PAR OU ÍMPAR?! <<< \033[m'
print('-' * 36)
print(f'{titulo:^40}')
print('-' * 36)

# Inicializa contador para as vitórias:
v = 0
while True:
    jogador = int(input('\033[1;41m Escolha um número: \033[m'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = 'm'
    while tipo not in 'PI':
        tipo = str(input('\033[41m PAR ou ÍMPAR?[P/I] \033[m')).strip().upper()[0]
    print(f'\033[47m Você jogou {jogador}, o computador jogou {computador} e o total foi {total}. \033[m', end='')
    print('\033[47m DEU PAR \033[m' if total % 2 == 0 else '\033[1;47m DEU ÍMPAR \033[m')
    # Um if dentro do outro para duas condiçoes:
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[1;42m VOCÊ VENCEU!!! \033[m')
            v += 1
        else:
            print('\033[1;41m VOCÊ PERDEU!!! \033[m')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('\033[1;42m VOCÊ VENCEU!!! \033[m')
            v += 1
        else:
            print('\033[1;41m VOCÊ PERDEU!!! \033[m')
            break
    print('\033[1;47m Vamos jogar novamente... \033[m')
print(f'\033[1;47m GAME OVER! Você venceu {v} vezes! \033[m')

