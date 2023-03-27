'''Create music player with keyboard controller.
 You have to be able to press keyboard: play, stop, next and previous as some keys. 
 Player has to react to the given command appropriately.'''
import pygame
import os


pygame.init()
pygame.mixer.music.load('The_Neighbourhood_-_Afraid_.mp3')
screen = pygame.display.set_mode((500, 500))  
running = True
l = 0
songs = ['The_Neighbourhood_-_Afraid_.mp3', 'The_Neighbourhood_-_Sweater_Weather_.mp3', 'The_Neighbourhood_-_Wires_.mp3']


while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_PAGEUP:
                pygame.mixer.music.stop()

            if event.key == pygame.K_PAGEUP :
                pygame.mixer.music.play(0)

            if event.key == pygame.K_END :
                l = l + 1
                pygame.mixer.music.load(songs[l])
                pygame.mixer.music.play(0)

            if event.key == pygame.K_PAGEDOWN :
                l = l - 1
                pygame.mixer.music.load(songs[l])
                pygame.mixer.music.play(0)
        

    pygame.display.flip()