# Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

titulo = '\033[1;42m >>> BEM-VINDO AO NOSSO BANCO <<< \033[m'
print('-' * 34)
print(f'{titulo:^30}')
print('-' * 34)


valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        # Para não imprimir a quantidade de notas de 0.
        if totced > 0:
            print(f'O total de {totced} de R${ced}')
        # Começamos subtraindo a quantidade máxima de notas de 50, e assim por diante.
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
            totced = 0
        if total == 0:
            break

print('\033[42m VOLTE SEMPRE AO NOSSO BANCO! \033[m')
