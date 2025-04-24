# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m)'))
imc = peso / (altura ** 2)

print('O seu Índice de Massa Corporal (IMC) é de {:.2f}.' .format(imc))

if imc < 18.5:
    print('\033[1;41m Você está abaixo do peso. \033[m')
elif 18.5 <= imc < 25:
    print('\033[1;47m Você está no peso ideal. \033[m')
elif 25 <= imc < 30:
    print('\033[1;45m Você está em sobrepeso. \033[m')
elif 30 <= imc < 40:
    print('\033[1;41m Você está com Obesidade. PROCURE UM MÉDICO! \033[m')
elif imc >= 40:
    print('\033[1;41m Você está com Obesidade Mórbida. PROCURE UM MÉDICO URGENTEMENTE! \033[m')
