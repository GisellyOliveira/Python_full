# --->>> LISTAS COMPOSTAS <<<---
# ---> Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
#    As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

# Declaramos uma variável 'teste'que recebe uma lista vazia:
teste = list()

# Adicionamos um nome e uma idade a esta lista:
teste.append('Gustavo')
teste.append(40)

print(teste) # Retorna: ['Gustavo', 40]

# Agora declaramos uma nova lista vazia, cuja variável se chamará 'galera':
galera = list()

# Adicionaremos o conteúdo da lista 'teste' dentro da lista 'galera':
# Observa-se a importância do parâmetro [:] para copiar a lista, evitando que seja feito uma ligação entre listas ao invés da copia do seu conteúdo.
galera.append(teste[:])

print(galera) # Retornará: [['Gustavo', 40]]

# Vamos substituir os valores do índice 0 e 1 da lista 'teste":
teste[0] = 'Maria'
teste[1] = 22

# E vamos dar um novo append() da lista 'teste'a lista 'galera':
galera.append(teste[:])

# Ao imprimir a lista galera, o segundo append() criará um novo índice com os novos valores da lista 'teste':
print(galera) # Retornará: [['Gustavo', 40], ['Maria', 22]]

###########################################################################

# Agora vamos declarar vários valores contendo nomes e idades, onde cada nome e idade de cada pessoa ocupará um índice na lista 'galera':
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

print(galera) # Retornará: [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0]) # Retornará: ['João', 19]
print(galera[0][0]) # Retornará: João
print(galera[2][1]) # Retornará: 13

# Utilizando o contador do laço for, o contador no índice 0 vai pegar o nome, e no índice 1 a idade:
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

# Agora vamos gerar 2 listas vazia:
galera = list()
dados = list()

# Aqui declaramos as variáveis totmaior e totmenor para calcular os pessoas que tem maior idade mais abaixo:
totmaior = totmenor =  0 # Isso só pode ser feito com variáveis simples. não pode ser feito com variáveis compostas.

# Num laço de range de 0 a 3, vamos inserir 3 nomes e idades na lista dados. 
# A cada iteração do laço, é atribuído um valor nome a lista 'dados', depois uma idade, todos inseridos pelo usuário.
# Em seguida, é feita uma cópia desses dados na estrutura 'galera'.
# Após os dados serem copiados para a lista 'galera', eles serão apagados da lista 'dados':
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: '))) 
    galera.append(dados[:]) # Copia os dados inseridos pelo usuário dentro da lista 'galera'
    dados.clear() # Os dados inseridos na lista dados são apargados.

print(galera) # Retorna os nomes e idades digitados.
print(dados)  # Retorna uma lista vazia: [] 

# Vamos mostrar as pessoas que forem maior e menor de idade:
for p in galera:
    if p[1] >= 21: # p[1] se refere  ao valor da idade fornecida pelo usuário.
        print(f'{p[0]} é maior de idade.') # Dá um print no nome das pessoas maiores de 21 anos.
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1

print(f'Temos {totmaior} maiores e {totmenor} menores.')
