# Para aumentar e diminuir, precisamos do preço e da taxa como parâmetros:
def aumentar(preco, taxa): 
    # return preco + (preco * taxa / 100) # Ao invés de inserir o cálculo no return, vamos definir uma variável para o cálculo.
    res = preco + (preco * taxa / 100)
    return res


# As variáveis das funções, apesar de terem os mesmos nomes, são diferentes, pois são variáveis de escopo local.
def diminuir(preco, taxa):
    res = preco - (preco * taxa)
    return res


def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco / 2
    return res
