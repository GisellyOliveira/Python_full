# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
# Vamos usar a biblioteca 'date' e a funcionalidade 'datetime'
from datetime import date

print('\033[31m - \033[m' * 30)
print('\033[1,41m CATEGORIA DOS ATLETAS: \033[m')
print('\033[31m - \033[m' * 30)

ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print('\033[1;47m Você nasceu em {} e tem {} anos. \033[m' .format(ano_nascimento, idade))

if idade <= 9:
    print('\033[1;37m Você pertence à categoria MIRIM. \033[m')
elif idade <= 14:
    print('\033[1;37m Você pertence à categoria INFANTIL. \033[m')
elif idade <= 19:
    print('\033[1;37m Você pertence à categoria JÚNIOR. \033[m')
elif idade <= 25:
    print('\033[1;37m Você pertence à categoria SÊNIOR. \033[m')
else:
    print('\033[1;37m Você pertence à categoria MASTER. \033[m')
    