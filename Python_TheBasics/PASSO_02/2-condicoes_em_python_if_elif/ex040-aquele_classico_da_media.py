# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

print('\033[31m - \033[m' * 50)
print('\033[1,41m CÁLCULO DA MÉDIA: \033[m')
print('\033[31m - \033[m' * 50)

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1 + nota2) / 2
print('\033[1;30m A sua média é: {:.1f} \033[m' .format(media))

if media < 5.0:
    print('\033[1;31m Você está REPROVADO!!! \033[m')
# Essa linha também poderia ser escrita da seguinte forma-> elif 7 > media >= 5:
elif media >= 5.0 and media < 7.0:
    print('\033[1;33m Você está de RECUPERAÇÃO! \033[m')
elif media >= 7.0:
    print('\033[1;32m Você está aprovado!!! \033[m')