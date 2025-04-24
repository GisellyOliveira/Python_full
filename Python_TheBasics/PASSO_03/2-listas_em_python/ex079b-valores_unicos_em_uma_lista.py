# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
# Esta resolução trata o input recebido do usuário se deseja ou não continuar.

lista = []

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
         print('Número já existente. ')

    #Loop para continuar ou sair:
    cont = " "
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break 

print('-' * 60)
lista.sort() # Para ordenar a lista em ordem crescente.
print(f'Você adicionou os números: {lista}')
print('-' * 60)
