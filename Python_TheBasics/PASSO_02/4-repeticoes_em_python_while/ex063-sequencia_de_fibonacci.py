# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

# APRESENTAÇÃO
print('=' * 40)
print('>>> SEQUENCIA DE FIBONACCI <<<')
print('=' * 40)

n = int(input('Quantos termos você quer mostrar? '))
# os dois primeiros valores da seuqencia Fibonacci são sempre 0 e 1. O terceiro valor será sempre a soma do segundo com o primeiro, sendo assim, o terceiro termo a soma de 0 +1:
t1 = 0
t2 = 1
print('{} -> {}' .format(t1, t2), end='')
# O terceiro valor será sempre a soma dos dois valores anteriores, ou seja, do segundo com o primeiro (0 + 1), e assim sucessivamente.
# Para fazer essa contagem do terceiro termo sucessivamente, definimos uma variável para ser usada como contador que já recebe o valor 3, pois está contando já o terceiro termo:
cont = 3
# Definimos um loop para continuar a sequencia:
while cont <= n:
    t3 = t1 + t2
    # Porém, a cada nova contagem do loop, o t1 se torna o t2, o t2 se torna o terceiro termo, e o t3 será recalculado:
    t1 = t2
    t2 = t3
    print(' -> {}' .format(t3), end='')
    cont += 1
print('-> FIM')
