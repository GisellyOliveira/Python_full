# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro 
# o ano de nascimento de uma pessoa, retornando um valor literal 
# indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import date # importação da biblioteca dentro da função, válida somente dentro do escopo da função (consome menos espaço na memória pois é utilizado somente durante a execução da função)
    #global nascimento
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nascimento = int(input('Ano de nascimento: '))
print(voto(nascimento))
