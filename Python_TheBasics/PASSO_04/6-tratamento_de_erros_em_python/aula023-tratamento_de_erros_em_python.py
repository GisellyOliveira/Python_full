# Vamos utilizar o exemplo da divisão, onde sabemos que, 
# caso o denominador seja 0, o retorno é de "ZeroDivisionError".
# Faremos o tratamento do erro com o try-except-else:

print('>>> Operação utilizando a estrutura de try-except-else-finally <<<')
print('-' * 60)
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print('Infelizmente tivemos um problema...')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigada!')


### Podemos, inclusive, retornar a classe do erro utilizando no except a palavra Exception:
print('>>> Operação utilizando a estrutura except Exception para retornar o tipo de erro <<<')
print('-' * 60)
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}...')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigada!')

### Podemos também incluir erros específicos no tratamento do except:
print('>>> Operação utilizando a estrutura except Exception para retornar o tipo de erro <<<')
print('-' * 60)
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com o tipo de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por 0.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigada!')
