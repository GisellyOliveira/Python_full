# Para aumentar e diminuir, precisamos do preço e da taxa como parâmetros:
# Definimos parâmetros opcionais em todas as funções.
# Nessa solução, vamos adicionar o parâmetro "format"que terá como valor opcional "False".

def aumentar(preco = 0, taxa = 0, format=False):
    # return preco + (preco * taxa / 100) # Ao invés de inserir o cálculo no return, vamos definir uma variável para o cálculo.
    res = preco + (preco * taxa / 100)
    # O parâmetro format será definido então numa condicional para podermos optar para ser retornado com a função moeda, que coloca a cifra em frente aos preços, ou sem como valor default.
    return res if format is False else moeda(res)


# As variáveis das funções, apesar de terem os mesmos nomes, são diferentes, pois são variáveis de escopo local.
def diminuir(preco = 0, taxa = 0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco = 0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res) # Mesma condicional das anteriores, porém feita de forma diferente.


def metade(preco = 0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco = 0, ciframoeda = 'R$'):
    return f'{ciframoeda}{preco:>.2f}'.replace('.', ',') # replace substitui todos os pontos (.) por vírgulas (,)
# :>8.2f -> 2 casas decimais, alinhada a direita.
