# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SAÁRIO, COM 15% DE AUMENTO.

s = float(input('Digite o valor do seu atual salário: R$ '))
#Calculo de 15% do salário
reajuste = s * 15 / 100

print('O valor do seu novo salário com reajuste de 15% será de R$ {:.2f}.' .format(s + reajuste))