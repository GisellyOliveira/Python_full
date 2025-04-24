# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

# Trataremos o texto digitado removendo eventuais espaços iniciais e finais com o "strip()".
nome = str(input('Digite o seu nome completo: ')).strip()

# Verificamos se tem a string "SILVA" dentro do nome completo (convertido em maiúscula) com o OPERADOR "in" ('SILVA' in nome).
# OBS.: o "in" é um OPERADOR, e não um módulo. 
# O "upper()" converterá os caracteres em maiúsculas para facilitar na verificação do resultado.
print('Seu nome tem "Silva"? {}' .format('SILVA' in nome.upper()))