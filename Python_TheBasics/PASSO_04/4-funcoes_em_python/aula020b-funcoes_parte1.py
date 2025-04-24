### Funcão para somar 2 valores:
def soma(a, b):
    s = a + b
    print(s)


# Programa principal, passando 2 diferentes parâmetros para serem somados:
soma(4, 5)
soma(a=8, b=9) # Pode explicitar o valor dos parâmetros
soma(b=2, a=1) # Pode alterar a ordem dos parâmetros desde que seja explícito.

### Empacotar parâmetros:
# Função que conta o número de parâmetros: * = desempacotador:
def contador(* num):
    print(num)
    # Podemos utilizar as tuplas retornadas em laços de repetição:
    for valor in num:
        print(f'{valor} ', end=' ')
    print('FIM')
    # Utilizando a função len():
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


# Definimos um contador que retorna tuplas com os valores foram passados dentro do parâmetro:
contador(5, 7, 3, 1, 4)
contador(8, 9)
contador(4, 4, 7, 6, 2)