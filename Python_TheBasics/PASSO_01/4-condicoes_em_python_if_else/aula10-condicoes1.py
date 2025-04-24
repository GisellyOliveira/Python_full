nome = str(input('Qual é o seu nome? '))
# Quando usamos somente o if na condição, a estrutura condicional é simples.
if nome == 'Charlotte':
    print('Que nome lindo você tem!')
# Quando usamos o else, é uma estrutura condicional composta.
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!' .format(nome))