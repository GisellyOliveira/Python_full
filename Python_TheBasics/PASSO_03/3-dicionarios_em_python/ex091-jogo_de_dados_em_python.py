# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
# Dicionário para pegar o item pela chave:
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
# Lista vazia que vai receber os jogadores em ordem decrescente:
# Se fosse criado como dicionário, ao receber os valores com o sorted(), será transformado em lista e tratado como tal.
# Isso determina o motivo pelo qual foi já declarado como lista.
ranking = list()

print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
# Usamos a função sorted() para ordenar o resultado.
# Passamos como parâmetro todos os itens da dicionário jogo
# O itemgetter vai capturar o valor do elemento quando [1] é passado como parâmetro..
# Passamos a chave que desejamos retornar, neste caso 0 para a chave e 1 para o valor da chave.
# reverse=True vai colocar na ordem decrescente.
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
# Usamos um laço para a lista ranking:
for i, v in enumerate(ranking):
    print(f'    {i + 1}o. lugar: {v[0]} com {v[1]}.')
    sleep(1)
