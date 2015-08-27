import pygame
from Shot import Shot
from random import randint

global shots

shots = []

def init_shot(speed, rect, maprects):
    global shots
    shots.append(Shot(speed, rect, maprects))

def move_shots(screen):
    global shots
    tmp_shots = []
    for shot in shots:
        if not shot == False:
            shot.move(screen)
            tmp_shots.append(shot)

    shots = tmp_shots


class Player:
    def __init__(self, player, rects):
        print(player)

        self.ID = player
        self.rects = rects;



        if player == 1:
            self.left = pygame.K_a
            self.right = pygame.K_d
            self.up = pygame.K_w
            self.down = pygame.K_s
            self.shoot = pygame.K_SPACE
        elif player == 2:
            self.left = pygame.K_LEFT
            self.right = pygame.K_RIGHT
            self.up = pygame.K_UP
            self.down = pygame.K_DOWN
            self.shoot = pygame.K_KP_ENTER

        self.dirX = False
        self.dirY = False

        self.width = 1600
        self.height = 800
        self.baseSpeed = 1
        self.speed = [0,0]
        self.obj = pygame.image.load("assets/ball.gif")
        self.objrect = self.obj.get_rect()
        self.objrect.x = randint(self.objrect.width, self.width) - self.objrect.width
        self.objrect.y = randint(self.objrect.height, self.height) - self.objrect.height



    def keydown(self, key):
            if key == self.left:
                self.speed[0] = -self.baseSpeed
                self.dirX = 'left'
            elif key == self.right:
                self.speed[0] = self.baseSpeed
                self.dirX = 'right'

            if key == self.down:
                self.speed[1] = self.baseSpeed
                self.dirY = 'down'
            elif key == self.up:
                self.speed[1] = -self.baseSpeed
                self.dirY = 'up'
            elif key == self.shoot:
                init_shot(self.speed, self.objrect, self.rects)



    def keyup(self, key):
        if key == self.left or key == self.right:
            self.speed[0] = 0
        elif key == self.up or key == self.down:
            self.speed[1] = 0





    def move(self, screen, players):

        if self.ID == 1:
            move_shots(screen)

        self.objrect = self.objrect.move(self.speed)

        for player in players:
            if not player.ID == self.ID:
                if pygame.Rect.colliderect(self.getRect(), player.getRect()):
                    self.speed[0] = 0
                    self.speed[1] = 0

        for rect in self.rects:
            if pygame.Rect.colliderect(self.getRect(), rect):
                self.speed[0] = 0
                self.speed[1] = 0


        if self.objrect.left < 0 or self.objrect.right > self.width:
            self.speed[0] = 0
        if self.objrect.top < 0 or self.objrect.bottom > self.height:
            self.speed[1] = 0

        screen.blit(self.obj, self.objrect)



    def getRect(self):
        return self.objrect