# Loop for
for i in range(6):
    print(i)

# OBS: A função range() pode ser representada de três formas diferentes:
    # range(stop_value) : considera o ponto inicial como zero.
    # range(start_value, stop_value) : Gera a sequência com base no valor inicial e final.
    # range(start_value, stop_value, step_size) : Gera a sequência incrementando o valor inicial usando o tamanho do passo até atingir o valor final.

### Exemplo2:
pares = [2, 4, 6, 8]
for i in range(len(pares)):
    print("Índice %d - Valor %d" % (i, pares[i]))
    