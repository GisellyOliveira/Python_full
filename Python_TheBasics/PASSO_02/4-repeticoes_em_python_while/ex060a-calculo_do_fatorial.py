# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

### PRIMEIRA SOLUÇÃO USANDO A BOBLIOTECA MATH:
# Usaremos a biblioteca math e o módulo math para calcular o fatorial
from math import factorial

print('\033[41;1m >>> PRIMEIRA SOLUÇÃO: <<< \033[m')
num = int(input('Insira um número para o cálculo fatorial: '))
# Atribuímos o resultado fatorial utilizado com o módulo "factorial" a variável "f"
fat = factorial(num)
print('O fatorial de {} é {}.' .format(num, fat))

### SEGUNDA SOLUÇÃO USANDO WHILE E CONDICIONAIS:
# Vamos porem apresentar esse simples exercício de uma forma diferente, utilizando a estrutura while:
print('\033[41;1m >>> SEGUNDA SOLUÇÃO: <<< \033[m')
n = int(input('Insira um número para o cálculo fatorial: '))
c = n
# Variável f recebe 1 para multiplicar pelos valores e retornar ele mesmo.
f = 1
print('Calculando {}! = ' .format(n), end='')
while c > 0:
    print('{}' .format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    # Para múltiplicar cada um dos valores cada vez que o contador contar um deles.
    f *= c   # É o mesmo que: f = f * c 
    # Para fazer a contagem regressiva dos valores até 1.
    c -= 1    #O mesmo que: c = c - 1
print('{}' .format(f))

### TERCEIRA SOLUÇÃO COMO SUGERIDA NA AULA: REFAZER O CÓDIGO ANTERIOR UTILIZANDO O "FOR"
print('\033[41;1m >>> TERCEIRA SOLUÇÃO: <<< \033[m')
numero = int(input('Insira um número para o cálculo fatorial: '))
resultado = 1
print('Calculando {}! = ' .format(numero), end='')
for d in range (1, numero+1):
    resultado *= d
    if d > 0:
        print('{}' .format(d), end='')
        print(' x ' if d < numero else ' = ', end='')

print(resultado)
