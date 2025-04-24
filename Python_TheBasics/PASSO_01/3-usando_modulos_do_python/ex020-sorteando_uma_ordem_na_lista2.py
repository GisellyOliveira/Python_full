# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#Importaremos a propriedade "shuffle" contido dentro do método "random" para embaralhar o nome dos alunos da lista:
from random import shuffle

# Embora não seja ncessário definir como string o módulo de input, explicitaremos no código que estarenos recebendo em nome do aluno um dado do tipo string.
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

# Vamos adicionar uma lista, utilizando colchetes [], para receber o nome desses alunos:
lista = [aluno1, aluno2, aluno3, aluno4]

# Chamaremos a propriedade "shuffle" que foi importada do método "random" para embaralhar a ordem dos alunos da variável "lista" que foi passada como parâmetro. 
shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)