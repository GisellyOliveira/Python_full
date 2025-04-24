### >>> MÓDULOS E PACOTES <<<
# Nessa aula, vamos continuar nossos estudos de funções em Python, 
# aprendendo como criar módulos em Python e reutilizar nossos códigos em outros projetos. 
# Vamos aprender também como agrupar vários módulos em um pacote, 
# ampliando ainda mais a modularização em grandes projetos em Python.


def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


# Programa principal:
num = int(input("Digite um valor: "))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')


### Neste exemplo, temos um programa composto por 3 funções e o programa principal.
# A modularização visa aumentar a legibilidade e facilitar a manutenção, portanto, vamos dividí-lo em 2 novos arquivos:
# O arquivo principal vai receber o programa principal.
# O arquivo secundário vai receber somente as funções.
