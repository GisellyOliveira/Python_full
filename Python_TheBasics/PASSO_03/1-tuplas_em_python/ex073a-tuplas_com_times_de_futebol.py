# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense (substituido por Cuiabá pois não foi escalado).

brasil24 = ('Flamengo', 'Palmeiras', 'Bahia', 'Botafogo', 'Athletico-PR', 
            'Bragantino', 'Internacional', 'Cruzeiro', 'São Paulo', 'Atlético-MG', 
            'Fortaleza', 'Juventude', 'Criciúma', 'Cuiabá', 'Vasco da Gama', 
            'Atlético-GO', 'EC Vitória', 'Corinthians', 'Grêmio', 'Fluminense')

# Lista de times:
print('\033[1;47m LISTA DE TIMES: \033[m')
print(brasil24, '\n')

# Os 5 primeiros times:
print('\033[1;42m OS 5 PRIMEIROS SÃO: \033[m')
print(brasil24[:5], '\n')

# 4 últimos colocados:
print('\033[1;41m OS 4 ÚLTIMOS SÃO: \033[m')
print(brasil24[-4:], '\n')

# Times em ordem alfabética:
print('\033[1;43m LISTA EM ORDEM ALFABÉTICA: \033[m')
print(sorted(brasil24), '\n')

# Posição do Cuiabá:
print('\033[1;44m POSIÇÃO DO CUIABÁ: \033[m')
print(f'{brasil24.index('Cuiabá') + 1}º lugar')
