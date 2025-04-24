# Faça um programa que tenha uma função chamada escreva(), 
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  
# Ex:                                                                                                                                                                        
# escreva(‘Olá, Mundo!’) 
# Saída:                                                                                                                         
#  ~~~~~~~~~                                                                                                                                                            
# Olá, Mundo!   


def escreva(msg):
    tam = len(msg) + 4 # Foram adicionados 4 caracteres a mais por questão estética.
    print('-' * tam) 
    print(f'  {msg}') # E foram adicionados 2 espaços no início por questão estética.
    print('-' * tam)


# Programa principal:
escreva('Olá Mundo!!!')
escreva('Curso de Python')
