# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

# Inserimos uma variável que recebe 0 para fazer a soma dos valores pares recebidos mais adiante.
# Inserimos uma variável que recebe 0 para fazer o contador dos valores pares que serão recebidos.
soma = 0
cont = 0

# Geramos um loop 6 vezes para receber 6 números do usuário:
for c in range(1, 7):
    num = int(input('Digite o {} valor inteiro: ' .format(c)))
    # Aqui inseimos a condicional que selecionará os valores pares:
    if num % 2 == 0:
        soma += num # É a mesma coisa que: soma = soma + num
        cont += 1   # É a mesma coisa que: cont  = cont + 1
print('Você informou {} números PARES e a soma deles foi {}. ' .format(cont, soma))