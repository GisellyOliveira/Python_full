# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python', 
            'curso', 'estudar', 'praticar', 'trabalhar', 
            'mercado', 'programador', 'futuro', 'tecnologia', )

for p in palavras: #Laço principal que pegará cada palavra da tupla
    print(f'\n Na palavra {p.upper()} temos ', end='') # Coloca em maíusculo a palavra para dar destaque na frase
    for letra in p: # Cada letra dentro da palavra p do laço interno
        if letra.lower() in 'aeiou': # Trata cada caractere maiúsculo que houver transformando-o em minúsculo. Para pegar vogais com acento, poderia ser usado 'aáàãâeéèêiou''
            print(letra, end=' ')
