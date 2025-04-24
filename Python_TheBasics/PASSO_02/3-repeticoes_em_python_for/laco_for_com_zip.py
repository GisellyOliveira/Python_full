# Em Python é possível que um comando for percorra sim várias sequências ao mesmo tempo.
# Mas, antes de dizer iss, melhor esclarecer algumas coisas: (1) o for em Python não é, em geral, usado para "contadores". Já que o for sempre vai percorrer uma sequência, o natural é o comando percorrer cada elemento de uma sequência, não o índice do elemento (para depois, dado o índice, extrair o elemento da sequência). Em outras linguagens essa construção em geral leva o nome de "for each":

for letra in "palavra":
   print(letra)

# em vez de:

for i in range(len("palavra")):
   letra = "palavra"[i]
   print(letra)

# E (2): poder "ver" ao mesmo tempo uma letra e a letra seguinte não vai te ajudar com esse problema da questão em particular - você vai precisar de dois for um dentro do outro mesmo.
# Então, em Python, o comando for usa o elemento sobre o qual vai interagir como um "iterador". Ou seja, for item in minhalista: vai chamar o equivalente a iter(minhalista), e no objeto (vamos chamar de ITER) retornado por isso, vai fazer o equivalente a next(ITER). Quando a chamada ao next falhar (com uma exeção interna de "StopIteration") o for é encerrado.
# Se o iterador usado no for retornar uma sequência, os valores retornados pela sequência são distribuidos para as variáveis do for.
# No caso mais simples, se eu tiver:

a = [1,2], [3,4], [5,6]
for b, c in a:
   print(b, c)

# O laço vai se repetir 3 vezes e a cada vez um item da sequência interna vai estar em b, e o outro em c.

# No caso de sequências, se você quer combinar elementos das mesmas no for, há a chamada conveniente zip- que pega um elemento de cada sequência e entrega de forma que pode ser usado no for:

a = range(10)
b = range(10, 20)

for c, d in zip(a, b):
   print(c,d)

# No caso de uma string, se desejar pegar sempre uma letra e a próxima letra é possível fazer:

a = "meu texto"
for letra1, letra2 in zip(a, a[1:]):
    print(letra1, letra2)

# (a[1:] é simplesmente a string em a a partir da letra de índice "1" até o final, ou seja, se a string for "palavra", na primeira interação serão usadas as letras "p" e "a")