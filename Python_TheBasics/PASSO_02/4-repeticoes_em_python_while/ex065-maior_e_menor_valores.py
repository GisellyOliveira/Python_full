# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

# Esta é a estrutura básica do código, recebendo os inputs do usuário e dando continuidade caso o usuário digite S (ou s minúscula):
'''
# ________________________________________________________________________________________________________________
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número: '))

    # O strip()[0] remove a primeira letra digitada caso o usuário digite mais de um caractere.
    resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
print('Fim')
# ________________________________________________________________________________________________________________
'''

'''
# ________________________________________________________________________________________________________________
### Cálculo da média:
resp = 'S'
# Definimos a variável "media", "soma" e "quant" que recebem o valor 0:
media = soma = quant = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    # A soma recebe o valor 0 anterior + o valor recebido em "num":
    soma += num
    # A variável "quant" recebe o valor inicial 0 somado sempre a 1 cada vez que o contador fizer mais um loop:
    quant += 1

    resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]

# A média será recalculada fora do loop recebendo os valores de "soma" dividido pela "quant":
media = soma / quant
print('Você digitou {} números e a média foi {}.' .format(quant, media))
# ________________________________________________________________________________________________________________
'''

# Agora que temos dois modelos de código: o primeiro básico com as entradas do usuário funcionanedo e, segundo, calculando a média,
# vamos inserir o cálculo do maior e do menor número digitado:

resp = 'S'
media = soma = quant = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    # Calculo do maior e do menor: o primeiro será sempre o menor e maior, pois é o único:
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]

media = soma / quant
print('Você digitou {} números e a média dos números digitados foi {}.' .format(quant, media))
print('O maior valor foi {} e o menor valor for {}.' .format(maior, menor))
