# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Importaremos a funcionalidade "randint" da biblioteca "random" para gerar um número inteiro de 0 a 5:
from random import randint
# Também importaremos a funcionalidade "time" do módulo "sleep" que faz com que possamos impostar alguns segundos de espera antes de mostrar o resultado:
from time import sleep

# O programa vai gerar um número de 0 a 5 aleatoriamente: 
computador = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número aleatório de 0 a 5. Tente adivinhar!')
print('-=-' * 20)

# Perguntamos ao usuário para descobrir o número escolhido:
jogador = int(input('Qual número eu pensei? '))

# Vamos inserir a funcionalidade "time" do módulo "sleep" para que passe 2 segundos antes de mostrar o próximo resultado:
print('PROCESSANDO...')
sleep(2)

# Usaremos a condicional para definir se o usuário acertou o número que o computador selecionou aleatoriamente:
if jogador == computador:
    print('O número escolhido foi "{}" \nPARABÉNS! Vcê conseguiu me vencer!' .format(computador))
else:
    print('O número escolhido foi "{}" \nGanhei! Tente novamente!' .format(computador))

# Usaremos também a condicional simplificada:
print('PARABÉNS!!!' if jogador == computador else 'TENTE NOVAMENTE!!!')

