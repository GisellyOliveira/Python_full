# Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. 
# Vamos imprimir 'Olá mundo!' em vermelho:
print('\033[31mOlá mundo!')
# Agora em letras vermelhas e fundo amarelo:
print('\033[31;43mOlá mundo!')
# Adicionando negrito:
print('\033[1;31;43mOlá mundo!')
# Adicionando o código reset (\33m[) para evitar que as impostações cessem após o texto:
print('\033[1;31;43mOlá mundo!\033[m')
# Sublinhado, letras brancas e fundo lilás:
print('\033[4;30;45mOlá, mundo!\033[m')
# Letra amarela e fundo padrão
print('\033[33mOlá, mundo!\033[m')
# Invertendo o padrão anterior:
print('\033[7;33mOlá, mundo!\033[m')

# Vamos colorir o exercício abaixo:
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[33m{}' .format(a,b))

# Usando o próprio print para colorir:
nome =  'Fulano'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!' .format('\033[4;34m', nome, '\033[m'))

# Uma outra maneira de colorir é através da criação de uma variavel chamada "cores":
nome = 'Ciclano'
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pretoebranco': '\033[7;30m'
}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!' .format(cores['pretoebranco'], nome, cores['limpa']))
