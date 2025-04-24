# Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:                                                                                                                                                
# A) Quantos números foram digitados.                                                                                                                    
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))

    # Deseja continuar?
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print('-' * 60)
# A) Quantos números foram digitados. 
print(f'Foram digitados {len(lista)} números.')

print('-' * 60)
# B) A lista de valores, ordenada de forma decrescente: 
lista.sort(reverse=True)
print(f'A lista decrescente foi: {lista}')

print('-' * 60)
# C) Se o valor 5 foi digitado e está ou não na lista.
if 5 in lista:
    print(f'O valor 5 FAZ parte da lista.')
else:
    print('O valor 5 NÃO faz parte da lista.')