# Vamos supor que precisemos imprimir um 'Oi' no console 6 vezes:

print('IMPRIMINDO UM "Oi" NO CONSOLE 6 VEZES:')

print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')

### Agora vamos utilizar LAÇOS DE REPETIÇÕES para automatizar essa ação específica.

# Desta forma, podemos controlar o número de repetições e alterá-las caso necessário.
# Vamos supor que precisamos imprimir no console a palavra 'Oi' inúmeras vezes:
# Vamos utilizar a variável "c" como padrão para a variável do contador:
# O contador parte do 0 e conta até 5, retornando um total de 6 repetições.
# Finalmente retorna uma única vez a palavra "FIM".

for c in range(0,6):
    print('Oi!')
print('FIM')

#Divisor
print('-' * 30)
print('ALTERANDO A INDENTAÇÃO DE "FIM" ')
print('IMPRIMINDO UM "Oi" NO CONSOLE 6 VEZES:')

### Atenção a identação que pode mudar drasticamente o resultado do código, exemplo:

for c in range(0,6):
    print('Oi!')
    print('FIM')

#Divisor
print('-' * 30)
print('IMPRIMINDO O CONTADOR "c" NO CONSOLE ')
print('-' * 30)

### Poderíamos definir a contagem de 1 até 6, definindo o range em (1,7), Para isso vamos substituir a string 'Oi!' pela variável 'c' para que nos retorne o contador:

for c in range(1,7):
    print(c)
print('FIM')

#Divisor
print('-' * 30)
print('CONTAGEM REGRESSIVA')
print('-' * 30)

### Tentamos uma contagem regressiva, de 6 até 0. Precisamos indicar o -1 para que isso ocorra, correspondente a iteração necessária, onde ele vai subtraindo 1 a cada número e fazer a contagem regressiva:

for c in range(6, 0, -1):
    print(c)
print('FIM')

#Divisor
print('-' * 30)
print('PULANDO NÚMEROS DURANTE A CONTAGEM ')
print('-' * 30)

### Podemos fazer como anteriormente mas com números positivos para pular um determinado número de caracteres:
# Aqui ele conta de 0 a 6, pulando de 2 em 2:
for c in range(0, 7, 2):
    print(c)
print('FIM')

#Divisor
print('-' * 30)
print('CONTANDO ATÉ UM VALOR RECEBIDO ATRAVÉS DO INPUT ')
print('-' * 30)

### A variável que foi recebida no console passa a fazer parte do laço de repetição em 'for'.
# No console será retornado a contagem de 0 até o número digitado (precisamos somar 1 para que isso ocorra), antes de apresentar a mensagem de 'FIM'.
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

#Divisor
print('-' * 30)
print('DEFININDO UM VALOR PARA DAR INÍCIO A CONTAGEM, UM VALOR PARA O FIM, E UM TERCEIRO VALOR PARA QUANTAS CASAS PRETENDEMOS PULAR ')
print('-' * 30)

### Podemos interagir salvando as variáveis de início e fim da contagem, assim como quantos números deve saltar durante a contagem:
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

#Divisor
print('-' * 30)
print('FAZ UM LOOP 3 VEZES DO INPUT PARA "DIGITE UM VALOR:" ')
print('-' * 30)

### Pede para digitar um valor 3 vezes, neste caso. 
for c in range(0, 3):
    n = int(input('Digite um valor:'))
print('fim')

#Divisor
print('-' * 30)
print('PEDE 4 VALORES E RETORNA A SOMA DOS VALORES DIGITADOS ')
print('-' * 30)

### Agora vamos alterar para 4 vezes o número de vezes que será pedido para digitar um número.
# Vamos também somar todos os valores digitados e apresentar o resultado.
# Precisamos criar uma variável que contenha o valor 0 , neste caso a variável 's', para ser somado ao valor recebido nos inputs, armazenados, neste caso, na variável 'n'.

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n
print('fim')
print('O somatório de todos os valores foi {}.'  .format(s))