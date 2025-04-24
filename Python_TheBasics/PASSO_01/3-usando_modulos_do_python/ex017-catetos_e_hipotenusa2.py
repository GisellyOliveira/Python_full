#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# Solução importando o método "math" para o cálculo da hipotenusa:
import math

cat_oposto = float(input('Comprimento do cateto oposto: '))
cat_adjacente = float(input('Comprimento do cateto adjacente: '))
hip = math.hypot(cat_oposto, cat_adjacente)

print('A hipotenusa vai medir {:.2f}' .format(hip))