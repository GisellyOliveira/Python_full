from lib.interface import *
from time import sleep

# 1- Vamos passar uma lista como parâmetro da função menu que está no módulo interface:
# menu(['Ver lista', 'Cadastrar pessoas', 'Sair do sistema'])

# 2- Criar laço infinito para gerar as opções do menu:
while True:
    # A lista com a função menu serão armazendas na variável resposta:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    # E agora determinamos com condicionais o comportamento do programa quando o usuário digitar uma opção:
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema.. Até logo!')
        break
    else:
        print('Erro! Digite uma opção válida!')
    sleep(2)
    

