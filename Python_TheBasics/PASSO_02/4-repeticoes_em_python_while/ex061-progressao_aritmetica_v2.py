# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

# APRESENTAÇÃO
print('=' * 40)
print('>>> 10 TERMOS DE UMA PA 2.0 <<<')
print('=' * 40)

# Desta forma, definimos as variáveis para a razão e a pa:
primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
# Definimos 2 variáveis: "termo" vai receber o valor de "primeirotermo" e, "cont" vai contar.
termo = primeirotermo
cont = 1

# Neste exemplo não utilizamos nenhuma fórmula para calcular o décimo termo da pa. Utilizamos somente a lógica e as duas variáveis, "termo" e "cont", para fazer a pa:
while cont <= 10:
    print('{} -> ' .format(termo), end='')
    termo += razao
    cont += 1
print('Fim.')