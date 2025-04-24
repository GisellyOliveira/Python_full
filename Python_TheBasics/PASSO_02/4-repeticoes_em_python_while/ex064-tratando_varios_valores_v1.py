### LER O FLAG DO LADO DE FORA E DEPOIS LER O FLAG DO LADO DE DENTRO FOI A SOLUÇÃO APRESENTADA PARA QUE O FLAG 999 NÃO FOSSE CONTABILIZADA.
### ESSA SOLUÇÃO NÃO FUNCIONOU AQUI.

# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

# O input do usuário está dentro do laço, desta forma, definimos um valor para essa variável antes para que ela possa ser manipulada dentro do laço: 
n = 0
#Definimos um contador para os números digitados:
cont = 0
#Definimos também a variável que faz a soma dos valores recebidos:
soma = 0
### Como todos esses valores tem o mesmo valor, poderiam ser também escritos da seguinte forma:
# n = cont = soma = 0

# Perguntaremos fora do laço o input do usuário, assim, se o usuário digitar 999, o laço será finalizado e o valor não será contabilizado: Essa soluçao foi comentada pois está excluindo somente o primeiro valor inserido:
#n = int(input('Digite um número ou 999 para parar: '))
while n != 999:
    n = int(input('Digite um número ou 999 para parar: '))
    soma += n
    cont += 1
print('Você digitou {} números e a soma entre eles foi {}. ' .format(cont, soma))
### A VARIÁVEL SOMA NÃO EXCLUI O VALOR 999.
# Uma segunda solução apresentada removendo a última contagem do contador e subtraindo 999 do total da soma::
print('Você digitou {} números e a soma entre eles foi {}. ' .format(cont - 1, soma - 999))
