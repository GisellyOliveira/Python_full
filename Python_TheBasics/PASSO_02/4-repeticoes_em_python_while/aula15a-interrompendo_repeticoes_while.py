# Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código. É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.
# Além disso, vamos aprender como trabalhar com as novas fstrings do Python.

cont  = 1
while cont <= 10:
    print(cont, end=' -> ')
    cont += 1
print('Fim')

# Se substituíssemos while cont <= 10: POR while True:
# Se formará um loop eterno. O comando Break quebra esse loop eterno.

### REPETIÇÃO COM FLAG:
# Vejamos o exercício que fizemos onde o número 99 interrompe o programa.
# Pediremos, porém, que o programa some os números digitados sem considerar o valor 999 da flag.
# No exercício anterior, usamos uma "gambiarra"subtraindo o valor 999 do total da soma.
# Agora utilizaremos o "break"para interromper a iteração a qualquer momento.

# Aqui, utilizaremos uma condicional dentro do laço para interromper o programa quando 999 for digitado, sem considerar o seu valor na soma total:
# Iniciaremos as variáveis "n" para o número que pediremos ao usuário e "s" para a soma de todos os valores. Elas começam recebendo o valor 0.
n = s = 0
# Criamos um loop infinito com while True:
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma dos números digitados é {}' .format(s))
