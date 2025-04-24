# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.
### Correção do código original:

# APRESENTAÇÃO
print('=' * 40)
print('>>> 10 TERMOS DE UMA PA 3.0 <<<')
print('=' * 40)

# Definimos as variáveis que receberá o input do usuário
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

# Definimos as variáveis para controlar o loop
termo = primeiro_termo
contador = 1
total = 0
mais = 10

# Mostramos os 10 primeiros termos
for i in range(1, mais + 1):
    print("{:3d} -> ".format(termo), end='')
    termo += razao
    contador += 1

print('PAUSA')

# Perguntamos ao usuário se deseja mostrar mais termos
continuar = True
while continuar:
    mais = int(input('Quantos termos você deseja mostrar a mais? '))

    if mais > 0:
        # Mostramos os termos adicionais
        for i in range(1, mais + 1):
            print("{:3d} -> ".format(termo), end='')
            termo += razao
            contador += 1

        print('PAUSA')

    else:
        continuar = False

# Mensagem final
print('Progressão finalizada com {} termos mostrados.'.format(contador))
