# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog='<desconhecido>', gol=0): #passando uma string como parâmetro opcional com aspas e < >.
    print(f'O jogador {jog} fez {gol} gol(s) no campenato.')


# Programa principal:
n = str(input('Nome do jogador: '))
g = str(input('Quantos gols ele fez? ')) # valor passado como str para poder receber valor vazio sem dar erro.
# Validando o valor recebido para os gols:
if g.isnumeric(): # e então checamos se o valor recebido é numérico.
    g = int(g)
else:
    g = 0
# Validando o valor recebido para o nome do jogado:
if n.strip() == '': # Se o nome do jogador for vazio ( e sem espaços no começo e final por conta do strip):
    ficha(gol = g) # A função recebe somente o gol do input do usuário como parâmetro.
else:
    ficha(n, g) # Senão recebe o nome e os gols informados.
