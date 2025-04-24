# Faça um programa que tenha uma função chamada contador(), 
# que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            
# a) de 1 até 10, de 1 em 1                                                                                                                                              
# b) de 10 até 0, de 2 em 2                                                                                                                                            
# c) uma contagem personalizada
from time import sleep

def contador(i, f, p):
    # Resovendo problema para converter passos do input do usuário negativos em positivos:
    if p < 0:
        p *= -1
    # Se passo for 0 será convertido em 1:
    if p == 0:
        p = 1
        
    print('-' * 40)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)



# Utilizamos a condicional para determinar a primeira situação onde o início é menor que o fim:
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ', flush=True) # flush para gerar o sleep de meio segundo a cada contagem.
            sleep(0.5) # O sleep vai gerar um buffer e só será executado no final do código. O flush evita essa situação.
            cont += p
        print('FIM!')

# Contagem retrógrada: o início é maior que o fim.
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

### Programa principal
# a) de 1 até 10, de 1 em 1 
contador(1, 10, 1)
# b) de 10 até 0, de 2 em 2 
contador(10, 0, 2)
# c) uma contagem personalizada
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
