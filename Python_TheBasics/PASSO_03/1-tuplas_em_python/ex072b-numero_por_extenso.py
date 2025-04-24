# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# Esta versão deverá perguntar ao usuário de deseja ou não continuar.

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
           'seis', 'sete', 'oito', 'nove', 'dez', 
           'onze', 'doze', 'treze', 'quantorze', 'quinze', 
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )
 
while True: # Loop principal
    while True: # Loop para validar a entrada do usuário
        numero = int(input('Digite um número de 0 a 20: '))
        if 0 <= numero <= 20:
            print(f'Você digitou o número {extenso[numero]}') 
            break # Sai do loop interno se o loop for válido
        else:
            print('Número inválido. ', end='')
    
    # Opção para o usuário continuar ou sair:
    continuar = " "
    while continuar not in "SN": # Loop interno para validar se o usuário quer ou não contnuar. Se recebe "S", reinicia o loop principal. Se recebe algum caractere inválido, o loop interno continua pedindo se o usuário deseja ou não continuar.
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == "N": # Se recebe "N" de entrada do usuário, sai do loop completamente e encerra o programa.
        break
