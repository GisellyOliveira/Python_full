# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. 
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

# Variável para contagem do valor total da compra: total
# Variável para contagem dos produtos que custam mais de R$1000.
# Variáveis para a contagem do menor preço: menor, cont
total = totmil = menor = cont = 0
# Ainda será necessário uma variável para capturar o [produto correspondente ao menor preço:
barato = ' '

# Apresentação
while True:
    titulo = '\033[1;41m >>> LOJA SUPER BARATÃO <<< \033[m'
    print('-' * 28)
    print(f'{titulo:^30}')
    print('-' * 28)

    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    # Contador que servirá para encontrar o menor preço dentro da condicional mais abaixo:
    cont += 1
    # Atribuimos ao total o valor do preço recebido:
    total += preco
    # Checando e contando se custa mais de mil reais:
    if preco > 1000:
        totmil += 1
    '''
    # O primeiro preço recebido sempre será o menor.
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    '''
    # Trecho comentado acima simplificado:
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    # Ativamos uma variavél vazia que receberá, dentro do loop, a resposta do usuário para continuar ou não. Toda vez que não for digitado nenhuma das opções solicitadas, o computador repete a pergunta.
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break

print('{:-^40}' .format('\033[1;47m FIM DO PROGRAMA \033[m'))
print(f'O total das compras é R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00.')
print(f'O produto mais barato foi {barato} que custa {menor}')
