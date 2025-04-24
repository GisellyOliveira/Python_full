# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM  NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR.

#Considere o câmbio do dólar a R$5,16
print('<<< CONVERSOR DE REAIS PARA DÓLAR >>>')

v = float(input('Digite o valor que será convertido: R$ '))
dolar = 5.16

print('R${:.2f} equivale a ${:.2f} no câmbio atual de {:.2f}.' . format(v, (v / dolar), (dolar)))