# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# É necessário que o arquivo mp3 esteja na mesma pasta deste arquivo .py

# Usaremos a biblioteca "pygame", que serve originalmente para jogos (mas jogos contém música...), para a reprodução do arquivo mp3.
#Para isso será primeiramente necessário instalar o pacote no console utilizando o comando $ pip3 install pygame
# Uma vez instalado o pacote, o importaremos:
import pygame
from pygame import mixer
# Agora iniciaremos o pygame utilizando a propriedade "initau"
pygame.init()
# Utilizaremos a propriedade "mixer" para selecionar o áudio mp3 que será passado como parâmetro:
mixer.music.load('helloworld.mp3')

# Com a propriedade "mixer.music.play", iniciaremos a arquivo mp3:
mixer.music.play()

# É necessário que ele espere o evento terminar para encerrar o programa, e, para isso, utilizaremos o "event.wait":
pygame.event.wait()

# O pygame não está funcionando no sonoma do macbook.