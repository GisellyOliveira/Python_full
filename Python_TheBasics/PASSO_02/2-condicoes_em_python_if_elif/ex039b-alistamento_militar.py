# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# SEGUNDA VERSÃO CONSIDERANDO O SEXO DO USUÁRIO ANTES DE INDICAR O ANO DE ALISTAMENTO.
# RETORNA 'VOCÊ NÃO PRECISA SE ALISTAR' PARA O SEXO FEMININO.
# Também usaremos o 'datetime' da biblioteca 'date'.
from datetime import date

print('\033[31m - \033[m' * 50)
print('\033[1,41m INFORMAÇÕES OBRIGATÓRIAS DAS FORÇAS ARMADAS \033[m')
print('\033[31m - \033[m' * 50)
print('''INFORME O SEU SEXO:
      [ 1 ] FEMININO
      [ 2 ] MASCULINO''')
gender = int(input('Sua opção: '))

if gender == 1:
    print('\033[1;47mVocê não precisa se alistar! Tenha um ótimo dia!\033[m')

elif gender == 2:
    ano_nascimento = int(input('Qual o ano do seu nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    print('\033[40mQuem nasceu em {} tem {} anos em {}.\033[m' .format(ano_nascimento, idade, ano_atual))
    
    if idade == 18:
        print('\033[41mVocê completa ou completou 18 anos neste ano e PRECISA SE ALISTAR até o dia 30 de julho!!!')
    elif idade < 18:
        saldo = 18 - idade
        print('\033[33;42mFalta(m) {} ano(s) para você se alistar!\033[m' .format(saldo))
        # Para calcular o ano do alistamento:
        ano = ano_atual + saldo
        print('\033[1;34;42mSeu alistamento será em {}!\033[m' .format(ano))
    # Usamos um segundo 'elif' mas também poderíamos ter usado o 'else':
    elif idade > 18:
        saldo = idade - 18
        print('\033[43mVocê deveria ter se alistado há {} ano(s).\033[m' .format(saldo))
        # Para calcular o ano do alistamento:
        ano = ano_atual - saldo
        print('\033[1;43mSeu alistamento foi em {}\033[m.' .format(ano))

else:
    print('\033[41mOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[m')