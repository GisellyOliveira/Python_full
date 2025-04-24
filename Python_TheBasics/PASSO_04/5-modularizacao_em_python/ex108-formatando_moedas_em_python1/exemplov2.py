import moedav2

p = float(input('Digite o preço: R$'))

#Removemos o R$, que será inserido através de uma função do módulo moedav2 -> "moedav2.moeda"
print(f'A metade de {moedav2.moeda(p)} é {moedav2.moeda(moedav2.metade(p))}')
print(f'O dobro de {moedav2.moeda(p)} é {moedav2.moeda(moedav2.dobro(p))}')
print(f'Aumentando 10%, temos {moedav2.moeda(moedav2.aumentar(p, 10))}')
# Podemos passar como parâmetro para a função moeda() o cifrão (com aspas duplas) de uma outra moeda, por exemplo:
print(f'O valor {moedav2.moeda(p)} poderia ser apresentado com o cifrão do dólar: {moedav2.moeda(p, "US$")}')
