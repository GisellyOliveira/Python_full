# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

#Utilizaremos somente a propriedade "choice"do módulo "random" para selecionar o nome do aluno a ser escolhido:
from random import choice

# Embora não seja ncessário definir como string o módulo de input, explicitaremos no código que estarenos recebendo em nome do aluno um dado do tipo string.
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

# Vamos adicionar uma lista, utilizando colchetes [], para receber o nome desses alunos:
lista = [aluno1, aluno2, aluno3, aluno4]

# E dentro da variável escolhido, vamos utilizar a propriedade "choice" do método "random" para selecionar um dos alunos de "lista". 
escolhido = choice(lista)

print('O aluno/a escolhido/a foi {}!' .format(escolhido))