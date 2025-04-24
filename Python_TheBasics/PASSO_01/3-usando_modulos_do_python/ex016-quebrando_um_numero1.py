# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# Resolução n.1: importando a biblioteca math para utilizar a propriedade 'trunc' para truncar o número como primeira alternativa:
import math

num = float(input('Digite um número: '))
# Resolução n.1: utilizando a propriedade 'trunc' da boblioteca math para a primeira resolução:
print('O valor digitado foi {} e a sua porção inteira é {}.' .format(num, math.trunc(num) ))