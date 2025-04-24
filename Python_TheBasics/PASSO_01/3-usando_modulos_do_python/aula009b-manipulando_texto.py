### Um TRUQUE para quebrar linhas do print com um trio de aspas duplas, ou seja, aspas duplas 3x!!!

print("""Quando se vê, já são 6 horas: há tempo…
      Quando se vê, já é 6ª-feira…
      Quando se vê, passaram 60 anos!
      Agora,  é tarde demais para ser reprovado…
      E se me dessem – um dia – uma outra oportunidade,
      eu nem olhava o relógio
      seguia sempre em frente… """)


### Como vimos nesta aula, uma string é imutável. O método replace não modifica permanentemente a string, somente temporariamente.
# Há, porém, a possíbilidade de salvar a alteração feita pelo método dentro da variável que receberá esse novo resultado, podendo desta forma conseguir manipular e alterar permanentemente a string.
frase = 'Curso em Vídeo Python'
frase = frase.replace('Python', 'Android')
print(frase)


### Manipulando uma lista criada com o split de uma string que foi salva dentro de uma variável chamada "dividido":
dividido = frase.split()
print(dividido) # Mostra todos os itens da lista
print(dividido[2]) # Mostra o item no índice dois dentro desta lista. Considerando que o primeiro item ocupa a posição o, no segundo índice encontra-se a palavra "Vídeo"
print(dividido[2][3]) # Mostra o caractere no terceiro índice da palavra que corresponde ao segundo item da lista.