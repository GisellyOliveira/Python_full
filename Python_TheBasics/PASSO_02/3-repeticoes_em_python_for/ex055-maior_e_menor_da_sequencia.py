# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# Utilizaremos a seguinte lógica para este exercício:
# Enquanto algumas resoluções atribuem um valor enorme para o maior para servir como comparação, aqui utilizaremos 0 para as duas variáveis que servirão para definir quem há o maior e menos peso:
maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: ' .format(p)))
    # O peso da primeira pessoa será o maior e o menor por ser o primeiro, então servirá como comparação para os próximos laços:
    if p == 1:
        maior = peso
        menor = peso
    # Desta forma, nos próximos laços ,se o peso for maior será substituído o valor na variável "maior", assim como para a variável "menor".
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg' .format(maior))
print('O menor peso lido foi de {} kg' .format(menor))
