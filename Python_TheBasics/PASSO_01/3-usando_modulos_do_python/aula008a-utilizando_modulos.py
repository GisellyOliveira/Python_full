#Utilizando a biblioteca math para calcular a raiz quadrada de um número:
import math

num = int(input('Digite um número: '))
# Quando digitamos math., todas as funcionalidades da biblioteca são apresentadas para serem selecionadas.
raiz = math.sqrt(num)

print('A raiz quadrada de {} é igual a {:.2f}' .format(num, raiz))

# Agora vamos mostrar a raiz quadrada arredondada para cima:
print('A raiz quadrada arredondada para cima de {} é igual a {}' .format(num, math.ceil(raiz)))

# Agora vamos mostrar a raiz quadrada arredondada para baixo:
print('A raiz quadrada arredondada para baixo de {} é igual a {}' .format(num, math.floor(raiz)))