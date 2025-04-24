# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.

# O "strip()" vai eliminar eventuais espaços tenham sido digitados no começo da string (e também no final).
cidade = str(input('Digite o nome de uma cidade: ')).strip()

# o parâmetro :5 (correspondente a 0:5) vai ler os caracteres do índice 0 ao 4.
# Para evitar que caracteres maiúsculos ou minúsculos interfiram no resultado, buscaremos um padrão tratando o dado com o "upper()" para padronizar o resultado em caracteres maiúsculos.
# Uma vez que o nome da cidade foi convertido em maiúsculas, será verificado se ele for == 'SANTO'. O console retorna True ou False.
print(cidade[:5].upper() == 'SANTO') 