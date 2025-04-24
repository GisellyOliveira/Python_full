# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

# APRESENTAÇÃO
print('=' * 40)
print('>>> 10 TERMOS DE UMA PA 3.0 <<<')
print('=' * 40)

# Definimos as variáveis que receberá o input do usuário:
primeirotermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
# Definimos as duas varáveis para inserir no laço: uma que recebe o valor do primeiro termo e ougra com valor 1 para ser utilizada como contador:
termo = primeirotermo
cont = 1
#Definimos mais duas variáveis para servirem de contador ao input de quantas pa's o usuário quer visualizar:
total = 0
mais = 10

# Vamos inserir o nosso while que faz o pa dentro de um outro laço while que defini a seguinte condição:
# Enquanto a variável "mais"for diferente de 0, a variável total receberá o valor das variáveis "total"e "mais".
while mais != 0:
    total = total + mais
    while cont <= mais:
        print('{} -> ' .format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('pausa')
    ############ BUGOU!!! NÃO ESTÁ MOSTRANDO OS TERMOS DIGITADOS MAS ESTÁ CONTABILIZANDO.
    mais = int(input('Quantos termos você deseja mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.' .format(total))
    