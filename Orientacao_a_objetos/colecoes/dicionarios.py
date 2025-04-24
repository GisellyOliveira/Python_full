# Os dicionários são definidos por {}.
# São coleções desordenadas, mutáveis e indexadas com chaves e valores.
# As chaves de um dicionário precisam ser únicas e de tipos imutáveis, como strings, números ou tuplas.
# Já os valores de um dicionário podem ser de qualquer tipo.

# criar e imprimir um dicionário:
notas = {"Ana": 8, "Maria": 5, "Thais": 10}
print(notas)

# acessar o valor correspondente à chave "Thais":
print("Selecionando o valor da chave Thais: ", notas["Thais"])

# incluir novo item:
notas["Zaira"] = 9
print("Adicionando uma nova chave Zaira com valor 9: ", notas)

# remover item:
del notas["Thais"]
print("Removendo a chave \"Thais\": ", notas)

# checar se notas comtém o item "Maria"
print("Tem Maria no dicionário notas? ","Maria" in notas)
