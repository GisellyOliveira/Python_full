# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

# Começamos especificando que o input é do tipo string.
# Também adicionaremos a propriedade "strip" para remover eventuais espaços vazios no começo e final do nome.
nome = str(input('Digite o seu nome completo: ')).strip()
separa = nome.split()

print('Analisando o seu nome...')
print('O seu nome com todas as letras maiúsculas é {}' .format(nome.upper()))
print('O seu nome com todas as letras minúsculas é {}' .format(nome.lower()))
# Uma vez que eventuais espaços vazios do começo e final da string já foram removidos ao serem atribuidas a variável nome, executaremos uma operação para contar todos os caracteres restantes da string exceto os espaços entre os nomes:
# Para isso chamaremos a contagem do nome com o "len", porém subtrairemos com a propriedade "count" todos os espaços da string durante a contagem. 
print('O total de letras do seu nome é {}' .format(len(nome) - nome.count(' ')))
#Para a solução deste exercício, podemos usar o "find" para mostrar o índice do primeiro espaço, o que também corresponde ao número de letras do primeiro nome já que o primeiro caractere inicia do índice 0. 
print('O seu primeiro tem {} letras.' .format(nome.find(' ')))
# Ou também podemos usar o "split" para separar cada um dos nomes da pessoa numa lista, atribuída a variável separa.
print('O seu primeiro nome é {} e ele possui {} letras.' .format(separa[0], len(separa[0])))
