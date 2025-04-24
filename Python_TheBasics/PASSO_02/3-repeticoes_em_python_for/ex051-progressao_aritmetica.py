# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# APRESENTAÇÃO
print('=' * 50)
print('10 TERMOS DE UMA PA')
print('=' * 50)

#Partimos deste exemplo da aula 13:
'''
### Podemos interagir salvando as variáveis de início e fim da contagem, assim como quantos números deve saltar durante a contagem:
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
'''

# Desta forma, definimos as variáveis para a razão e a pa:
primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Digite a razão: '))
# Precisamos calcular o décimo termo da pa com a seguinte fórmula:
decimo = primeirotermo + (10 - 1) * razao

# Definimos o laço que executa a leitura destes dados da seguinte forma:
for c in range(primeirotermo, decimo + razao, razao):
    print('{}' .format(c), end='-> ')
print('ACABOU')