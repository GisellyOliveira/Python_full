from utilidades import moeda, dado

p = dado.leiaDinheiro('Digite o preço: R$')

# especificando 20% de aumento e 12% de redução
moeda.resumo(p, 20, 12)