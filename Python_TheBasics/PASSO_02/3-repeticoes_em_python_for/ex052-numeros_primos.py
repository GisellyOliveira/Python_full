# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro: '))
# Criamos uma variável para contar os números que não são primos dentro do laço.
tot = 0
# Determinamos um contador de 1 até o número acima do que foi inserido no input. Isso fará com que o contador retorne no console uma contagem de 1 até o número que foi determinado se dermos print na variável "c":
for c in range(1, num+1):
    # Todos os números que forem divisíveis pelo número correspondente ao contador, retornará na cor amarelo.
    # Senão retornará vermelho, quando não for divisível.
    if num % c == 0:
        # Se le for divisível, o inseriremos na contagem usando a variável "tot"
        tot += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}' .format(c), end=' ')
print('\n\033[m O número {} foi divisível {} vezes.' .format(num, tot))

# Todos número primo é divisível apenas duas vezes, por ele mesmo e por 1. Então, para sabermos quais são os números primos:
# Usaremos outras estrutura condicional fora do laço anterior:
if tot == 2:
    print('E por isso ele É PRIMO!') 
else:
    print('E por isso ele NÃO É PRIMO!')