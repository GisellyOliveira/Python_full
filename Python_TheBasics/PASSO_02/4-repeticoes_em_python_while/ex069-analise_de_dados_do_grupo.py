# Crie um programa que leia a idade e o sexo de várias pessoas. 
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

# Esta é a base do código.
'''
while True:
    # Apresentação
    titulo = '\033[1;41m >>> CADASTRE UMA PESSOA <<< \033[m'
    print('-' * 30)
    print(f'{titulo:^30}')
    print('-' * 30)

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    # Aqui entrarão as funcionalidades pedidas no enunciado:
        
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
        
print('Fim')
'''

# Variável inicializada com valor 0 para calcular quantas pessoas tem mais de 18 anos:
tot18 = 0
# Variável incializada com valor 0 para contar o total de homens cadastrados:
totH = 0
# Variável inicializada com valor 0 para testar quantas mulheres tem menos de 20 anos:
totM20 = 0

while True:
    # Apresentação
    titulo = '\033[1;41m >>> CADASTRE UMA PESSOA <<< \033[m'
    print('-' * 30)
    print(f'{titulo:^30}')
    print('-' * 30)

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    # Aqui entrarão as funcionalidades pedidas no enunciado:
    # Cálculo de quantas pessoas tem mais de 18 anos:
    if idade >= 18:
        tot18 += 1
    
    # Cálculo do total de homens:
    if sexo == 'M':
        totH += 1
    
    # Cálculo do total de mulheres com menos de 20 anos:
    if sexo == 'F' and idade < 20:
        totM20 += 1

        
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

        
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados. ')
print(f'E temos {totM20} mulheres com menos de 20 anos.')