# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

### ESTA SOLUÇÃO SE APLICA SOMENTE A LINGUAGEM PYTHON:

# Primeiro, definimos um input para o usuário digitar a frase. O input será já tratado revomendo eventuais espaços no início ou final da frase:
frase = str(input('Digite uma frase: ')).strip().upper()
# Definimos então uma variavél que receberá, utilizando o "split", cada uma das palavras da frase digitada dentro de uma coleção. A separação de cada uma das palavras removerá todos os eventuais espaços entre cada uma das palavras da frase.
palavras = frase.split()
# Definimos mais uma variável para receber, juntas e sem espaço '', todas as palavras que foram separadas e estão dentro da variável "palavras" , da seguinte forma:
junto = ''.join(palavras)

# print('Você digitou a frase {}, formadas pelas palavras {}, resultando em {}' .format(frase, palavras, junto))

'''
### Esta seria a lógica da primeira versão deste exercício:
# Agora que temos toda a frase em maiúscula e sem espaços, vamos definir uma varável que receberá o inverso da frase digitada. A princípio ela receberá um valor vazio:
inverso = ''
# E utilizamos uma iteração para ler da última letra até a primeira, invertendo a frase desta forma.
# Para isso, é necessário capturar a última letra que será digitada. Utilizamos: len(junto) -1. O índice que o "len" conta da variável tudo junto -1 corresponderá ao índice da última letra digitada.
# Utilizamos -1 para que o contador leia até a letra que se encontra no índice 0.
# Utilizamos -1 para que o contador leia no ordem reversa.
# O contador, desta vez, se chamará "letra".
for letra in range(len(junto) -1, -1, -1):
    # Este print retorna no console a frase já invertida.
    # print(junto[letra])
    # Porém queremos atribuir essa inverão à variável "inverso", sendo inverso = inverso + junto[letra]
    inverso += junto[letra]
# Este print mostra frase digitada assim como ao contrário.
'''

### Utilizaremos uma linha de código que resumirá toda a ação anterior, atribuindo a variável "inverso" o conteúdo de "junto" invertido:
# Não passaremos parâmtros para indicar e ele lerá do final ao início, atribuindo o -1 para que essa leitura seja feita da forma inversa.
inverso = junto[::-1]

print('O inverso de {} é {}' .format(junto, inverso))
# Como queremos saber se é um palíndromo, utilizaremos uma condicional para verificar se as variáveis "juntos" e "inverso" contém os mesmos caracteres:
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
    