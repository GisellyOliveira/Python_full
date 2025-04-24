# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
# No final, mostre a lista ordenada na tela.

lista = []

for n in range(0, 5):
    numero = int(input(f'Digite o {n + 1}º número: '))
    
    ### Caso o número seja o primeiro ou maior que o último, ele simplismente será inserido.
    '''
    if n == 0:
        lista.append(numero)
        print('Adicionado ao final da lista...')
    elif numero > lista[-1]: # Ou para pegar o último elemento: [len(lista) - 1] 
        lista.append(numero)
    '''
    # Resumindo a parte superior:
    if n == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista...')

    ### Caso ele não seja o primeiro, e nem o maior, ele deverá ser inserido no índice correto.
    # Para isso faremos uma varredura da posição 0 até o último item da lista:
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1

print(lista)
print(f'Os valores digitados em ordem foram: {lista}')
    