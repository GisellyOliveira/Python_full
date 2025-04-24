# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

# Usaremos a biblioteca "date" e sua funcionalidade "datetime"
from datetime import date

# E capturamos com essa biblioteca o ano atual:
atual = date.today().year

'''
### Aqui faremos o cálculo da idade de uma só pessoa, e utlizaremos isso mais adiante dentro de um laço para fazer para as 7 pessoas:
# Inserimos os inputs para que o usuário possa inserir o ano de nascimento das 7 pessoas:
nasc = int(input('Em que ano a pessoa ansceu? '))

# Calculamos a idade da pessoa subtraindo o ano atual pelo ano de nascimento:
idade = atual - nasc

# Este print retorna a idade da pessoa.
# print('Essa pessoa tem {} anos.' .format(idade))

# Como queremos retornar também se ela é maior ou menor de idade, considerando a maioridade aos 21 anos:
if idade >= 21:
    print('Essa pessoa é maior')
else:
    print('Essa pessoa é menor')
'''

# Antes de fazer o laço, vamos estruturar duas variáveis que vão ser utlizadas como contador para saber quantas pessoas são de maior e quantas são de menor:
totmaior = 0
totmenor = 0

# Agora prosseguiremos com a lógica anterior, porém dentro de um laço for que o repete 7 vezes:
for pess in range(1, 8):
    # nasc = int(input('Em que ano a pessoa nasceu? ')) -> Vamos estruturar melhor:
    nasc = int(input('Em que ano a {}ª pessoa nasceu? ' .format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
# Damos o print fora do laço:
print('Ao todo tivemos {} pessoas maiores de idade. ' .format(totmaior))
print('E também tivemos {} pessoas menores de idade.' .format(totmenor))