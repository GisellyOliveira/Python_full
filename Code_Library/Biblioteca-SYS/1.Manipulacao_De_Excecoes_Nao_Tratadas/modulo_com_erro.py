# modulo_com_erro.py

def funcao_que_falha():
    """Esta função contém código que gera uma exceção não tratada."""
    print("--- Dentro do modulo_com_erro.funcao_que_falha ---")
    print("Preparando para causar um erro...")

    # Escolha uma das linhas abaixo para causar o erro:
    
    # OPÇÃO 1: Divisão por zero
    resultado = 10 / 0

    # OPCÃO 2: Variável inexistente 
    #print(variavel_que_nao_existe)

    # OPÇÃO 3:
    #lista = [1, 2]
    #print(lista[5])

    # IMPORTANTE: Não coloque um try try...except aqui dentro
    # se você quiser que o sys.excepthook global seja acionado

    print("Esta linha DENTRO de funcao_que_falha NUNCA será executada.")


print("Módulo modulo_com_erro.py foi importado.") # Descomente para ver quando é importado
