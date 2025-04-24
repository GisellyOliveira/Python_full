### MODULARIZAÇÃO ###
# Este será o arquivo secundário, que será composto pelas 3 funções que foram criadas para serem utilizadas no programa p[rincipal, localizado em um arquivo separado:

def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3
