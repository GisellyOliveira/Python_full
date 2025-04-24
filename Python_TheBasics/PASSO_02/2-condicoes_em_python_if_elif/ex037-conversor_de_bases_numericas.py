# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

print('\033[30;42m-' * 40)
print('\033[30;42mCONVERSOR DE BASES:')
print('\033[30;42m-\033[m' * 40)
numero = int(input('Digite um número inteiro: '))

# Vamos utilizar aspas triplas ''' no começo e final do print para que todo o exto seja apresentado em linhas separadas:
print('''ESCOLHA UMA DAS BASES PARA CONVERSÃO:
[ 1 ] CONVERSÃO BINÁRIO
[ 2 ] CONVERSÃO OCTAL
[ 3 ] CONVERSÃO HEXADECIMAL''')
opcao = int(input('Qual a sua opção? '))

# Os dois primeiros caracteres da conversão são correspondete ai tipo de conversão, sempre 0b para binário, 0o para octal e 0x para hexadecimal.
# Vamos fatiar os dois primeiros índices tratando esses dados entre chaves para excluir os dois primeiros índices -> ex: .format(numero, bin(numero)[2:]):

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}.' .format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}.' .format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.' .format(numero, hex(numero)[2:]))
else:
    print('\033[41mOPCÃO INVÁLIDA! TENTE NOVAMENTE!')

