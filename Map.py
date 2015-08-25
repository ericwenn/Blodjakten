import pygame

class Map:
    def __init__(self):
        #Test kommentar
        self.width = 1600
        self.height = 800
        boxheight = 50
        boxwidth = 50
        self.bg = pygame.Rect(w = self.width, h = self.height, x = 0, y = 0)

        self.box1 = pygame.Rect(w = boxwidth, h = boxheight, x = 100, y = 100)

