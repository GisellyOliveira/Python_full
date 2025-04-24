# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

# Removemos eventuais espaços no início e final da frase digitada com o módulo "strip()"
frase = str(input('Digite alguma coisa: ')).strip()

# O módulo "upper()" poderia ter sido usado na linha 4 associado ao método "strip()" - .strip().upper() - ao invés de estar contido na linha de cada print.
print('Analisando o texto digitado...')
print('A letra "A" aparece {} vezes no texto digitado.' .format(frase.upper().count('A')))
# Como o índice 0 corresponde à primeira posição, somaremos +1 no resultado do índice que o módulo "find()" retorna.
print('A letra "A" aparece pela primeira vez na posição {}.' .format(frase.upper().find('A')+1))
# Utilizando o módulo "rfind()", buscaremos o caractere a partir do lado direito, encontrando a sua última ocorrência.
print('A letra "A" aparece pela última vez na posição {}.' .format(frase.upper().rfind('A')+1))