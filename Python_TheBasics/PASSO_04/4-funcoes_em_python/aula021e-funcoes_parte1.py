# Função que calcula o número fatorial:
def fatorial(num=1): # 1 foi passado como parâmetro opcional.
    f = 1 # variável local
    for c in range(num, 0, -1): # começa no número até 0, voltando de 1 em 1.
        f *= c
    return(f)


n = int(input('Digite um número: '))
print(fatorial(n))
print(f'O fatorial de {n} é igual a {fatorial(n)}.')

# ou então:
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')


print('=' * 40)
### O return pode retornar um valor lógico, verdadeiro ou falso, etc.
def par(n=0):
    if n % 2 == 0:
        return True # retorna True se o número for PAR
    else:
        return False # retorna False se o número for ÍMPAR


num = int(input('Digite um número: '))
print(par(num))
#ou
if par(num):
    print('É PAR!')
else:
    print('NÃO é PAR!')
