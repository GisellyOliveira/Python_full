# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

# Vamos declarar uma lista contendo duas listas vazias que receberão os valores pares e ímpares.
lista = [[], []]
# Declaramos uma variável que recebe 0 e, dentro do laço for, vai receber o input do usuário para ser tratado.
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    # Tratando os valores pares:
    if valor % 2 == 0:
        lista[0].append(valor) # Vamos dar um append no índice 0 para os pares.
    else:
        lista[1].append(valor) # E os outros (ímpares) vão para o índice 1.

print(f'Todos os valores: {lista}')
# Se darmos um sort em toda a lista, todos os valores são organizados. Vamos organizar, ao invés disso, o índice 0 e 1 separadamente.
# Ordem crescente do índice 0:
lista[0].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
# Orden crescente do índice 1:
lista[1].sort()
print(f'Os valores ímpares digitados foram: {lista[1]}')
