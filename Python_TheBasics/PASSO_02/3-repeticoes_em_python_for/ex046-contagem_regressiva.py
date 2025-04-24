# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

# Importando módulo que fará a pausa de 1 segundo durante a contagem:
from time import sleep

# Apresentação ao usuário com pausa de 1 segundo para iniciar a contagem:
print('-' * 50)
print('>>> A CONTAGEM REGRESSIVA VAI COMEÇAR!!! <<<')
print('-' * 50)
sleep(1)

# Definimos a contagem regressiva de 10 a 0 (e para isso é necessário definir a contagem até -1 para que ele conte o 0):
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print(' \033[1;41m *** BOOM!!! E VIVA!!! BUM! POOOW!!! *** \033[m ')