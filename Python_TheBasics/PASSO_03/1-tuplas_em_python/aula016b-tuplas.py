# Declaramos duas tuplas contendo números inteiros:
a = (2, 5, 4)
b = (5, 8, 1, 2)

# Se criarmos uma variável c que recebe a + b, o resultado será a CONCATENAÇÃO das duas tuplas:
c = a + b
print(c) # Retorna: (2, 5, 4, 5, 8, 1, 2)

# A ordem dos elementos das variáveis é respeitada durante a concatenação, e é alterado se a variável receber o valor de b + a, por exemplo:
d = b + a
print(d) # Retorna: (5, 8, 1, 2, 2, 5, 4)

# Podemos usar o "len" para contar quantos elementos estão contidos dentro da tupla:
print(len(c)) # Retorna: 7

### EXISTEM MÉTODOS INTERNOS DENTRO DAS TUPLAS, como, por exemplo: 
# O método "count()" - Aqui o utilizamos para contar quantas vezes o número 5 aparece dentro da variável c:
print(c.count(5)) # Retorna: 2
# Ou retornar 0 caso o número solicitado não estaja contido na tupla.
print(c.count(9)) # Retorna: 0

# O método "index()" - Retorna o índice dentro da tupla do número solicitado:
print(c.index(8)) # Retorna: 4
print(d.index(8)) # Retorna: 1
# Se houver a ocorrência do número solicitado mais de uma vez, ele retornará o índice do primeiro elemento encontrado:
print(d.index(5)) # Retorna: 0
print(d.index(5, 1)) # Aqui ele busca o número 5 a partir do índice 1, ignorando o número 5 que aparece no índice 0. Retorna: 5

# A funcionalidade das tuplas em outras linguagens geralmente não aceita tipos diferentes de variáveis dentro da mesma tupla.
# No Python, as tuplas podem conter tipos diferentes de dados, como strings, números, etc.
pessoa = ('Joana', 31, 'F', 65.80) 
print(pessoa)

### DEL -> As tuplas não podem ser alteradas mas podem ser completamente deletadas, sem deixar resquícios:
# É possível deletar toda a tupla, porém não é permitido deletar somente um dos itens pertencentes a uma tupla.
del(pessoa)
