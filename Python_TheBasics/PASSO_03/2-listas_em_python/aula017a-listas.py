num  = [2, 5, 9, 1]
# Substitui o elemento do índice 2 ('9') pelo '3'
num[2] = 3
print(num) # [2, 5, 3, 1]

# Adicionando novos elementos e índices:
num.append(7) 
print(num) # [2, 5, 3, 1, 7]

# Organiza números em forma crescente:
num.sort() 
print(num) # [1, 2, 3, 5, 7]

# Organiza números em forma decrescente:
num.sort(reverse=True) 
print(num) # [7, 5, 3, 2, 1]

# Inseri um número num determinado índice (inseri no índice 2 o número 0):
num.insert(2, 0) 
print(num) # [7, 5, 0, 3, 2, 1]

# Remove o último elemento:
num.pop()
print(num) # [7, 5, 0, 3, 2]

# Remove o elemento no índice 2:
num.pop(2)
print(num) # [7, 5, 3, 2]

# Vamos inserir um número repetido dentro da lista:
num.insert(2, 2)
print(num) # [7, 5, 2, 3, 2]

# Vamos remover o número 2, porém o método remove() vai capturar o que aparece primeiro, ou seja, no menor índice:
num.remove(2)
print(num) # [7, 5, 3, 2]

# Se pedirmos a remoção de um elemento não existente, temos um erro.
# Vamos utilizar um laço para evitar quebras no código utilizando o método remove():
# Removendo o número caso da lista, caso exista:
if 4 in num:
    num.remove(4)
else:
    print('Não foi possível a remoção. O número não existe.')

# Retorna a quantidade de elementos dentro de uma lista:
print(f'Essa lista tem {len(num)} elementos')