#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# Solução importando somente a propriedade "hypot"do método "math":
from math import hypot

cat_oposto = float(input('Comprimento do cateto oposto: '))
cat_adjacente = float(input('Comprimento do cateto adjacente: '))
hip = hypot(cat_oposto, cat_adjacente)

print('A hipotenusa vai medir {:.2f}' .format(hip))