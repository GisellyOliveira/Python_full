# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: 
# a média de idade do grupo, 
# qual é o nome do homem mais velho e 
# quantas mulheres têm menos de 20 anos.

# Para o cálculo da média da idade do grupo, setaremos duas variáveis:
somaidade = 0
mediaidade = 0
# Para o cálculo do homem mais velho e seu respectivo nome, setaremos mais duas variáveis: uma para capturar a maior idade e outra vazia que capturará o seu nome.
maioridadehomem = 0
nomevelho = ''
# Variáveis para calcular quantas mulheres tem ais de 20 anos:
totmulher20 = 0 


for p in range(1, 5):
    print('>>> {}ª PESSOA <<<' .format(p))
    nome = str(input('Digite o seu nome: ')).strip()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip()
    # Vamos setar uma variável para somar as idades recebidas:
    somaidade += idade
    # Usaremos uma condicional para atribuir o peso do primeiro HOMEM como o maior, assim como seu nome.
    # Se houvéssemos usado o "upper()", poderíamos escrever essa linha para receber o m maiúsculo e minúsculo da seguinte forma: 
    # if p == 1 and sexo == 'M':
    # Mas vamos usar o 'in' para receber o m maiúsculo ou minúsculo:
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    # Para os outros laços, o HOMEM que tiver maior idade será substituído no laço:
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    # Para calcular quantas mulheres tem menos de 20 anos:
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

# A variável "mediaidade" recebe a soma de todas as idades do laço acima:
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.' .format(mediaidade))
# Retorna o nome do homem mais velho e sua idade:
print('O nome do homem mais velho tem {} anos e se chama {}.' .format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.' .format(totmulher20))
    