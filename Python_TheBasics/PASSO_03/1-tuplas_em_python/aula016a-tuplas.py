# Até o python 3.5, são usadas () para as tuplas, [] para as listas e {} para os dicionários:
# Mas tbm podemos remover os parênteses (vamos utilizar parênteses por questões didáticas):
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
print(lanche) # Retorna todos os itens da tupla: ('Hamburger', 'Suco', 'Pizza', 'Pudim')
print(lanche[1]) # Retorna o elemento no índice 1: 'Suco'
print(lanche[-2]) # retorna o penúltimo item: 'Pizza'
print(lanche[1:3]) # Retorna elemento 1 e 2 (não mostra o índice 3): ('Suco', 'Pizza')
print(lanche[2:]) # Retorna do elemento 2 até o final: ('Pizza', 'Pudim')
print(lanche[:2]) # Do início até o elemento 2, sendo que o elemento 2 não é retornado: ('Hamburger', 'Suco')
print(lanche[-2:]) # Inicia do penúltimo elemento e vai até o último: ('Pizza', 'Pudim')
print(lanche[-3:]) # Retorna do antepenúltimo elemento até o último: ('Suco', 'Pizza', 'Pudim')

print('-' * 50)
##########################################################
### Apresentação no console utilizando fstrings dentro de um laço de repetição:
# As vezes é necessário utilizar um modelo de laço, e outras vezes é necessário utilizar um segundo modelo. Vejamos ambos:
# Exemplo 1:
for comida in lanche:
    print(f'Eu vou comer {comida}.')
# Retorna:
''' 
Eu vou comer Hamburger.
Eu vou comer Suco.
Eu vou comer Pizza.
Eu vou comer Pudim.
'''

print('-' * 50)
# Exemplo 2:
# Este modelo, porém, não retorna o índice do elemento. Para isso, podemos utilizar alternativamente o "enumerate" para dar número aos índices:
# "pos" retona a posição.
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer o/a {comida} do índice {pos}')
# Retorna:
'''
Eu vou comer o/a Hamburger do índice 0
Eu vou comer o/a Suco do índice 1
Eu vou comer o/a Pizza do índice 2
Eu vou comer o/a Pudim do índice 3
'''

print('-' * 50)
# Exemplo 3:
for cont in range(0, len(lanche)):
    print(cont) # Retorna: 0, 1, 2, 3 e 4.
    print(lanche[cont], cont) # A cada loop retorna o lanche no índice do contador:
# Retorna:
'''
0
Hamburger
1
Suco
2
Pizza
3
Pudim
Comi pra caramba!
'''
##########################################################

print('-' * 50)
# Utilizando o len:
print(len(lanche), '<--- Número de elementos dentro da tupla utilizando "len"') # Retorna 4, que é o número de elementos dentro da tupla.

##########################################################
### TUPLAS SÃO IMUTÁVEIS ###
# lanche[1] = 'Refrigerante'
# print(lanche[1])
# O comando acima não poderá ser executado substituindo o valor de 'Suco' por 'Refrigerante'
##########################################################

print('-' * 50)
# Utilizando o "sorted" para reorganizar a ordem os elementos dentro de uma lista []:
print(sorted(lanche))
# Retorna:
'''
['Hamburger', 'Pizza', 'Pudim', 'Suco']
'''


