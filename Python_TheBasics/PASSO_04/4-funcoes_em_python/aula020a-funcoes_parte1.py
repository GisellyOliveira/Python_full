# Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python. 
# Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python. 
# Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.

print('-' * 30)
print(('    CURSO EM VÍDEO  '))
print('-' * 30)
print('-' * 30)
print(('    APRENDA PYTHON  '))
print('-' * 30)
print('-' * 30)
print(('    GUSTAVO GUANABARAS  '))
print('-' * 30)
print()

# Entre a função e o programa principal deve haver 2 linhas vazias:
def lin():
    print('-' * 30)


### Utilizamos lin() para chamar a função def lin():
lin()
print(('    CURSO EM VÍDEO  '))
lin()
lin()
print(('    APRENDA PYTHON  '))
lin()
lin()
print(('    GUSTAVO GUANABARA  '))
lin()
print()

# Desta forma criamos um comando novo que chama uma função especificada anteriormente.
### Também é possível trabalhar com funções com parâmetros, sintetizando valores que podem ser substituídos e alterados.
# No exemplo anterior, vimos que o bloco linha - mensagem - linha se repete três vezes.
# Vamos utilizar uma variável e passar uma mensagem como parâmetro que vem a ser substituída no código principal:
def mensagem(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)

mensagem('SISTEMA DE ALUNOS')
mensagem('APRENDA PYTHON')
mensagem('GUSTAVO GUANARABA')