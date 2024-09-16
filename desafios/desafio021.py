# Faça um programa em python que abra e reproduza um arquivo de áudio em formato mp3.

import pygame

pygame.mixer.init()

pygame.mixer.music.load('yesterday.mp3')

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)