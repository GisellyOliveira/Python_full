# Resolução da problemática sobre o motivo da seguinte lógica não funcionar:
'''
sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while sexo != 'M' or 'F':
    sexo = str(input('Dados inválidos. Informe seu sexo novamente: [M/F] ')).upper().strip([0])
print('Sexo {} registrado com sucesso.' .format(sexo))
'''

# Justificativa:
''' 
Você pensou: "Enquanto o sexo digitado for diferente de 'M' ou diferente de 'F', peça a digitação novamente". E a ideia faz sentido! Mas, para o Python, essa linha tem outra interpretação.
Entendendo o "or": O "or" em Python funciona como um "ou" mesmo, mas ele avalia cada lado da expressão separadamente.
Primeiro ele checa: sexo != 'M'. Se a pessoa digitar 'F', essa parte será verdadeira (pois 'F' é diferente de 'M').
Depois, ele checa: 'F'. Repare que ele não está comparando 'F' com nada! O Python interpreta qualquer string não vazia como verdadeira.
Resultado? A condição do seu while sempre será verdadeira, porque ou o sexo será diferente de 'M', ou 'F' sozinho já é considerado verdadeiro. É como se o código entendesse que, não importa o que você digite, sempre haverá um motivo para pedir a digitação novamente!

A solução do professor: not in
O professor usou a expressão `while sexo not in 'MmFf': 
'''
