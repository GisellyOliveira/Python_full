# fstring: lançada numa nova PEP, está presente a partir do python 6.3.0 e substitui o .format()

n = s = 0
while True:
    n = int(input('Digite um número ou 999 para parar: '))
    if n == 999:
        break
    s += n

# Inserindo a letra "f" antes das aspas da string, o pythion fará a INTERPOLAÇÃO DENTRO DE STRINGS!
# Isso quer dizer que podemos passar a variável diretamente dentro dos colchetes, sem usar o .format()
print(f'A soma dos números digitados vale {s}')


### Vejamos aqui diferentes versões usadas no Python2, Python3 e Python3.6:
nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.') #Python3.6+
print('O {} tem {} anos.' .format(nome, idade)) #Python3
print('O %s tem %d anos.' %(nome, idade))  #Python2

# Vejamos mais exemplos das fstrings:
salario = 987.35
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')
# As formatações que utilizamos também funcionam dentro das fstrings:
print(f'{nome:20}') #O nome aparece no espaço de 20 caracteres
print(f'{nome:^20}') #O nome aparece no espaço de 20 caracteres e centralizado
print(f'{nome:-^20}') #O nome aparece no espaço de 20 caracteres, centralizado com traços nos espaços vazios do início e final.
print(f'{nome:->20}') #O nome aparece no espaço de 20 caracteres, à direita, com traços nos espaços vazios iniciais.
print(f'{nome:-<20}') #O nome aparece no espaço de 20 caracteres, à esquerda, com traços nos espaços vazios finais.
