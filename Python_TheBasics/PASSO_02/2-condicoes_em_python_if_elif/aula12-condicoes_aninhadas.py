nome = str(input('Qual é o seu nome? '))
# ESTRUTURA CONDICIONAL ANINHADAS:
if nome == 'Fulano':
        print('Que nome bonito!')
elif nome == 'Ciclano' or nome == 'João' or nome == 'Maria':
        print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
        print('Belo nome feminino.')
else:
        print('Seu nome é bem normal.')

print('Tenha um bom dia, {}!' .format(nome))
