# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

print('\033[43mCOMPARADOR DE NÚMEROS: \033[m')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 == n2:
    print('\033[46mOs DOIS valores são IGUAIS!\033[m')
elif n1 > n2:
    print('\033[44mO primeiro número ({}) é o MAIOR valor.\033[m' .format(n1))
    print('\033[44mO segundo número ({}) é o MENOR valor.\033[m' .format(n2))
else:
    print('\033[45mO segundo número ({}) é o MAIOR valor.\033[m' .format(n2))
    print('\033[45mO primeiro número ({}) é o MENOR valor.\033[m' .format(n1))
# Deixar uma linha vazia no final para indicar o final do programa:
    