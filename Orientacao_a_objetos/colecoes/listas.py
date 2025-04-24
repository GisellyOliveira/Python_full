# As listas são similares aos arrays e são definidas por [].
# São sequências mutáveis e ordenadas, normalmente usadas para armazenar coleções de itens.

### Exemplo:
numeros = [1, 10, 100, 1000]
print(numeros)

# imprimir o elemento de índice 2 - o primeiro índice é 0
print("O elemento no índice 2 é: %d"
      % (numeros[2]))


### Operações de Listas:
# incluir 2 itens na lista usando +=
numeros += [10000, 100000]
print("A lista agora é composta por: ", numeros)

# incluir 1 item na lista usando append
numeros.append(1000000)
print("A lista agora chega a um milhão: ", numeros)

# substituir os itens dos índices 1 e 2 da lista por 7
# [índice_incluído:índice_excluído]
numeros[1:3] = [7]
print("Substituição dos itens dos índices 1 e 2 pelo valor 7: ", numeros)

# remover os itens nas posições 1 e 2 da lista
numeros[1:3] = []
print("Removendo itens dos índices 1 e 2: ", numeros)

# tamanho da lista
print("Quantidade de itens remanescentes: ", len(numeros))
