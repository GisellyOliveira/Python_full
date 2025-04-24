# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# Usamos a funcionalidade date da biblioteca datetime para localizar na máquina o dia atual caso o usuário digite 0:
from datetime import date

# Vamos aceitar 0 para a data atual com a biblioteca date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:  '))

# Usamos a biblioteca datetime e uma condicional para buscar o ano atual, caso o usuário digite 0:
if ano == 0:
    ano = date.today().year

# Agora vamos a condicional para calcular se o ano é ou não é bissexto, considerando as seguintes regras:
# Se o ano divisível por 4 ( se o resto da divisão por quatro for 0), o ano é bissexto:
# AND ele também não pode ser divisível por 100 (ano % 100 != 0), pois não são bissextos os anos múltiplos de 100
# OR ser divisível por 400 (o resto da divisão é igual a 0), pois são bissextos todos os anos múltiplos de 400, exceto se for múltiplo de 100, mas não de 400, por exemplo: 1996, 2000, 2004, 2008, 2012, 2016, 2020
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO' .format(ano))
else:
    print('O ano {} NÃO É BISSEXTO' .format(ano))