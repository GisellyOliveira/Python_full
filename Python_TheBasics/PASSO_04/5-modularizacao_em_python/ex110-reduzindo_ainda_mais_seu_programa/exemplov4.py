import moedav4

p = float(input('Digite o preço: R$'))
'''
### Vamos diminuir o programa principal.
# Ao invés de inserir uma função dentro de outra, utilizaremos o parâmetro True para retornar os valores com os cifrões.
print(f'A metade de {moedav4.moeda(p)} é {moedav4.metade(p, True)}')
print(f'O dobro de {moedav4.moeda(p)} é {moedav4.dobro(p, True)}')
print(f'Aumentando 10%, temos {moedav4.aumentar(p, 10, True)}')
print(f'Reduzindo 13% do preço, temos {moedav4.diminuir(p, 13, True)}')
'''

moedav4.resumo(p)

# especificando 20% de aumento e 12% de redução
moedav4.resumo(p, 20, 12)
