# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('-=-' * 30)
print('Insira o comprimento de 3 retas para verificar se elas podem formar um triângulo:')
print('-=-' * 30)
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

# Testando se é triângulo e, se for, qual tipo:
if (r1 + r2 < r3) or (r1 + r3 < r2) or (r2 + r3 < r1):
    print('\033[1;31m AS RETAS NÃO PODEM FORMAR UM TRIÂNGULO! \033[m')
elif (r1 == r2) and (r1 == r3) :
        print('\033[1;47m As retas podem formar um triângulo EQULÁTERO. \033[m')
elif (r1 == r2) or (r1 == r3) or (r2 == r3):
    print('\033[1;47m As retas podem formar um triângulo ISÓSCELES. \033[m')
else:
    print('\033[1;47m As retas podem formar um triângulo ESCALENO. \033[m') 
    