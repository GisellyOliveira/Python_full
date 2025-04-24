# Reescreva a função leiaInt() que fizemos no desafio 104, 
# incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from utilidades import lerNumeros

n1 = lerNumeros.leiaInt('Digite um número inteiro: ')
n2 = lerNumeros.leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n1} e o número real foi {n2}')

