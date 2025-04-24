# CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA:

n = int(input('Digite um valor: '))
print('O dobro de {} é {}, seu triplo é {} e sua raiz quadrada é {:.2f}.'.format(n, (n * 2), (n * 3), pow(n, (1/2))))
# A variável foi definida como número do tipo "integer" e sua exibição definida para mostrar até duas casas decimais do número float para o resultado da raiz quadrada, onde foi usada a função "power"para resolução da raiz quadrada.