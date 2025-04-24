# QUEBRAR LINHA OU JUNTAR LINHAS EM UMA SÓ QUANDO EXIBIR O RESULTADO DO PRINT:

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}' .format(s, m, d))
print('Divisão inteira {} e potência {}' .format(di, e))

#Vamos unir as duas linhas cancelando a quebra de linhas com o end='':
print('Unindo linhas: A soma é {}, o produto é {} e a divisão é {:.3f}' .format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}' .format(di, e))
#As aspas recebem o conteúdo que será exibido na união das duas linhas, como, por exemplo, um espaço ou nada.
print('Unindo linhas com >>>: A soma é {}, o produto é {} e a divisão é {:.3f}' .format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {}' .format(di, e))

# É possível quebrar a linha dentro do próprio print utilizando o \n:
print('Quebrando linhas: A soma é {}, \n o produto é {} \n e a divisão é {:.3f}' .format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}' .format(di, e))