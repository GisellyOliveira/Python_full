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


# Função para criar linha divisória
def linha(carac = '-', tam = 42):
    return carac * tam


# Cabeçalho com linhas divisórias e texto
def cabecalho(txt):
    print(linha())
    print(txt.center(42)) #center para centralizar, 42 caracteres ao total
    print(linha())


# Menu com cabeçalho e opções cadastradas
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1 # contador
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
    


