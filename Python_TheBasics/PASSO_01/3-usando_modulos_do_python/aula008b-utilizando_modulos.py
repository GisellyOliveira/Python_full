#Caso quisessemos importar somente a utilidade sqrt, ou raiz quadrada, além de importar somente a funcionalidade necessário, ao chamá-la, eliminamos o "math" do código ficando da seguinte forma: 
#from math import sqrt

#Como vamos utilizar o floor para arredondar para baixo também, vamos importar a funcionalidade sqrt assim como o floor.
from math import sqrt, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz quadrada de {} é igual a {:.2f}' .format(num, raiz))

# Para raiz quadrada arredondada para cima:
print('A raiz quadrada arredondada para baixo de {} é igual a {}' .format(num, floor(raiz)))
