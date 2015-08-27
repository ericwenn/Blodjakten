import pygame



class Player:
    def __init__(self, player):
        print(player)

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
                print("SHOT")



    def keyup(self, key):
        if key == self.left or key == self.right:
            self.speed[0] = 0
        elif key == self.up or key == self.down:
            self.speed[1] = 0





    def move(self, screen):
        self.objrect = self.objrect.move(self.speed)
        if self.objrect.left < 0 or self.objrect.right > self.width:
            self.speed[0] = 0
        if self.objrect.top < 0 or self.objrect.bottom > self.height:
            self.speed[1] = 0

        screen.blit(self.obj, self.objrect)



    def getRect(self):
        return self.objrect