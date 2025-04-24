# Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python. Por exemplo:
'''
c=1 while c !=10:
print(c)
c+=1
print(‘Acabou’)
'''

# Aqui temos um programa que conta do 1 aé o 9 utilizando a estrutura "for":
print('>>> CONTANDO DE 1 ATÉ 9 USANDO A ESTRUTURA "FOR" <<<')
for c in range (1, 10):
    print(c, end=' ')
print('Fim')

# Aqui temos o mesmo programa utilizando a estrutura "while":
# Precisamos determinar uma variável que recebe o valor do começo do contador.
# Passo o while determinando até quando o contador irá (neste caso enquanto for menos que 10)
# Então, após a impressão no console, o contador recebe mais um e continua contando até 9.
print('>>> CONTANDO DE 1 ATÉ 9 USANDO A ESTRUTURA "WHILE" <<<')
c = 1
while c < 10:
    print(c, end=' ')
    c = c + 1
print('Fim')

# Quando não temos um range, podemos usar somente o while.
# Vamos para um outro exemplo usando o for onde ele pergunta 4 vezes para o usuário digitar um valor:
print('>>> DIGITE UM VALOR 4 VEZES UTILIZANDO A ESTRUTURA "WHILE" <<<')
for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')

# Mas e se não soubermso quantas vezes devemos perguntar? E se precisarmos sair da pergunta somente quando digitar 0? Observer abaixo:
# Utilizamos uma "flag", ou ponto de parada, que, no caso abaixo, será o número 0 para sair.
print('>>> DIGITE 0 PARA SAIR - UTILIZANDO UMA FLAG OU PONTO DE PARADA <<<')
n = 1
while n != 0:
    n = int(input('Digite um valor ou 0 para sair: '))
print('Fim')

# Vamos a um outro exemplo:
# Enquando a resposta for igual a SIM, o usuário continua repetindo o laço.
print('>>> DIGITE S PARA CONTINUAR - UTILIZANDO UMA FLAG OU PONTO DE PARADA <<<')
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')

# Reutilizamos o exemplo onde o usuário continua digitando um valor o 0 para sair.
# Neste exemplo, porém, queremos saber quantas vezes o usuário digitou um valor ímpar e quantas vezes digitou um valor par:
# O 0 serve para sair do laço.
print('>>> DIGITE 0 PARA SAIR - UTILIZANDO UMA FLAG OU PONTO DE PARADA <<<')
n = 1
par = impar = 0
while n!= 0:
    n = int(input('Digite um valor ou 0 para sair: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!' .format(par, impar))
