# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

# Apresentação:
titulo = '>>> GERADOR DE TABUADA <<<'
print('-' * 40)
print(f'\033[41m {titulo:^38} \033[m')
print('-' * 40)

# Ativa variável relativo ao contador de 1 a 10 da multiplicação:

while True:
    n = int(input('\033[47m DIGITE UM NÚMERO PARA GERAR A TABELA DE TABUADA (OU VALOR NEGATIVO PARA PARAR): \033[m'))
    if n < 0:
        break
    print('-' * 40)
    for c in range(1, 11):
       print(f'\033[1;45m {n:3} x {c:2} = {n*c:3} \033[m') 
    print('-' * 40)

print('\033[1:47m PROGRAMA ENCERRADO! VOLTE SEMPRE! \033[m')
