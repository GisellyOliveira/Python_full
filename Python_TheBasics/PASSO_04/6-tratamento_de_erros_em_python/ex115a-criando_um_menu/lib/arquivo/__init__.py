from lib.interface import cabecalho

# Função para verificar se o arquivo existe
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # A função open abre um arquivo. Como parâmetro, recebe o nome do arquivo e 'rt'para 'read & text', pois queremos abrir um arquivo txt.
        a.close() # E então vamos fechar o arquivo
    # Se o arquivo não for encontrado, retornaremos, False:
    except FileNotFoundError:
        return False
    # Senão, se o arquivo abriu e fechou em try, vamos retornar True:
    else:
        return True


# Função para criar um novo arquivo
def criarArquivo(nome):
    # A função cria um arquivo com open, cujos parâmetros são o nome do arquivo e 'wt+' para write a text, e + para criar o arquivo caso ele não exista.
    try:
        a = open(nome, 'wt+') 
        a.close() # para fechar o arquivo depois de criar
    # Se não for possível criar o arquivo:
    except:
        print('Houve um ERRO na criação do arquivo!')
    # Se tiver sucesso na criação do arquivo:
    else:
        print(f'Arquivo {nome} criado com sucesso!')


# Função para ler o arquivo e mostrar os dados do arquivo
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        #print(a.readlines()) # Pega aslinhas do arquivo e coloca dentro de uma lista
        #print(a.read()) # Melhor apresentação do conteúdo do arquivo. Vamos utilizar outro método.
        for linha in a:
            ### Opção Guanabara não funciona ###
            #dado = linha.split(';')
            #dado[1] = dado[1].replace('\n', '')
            #print(f'{dado[0]}{dado[1]}')
            dado = linha.split(':')  # Corrigido para usar ':' como separador
            print(f'{dado[0].strip():<30} {dado[1].strip():>3} anos')  # Adiciona strip() para remover. Imprimi nome e idade de cada um.
    finally:
        a.close() # dandon certo ou errado, vamos finalizar fechando o arquivo



# Função para cadastrar pessoas:
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') # at = append text file, vai dar um append no texto
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try: # outro try caso de algum erro na criação do arquivo
            a.write(f'{nome}: {idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo cadastro de {nome} adicionado.')
            a.close()
        
