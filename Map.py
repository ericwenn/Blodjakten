import pygame
from random import randint

class Map:
    def __init__(self, screen):
        self.width = 1600
        self.height = 800
        self.boxheight = 80
        self.boxwidth = 80
        self.white = (255,255,255)


        self.createBoxes(screen, 7)

    def createBoxes(self, screen, amount):
        counter = 0
        self.boxes = []
        positions = []
        while (counter < amount):
            positions.append([randint(self.boxwidth, self.width) - self.boxwidth, randint(self.boxheight, self.height) - self.boxheight])
            counter += 1
        counter = 0
        while (counter < amount):
            self.boxes.append(pygame.draw.rect(screen, self.white, (positions[counter][0], positions[counter][1], self.boxwidth, self.boxwidth), 0))
            counter += 1
        self.boxes.append(positions)

    def update(self, screen):
        counter = 1
        positions = self.boxes[len(self.boxes) - 1]
        while counter < len(self.boxes):
            self.boxes[counter - 1] = pygame.draw.rect(screen, self.white, (positions[counter - 1][0], positions[counter - 1][1], self.boxwidth, self.boxheight), 0)
            counter += 1

    def getRects(self):
        newboxes = []
        counter = 1
        while counter < self.boxes[len(self.boxes)]:
            newboxes = self.boxes[counter - 1]
            counter += 1
        return newboxes
