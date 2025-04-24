# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-' * 30)
print('Insira o comprimento de 3 retas para verificar se elas podem formar um triângulo:')
print('-=-' * 30)
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

# Para que as retas formem um triângulo, a soma das duas retas deve ser superior a terceira.
if r1 < r2 + r3  and r2 < r3 + r1 and r3 < r1 + r2:
    print('PARABÉNS!!! As suas retas podem formar um TRIÂNGULO!')
else:
    print('Sinto muito mas as suas retas não formam um triângulo. TENTE NOVAMENTE!')
    