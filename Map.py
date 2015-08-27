import pygame

class Map:
    def __init__(self, screen):
        self.width = 1600
        self.height = 800
        self.boxheight = 50
        self.boxwidth = 50
        self.white = (255,255,255)
        self.box1 = pygame.draw.rect(screen, self.white, (100, 100, self.boxwidth, self.boxwidth), 0)
        # self.bg = pygame.draw.rect(w = self.width, h = self.height, x = 0, y = 0)

        # self.box1 = pygame.Rect(w = boxwidth, h = boxheight, x = 100, y = 100)

        # pygame.draw.rect(screen, )

    def update(self, screen):
        self.box1 = pygame.draw.rect(screen, self.white, (100, 100, self.boxwidth, self.boxwidth), 0)
