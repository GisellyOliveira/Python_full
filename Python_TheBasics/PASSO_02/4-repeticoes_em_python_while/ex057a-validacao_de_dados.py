# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

# Definimos uma variável para receber o input do usuário.
# Removemos eventuais espaços ao início ou final da digitação com o módulo strip().
# Transformamos em maiúsculos os caracteres digitados e retornamos somente o caractere do índice 0 com upper()[0]
sexo = str(input('Informe seu sexo:[M/F] ')).strip().upper()[0]
# print(sexo) # Este print testa o tratamento do input do usuário.

# Poderíamos usar a condicional, mas utilizaremos neste exercício uma técnica de validação de dados:
# Poderíamos passar como parâmetros somente o 'MF', sem as letras minúsculas pois o input já foi transformado em maiúsculas.
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informa seu sexo:[M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!' .format(sexo))
