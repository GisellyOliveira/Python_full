### Melhore o jogo do EXERCÍCIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
### Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
# ---> SOLUÇÃO DO PROFESSOR:

# Utilizamos a biblioteca random e sua funcionalidade "randint" para gerar um número aleatório de 0 a 10.
from random import randint

# O computador vai gerar um número de 0 a 10 aleatoriamente:
computador = randint(0, 10)
print(computador, '<<< Resposta do computador') #Este print retorna o número aleatório que o computador escolheu.

# Apresentação:
print('\033[41m=\033[m' * 66)
print('\033[41m Sou seu computador... e acabei de pensar em um número de 0 a 10. \033[m')
print('\033[41m >>>>>>>>>> SERÁ QUE VOCÊ CONSEGUE ADIVINHAR QUAL FOI? <<<<<<<<<< \033[m')
print('\033[41m=\033[m' * 66)

# Vamos definir uma variavel chamada "acertou" que contêm o valor "False" para ser usada nas respostas erradas do usuário:
acertou = False
# Definimos também a variável "palpites" para servir cmo contador das tentaivas do usuário:
palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[1;31m MAIS!!! Tente novamente! \033[m')
        elif jogador > computador:
            print('\033[1;31m MENOS!!! Tente novamente! \033[m')
print('\033[1;32m >>> Você acertou com {} tentativas. PARABÉNS! <<< \033[m]' .format(palpites))
