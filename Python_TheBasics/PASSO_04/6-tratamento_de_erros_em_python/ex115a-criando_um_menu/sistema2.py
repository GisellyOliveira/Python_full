# Vamos finalizar o projeto de acesso a arquivos em Python.

# * para importar tudo da biblioteca.
from lib import interface
from lib.interface import *
from lib.arquivo import * 
from time import sleep


# Verificar se um determinado arquivo existe:
arq = 'cursoemvideo.txt'


# So irá criar o arquivo se o arquivo não existe. Se não existe, vamos chamar a função criarArquivo():
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta= interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do sistema'])
    if resposta == 1:
        #interface.cabecalho('Opção 1')
        # Opção de listar o conteúdo de um arquivo:
        lerArquivo(arq)
    elif resposta == 2:
        #interface.cabecalho('Opção 2')
        #Opção de cadastrar uma pessoa:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        interface.cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(1)
    