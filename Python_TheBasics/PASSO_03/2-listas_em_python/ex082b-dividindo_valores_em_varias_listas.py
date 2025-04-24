# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.
# Solução personalizada.

lista = []
pares = []
impares = []

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    
    if numero % 2 == 1:
        impares.append(numero)
 

    # Deseja continuar?
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print('-' * 60)
lista.sort()
print(f'Você digitou os números: {lista}')

pares.sort()
print(f'Os números pares digitados foram: {pares}')

impares.sort()
print(f'Os números ímpares digitados foram: {impares}')
