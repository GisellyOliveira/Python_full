# Para aumentar e diminuir, precisamos do preço e da taxa como parâmetros:
# Definimos parâmetros opcionais em todas as funções.
def aumentar(preco = 0, taxa = 0):
    # return preco + (preco * taxa / 100) # Ao invés de inserir o cálculo no return, vamos definir uma variável para o cálculo.
    res = preco + (preco * taxa / 100)
    return res


# As variáveis das funções, apesar de terem os mesmos nomes, são diferentes, pois são variáveis de escopo local.
def diminuir(preco = 0, taxa = 0):
    res = preco - (preco * taxa / 100)
    return res


def dobro(preco = 0):
    res = preco * 2
    return res


def metade(preco = 0):
    res = preco / 2
    return res


def moeda(preco = 0, ciframoeda = 'R$'):
    return f'{ciframoeda}{preco:>.2f}'.replace('.', ',') # replace substitui todos os pontos (.) por vírgulas (,)
# :>8.2f -> 2 casas decimais, alinhada a direita.
