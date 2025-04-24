### Melhore o jogo do EXERCÍCIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
### Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
# ---> MINHA SOLUÇÃO:

# Utilizamos a biblioteca random e sua funcionalidade "randint" para gerar um número aleatório de 0 a 10.
from random import randint

# O computador vai gerar um número de 0 a 10 aleatoriamente:
computador = randint(0, 10)
print(computador, '<<< Resposta do computador') #Este print retorna o número aleatório que o computador escolheu.

# Vamos definir uma variável paras servir como contador das tentaivas feitas, recebendo o valor 1 pois ele será usado após a primeira tentativa do usuário:
cont = 1

print('\033[41m=\033[m' * 65)
print('\033[41m Vou pensar em um número aleatório de 0 a 10. TENTE ADIVINHAR!!! \033[m')
print('\033[41m=\033[m' * 65)
# Pedimos ao usuário para adivinhar o número:
jogador = int(input('Qual o seu palpite? '))

while jogador != computador:
    cont += 1
    if jogador < computador:
        print('\033[1;31m MAIS! TENTE NOVAMENTE!!! \033[m')
    if jogador > computador:
        print('\033[1;31m MENOS! TENTE NOVAMENTE!!! \033[m')
    jogador = int(input('Qual o seu palpite?  '))
print('\033[1;42m >>> PARABÉNS!!! RESPOSTA CORRETA!!! <<< \033[m')
print('\033[1;32m Você acertou com {} tentativas! \033[m' .format(cont))