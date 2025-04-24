# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, 
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n=1, show=False): # O parâmetro show=False é o parâmetro default e pode ser omitido como parâmetro da função. Foi passado para tornar a função mais flexível e o código mais claro
    #DOCSTRING:
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta. Se True, mostra o processo de cálculo. Defaults to False.
    :return: O valor do Fatorial de um número n.

    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ') # imprime o número recebido como parâmetro para o calcule fatorial
            if c > 1:
                print(' x ', end=' ') # sinal de multiplicação enquanto o contador for maior que 1
            else:
                print(' = ', end=' ') # senão, sinal de igual para apresentar o resultado
        f *= c
    return f


# Programa principal:
# print(fatorial(5, show=True)) #!!!Solução Guanaraba: ERRO DE EXECUÇÃO pois show=True é um argumento qur não pode ser passado dentro de print().
# num = 5 # -> a variável recebe um valor para o cálculo dentro do programa OU:
num = int(input('Digite um número para o cálculo fatorial: ')) # a variável recebe um valor através do input do usuário.
resultado = fatorial(num, show=True) # chamada da função dentro da variável
print(resultado)
help(fatorial) # "q" para sair da docstring.
