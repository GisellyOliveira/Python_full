# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.



def calculaArea(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {area:.2f}m2.')


print(' CONTROLE DE TERRENOS ')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m):'))
calculaArea(l, c)
