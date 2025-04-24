# Importando o módulo moeda
import moedav1

p = float(input('Digite o preço: R$'))
# Utilizando a função metade do módulo moeda
print(f'A metade de R${p} é R${moedav1.metade(p)}')
# Utilizando a função dobro do módulo moeda
print(f'O dobro de R${p} é R${moedav1.dobro(p)}')
# Utilizando a função aumentar do módulo moeda para aumentar 10%, onde o primeiro parâmetro é o preço e o segundo a porcentagem a ser aumentada.
print(f'Aumentando 10%, temos R${moedav1.aumentar(p, 10)}')
# Nos exercícios, não utilizamos a função diminuir().
