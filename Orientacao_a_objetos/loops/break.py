# Break

count = 0

# loop infinito - nunca é False
while True:
    print(count)
    count += 1
    if count >= 5:
        break  # sai do loop

### Exemplo2:
naipes = ['copas', 'ouro', 'espadas', 'paus']

# loop infinito - nunca é False
while True:
    # pop(): retira e retorna o último item da lista
    elemento = naipes.pop()
    print(elemento)
    if elemento == "ouro":
        break
# Saída: 
# paus
# espadas
# ouro