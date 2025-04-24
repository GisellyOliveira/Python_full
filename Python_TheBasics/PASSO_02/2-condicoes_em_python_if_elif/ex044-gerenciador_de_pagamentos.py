# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

# VAMOS INSERIR O NOME DA LOJA FORMATADO, APRESENTADO NUM ESPAÇO DE 40 CARACTERES, CENTRALIZADO, COM O SÍMBOLO = PREENCHENDO O ESPAÇO VAZIO:
print('{:=^40}'.format('\033[1;42m LOJAS BRASILEIRAS \033[m'))

preco = float(input('Insira o valor da compra: R$'))

print('\033[1;43m ESCOLHA A SUA FORMA DE PAGAMENTO: \033[m ')
print ('''\033[1;37m [ 1 ] À VISTA EM DINHEIRO OU CHEQUE
 [ 2 ] À VISTA NO CARTÃO
 [ 3 ] 2X NO CARTÃO
 [ 4 ] 3X OU MAIS NO CARTÃO \033[m''')
opcao = int(input('Digite uma das opções: '))

if opcao == 1:
    preco_final = preco - (preco * 10 / 100)
    print('\033[1;47m O seu produto custa R${:.2f} e você terá 10% de desconto, pagando somente R${:.2f} \033[m' .format(preco, preco_final))
elif opcao == 2:
    preco_final = preco - (preco * 5 / 100)
    print('\033[1;47m O seu produto custa R${:.2f} e você terá 5% de desconto, pagando somente R${:.2f} \033[m' .format(preco, preco_final))
elif opcao == 3:
    parcela = preco / 2
    print('\033[1;47m Sua compra de R${} será parcelada em 2x de R${}. \033[m' .format(preco, parcela))
elif opcao == 4:
    preco_final = preco + (preco * 20 / 100)
    tot_pac = int(input('Em quantas parcelas você deseja pagar? '))
    parcela = preco_final / tot_pac 
    print('\033[1;47m O valor do seu produto é de R${:.2f} e sua parcela será de R${:.2f} em {}x no cartão com 20% de juros, totalizando R${:.2f}. \033[m' .format(preco, parcela, tot_pac, preco_final))
else:
    print('\033[1;41m OPCÃO INVÁLIDA. TENTE NOVAMENTE! \033[m')

