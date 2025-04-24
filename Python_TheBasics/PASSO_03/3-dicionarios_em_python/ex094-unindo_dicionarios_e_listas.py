# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

galera = list()
pessoa = dict()
soma = media = 0

while True:
    # Esvazia o dicionário cada vez que o laço inicia para recebimento dos novos dados:
    pessoa.clear()
    # Input do usuário para nome:
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    # Input do usuário para sexo, com validação:
    while True: 
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa["sexo"] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    # Input do usuário para idade:
    pessoa['idade'] = int(input('Idade: '))
    # Soma da idade vai receber o valor da idade para ser somado dentro da variável que inicia com 0:
    soma += pessoa['idade']
    # A lista galera vai receber uma cópia dos dados inseridos no dicionário pessoa:
    galera.append(pessoa.copy())
    # Continuar? Com validação:
    while True:
        resp = str(input('Quer continuar? ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30) # Linha divisória
# A) Quantas pessoas foram cadastradas 
# Utilizamos o len(galera) para retornar quantas pessoas foram cadastradas:
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')

# B) A média de idade 
# Calculo da média:
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.') # 5.2f = 5 casas flutuantes, sendo 2 decimais.

# C) Uma lista com as mulheres 
print('As mulheres cadastradas foram: ', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end=' ')

# D) Uma lista de pessoas com idade acima da média
print('\nPessoas acima da média: ', end=' ')
for p in galera:
    if p['idade'] >= media:
        print('   ', end=' ')
        for k, v in p.items():
            print(f'\n{k} = {v}', end=' ')
        print() # Quebra de linha

print('<<< ENCERRADO >>>')
