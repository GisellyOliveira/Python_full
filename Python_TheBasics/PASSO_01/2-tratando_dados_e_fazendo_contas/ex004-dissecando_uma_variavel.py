a = input('Digite algo: ')

#Podemos usar o print com o comando format que armazena todos os valores que serão devolvidos:
print('O tipo primitivo desse valor é {} \n Só tem espaços? {} \n É um número? {} \n É alfabético? {} \n Está em maiúsculas? {} \n Está em minúsculas? {} \n Está capitalizado? {}' .format(type(a), a.isspace(), a.isnumeric(), a.isalpha(), a.isupper(), a.islower(), a.istitle() ))

#Podemos imprimir da velha maneira:
print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())
