# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. (Vou fazer 6)
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint # Biblioteca para randomização


# Geramos uma variável composta por 6 sorteadores aleatórios de números do 1 ao 60:
aleatorios = (randint(1, 60), randint(1, 60), randint(1, 60),
              randint(1, 60), randint(1, 60), randint(1, 60))
print('Os números sorteados foram: ', end='')
# Poderíamos inserir os 6 valores aleatórios no print acima, mas vamos usar um laço para mostrá-los sem parênteses:
for n in aleatorios:
    print(f'{n} ', end='')

# Para cálculo do maior e menor valor, serão usados os métodos "max" e "min", respectivamente:
print(f'\nO maior valor sorteado foi {max(aleatorios)}')
print(f'O menor valor sorteado foi {min(aleatorios)}')
