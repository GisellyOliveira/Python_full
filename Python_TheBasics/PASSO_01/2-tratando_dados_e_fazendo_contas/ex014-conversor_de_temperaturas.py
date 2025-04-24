# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print('<<< Conversor de graus Celcius para Fahrenheit >>>')

c = float(input('Digite quantos graus Celsius você precisa converter em Fahrenheit: '))
#Calcularemos com a fórmula para conversão de Celsius para Fahrenheit:
f = 9 * c / 5 + 32
print('{}ºC correspondem a {}ºF.' .format(c, f))

