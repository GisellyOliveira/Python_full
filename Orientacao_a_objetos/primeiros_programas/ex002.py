# Faça um programa que leia 3 notas de um aluno e calcule a sua média aritimética,
# imprimindo, em seguida, uma mendagem dizendo se o aluno foi aprovado, reprovado ou deverá fazer a prova final.
# O critério de aprovação ;e:
# Se a média for maior ou igual a 7, está aprovado.
# Se a média for menor que 3, está reprovado.
# Se a m'edia estiver entre 3 e 7, est'a em prova final.

# Mensagem de título:
print("**********************************")
print(">>> O aluno foi aprovado? <<<")
print("**********************************")

nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
nota_3 = float(input("Nota 3: "))

media = (nota_1 + nota_2 + nota_3) / 3 # calcula a média

if media >= 7:
    print("O aluno foi APROVADO! Sua média foi %.2f" % media)
elif media < 3:
    print("O aluno foi REPROVADO! Sua média foi %.2f" % media)
else:
    print("O aluno ficou em PROVA FINAL! Sua média foi %.2f" % media)
