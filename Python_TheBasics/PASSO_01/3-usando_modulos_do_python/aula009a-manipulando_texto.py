# Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

# No Python, toda cadeia de caracteres, ou string, são representadas por aspas simples '' ou aspas duplas "". (há a possibilidade do uso de aspas triplas em certos casos.)
### Atribuiremos uma cadeia de string com a frase 'Cusro em Vídeo Python'a uma variável chama "frase".
frase1 = 'Curso em Vídeo Python'
# Cada um dos caracteres da frase, incluindo os espaços, ocupam um índice na cadeia da string, sendo o primeiro caractere correspondente ao índice 0.
# Por conta desse índice, podemos executar algumas operações com as strings, como, por exemplo, o fatiamento da string usando um par de colchetes que representa uma coleção, onde passamos o índice do caractere que queremos fatiar. Exemplo:
print(frase1[9]) # O caractere que está contido no nono índice é o V (v maiúsculo e minúculo são caracteres diferentes)

### Podemos também isolar uma parte da cadeia de string passando como parâmetro entre colchetes um 'range' do primeiro caractere a ser contablizado até o último que não será contabilizado. Exemplo:
print(frase1[9:13]) # Fatiará a partir do nono caractere (V) até o décimo terceiro, sendo que o último a entrar na coleçãos será do décimo segundo pois, quando a leitura chegará no décimo terceiro caractere indicado, não mais os contará e efetuará o fatiamento resultando nos carcteres "Víde".

# Considerando que o último caractere corresponde ao índice 20, de definirmos um range do caractere 9 até o 21, ele mostrará os caracteres do 9 até o 20, que corresponde ao último caractere:
print(frase1[9:21])

# Uma outra forma de utilizar o range é adicionando mais um valor ao range que corresponde a um salto do número x de caracteres que foram passados como parâmetro.
# Repetindo o exemplo acima, executaremos o fatiamento do caractere número 9 até o 20 (passando 21 como range), porém determinaremos que ele pulará de 2 em 2 caracteres na contagem dos índices, ignorando um dos caracteres durante o salto:
print(frase1[9:21:2])

# Quando omitimos o índice a iniciar a contagem, ele conta desde o índice 0 até o valor anterior do índice determinado para acabar:
print(frase1[:5]) # Contará do índice 0 ao 4, retornando a palavra "Curso"

# Quando informamos somente o primeiro índice a contar, ele contará do índice indicado até o último:
print(frase1[15:]) # Retornará a palavra "Python"

# No seguinte exemplo, indicaremos o primeiro índice, não indicaremos o último índice, que fará com que seja fatiado do índice 9 até o final, porém indicaremos também o número 3 que determinará de quantos em quantos caracteres ele pulará e quais caracteres serão ignoradas durante esse processo:
print(frase1[9::3]) # Retornará somente os caracteres "VePh"


### Uma outra forma de manipular string é através da ANÁLISE da string, utilizando diversas funçòes como:
# len (lenght): analisa a quantidade de caracteres da string
print(len(frase1)) #Retornará o valor 21 que corresponde a quantidade de caracteres presentes na string

# count -> Contará quantas vezes aparece o caractere indicado
print(frase1.count('o')) # Retorna o valor 3 que corresponde a quantas vezes a letra 'o' aparece na string

# Podemos executar o fatiamento dentro da função count, retornando quantas vezes o caractere está contido dentro o range de caracteres definido:
print(frase1.count('o', 0, 13)) #Retorna o valor 1, pois o 'o' que corresponde ao índice 13 não será incluído, e, sendo assim, o caractere 'o' estará contido no range indicado somente uma vez.

# Podemos transformar todas as letras em maiúsculas com o método upper e então execuatar também o método count para contar quantos O maiúsculos tem na string (utilizando mais de um método juntos):
print(frase1.upper().count('O'))

# find -> encontra em que posição está o caractere que foi indicado ou onde inicia a cadeia de caracteres determinada:
print(frase1.find('deo')) # Retorna que a cadeia de caracteres 'deo'inicia no índice 11

# Se for indicado uma cadeia de caracteres que não existe dentro da string, ele retornará o valor -1:
print(frase1.find('Android'))

# O operador "in" também encontra se uma determinada cadeia de caracteres está presente na string, mas retorna um valor booleano:
print('Curso' in frase1) # Retorna o valor "True", já que a cadeia de caracteres "Curso"está contida na string.

### Uma outra categoria de funcionalidade é a TRANSFORMAÇÃO:
# Em teoria, uma lista de string 'imutável! Mas é possível manipular-la e modifica-la com os métodos.
# replace -> Substitui a cadeia de caracteres indicada por uma nova cadeia.
print(frase1.replace('Python', 'Android')) # Retornerá "Curso em Vídeo Android, mesmo que adicione um índice durante a transformação"

# upper -> Torna todos os caracteres em maiúsculo
print(frase1.upper()) # O upper é um método e é precedido por parênteses obrigatoriamente.

# lower -> Torna todos os caracteres minúsculos
print(frase1.lower()) # É também um método e necessita de parênteses.

# capitalize -> Somente o primeiro caractere será maiúsculo e todos os outros serão minúsculos
print(frase1.capitalize()) #Necessita de parênteses por ser um método.

# title -> Analisa quantas palavras a string possui e coloca em maiúsculo a primeira letra de cada palavra.
print(frase1.title()) # É um método.

###Mudaremos a frase da string para '   Aprenda Python  ', que possui, além do espaço entre as palavras que ocupa 1 índice, 3 índices de espaço no começo e dois no final.
frase2 = '   Aprenda Python  '

# Agora utilizaremos a propriedade "stripe" para remover automaticamente os espaços do começo e do final, mantendo o espaço do meio entre as palavras porém:
print(frase2.strip()) # É um método e retorna "Aprenda Python", sem os espaços do começo e final.

# Com o "rstrip", removemos somente os espaços do lado direito (r = right), ou seja, do final da string.
print(frase2.rstrip()) # Retornerá "   Aprenda Python"

# Com o "lstrip", removemos somente os espaços do lado esquerdo (l = left), ou seja, do começo da string.
print(frase2.lstrip()) # Retornerá "Aprenda Python  "


###Outra categoria de funcionalidades é a DIVISÃO:
# split -> O método split separa cada uma das palavras, armazenando cada uma como um valor individual dentro de uma lista. Desta forma, cada uma das palavras inicia do índice 0.
print(frase1.split()) # É um método e retorna a lista ['Curso', 'em', 'Vídeo', 'Python']

###Outra categoria de funcionalidades é a JUNÇÃO:
# join -> Junta todos os elementos de frase, respeitando a ordem das palavras e inserindo espaçamento e, caso algum caractere seja indicado, será apresentado entre cada uma das letras:
print('-'.join(frase1)) # Reúne os elementos separados em lista anteriormente inserindo o caractere "-" entre cada uma das letras"