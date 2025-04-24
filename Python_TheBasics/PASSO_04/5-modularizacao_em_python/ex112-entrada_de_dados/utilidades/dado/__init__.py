def leiaDinheiro(msg):
    valido = False
    while not valido:
        # Replace() substitui a vírgula das casas decimais pelo ponto
        # O strip() remove os espaços inciais e finais de entrada.
        entrada = str(input(msg)).replace(',','.').strip()
        # Validando entrada alphanúmerica ou vazia com retorno de msg de erro.
        if entrada.isalpha() or entrada == '': 
            print(f'\033[0;31m ERRO: \"{entrada}\" é um preço inválido! \033[m')
        else:
            valido = True
            return float(entrada)

# Vamos definir uma função que já foi feita anteriormente para ler inteiro:
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m ERRO! Digite um número inteiro válido. \033[m')
        if ok:
            break
        return valor
