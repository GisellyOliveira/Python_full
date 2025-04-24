# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep

def sorteia(lista):
    print('>>> SORTEANDO 5 VALORES DA LISTA <<<')
    for cont in range(0, 5):
        # lista.append(randint(1, 10)) -> Essa linha sorteia todos os 5 números aleatórios para a lista.
        # Para melhor apresentação:
        n = randint(1, 10) # Definimos uma variável para receber cada um dos números aleatórios sorteados.
        lista.append(n) # A variável vai ser recebida na lista passada como parâmetro ao chamar a função.
        print(f'{n} ', end=' ', flush=True) # Flush para o sleep
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista): 
    soma = 0 
    pares = list()
    # Vamos varrer todo o vetor
    for valor in lista:
        if valor % 2 == 0:
            pares.append(valor)
            soma += valor
    print(f'Na lista {lista}, os valores pares são {pares}, cuja soma temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
