# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA.

print('<<< TABELA MÁGICA DE TABUADA >>>')

v = int(input('\n Digite o número para gerar tabela: '))
#Inseri uma linha de tracinhos e formatei a tabela da tabuada para receber dois dígitos na valor a ser multiplicado e ser apresentada com alinhamento no resultado.
print('-' * 12)
print('{} * {:2} = {}' .format(v, 1, v*1))
print('{} * {:2} = {}' .format(v, 2, v*2))
print('{} * {:2} = {}' .format(v, 3, v*3))
print('{} * {:2} = {}' .format(v, 4, v*4))
print('{} * {:2} = {}' .format(v, 5, v*5))
print('{} * {:2} = {}' .format(v, 6, v*6))
print('{} * {:2} = {}' .format(v, 7, v*7))
print('{} * {:2} = {}' .format(v, 8, v*8))
print('{} * {:2} = {}' .format(v, 9, v*9))
print('{} * {:2} = {}' .format(v, 10, v*10))
print('-' * 12)
