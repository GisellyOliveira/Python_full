### MODULARIZAÇÃO ###
# Este será o arquivo principal, composto somente pelo programa principal na mesma pasta do programa secundário:
# Para utilizar as funções que agora estão no arquivo secundário, vamos importar aqui o arquivo que comporta as funções:
import modulo
# Importamos o módulo passando o nome do arquivo que comporta as funções.
    # Também poderíamos utilizar:
# from modulo import fatorial, dobro
    # Esta importação pode gerar conflitos caso outras bibliotecas tenham funções com o mesmo nome.
    # Em alguns casos, o pyhton considera a última funçao a ser criada. Nem sempre ela será a função que precisamos, gerando conflito.


# Programa principal:
num = int(input("Digite um valor: "))
# Quando chamamos uma função que está localizada no módulo importando, precisamos citá-lo na chamada da função da seguinte forma:
fat = modulo.fatorial(num)
print(f'O fatorial de {num} é {fat}')
# Aqui tbm precisamos citar o arquivo importando:
print(f'O dobro de {num} é {modulo.dobro(num)}')
