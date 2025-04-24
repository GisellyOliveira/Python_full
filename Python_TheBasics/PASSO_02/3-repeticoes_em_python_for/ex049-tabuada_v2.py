# Refaça o EXERCÍCIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('-' * 50)
print('\033[1;41m >>> GERADOR DE TABUADA <<< \033[m')
print('-' * 50)

# Definiremos uma variável para receber o input do usuário:
num = int(input('Digite um númera para gerar a tabuada: '))

# Aqui definiremos o loop que gerará a tabuada:
for c in range(1, 11):
    print('{} x {:2} =  {}' .format(num, c , num*c))
