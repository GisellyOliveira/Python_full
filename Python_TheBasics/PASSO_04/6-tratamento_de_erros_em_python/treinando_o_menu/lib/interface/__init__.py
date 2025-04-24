#########################################################################################
### PASSO #2: INSERIMENTO DA FUNÇÃO LeiaInt() para validar a opção do menu recebida ###
#########################################################################################
# Exercício desenvolvido anteriormente para ler um número inteiro com correção de erros.
def leiaInt(msg): # O parâmetro msg é o que será exibido quando será solicitado um número para ser digitado
    while True:
        try:
            n = int(input(msg)) # recebe o input do usuário que tentará ser aceito como número inteiro
        except(ValueError, TypeError): # msg de erro caso não seja digitado um número inteiro
            print('\033[0;31m ERRO! Digite um número inteiro válido. \033[m')
            continue # joga para o laço novamente.
        except KeyboardInterrupt: # msg de erro caso o progama seja interrompido
            print('\033[0;31m Entrada de dados interrompida pelo usuário. \033[m')
            return 0
        else: # se o número inteiro for válido, será retornado o número digitado.
            return n

#########################################################################################
### PASSO #1: CRIAÇÃO DO CABEÇALHO ###
#########################################################################################

# Função para criar linha divisória:
def linha(tam=42): # Padronizamos 42 caracteres como parâmetro opcional
    #print('-' * tam) -> Essa solução retorna um "none" após a linha. Solução utilizando o return:
    return '-' * 42


# Função para criar o título do menu com linha e opções:
def cabecalho(txt):
    print(linha())
    print(txt.center(42)) #center = centralizado | (42) para num. caracteres
    print(linha())


# Função para criar o menu completo, com linhas e título:
def menu(lista): # A função vai receber uma lista
    cabecalho('MENU PRINCIPAL') # inseri linhas e título do menu
    c = 1 # contador para enumerar as opções do menu
    for item in lista:
        print(f'{c} - {item}') # imprimi contador e a item da lista recebida
        c += 1
    print(linha()) # finalizar com linha divisória
    opc = leiaInt('Sua opção: ')
    return opc


