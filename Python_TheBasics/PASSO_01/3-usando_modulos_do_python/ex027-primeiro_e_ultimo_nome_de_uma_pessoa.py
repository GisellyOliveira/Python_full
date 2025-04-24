# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# Removeremos eventuais espaços no início e final da string com ".strip()"
nome = str(input('Digite seu nome completo: ')).strip()
# Usamos o ".split()" para transformar a string em uma lista com cada um dos nomes digitados correspondendo a um item da lista.
lista_nome = nome.split()

# Para capturar o primeiro nome, basta indicar o item 0 da lista de nomes, que corresponde ao primeiro nome digitado:
print('Seu primeiro nome é {}' .format(lista_nome[0]))
# Para capturar o último nome, usaremos uma operação feita com o módulo "len()".
# O "len(lista_nome)" vai retornar quantos itens há dentro da lista. O total de itens - 1 corresponde ao índice do último nome da lista:
print('Seu último nome é {}' .format(lista_nome[len(lista_nome)-1]))
