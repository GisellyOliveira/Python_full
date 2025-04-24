# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

#Solução usando as propriedade "sin"para seno, "cos" para cosseno e "tan" para tangente utilizando a importação do módulo "math":
import math
angulo = float(input('Digite o ângulo que você deseja: '))

#Precisaremos usar a função "math.radians()" para converter" o ângulo informado no input de graus para radianos, pois a propriedade "sin", "cos"e "tan"do método "math" precisa do valor em radianos ao invés de graus.
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}' .format(angulo, seno))

cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}' .format(angulo, cosseno))

tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}' .format(angulo, tangente))