# Faça um programa que tenha uma função notas() 
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas  
# – A maior nota   
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*n, sit=False): # desempacota todas as notas recebidas
    #Docstring:
    """
    -> Função para analiasr notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionários com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n) # total de notas passadas
    r['maior'] = max(n) # a maior nota
    r['menor'] = min(n) # a menor nota
    r['media'] = sum(n)/len(n) # média das notas
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'

    return r


# Programa principal:
resp = notas(5, 7.5, 9.5, sit=True) #"sit=True" é opcional para mostrar a situação do aluno. Pode ser omitida.
print(resp)

# Para docstrings:
#help(notas)
