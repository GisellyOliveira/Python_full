# Aqui vamos criar uma lista vazia:
valores = [] # OU: valores  = list()

# Adicionamos alguns valores com o método append()
valores.append(5)
valores.append(9)
valores.append(4)

# E vamos utilizar um laço para mostrar os valores:
for v in valores:
    print(f'{v}...', end='')

print('-' * 50)
# Se quiséssemos verificar também o índice, podemos utilizar mais um contador para o índice utilizando o módulo enumerate():
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

print('-' * 50)
# Ler valores pelo teclado e colocar dentro da lista:
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores) # [5, 9, 4, 4, 7, 0, 8, 1]
# Aqui ele adicionou os valores inseridos pelo teclado à lista.

print('-' * 50)
# LIGAÇÃO ENTRE LISTAS:
# Declaramos uma lista a com 4 valores:
a = [2, 3, 4, 7]
print(f'Essa é a lista A: {a}')
b = a
print((f'Essa é a lista B: {b}'))
# Quando b recebe os valores de a, estabelece uma ligação recíproca entre ambas as listas.
# Se alterarmos um valor num determinado índice de b, veremos que a também será altomaticamente alterada.
b[2] = 8
print(f'Esta é a lista B após receber o valor 8 no índice 2: {b}')
print(f'Essa é a lista A depois que a B foi alterada: {a}')

print('-' * 50)
# COPIAR LISTAS:
# Para fazer uma cópia de uma lista sem estabelecer a ligação anterior, devemos passar como parâmetro em colchetes os valores que esta receberá:
c = [4, 6, 1, 0]
print(f'Essa é a lista C: {c}')
d = c[:] # Fatiamento de string: passamos dois pontos para pegar todos os valores da lista.
print(f'Essa é a lista D: {d}, que é uma cópia da lista C.')
d[2] = 5
print(f'Esta é a lista D após receber o valor 5 no índice 2: {d}')
print(f'Essa é a lista C depois que a D foi alterada: {c}')
