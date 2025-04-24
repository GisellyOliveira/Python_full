# -*- coding: utf-8 -*-

# Em programação, é muito comum o usuário querer executar um comando apenas se determinada condição for atendida. 
# Para isso, há os operadores if (se), else (senão) e elif (senão-se), 
# que sempre retornam um resultado booleano (True ou False) e podem ser utilizados em conjunto com operadores de igualdade, lógicos e de comparação.

"""
Exemplo simples do operador if em Python.
"""

# Definindo a idade de uma pessoa
idade = 20

# Verificando se a pessoa é maior de idade (>= 18 anos)
if idade >= 18:
    # Este bloco de código só é executado se a condição (idade >= 18) for verdadeira
    print("Você é maior de idade.")
else:
    # Este bloco de código só é executado se a condição (idade >= 18) for falsa
    print("Você é menor de idade.")

# Exemplo adicional com notas
nota = 7.5

if nota >= 7:
    print("Parabéns! Você foi aprovado!")
elif nota >= 5:  # else if - Verifica outra condição se a anterior for falsa
    print("Você está de recuperação.")
else:
    print("Infelizmente, você foi reprovado.")
    