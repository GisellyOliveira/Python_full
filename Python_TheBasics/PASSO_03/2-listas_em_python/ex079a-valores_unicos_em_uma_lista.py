# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
# Solução da aula. Funciona mas apresenta problemas ao não validar a resposta do usuário de deseja ou não continuar.

lista = []

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
         print('Número já existente. ')

    # A resposta não será validada.
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r in 'Nn':
        break

print('-' * 60)
lista.sort() # Para ordenar a lista em ordem crescente.
print(f'Você adicionou os números: {lista}')

