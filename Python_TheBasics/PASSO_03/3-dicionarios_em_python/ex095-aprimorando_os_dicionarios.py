# Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

# Foi adicionado uma nova lista vazia time:
time = list()
jogador = dict()
partidas = list()

while True: # Novo laço
    jogador.clear() # a variável é esvaziada ao início de cada laço
    jogador['nome'] = str(input('Nome do Jogador: ')).capitalize()

    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy()) # Copiando os dados inseridos do dicionário jogador antes que sejam deletadas ao reiniciar o laço.

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

# Cabeçalho com dados dos jogadores:
print('-=' * 30)
print('cod ', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()

# Resultado:
print('-' * 60)
for k, v in enumerate(time):
    print(f'{k:^4}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-' * 60)

# Mostrar opção para ver dados do jogador:
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    Na {i+1}a. partida fez {g} gols.')  
    print('-' * 60)

print('>>> VOLTE SEMPRE <<<') 
