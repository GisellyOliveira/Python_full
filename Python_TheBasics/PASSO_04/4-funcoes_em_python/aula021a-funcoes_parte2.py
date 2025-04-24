# help() é uma função interna do python para acessar o INTERACTIVE HELP do python.
# O INTERACTIVE HELP é uma documentação muito completa sobre todas as funcionalidades do python.
# Também pode ser usada no código, utilizando a função help() e passando como parâmetro o assunto a ser pesquisado, ex.:
help(input) # Busca a documentação da função interna input()
### Retorna:
#Read a string from standard input.  The trailing newline is stripped.

#The prompt string, if given, is printed to standard output without a
#trailing newline before reading input.

#If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
#On *nix systems, readline is used if available.
# (END) -> q para sair

### Essa informação também pode ser acessada imprimindo a documentação do comando da seguinte forma:
# print(comandoquedesejamos.__doc__)
# Vamos imprimir a documentação do comando inpu, por exemplo:
print(input.__doc__)

