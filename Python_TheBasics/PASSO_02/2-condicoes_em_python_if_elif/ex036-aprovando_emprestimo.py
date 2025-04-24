# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('\033[44m-' * 60)
print('\033[44mSIMULE O SEU EMPRÉSTIMO:')
print('\033[44m-\033[m' * 60)

casa = float(input('Qual o valor da casa que você deseja adquirir? R$'))
salario = float(input('Qual a sua atual renda mensal? R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)

# Vamos simular a situação de aprovação do empréstimo.
if prestacao > (salario * 30 / 100):
    print(('\033[31;41mSinto muito mas o valor das parcelas supera 30% do valor da sua renda mensal. \nAumente a quantidade de anos para diminuir o valor das parcelas e tente novamente!!!\033[m'))
else:
    print('\033[36;42mParabéns! O SEU EMPRÉSTIMO FOI APROVADO!!!\033m')
    print('Para um empréstimo de R$ {:.2f}, você poderá quitar o seu financiamento em {} anos em parcelas de apenas R${:.2f}.' .format(casa, anos, prestacao))
