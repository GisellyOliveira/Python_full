# Crie um programa que tenha a função leiaInt(), 
# que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt(‘Digite um n: ‘)

###!!! Solução Guanabara gera um eterno loop!!!###
'''
# Solução Guanabara bugada:
def leiaInt(msg):
   ok = False
   valor = 0
   while True:
      n = str(int(msg))
      if n.isnumeric():
         valor = int(n)
         ok = True
      else:
        print('ERRO! Digite um número inteiro válido.')
      if ok:
         break
   return valor
'''
# Melhor solução:
def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n) # Interrompe a função quando alcançada a condição (sem precisar do break)
            # O "return" converte a string n para um inteiro.
            # Retorna esse inteiro para o código que chamou a função leiaInt().
            # Sai do loop: Ao retornar, a função leiaInt() termina, automaticamente interrompendo o loop while True.
        else:
            print('\033[0;31m ERRO! Digite um número inteiro válido. \033[m')
     


# Programa principal:
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
