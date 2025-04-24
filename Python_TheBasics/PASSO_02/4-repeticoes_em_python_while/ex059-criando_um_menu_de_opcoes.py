# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

# Vamos utilizar a funcionalidade "sleep" para dar uma pausa entre o resultado e o novo laço do menú de opções mais adiante:
from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
# Atribuimos o valor 0 a variável "opcao" para usar como contador.
opcao = 0
# Definimos o laço onde, qualquer número diferente de 5 continua o laço, e o número igual à 5 termina o programa. 0 É diferente de 5,então dá início ao laço.
while opcao != 5:
    print('''    \033[45m [ 1 ] somar \033[m
    \033[42m [ 2 ] multiplicar \033[m
    \033[43m [ 3 ] maior \033[m
    \033[44m [ 4 ] novos números \033[m
    \033[46m [ 5 ] sair do programa \033[m''')
    # Atribuímos o input do usuário a uma variável:
    opcao = int(input('\033[47m Qual é a sua opção? \033[m'))
    # Utilizamos a variável dentro de um estrutura condicional inserida dentro do laço:
    if opcao == 1:
        soma = n1 + n2
        print('\033[45m A soma de {} + {} = {} \033[m' .format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('\033[42m O resultado de {} x {} = {} \033[m' .format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('\033[43m Entre {} e {} o maior valor é {}. \033[m' .format(n1, n2, maior)) 
    elif opcao == 4:
        print('\033[44m Informe os números novamente: \033[m')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('\033[46m Finalizando... \033[m')
    else:
        print('\033[41m Opção Inválida. Tente Novamente. \033[m')
    print('=-=' * 10)
    # Vamos usar o sleep para dar uma pequena pausa antes que ele seja mostrado novamente.
    sleep(2)
print('\033[1;47m Fim do programa! Volte sempre! \033[m')
