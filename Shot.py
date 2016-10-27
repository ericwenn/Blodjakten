import pygame

class Shot:
    def __init__(self, speed, rect, mapRects):

        self.maxWidth = 1600
        self.maxHeight = 800
        self.mapRects = mapRects;

        self.speed = [speed[0] * 2, speed[1] * 2]
        self.obj = pygame.image.load("assets/ball.gif")
        self.objrect = self.obj.get_rect()

        self.objrect.centerx = rect.centerx
        self.objrect.centery = rect.centery
        print(self.objrect)


    def move(self, screen):
        if self.speed[0] == 0 and self. speed[1] == 0:
            return False
        elif self.objrect.x > self.maxWidth or self.objrect.y > self.maxHeight:
            return False
        elif self.objrect.x < 0 or self.objrect.y < 0:
            return False

        for rect in self.mapRects:
            if pygame.Rect.colliderect(self.objrect, rect):
                return False

        self.objrect = self.objrect.move(self.speed)
        screen.blit(self.obj, self.objrect)




