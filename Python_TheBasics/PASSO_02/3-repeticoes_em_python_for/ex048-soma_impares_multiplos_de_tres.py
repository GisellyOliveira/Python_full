# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# Primeiramente é gerado um acumulador, ou seja, uma variável que recebe o valor 0 para ser somada ao valor da variável "c" gerado no contador. Ela possibilita fazer a soma dos valores que "c" receberá.
soma = 0
# Valos estipular também um contador que será usado para contar cada um dos valores divisíveis por 3 nas condições estipuladas, ele contará um valor.
cont = 0

# Geramos o contador entre 1 e 500 (para isso passamos os valores 1 e 501) e estabelecemos também o valor 2 para a quantidade de números que o contador pulará:
# Desta forma ele retornará uma contagem dos números ímpares de 1 a 500.
for c in range(3, 501, 2):
    if c % 3 == 0:
        # Aqui definimos o contador para contar quantos valores serão somados. Também poderia ser representado igualmente em: cont += 1
        cont = cont + 1
        # Aquiutilizamos a variável "soma" que contém o valor 0 para somar os valores recebidos em "c". Também poderia ser igualmente represemtado em: soma += c
        soma = soma + c
    # Se a indentação de soma fosse modificada e ela se encontrasse da seguinte forma, alinhada ao if do loop:
    # cont  = cont + 1
    # O resultado seria completamente diferente do esperado, retornando: " A soma de todos os 250 valores solicitados é 20667. "
print('A soma de todos os {} valore solicitados é {}' .format(cont, soma))

### O resultado esperado é: "A soma de todos os 83 valores solicitados é 20667"
