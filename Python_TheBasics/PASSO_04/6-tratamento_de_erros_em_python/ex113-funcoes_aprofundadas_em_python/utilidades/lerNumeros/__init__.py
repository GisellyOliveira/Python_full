# Função Guanabara para ler números inteiros com tratamento de erros:
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31m ERRO! Digite um número inteiro válido. \033[m')
            continue # joga para o laço novamente.
        except KeyboardInterrupt:
            print('\033[0;31m Entrada de dados interrompida pelo usuário. \033[m')
            return 0
        else:
            return n


# Função sem bugs para ler números float:
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31m ERRO! Digite um número inteiro válido. \033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31m Entrada de dados interrompida pelo usuário. \033[m')
            return 0
        else:
            return n
