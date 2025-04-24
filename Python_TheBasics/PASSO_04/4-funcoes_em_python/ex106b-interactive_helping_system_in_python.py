### ALTERAÇÕES NO CÓDIGO ORIGINAL ###
# -> Organização de cores: As cores foram colocadas no início do código como constantes, com nomes descritivos para facilitar a leitura.
# -> Uso de __doc__ na função ajuda(): A função help() agora utiliza a opção __doc__ para exibir a docstring do comando, o que oferece um output mais organizado.
# -> Validação do comando na função ajuda(): A função agora utiliza um try...except para lidar com comandos que não possuem documentação.
# -> Remoção de sleep(): A função sleep() foi removida, o que torna a experiência do usuário mais fluida.
# -> Consistência de cores: O código agora usa as cores de forma consistente, sempre utilizando as constantes definidas no início do código.
# -> Organização do código: A estrutura do código foi reorganizada para melhorar a legibilidade e facilitar a manutenção.


from time import sleep

# Cores para o terminal
VERMELHO = '\033[0;30;41m'
VERDE = '\033[0;30;42m'
AMARELO = '\033[0;30;43m'
AZUL = '\033[0;30;44m'
ROXO = '\033[0;30;45m'
BRANCO = '\033[7;30m'
SEM_CORES = '\033[m'

def ajuda(com):
    """Exibe a documentação do comando informado."""
    titulo(f'Acessando o manual do comando \'{com}\'', AZUL)
    try:
        print(BRANCO, end=' ')
        print(com.__doc__) # Exibe a docstring do comando
        print(SEM_CORES, end=' ')
    except AttributeError:
        print(VERMELHO, end=' ')
        print(f'A documentação para o comando \'{com}\' não foi encontrada.')
        print(SEM_CORES, end=' ')

def titulo(msg, cor=SEM_CORES):
    """Exibe um título com a cor especificada."""
    tam = len(msg) + 4
    print(cor, end=' ')
    print('˜' * tam)
    print(f'{msg}')
    print('˜' * tam)
    print(SEM_CORES, end=' ')


# Programa principal:
while True:
    titulo('  SISTEMA DE AJUDA PyHELP', VERDE)
    comando = str(input('Digite a função ou biblioteca ou "FIM" para sair: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('  ATÉ LOGO!', VERMELHO)
