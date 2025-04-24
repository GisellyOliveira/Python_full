# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expr = str(input('Digite a expressão: '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop() # Remove o último elemento da lista
            # Deixa a pilha vazia cada vez que encontra um ')'
        else:
            pilha.append(')') 
            break

if len(pilha) == 0:
    print('Sua expressão está válida.')
else: # Se o len(pilha) for maior que 0, a expressão está incorreta.
    print('Sua expressão está errada.')