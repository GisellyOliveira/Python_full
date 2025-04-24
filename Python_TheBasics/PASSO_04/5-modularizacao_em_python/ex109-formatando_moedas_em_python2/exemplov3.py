import moedav3

p = float(input('Digite o preço: R$'))
# Ao invés de inserir uma função dentro de outra, utilizaremos o parâmetro True para retornar os valores com os cifrões.
print(f'A metade de {moedav3.moeda(p)} é {moedav3.metade(p, True)}')
print(f'O dobro de {moedav3.moeda(p)} é {moedav3.dobro(p, True)}')
print(f'Aumentando 10%, temos {moedav3.aumentar(p, 10, True)}')
print(f'Reduzindo 13% do preço, temos {moedav3.diminuir(p, 13, True)}')
