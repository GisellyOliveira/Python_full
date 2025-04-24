n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}' .format(m))

# Estruturamos uma condicional onde, se a média for maior que 6, retornamos que a média foi boa.
# CONDIÇÃO SIMPLES: Quando somente o if é usado.
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
# CONDIÇÃO COMPOSTA: Quando o else também é utilizado.
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

# CONDIÇÃO SIMPLIFICADA:  Refaremos a estrutura usando o if simplificado:
print('PARABÉNS!' if m >= 6 else 'ESTUDE MAIS!')