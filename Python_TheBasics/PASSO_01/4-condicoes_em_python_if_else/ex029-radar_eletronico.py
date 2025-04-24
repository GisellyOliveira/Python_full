# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('Qual a velocidade atual do carro? '))

if vel > 80:
    print('MULTADO!!! \nA velocidade máxima permitida é de 80km/h!!!')
    multa = (vel - 80) * 7
    print('Você receberá uma multa de R${}' .format(multa))
else:
    print('Você é um excelente motorista!!! \nTenha um bom dia e dirija com atenção!')