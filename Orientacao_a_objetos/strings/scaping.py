# -*- coding: utf-8 -*-
"""
Exemplos de escaping em Python.

Demonstração do uso de caracteres de escape para incluir 
caracteres especiais dentro de strings.
"""

# Usando \ para escapar aspas simples dentro da string
frase1 = 'Ele disse: \'Olá!\' '
print(frase1)  # Saída: Ele disse: 'Olá!' 

# Usando \ para escapar aspas duplas dentro da string
frase2 = "Ela respondeu: \"Oi, tudo bem?\""
print(frase2)  # Saída: Ela respondeu: "Oi, tudo bem?"

# Usando \n para criar uma quebra de linha
frase3 = "Esta é uma frase\ncom duas linhas."
print(frase3)
# Saída: 
# Esta é uma frase
# com duas linhas.

# Usando \t para inserir uma tabulação horizontal
frase4 = "Nome:\tJoão\nIdade:\t30"
print(frase4)
# Saída:
# Nome:   João
# Idade:  30

# Usando uma raw string (r) para caminhos de arquivo no Windows
# Observe que as barras invertidas não são interpretadas como caracteres de escape
caminho_windows = r'C:\Users\Documentos\arquivo.txt'
print(caminho_windows)  # Saída: C:\Users\Documentos\arquivo.txt