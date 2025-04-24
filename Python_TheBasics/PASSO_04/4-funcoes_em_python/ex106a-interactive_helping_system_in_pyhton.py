# Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. 
# Importante: use cores.

from time import sleep

# Lista de cores para facilitar a inserção:
listacor = ('\033[m',      #0 - sem cores
         '\033[0;30;41m',  #1 - vermelho
         '\033[0;30;42m',  #2 - verde
         '\033[0;30;43m',  #3 - amarelo
         '\033[0;30;44m',  #4 - azul
         '\033[0;30;45m',  #5 - roxo
         '\033[7;30')      #6 - branco
         

def ajuda(com):
    # Dentro da função ajuda(), vamos chamar a função titulo():
    titulo(f'Acessando o manual do comando \'{com}\'', 4) #A contrabarra \ é um caractere de escape. Ela indica que o caractere seguinte deve ser interpretado de forma especial.
    # As contrabarras antes das aspas simples dentro das chaves \' são necessárias para escapar as aspas simples dentro da string. Isso é importante para que o Python não interprete a string como tendo um final prematuro.
    # Usamos 4 para a cor azul.
    print(listacor[6], end=' ')
    help(com)
    print(listacor[0], end=' ')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4 # + 4 para dar 4 ~ a mais por questão estética.
    print(listacor[cor], end=' ')
    print('˜' * tam)
    print(f'{msg}')
    print('˜' * tam)
    print(listacor[0], end=' ')
    sleep(1)


# Programa principal:
comando = ' '
while True:
    titulo('  SISTEMA DE AJUDA PyHELP', 2) #1 para cor vermelha
    comando = str(input('Digite a função ou biblioteca ou "FIM" para sair: '))
    if comando.upper() == 'FIM': #upper() converte aqui em maiúsculo o input da variável comando.
        break
    else:
        ajuda(comando)

titulo('  ATÉ LOGO!', 1)
