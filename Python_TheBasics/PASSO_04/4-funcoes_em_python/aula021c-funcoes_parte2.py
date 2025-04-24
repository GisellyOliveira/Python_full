### ESCOPO DE VARIÁVEIS ###

## >>> ESCOPO GLOBAL <<< ##
# Vamos supor uma variável n que recebe valor 2.
# Inserimos uma função sem parâmetro e vejamos qual valor é atribuído a n se a usarmos dentro da função:

def teste():
    print(f'Na função teste, n vale {n}, pois tem escopo global.') # -> n vale 2

# Programa principal:
n = 2
print(f'No programa principal, n vale {n}, pois o escopo global compreende todo o código.') # -> n vale 2
teste()
print('=' * 80)


# A variável tem escopo global, pois o seu valor será recebido em todo o escopo do programa.
# Variável com escopo global é declarada no programa principal.


## >>> ESCOPO LOCAL <<< ##
# Quando uma variável e declarada dentro de uma função, ela tem escopo local.
# Se dermos um print na variável fora do seu escopo, ou seja, fora da função, o retorno será um erro.
def teste1():
    x = 8
    print(f'A variável x tem valor {x} somente dentro da função, pois tem escopo local.')


teste1()
print('=' * 80)


# Neste exemplo, declaramos uma variável fora da função e dentro da função com outro valor.

def teste3(param): 
    # Se declararmos a mesma variável dentro da função com outro valor,
    # esse outro valor terá somente escopo local, dentro da função.
    # O parâmetro recebido porém, será sempre o de escopo global.
    v = 8
    param += 4
    print(f'> Aqui a variável recebe o valor {v} somente dentro do escopo da função.')
    print(f'> E aqui o parametro da função recebe o valor da variável e soma ao valor 4 somente dentro da função, resultando em {param}.')


# Programa principal:
v = 5
print(f'> A variável fora da função tem valor {v} e escopo global.')
teste3(v)


print('=' * 80)
## ALTERANDO O VALOR DA VARIÁVEL DE ESCOPO GLOBAL DENTRO DA FUNCÃO ##
# É possível alterar o valor de uma variável de escopo global dentro da função da seguinte forma:
def maisUmTeste(x):
    global y
    y = 9


y = 4
print(f'Y recebe o valor {y} com escopo global.')
maisUmTeste(y)
print(f'Com > global y < especificado dentro da função, ela foi alterada dentro da função e passa a valer {y} globalmente.')
    