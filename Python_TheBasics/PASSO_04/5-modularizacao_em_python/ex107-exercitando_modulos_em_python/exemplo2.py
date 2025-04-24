# Importando somente algumas funções do módulo para carregar somente o necessário:
from moedav1 import dobro, metade

p = float(input('Digite o preço: R$'))
# Utilizando a função metade do módulo moeda, quando a função foi especificada na importação.
print(f'A metade de R${p} é R${metade(p)}')
# Utilizando a função dobro do módulo moeda, quando a função foi especificada na importação.
print(f'O dobro de R${p} é R${dobro(p)}')