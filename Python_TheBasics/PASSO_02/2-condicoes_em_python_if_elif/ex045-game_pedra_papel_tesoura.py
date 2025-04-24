# Crie um programa que faça o computador jogar Jokenpô com você.
# Vamos utilizar a biblioteca 'random' para o computador escolher uma das opções a jogar.
from random import randint
# Vamos importar a funcionalidade 'sleep' da biblioteca 'time' para anunciar pausadamente as sílabas JO, KEN e PÔ antes do resultado:
from time import sleep

itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)

print('{:=^40}'.format('\033[1;45m JOKENPÔ \033[m'))
print(('{:^40}'.format('\033[1;46m SUAS OPÇÕES \033[m')))
print('''[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('\033[1;37m Qual é a sua jogada? \033[m'))

print('{:^40}'.format('\033[1;41m JO \033[m'))
sleep(1)
print('{:^40}'.format('\033[1;41m KEN \033[m'))
sleep(1)
print('{:^40}'.format('\033[1;41m PÔ! \033[m'))
sleep(1)

print('*' * 40)
print('O computador jogou {}' .format(itens[computador]))
print('O jogador jogou {}' .format(itens[jogador]))
print('*' * 40)

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('{:^40}'.format('\033[1;43m EMPATE \033[m'))
    elif jogador == 1:
        print('{:^40}'.format('\033[1;42m JOGADOR VENCE \033[m'))
    elif jogador == 2:
        print('{:^40}'.format('\033[1;44m COMPUTADOR VENCE \033[m'))
    else:
        print('{:^40}'.format('\033[1;41m JOGADA INVÁLIDA! \033[m'))
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('{:^40}'.format('\033[1;44m COMPUTADOR VENCE \033[m'))
    elif jogador == 1:
        print('{:^40}'.format('\033[1;43m EMPATE \033[m'))
    elif jogador == 2:
        print('{:^40}'.format('\033[1;42m JOGADOR VENCE \033[m'))
    else:
        print('{:^40}'.format('\033[1;41m JOGADA INVÁLIDA! \033[m'))
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('{:^40}'.format('\033[1;42m JOGADOR VENCE \033[m'))
    elif jogador == 1:
        print('{:^40}'.format('\033[1;44m COMPUTADOR VENCE \033[m'))
    elif jogador == 2:
        print('{:^40}'.format('\033[1;43m EMPATE \033[m'))
    else:
        print('{:^40}'.format('\033[1;41m JOGADA INVÁLIDA! \033[m'))
