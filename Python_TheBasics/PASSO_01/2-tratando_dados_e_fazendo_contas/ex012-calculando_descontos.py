# FAÇA UM ALGORÍTMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.

preco = float(input('Digite o preço do produto: R$ '))
desconto = preco * 5 / 100

print('O porduto que custa R${:.2f} sairá por {:.2f} na promoção com 5% de desconto.' .format(preco, (preco - desconto)))