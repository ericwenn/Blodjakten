global players, shots

def init_map(screen, n):
    global map, boxes
    map = Map(screen)

def init_players(n):
    global players
    players = []
    while n > 0:
        players.append(Player(n))
        n -= 1


def keydown_players(key):
    for player in players:
        player.keydown(key)


def keyup_players(key):
    for player in players:
        player.keyup(key)

def move_players(screen):
    for player in players:
        player.move(screen)

def init_shot(speed):
    global shots
    shots.append(Shot(speed))




import pygame, sys, os
global pygame

from Player import Player
from Map import Map





pygame.init()

size = width, height = 1600, 800



black = (0, 0, 0)
white = (255,255,255)


screen = pygame.display.set_mode(size)




gameover = False
init_map(screen, 5)
init_players(2)

while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        if event.type == pygame.KEYDOWN:
            keydown_players(event.key)



        if event.type == pygame.KEYUP:
            keyup_players(event.key)



    screen.fill(black)
    map.update(screen)
    move_players(screen)

    pygame.display.flip()

pygame.quit()