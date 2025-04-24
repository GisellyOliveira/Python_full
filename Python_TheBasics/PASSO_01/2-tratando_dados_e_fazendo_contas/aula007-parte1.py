#Vamos testar os operadores aritméticos vistos durante a aula:

print(5+3*2)
print(5**2)
print(5**3)
print(19//2)
print(19/2)

#O python apresenta uma quantidade gigantesca de caracteres:
print(365**522)

#Outros operadores:
print(18 % 2)
print(122 % 3)

#Calculando a potência:
    #1. Normalmente usamos dois asteriscos ( ** ) para o cálculo da potência, que tem preferência de nível 2 segundo a lista da ordem de preferência:
print(4 ** 3)

    #2. Porém é possível usar a função "power"para executar a função, atentando-se que a função PERDE a preferência dentro do cálculo.
print(pow(4, 3))

#Calculando a raiz quadrada:
    #É possível realizar o cálculo da raiz quadrada elevando o número a 1/2 (meio).
    #Exemplo da raiz quadrada de 81:
print(81 ** (1/2))
    #Exemplo de raiz quadrada de 25:
print(25 ** (1/2))

#Calculando a raiz cúbica:
    #Seguindo a lógica da raiz quadrada, é possível calcular a raiz cúbida elevando o número a um terço(1/3):
    #Exemplo raiz cúbica de 127:
print(127 ** (1/3))

###
# Utilizando o operador mais (+) como concatenador em strings:
    #1. Concatenado duas strings:
print('Oi' + 'Olá')
    #2. Se concatenar com um número, a string será exibida o número de vezes que foi multiplicada:
print('Oi' * 5)

