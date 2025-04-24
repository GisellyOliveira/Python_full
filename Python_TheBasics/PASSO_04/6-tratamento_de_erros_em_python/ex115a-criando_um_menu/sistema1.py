# * para importar tudo da biblioteca.
from lib import interface
from lib.arquivo import * 
from time import sleep


# Verificar se um determinado arquivo existe:
arq = 'cursoemvideo.txt'

'''
# Criamos a função arquivoExiste() para verificar se o arquivo existe, ou não: 
# Etestamos nas linhas abaixo:

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado.')
    # E vamos criar um arquivo com o valor atribuído a variável arq:
    criarArquivo(arq)
'''

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
        interface.cabecalho('Opção 2')
    elif resposta == 3:
        interface.cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(1)
    