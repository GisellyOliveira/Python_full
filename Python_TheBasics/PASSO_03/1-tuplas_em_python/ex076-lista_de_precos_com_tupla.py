# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Lápis', 1.75, 
         'Borracha', 2,
         'Carderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS:":^40}') # Fstring centralizada ocupando 40 caracteres
print('-' * 40)

# Laço para validar os índices pares e ímpares.
# Os pares serão alinhados a esquerda, contendo os nomes dos produtos.
# Os ímpares serão alinhados a esquerda.
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end='') # Alinahdo a esquerda, ocupando 30 caracteres
    else:
        print(f'R${lista[i]:>7.2f}') # Alinhado a direita, ocupando 7 caracteres e apresentando como número do tipo flot ocupando 2 casas decimais.

print('-' * 40)