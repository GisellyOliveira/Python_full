# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

# Para testar qual o menor número, podemos seguir o raciocício do seguinte código comentado:
'''
if n1 < n2 and n1 < n3:
    menor = a
if n2 < n3 and n2 < n1:
    menor = b
if n3 < n1 and n3 < n2:
    menor = c
'''
# Vamos eleminar um if considerando, em primeira hipótese, que o n1 seja o menor número. Desta forma, precisamos testar somente os outros dois casos, da seguinte forma:
# utilizaremos sempre CONDICIONAIS SIMPLES: 
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3 

# Utilizamos a mesma lógica para calcular o número maior:
maior = n1
if n2 > 1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

print('O menor valor digitado foi {}' .format(menor))
print('O maior valor digitado foi {}' .format(maior))