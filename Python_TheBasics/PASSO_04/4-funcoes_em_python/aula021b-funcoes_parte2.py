### DOCSTRINGS ###
# Vamos inserir uma docstring na função contador e acessá-la pelo terminal ao final do código com a função help():
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :parametro i: início da contagem
    :parametro f: fim da contagem
    :parametro p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end=' ')
        c += p
    print('FIM!')


help(contador) # -> q para sair do console e continuar o código


### PARÂMETROS OPCIONAIS ###
# Vamos inserir uma funçao chamada somar que soma o valor recebido por 3 parâmetros, a, b e c.
# Caso nenhum parâmetro seja passado na chamada da função, a função receberá os valores inseridos nos parâmetros opcionais da função:
def somar(a=0, b=0, c=0): # -> Parâmetros opcicionais recebem valor 0 como default
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar()

# Para receber qualquer quantidade de parâmetros na chamada, é necessário utilizar o desempacotamente.
# Os parâmetros opcionais servem somente para sanar valores vazios que a função precisa receber.


