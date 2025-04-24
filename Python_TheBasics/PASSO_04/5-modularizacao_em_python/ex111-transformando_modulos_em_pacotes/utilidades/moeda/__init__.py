def aumentar(preco=0, taxa=0, cifrao=False):
    '''
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar
    :param taxa: qual é a porcentagem do aumento
    :param cifrao: saída formatada com cifrão da moeda especificado. Parâmetro opcional é False, sem formatação.
    :return: o valor reajustado, com ou sem formato.
    '''
    res = preco + (preco * taxa / 100)
    return res if cifrao is False else moeda(res)


def diminuir(preco=0, taxa=0, cifrao=False):
    '''
    -> Calcula o decréscimo de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar
    :param taxa: qual é a porcentagem do decréscimo
    :param cifrao: saída formatada com cifrão da moeda especificado. Parâmetro opcional é False, sem formatação.
    :return: o valor reajustado, com ou sem formato.
    '''
    res = preco - (preco * taxa / 100)
    return res if cifrao is False else moeda(res)


def dobro(preco=0, cifrao=False):
    '''
    -> Calcula o dobro de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar
    :param cifrao: saída formatada com cifrão da moeda especificado. Parâmetro opcional é False, sem formatação.
    :return: o valor reajustado, com ou sem formato.
    '''
    res = preco * 2
    return res if cifrao is False else moeda(res)


def metade(preco=0, cifrao=False):
    '''
    -> Calcula a metade de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar
    :param cifrao: saída formatada com cifrão da moeda especificado. Parâmetro opcional é False, sem formatação.
    :return: o valor reajustado, com ou sem formato.
    '''
    res = preco / 2
    return res if cifrao is False else moeda(res)


def moeda(preco=0, ciframoeda='R$'):
    '''
    -> Inseri o cifrão correspondente a moeda,
    retornando o resultado formatado.
    :param preco: o preço que se quer formatar
    :param cifraomoeda: saída formatada com cifrão da moeda especificado. Cifrão default é R$. 
    :return: o valor formatado.
    '''
    return f'{ciframoeda}{preco:>.2f}'.replace('.', ',')


# Função resumo para trazer um resumo de todas as informações.
# Definimos como parâmetros o preço (opcional 0), uma taxa para aumentar (opcional 10), e outra para dominuir (opcional 5)
def resumo(preco=0, aumenta=10, diminui=5):
    '''
    -> Tráz todas as funções anteriores apresentadas em uma lista,
    retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar
    :param aumenta: valor da porcentagem de aumentado que será aplicada. O valor default é de 10%
    :param diminui: valor da porcentagem de decréscimo que será aplicada. O valor default é de 5%
    :return: o valor reajustado, com ou sem formatação.
    '''
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40)) #.center(40) para centralizar o texto contendo no espaço total 30 caracteres.
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(preco)}') # \t para tabulação
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumenta}% de aumento: \t{aumentar(preco, aumenta, True)}')
    print(f'{diminui}% de redução: \t{diminuir(preco, diminui, True)}') #-> Essa tabulação está meio bugada!!!
    print('-' * 40)
