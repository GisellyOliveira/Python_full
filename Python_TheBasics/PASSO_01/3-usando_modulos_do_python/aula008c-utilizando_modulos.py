#Explorando a biblioteca ramdom:
#   Ela gera um número float aleatório entre 0 e 1.

import random

num = random.random()
print('O número aleatório float entre 0 e 1 gerado é {}' .format(num))

# Se quisermos gerar um número aleatório entre 1 e 10, por exemplo, podemos utilizar a propriedade do random chamada randint, que gera um número aleatório inteiro entre os números passados como parâmetros. Exemplo:
num = random.randint(1, 10)
print('O número aleatório entre 1 e 10 gerado é: {}' .format(num))