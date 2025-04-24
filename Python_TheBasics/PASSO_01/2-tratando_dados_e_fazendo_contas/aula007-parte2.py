# Formatando a quantidade de caracteres dentro uma máscara de sustituição {} :
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!' .format(nome))

# Esse par de colchetes {} que representama máscara de substituição pode ser formatado.
# 1. Definindo o número de caracteres que a máscara deve conter - neste caso definiremos que o valor atribuído a variável "nome" deverá ser apresentada num espaço de 20 caracteres:
print('Prazer em te conhecer {:20}!' .format(nome))

# Se adicionarmos um sinal de maior >, alinhamos o conteúdo desses 20 caracteres à direita:
print('Prazer em te conhecer {:>20}!' .format(nome))

# Com o sinal de menor < define-se que o conteúdo deve permanecer à esquerda:
print('Prazer em te conhecer {:<20}!' .format(nome))

# Com o uso do acento circunflexo ^ define-se que o conteúdo deve alinhar-se ao centro:
print('Prazer em te conhecer {:^20}!' .format(nome))

# Centralizando o nome e decorando o espaço com um tipo de caractere (ex: =):
print('Prazer em te conhecer {:=^20}!' .format(nome))

# Formatando uma máscara de substituição que recebe um número no qual definiremos que apareça até 3 casas decimais (.3) e que o número seja do tipo float (f):
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
divisao = n1 / n2
print('A divisão é {:.3f}.' .format(divisao))