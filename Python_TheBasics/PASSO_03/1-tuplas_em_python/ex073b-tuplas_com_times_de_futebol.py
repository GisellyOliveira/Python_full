# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

brasil24 = ('Flamengo', 'Palmeiras', 'Bahia', 'Botafogo', 'Athletico-PR', 
                   'Bragantino', 'Internacional', 'Cruzeiro', 'São Paulo', 'Atlético-MG', 
                   'Fortaleza', 'Juventude', 'Criciúma', 'Cuiabá', 'Vasco da Gama', 
                   'Atlético-GO', 'EC Vitória', 'Corinthians', 'Grêmio', 'Fluminense')

# Lista de times:
print('\033[1;47m LISTA DE TIMES \033[m') 
for time in brasil24:
    print(time)

# a) Os 5 primeiros times:
print('\033[1;42m 5 MELHORES DO BRASILEIRÃ0 2024 \033[m') 
for position in range(0, 5):
    print(f'{position + 1}º lugar - {brasil24[position]}')

# b) Os 4 últimos colocados:
print('\033[1;41m 4 ÚLTIMOS COLOCADOS DO BRASILEIRÃ0 2024 \033[m') 
print(brasil24[-4:])

# c) Times em ordem alfabética: usando o "sorted"
print('\033[1;43m LISTA EM ORDEM ALFABÉTICA: \033[m') 
print(sorted(brasil24))

# d) Lugar do (Chapecoense) Cuiabá usando o "index":
print('\033[1;44m O CUIABÁ ESTÁ NO: \033[m') 
print(f'{brasil24.index('Cuiabá')}º lugar')



