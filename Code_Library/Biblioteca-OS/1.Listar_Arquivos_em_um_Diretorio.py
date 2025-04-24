# LISTAR ARQUIVOS EM UM DIRETÓRIO

# PASSO 1
import os

# PASSO 2
class ListarArquivos:

    # PASSO 3
    def __init__(self, diretorio):
        # PASSO 4
        self.diretorio = diretorio
    

    # PASSO 5
    def listar(self):
        # PASSO 6
        arquivos = os.listdir(self.diretorio)
    
    # PASSO 7
        for arquivo in arquivos:
            # PASSO 8
            print(arquivo)


# PASSO 9
diretorio_atual = os.getcwd()

# PASSO 10
listador = ListarArquivos(diretorio_atual)

# PASSO 11
listador.listar()



########################################################################
# PASSO-A-PASSO:
########################################################################

# PASSO 1. Importa a biblioteca "os", que fornece funções para interagir com o sistema operacional,
# incluindo manipulação de arquivos e diretórios.

# PASSO 2. Define uma classe chamada "ListarArquivos".
# O objeto dessa classe é fornecer uma maneira organizada de listar arquivos em um diretório.

# PASSO 3. Método construtor da classe, executado quando um objeto da classe é criado.
# Recebe como argumento o caminho do diretório ("diretorio") que se deseja listar os arquivos.
# O argumento "self" é uma referência ao próprio objeto, permitindo acesso aos atribustos e métodos da classe.

# PASSO 4. Armazena o caminho do diretório recebido como argumento no atributo "diretorio" do objeto.
# Isso torna o caminho do diretório acessível a outros métodos da classe.

# PASSO 5. Método da classe que lista os arquivos presentes no diretório especificado.

# PASSO 6. Utiliza a função "os.listdir()" da biblioteca "os" para obter uma lista dos arquivos e subdiretórios
# presentes no diretório armazenado no atributo "self.diretorio".
# A lista é armazenada na variável "arquivos".

# PASSO 7. Inicia um loop "for" para iterar sobre cada elemento da lista "arquivos".
# A cada iteração, a variável "arquivo" recebe o nome de um arquivo ou subdiretório.

# PASSO 8. Imprime o nome do arquivo ou subdiretório no console.

# PASSO 9. Chama a função "os.getcwd()" da biblioteca "os" para obter o caminho completo do diretório atual
# (onde o script Python está sendo executado).
#  Armazena o caminho obtido na variável "diretorio_atual".

# PASSO 10. Cria um objeto da classe "ListarArquivos", passando o caminho do diretório atual como argumento.
# O objeto criado é atribuído à variável "listador".

# PASSO 11. Chama o método "listar()" do objeto "listador". Isso executa o código dentro do método "listar()",
# que lista os arquivos presentes no diretório especificado durante a criação do objeto (no caso, o diretório atual).