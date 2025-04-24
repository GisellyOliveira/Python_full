# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# Resolução n.3:utilizando a função int sem nenhuma necessidade de importar nenhuma biblioteca.
num = float(input('Digite um número: '))
# Resolução n.3: utilizando a 'int'para converter o número float em inteiro na tela.
print('O valor digitado foi {} e a sua porção inteira é {}.' .format(num, int(num)))