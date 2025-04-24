# Para aumentar e diminuir, precisamos do preço e da taxa como parâmetros:
# Definimos parâmetros opcionais em todas as funções.
# Nessa solução, vamos adicionar o parâmetro "format"que terá como valor opcional "False".

# O parâmetro formato foi substituído por cifrao para melhor compreensão..
def aumentar(preco=0, taxa=0, cifrao=False):
    res = preco + (preco * taxa / 100)
    return res if cifrao is False else moeda(res)


def diminuir(preco=0, taxa=0, cifrao=False):
    res = preco - (preco * taxa / 100)
    return res if cifrao is False else moeda(res)


def dobro(preco=0, cifrao=False):
    res = preco * 2
    return res if cifrao is False else moeda(res)


def metade(preco=0, cifrao=False):
    res = preco / 2
    return res if cifrao is False else moeda(res)


def moeda(preco=0, ciframoeda='R$'):
    return f'{ciframoeda}{preco:>.2f}'.replace('.', ',')


# Função resumo para trazer um resumo de todas as informações.
# Definimos como parâmetros o preço (opcional 0), uma taxa para aumentar (opcional 10), e outra para dominuir (opcional 5)
def resumo(preco=0, aumenta=10, diminui=5):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40)) #.center(40) para centralizar o texto contendo no espaço total 30 caracteres.
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(preco)}') # \t para tabulação
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumenta}% de aumento: \t{aumentar(preco, aumenta, True)}')
    print(f'{diminui}% de redução: \t{diminuir(preco, diminui, True)}') #-> Essa tabulação está meio bugada!!!
    print('-' * 40)
