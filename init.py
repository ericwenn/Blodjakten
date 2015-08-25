import pygame, sys, os
from Player import Player

global pygame

pygame.init()




size = width, height = 1600, 800
black = (0, 0, 0)
white = (255,255,255)


screen = pygame.display.set_mode(size)




gameover = False
player1 = Player('first')
player2 = Player('second')

while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        if event.type == pygame.KEYDOWN:
            player1.keydown(event.key)
            player2.keydown(event.key)



        if event.type == pygame.KEYUP:
            player1.keyup(event.key)
            player2.keyup(event.key)



    screen.fill(black)

    player1.move(screen)
    player2.move(screen)






    pygame.display.flip()
