# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('>>> Vamos calcular o total do aluguel do seu carro! <<<')

dias = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos km você rodou nesse período? '))
total = (dias * 60) + (km * 0.15)

print('Para o total de {} dias e {} km rodados, o total do seu aluguel é de R${:.2f}.' .format(dias, km, total))