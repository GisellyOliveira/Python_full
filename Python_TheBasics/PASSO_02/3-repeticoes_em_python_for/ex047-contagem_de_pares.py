# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.


### AQUI APRESENTAMOS DUAS SOLUÇÕES:

## PRIMEIRA SOLUÇÃO: Esta solução executa o dobro de iterações que a segunda solução.
print('>>> PRIMEIRA SOLUÇÃO <<<')
# Geramos o contador entre 1 e 50 (para isso passamos os valores 1 e 51):
# Inserimos uma condicional na iteração onde, se o resto da divisão por 2 for 0, o número será par e, assim, impresso no console.
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('Fim')

## SEGUNDA SOLUÇÃO: Esta solução executa a metade de iterações que a primeira solução, sendo muito mais econômica em termo de dados.
print('>>> SEGUNDA SOLUÇÃO <<<')
# Geramos o contador entre 2 e 50 (para isso passamos os valores 2 e 51) e estabelecemos também o valor 2 para a quantidade de números que o contador pulará:
# Desta forma ele contará o número 2 e, pulará uma casa a cada contagem, retornando somente os números pares.
for c in range(2, 51, 2):
    print(c, end=' ')
print('Fim')