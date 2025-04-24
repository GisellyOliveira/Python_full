# Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. 
# Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas) # Retorna: {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# Não podemos utilizar o número do índice como nos listas:
print(pessoas['nome']) # Retorna: Gustavo
print(pessoas['idade']) # Retorna: 22

# Quando utilizamos fstrings, o valor das chaves precisam ser passadas entre aspas duplas " ", pois a fstring já inicia e termina com aspas simples.
# Na hora de referenciar os elementos dentro do dicionário usamos aspas simples. Quando chamamos o elemento, usamos aspas duplas. 
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') # Retorna: O Gustavo tem 22 anos.

# Retornando as chaves, valores e itens:
print(pessoas.keys()) # Retorna: dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values()) # Retorna: dict_values(['Gustavo', 'M', 22])
# Retorna uma lista com 3 tuplas:
print(pessoas.items()) # Retorna: dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])

# Acessar as chaves:
for k in pessoas.keys():
    print(k)
# Retorna: nome     sexo        idade

# Acessar os valores por chaves:
for k in pessoas.values():
    print(k)
# Retorna: Gustavo  M   22

# Acessar os items - é necessário passar um contador para as chaves (k) e valores (v):
# O "enumerate" não é utilizado.
for k, v in pessoas.items():
    print(f'{k} = {v}') # Retorna: nome = Gustavo   sexo = M    sexo = M
                                
# Deletando um item pela chave:
del pessoas['sexo'] 
print(pessoas) # Retorna: {'nome': 'Gustavo', 'idade': 22}

# Modificando o valor de uma chave:
pessoas['nome'] = 'Leandro'
print(pessoas) # Retorna: {'nome': 'Leandro', 'idade': 22}

# Adicionando um novo elemento - não se utiliza o append():
pessoas['sexo'] = 'M'
pessoas['peso'] = 98.5
print(pessoas) # Retorna: {'nome': 'Leandro', 'idade': 22, 'sexo': 'M', 'peso': 98.5}

# Criando um dicionário dentro de uma lista:
# Vamos criar uma lista chamada "Brasil" que vai receber os dicionários estado1 e estado2:
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1) # Retorna dicionário: {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(estado2) # Retorna dicionário: {'uf': 'São Paulo', 'sigla': 'SP'}
print(brasil) # Retorna lista com 2 dicionários: [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
print(brasil[0]) # Retorna: {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(brasil[1]) # Retorna: {'uf': 'São Paulo', 'sigla': 'SP'}
print(brasil[0]['uf']) # Retorna: Rio de Janeiro
print(brasil[1]['sigla']) # Retorna: SP

# Vamos pedir o estado e a sigla dentro de um laço:
estado = dict()
brasil1 = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    # É necessário fazer o fatiamento quando adicionar a lista. O fatiamento é fito com o copy() ao invés de dois pontos :
    # Se o fatiamento não é feito, o laço replica 3 vezes od dados do input do primeiro laço.
    brasil.append(estado.copy())

print(brasil) # Retorna: [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}, {'uf': 'Sao Paulo', 'sigla': 'SP'}, {'uf': 'Mato Grosso', 'sigla': 'MT'}, {'uf': 'Goias', 'sigla': 'GO'}]

### Podemos fazer um outro laço para uma melhor apresentação:
for e in brasil:
    print(e)

for e in brasil:
    for v in e.values():
        print(v)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
