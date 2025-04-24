# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

### Primeira solução utilizando os conceitos das aulas anteriores.
numero = int(input('Digite um número entre 0 e 9999: '))

### Essa solução apresenta, porém, um bug: quando o número possui menos de 4 díditos, o código quebra.
'''
# Vamos converter o número recebido e convertê-lo somente em seguida em string:
n = str(numero)

print('Analisando o número {}...' .format(numero))
print('Dígito da unidade: {}' .format(n[3]))
print('Dígito da dezena: {}' .format(n[1]))
print('Digito da centena: {}' .format(n[2]))
print('Digito do milhar: {}' .format(n[3]))
'''

# Como essa solução está bugada, vamos resolver o problema com uma segunda solução que utilizará somente um cálculo aritmético para determinar e retornar a unidade, dezena, centelha e milhar de cada número digitado:
# Para isso, usaremos o seguinte cálculo: Faremos uma DIVISÀO INTEIRA (//) do número digitado por 1, e então pegamos veste resultado (que vai ser o próprio número) e fazemos o MÓDULO (%) de 10 para as unidades.
unidade = numero // 1 % 10

# Faremos uma DIVISÀO INTEIRA (//) do número digitado por 10, e então pegamos este resultado (que vai ser o próprio número) e fazemos o MÓDULO (%) de 10 para as dezenas:
dezena = numero // 10 % 10

# Faremos uma DIVISÀO INTEIRA (//) do número digitado por 100, e então pegamos este resultado (que vai ser o próprio número) e fazemos o MÓDULO (%) de 10 para as centenas:
centena = numero // 100 % 10

# Faremos uma DIVISÀO INTEIRA (//) do número digitado por 1000, e então pegamos este resultado (que vai ser o próprio número) e fazemos o MÓDULO (%) de 10 para os milhares:
milhar = numero // 1000 % 10

print('Analisando o número {}...' .format(numero))
print('Unidade: {}' .format(unidade))
print('Dezena: {}' .format(dezena))
print('Centena: {}' .format(centena))
print('Milhar: {}' .format(milhar))