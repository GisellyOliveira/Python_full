# Ao invés de trabalharmos com as tuplas, como nos exemplos anteriores, podemos também trabalhar com listas:
# Suponhamos que temos uma lista com diferentes valores:
# Suponhamos que desejamos dobrar os valores contidos dentro da lista valores:
def dobra(lst):
    pos = 0 # Criamos um contador
    while pos < len(lst): # enquanto o contador for menor que o tamanho de itens da lista
        lst[pos] *= 2 #o parâmetro recebido é multiplicado por 2
        pos += 1 # e o contador recebe um valor a mais para continuar o laço.

valores = [7, 2, 5, 0, 4] # Cada um desses valores tem um índice
dobra(valores)
print(valores)

# Esse processo não é um desempacotamento.
# Poderíamos utilizar o desempacotamento:
def soma(* numeros):
    s = 0
    for num in numeros:
        s += num
    print(f'Somando os números {numeros} temos {s}')


soma(5, 2)
soma(2, 9, 4)
