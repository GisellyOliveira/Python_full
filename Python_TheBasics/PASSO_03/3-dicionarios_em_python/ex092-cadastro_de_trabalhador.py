# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

# Biblioteca usada para calcular a idade:
from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = int(input('Salário: R$'))
    # Para calcular o ano de aposentadoria, convencionamos 35 de contribuição:
    #((dados['contratacao']) + 35) calcula o ano em que a pessoa vai se aposentar.
    # Será subtraído o ano atual do ano de aposentadoria para saber quantos anos a pessoa ainda precisa trabalhar. 
    # Esse valor será somado a idade para calcular a idade em que a pessoa alcançará a aposentadoria.
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao']) + 35) - datetime.now().year

print('-' * 30)
for k, v in dados.items():
    print(f'    - {k} tem o valor {v}')
