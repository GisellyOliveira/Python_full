# Loop while
numero1 = 1

# imprimir de 1 a 7
while numero1 <= 7:
    print(numero1)
    numero1 += 1

### exemplo2:
# imprimir os quadrados menores que 25
numero = 1
quadrado = 1

while quadrado <= 24:
    print("Número %d - Quadrado %d" % (numero, quadrado))
    numero += 1
    quadrado = numero ** 2

print("Ao sair do while, número tem o valor %d" % numero)
