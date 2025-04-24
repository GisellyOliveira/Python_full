# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número inteiro: '))
#Para descobrir se é par ou impar, calculamos o resto da divisão por 2. Se sobrar 1, é impar. Se sobrar 0, é par.
resultado = num % 2

if resultado == 0:
    print('O número {} é par.' .format(num))
else:
    print('O número {} é ímpar.' .format(num))