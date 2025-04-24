# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
# No final, mostre:                                                                                                    
# A) Quantas pessoas foram cadastradas.                                                                                                                
# B) Uma listagem com as pessoas mais pesadas.                                                                                                    
# C) Uma listagem com as pessoas mais leves.

dadospessoa = []
cadastro = []
# É possível utilizar um contador para saber quantas pessoas foram cadastradas.
# Neste exercício, vamos simplificar utilizando o len():
# cont = 0

# Vamos declarar duas variávei que recebem 0 para receber o maior e menor peso:
maior = menor = 0

while True:
    dadospessoa.append(str(input('Nome: ')))
    dadospessoa.append(float(input('Peso: ')))
    ### Aqui inserimos o cálculo do maior e menor peso:
    # O peso do índice 0 vai ser o maior e menor por ser o primeiro.
    if len(cadastro) == 0:
        maior = menor = dadospessoa[1]
    # Senão verificamos qual é o maior e o menor peso com mais 2 condicionais:
    else:
        if dadospessoa[1] > maior:
            maior = dadospessoa[1]
        if dadospessoa[1] < menor:
            menor = dadospessoa[1]

    cadastro.append(dadospessoa[:])
    dadospessoa.clear()
    # cont += 1

    # Continuar?
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print('=-' * 30)

print(f'Os dados foram:  {cadastro}')
# A) Quantas pessoas foram cadastradas.
# print(f'{cont} pessoas foram cadastradas com sucesso! ') # Vamos utilizar o len() para contar.
print(f'Ao todo você cadastrou {len(cadastro)} pessoas. ')

print(f'O maior peso foi de {maior}kg de ', end='')
# B) Uma listagem com as pessoas mais pesadas. 
# Vamos gerar a lista com um laço for onde, para cada peso i[1] que for igual ao maior, vamos retornar o nome da pessoa i[0].
for i in cadastro:
    if i[1] == maior:
        print(f'-> {i[0]} <-', end=' ')

print(f'\nO menor peso foi de {menor}kg de ', end='')
# C) Uma listagem com as pessoas mais leves.
for i in cadastro:
    if i[1] == menor:
        print(f'-> {i[0]} <-', end=' ')
