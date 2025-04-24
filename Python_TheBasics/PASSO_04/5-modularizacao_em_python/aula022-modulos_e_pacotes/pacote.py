### O arquivo pacote contém somente o programa principal.  
# Importaremos o pacotenumeros para ser utilizado aqui. Ele executará as funções de cálculo numéricos feitos anteriormente, agora contindos no arquivo __init__ dentro do modulo "modulonumeros".
# Importando o "pacotenumeros"dentro da pasta pacote:
from pacote import pacotenumeros

# Programa principal:
num = int(input("Digite um valor: "))
# Quando chamamos uma função que está localizada no pacotenumeros, na pasta pacotes (toda pasta é um pacote), precisamos citá-lo na chamada da função da seguinte forma:
fat = pacotenumeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
# Aqui tbm precisamos citar o pacote importado:
print(f'O dobro de {num} é {pacotenumeros.dobro(num)}')