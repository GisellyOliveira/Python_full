# Calculadora simples em Python
# A calculadora será composta por 3 funções: a primeira imprime uma mensagem de abertura, 
# a segunda função faz cálculos de adição, subtração, multiplicação e divisão,
# e a terceira funcão que pergunta se quer calcular novamente ou sair do programa.

# 1. Mensagem de abertura
def bem_vindo():
    print("*************************************")
    print(">>> Calculadora simples em Python <<<")
    print("*************************************")


# 2. Função para fazer operações:
def calcular():

    print("\nQual operação deseja executar? (1) Soma  (2) Subtração  (3) Multiplicação  (4) Divisão  (5) Outra")
    operacao = int(input("Digite a operação a ser realizada: "))

    if(operacao != 1 and operacao != 2 and operacao != 3 and operacao != 4):
        print("Desculpe, esta calculadora ainda não suporta outras operações. Por favor, execute o programa novamente.")
        return
    
    primeiro_numero = float(input("Digite o primeiro número: "))
    segundo_numero = float(input("Digite o segundo número: "))

    if operacao == 1:
        soma = primeiro_numero + segundo_numero
        print("O resultado é %.2f" % soma)
    
    if operacao == 2:
        subtracao = primeiro_numero - segundo_numero
        print("O resultado é %.2f" % subtracao)
    
    if operacao == 3:
        multiplicacao = primeiro_numero * segundo_numero
        print("O resultado é %.2f" % multiplicacao)
    
    if operacao == 4:
        divisao = primeiro_numero / segundo_numero
        print("O resultado é %.2f" % divisao)
    

    calcular_outra_vez()



def calcular_outra_vez():
    outra_vez = str(input("Deseja realizar outra operação? Digita S para SIM e N para NÃO: ").strip().upper())
    
    if outra_vez[0] == "S":
        calcular()
    elif outra_vez[0] == "N":
        print("Até a próxima!")
    else:
        print("Opção inválida.")
        calcular_outra_vez()



bem_vindo()
calcular()
    