# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# Resolução n.2:importando somente a propriedade 'trunc' da biblioteca math para a segunda resolução:
from math import trunc

num = float(input('Digite um número: '))
# Resolução n.2: utilizando a propriedade 'trunc' porém fazendo as alterações necessárias já que somente a propriedade for importada da biblioteca.:
print('O valor digitado foi {} e a sua porção inteira é {}.' .format(num, trunc(num)))