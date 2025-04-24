# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), 
       int(input('Digite mais um número: ')), int(input('Digite o último número: ')))

print(f'VOcê digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes') # Utiliza o "count"para contar quantas vezes o caractere aparece

# A solução abaixo quebra o código quando não recebe nenhum número 3.
# print(f'O número 3 apareceu na {num.index(3) + 1}ª  posição.') # O método index aponta o índice.
# Solucionamos com uma condicional:
if 3 in num:
    print(f'O valor 3 foi digitado na {num.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado nenhuma vez.')

print('Os valores pares digitados foram:', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
        